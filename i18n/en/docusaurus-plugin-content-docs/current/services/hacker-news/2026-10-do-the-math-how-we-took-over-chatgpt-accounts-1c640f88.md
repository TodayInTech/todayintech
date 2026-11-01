---
title: "Do the math: How we took over ChatGPT accounts"
sidebar_label: "Do the math: How we took over ChatGPT accounts"
description: "Parameter Labs 연구진은 ChatGPT의 공개 공유 링크와 Preview, MathLive의 postMessage 처리, iframe srcdoc·YouTube JSONP 조합으로 공격자가 공유 링크만으로 피해자 세션에서 chatgpt.com 신분의 자바스크립트를 실행해 사적 대화를 조회·유출할 수 있음을 시연했으며, OpenAI는 2026-10-26에 두 웹 프론트엔드를 패치해 문제를 해결했습니다."
---

# Do the math: How we took over ChatGPT accounts

> Hacker News · 2026-10-31 · Security

---

Parameter Labs가 공개한 재현은 한 번의 공유 링크 클릭만으로 다른 사용자의 서명된 ChatGPT 세션에서 **chatgpt.com 신분으로 임의 자바스크립트가 실행되어 사적 대화를 조회·유출**할 수 있음을 보여준다. OpenAI는 해당 보고서를 P1으로 재분류했고, 2026-10-26에 두 웹 프론트엔드에 걸쳐 수정이 완료되었다고 확인했다. 버그 바운티는 총 $5,000였다.

## 샌드박스 경계가 무너진 경로

공격 체인은 서로 독립적으로 합리적으로 보였던 기능들의 조합에서 나왔다. 핵심은: (1) ChatGPT의 HTML Preview(샌드박스된 별도 주소에서 실행) (2) 대화에 포함된 그래프가 로드한 MathLive 라이브러리(메인 페이지에 postMessage 리스너 설치) (3) iframe의 srcdoc을 통한 새 문서 생성, (4) CSP로 허용된 www.youtube.com의 oEmbed(JSONP) 응답을 이용한 스크립트 실행이었다.

MathLive는 가상 키보드 레이아웃을 메시지로 변경할 수 있게 했고, 해당 레이아웃은 HTML을 포함할 수 있었다. 이 리스너는 event.origin/event.source 검증을 하지 않아 Preview(격리된 프레임)에서 보낸 메시지를 신뢰하여 메인 페이지에 innerHTML로 삽입했다. innerHTML에 삽입된 &lt;iframe srcdoc&gt;가 sandbox 속성 없이 생성되면, 그 프레임은 부모인 https://chatgpt.com 동일 출처(identity)을 상속받아 같은-origin 자바스크립트를 실행할 수 있다.

## CSP 우회: YouTube oEmbed(JSONP)

ChatGPT의 CSP는 인라인 스크립트를 차단했지만 www.youtube.com은 허용되어 있었다. YouTube의 oEmbed 엔드포인트가 callback 파라미터로 JSONP 형태의 응답을 반환하면서, 연구진은 응답 앞뒤에 ;void 등을 붙여 오류 객체를 소비하고 결국 허용된 출처로부터 임의 코드가 로드되게 했다. 결과적으로 공격자는 chatgpt.com 신분의 실행 컨텍스트를 얻었다.

## 인증된 API 접근과 데이터 유출

인젝션된 스크립트는 페이지 내 #client-bootstrap에서 액세스 토큰과 계정 ID를 추출해 다음과 같은 인증된 엔드포인트를 호출했다: GET /backend-api/conversations?...&amp;limit=20... 및 GET /backend-api/conversations/&lt;conversation-id&gt;?num_turns=2 (디테일 요청 실패 시 레거시 /backend-api/conversation/&lt;id&gt;?include_full_conversation=true를 시도). 응답을 받아 이미지 요청을 통해 공격자 서버로 일부 값을 전송하는 방식으로 데이터 유출을 증명했다. 이로써 공격자는 피해자 계정으로 가능한 모든 프론트엔드 인증 액션을 실행할 수 있는 보안 경계 침해를 입증했다.

## 수정, 타임라인, 교훈

주요 일정: 10월13일 재현된 경로 확인 → 10월18일 보고서 제출 → 10월21일 OpenAI가 재현 → 10월26일 두 프론트엔드 모두에서 보고된 메시지 타입을 거부하도록 패치하고 문제 해결을 확인했다. 문제의 근본 원인은 단일 취약점이 아니라 "검증되지 않은 cross-frame 메시지 수용"과 "신뢰할 수 없는 마크업이 unsandboxed 문서로 진입"하는 디자인 결함의 조합이었다. Parameter Labs는 방어권고로 event.origin과 event.source 검증, 크로스-윈도우 설정에 원시 HTML 허용 금지, 외부로 영향받을 수 있는 동적 문서는 항상 sandbox 유지, CSP는 보조 방어책으로 유지할 것을 제시했다.

기사의 근거는 제공된 재현 코드 흐름과 타임라인, OpenAI의 수정 확인에 한정된다. 공개된 체인은 보안 경계가 구성요소 간의 '이음새'에서 깨질 수 있음을 기술적으로 잘 보여주며, 유사한 기능(공유 가능한 공개 콘텐츠 + 프리뷰 + 서드파티 자원 허용)이 있는 서비스에게 중요한 실무적 시사점을 준다.

[Hacker News에서 원문 읽기 →](https://www.parameter.ai/labs/we-found-a-gap-at-openai)

