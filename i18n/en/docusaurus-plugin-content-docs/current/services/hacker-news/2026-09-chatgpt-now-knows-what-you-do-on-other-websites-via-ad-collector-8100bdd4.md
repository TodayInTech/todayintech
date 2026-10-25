---
title: "ChatGPT now knows what you do on other websites via ad collector"
sidebar_label: "ChatGPT now knows what you do on other websites via ad collector"
---

# ChatGPT now knows what you do on other websites via ad collector

> Hacker News · 2026-09-20 · 프라이버시/보안

---

분석 결과 OpenAI의 광고 수집기(bzr.openai.com)는 ChatGPT 클라이언트가 생성한 식별자(obi)를 계정 식별자(sub)와 RS256 서명 토큰으로 연결한 뒤, 크로스-사이트로 __obi 쿠키를 .openai.com 도메인에 설정합니다. 클라이언트는 POST /backend-api/bazaar/obi/sync-token로 JWT를 받고 bzr.openai.com/v1/obi/sync에 토큰을 보내면 SameSite=None, Secure, Max-Age=1년 설정의 __obi가 발급됩니다. 브라우저는 로 로드되는 OpenAI SDK 요청 등에서 이 쿠키를 자동으로 첨부했고, SDK는 광고주 페이지의 폼·렌더된 텍스트·태그 관리자 데이터(in, fm, ht, js)를 수집해 OpenAI로 전송했습니다. 이메일·전화·이름은 SHA-256 해시로 전송되지만 국가·지역·우편번호 등은 평문으로 전송되며, URL 쿼리스트링은 제거되나 경로(path)는 보존되어 의료·부채·소송 관련 경로가 수집 사례에 포함됐습니다.
저자는 자신의 휴대전화에서 두 가지 캡처 방식으로 메커니즘을 재현하고 936개의 광고 픽셀과 1,029개 호스트를 관찰했다고 보고합니다. 한 장치의 __obi는 Chewy·Wayfair·ThriftBooks·Eventbrite·HelloFresh·Coursera·SeatGeek 등 적어도 12개 상업 사이트로부터 수집됐고, 자동 매칭 설정은 관측된 881개 픽셀 중 638개에서 활성화돼 있었습니다. 해당 동작은 Chrome 안드로이드에서 관찰되었고 iOS의 Safari 등은 서드파티 쿠키 차단으로 이 메커니즘이 작동하지 않는다고 적시합니다. OpenAI는 질의에 대해 답변을 회신했으나 핵심 설명은 제공하지 않았습니다. 기술적으로는 기존 광고기술과 구조적으로 유사하되, AI 챗 서비스의 계정·대화 맥락과 결합된다는 점에서 개인정보 보호와 동의 모델 측면의 함의가 크다는 점이 요지입니다.

[Hacker News에서 원문 읽기 →](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

