---
title: "Decisions API is in public beta"
sidebar_label: "Decisions API is in public beta"
---

# Decisions API is in public beta

> Hacker News · 2026-10-06 · API

---

OpenAI가 Decisions API의 공개 베타를 발표했다. 이 API는 텍스트와 이미지를 입력으로 받아 분류·라우팅·우선순위 지정에 바로 쓸 수 있는 '타입화된' 답변을 반환하도록 설계됐으며, Responses API보다 약 10배 빠른 응답을 제공한다고 소개한다. 요청은 model, input, questions 세 부분으로 구성되고 현재 사용 가능한 모델은 gpt-6-luna뿐이다. 질문 종류로는 특정 조건의 참/거짓 확률을 반환하는 predicate, 고정된 선택지 중 하나를 고르는 choice, 순서가 있는 레벨에 대해 확률 가중 평균을 반환하는 score가 있어, 각각 probability·choice·score 등으로 결과가 나오는 구조다. 이미지 처리 시에는 인라인 base64 데이터 URL만 허용되며 텍스트와 이미지를 같은 user 메시지 안에 결합해 평가할 수 있다.
기술적으로 Decisions API는 조건 판정, 카테고리 분류, 루팅 결정, 심각도 판정 같은 운영형 의사결정 워크로드를 실시간으로 처리하는 데 적합하다. choice와 score 응답은 각 선택지에 대한 확률 분포와 별도의 confidence 값을 제공해 임계값 기반의 라우팅·검토 플로우 설계가 가능하고, score는 레벨 인덱스의 확률가중평균으로 연속값을 도출해 우선순위 산정에 유용하다. 요금은 gpt-6-luna 입력 토큰에 대해 1M토큰당 $0.10이며 출력 토큰 요금은 없고 지역별 처리 프리미엄과 장문 입력 가격 승수가 적용될 수 있다. 또한 Zero Data Retention(ZDR)와 HIPAA 지원(자격 대상자), 미국·유럽(EEA+스위스) 데이터 레지던시·지역 처리 등을 제공한다고 밝혀 규제·프라이버시 요건이 있는 기업 적용 가능성을 염두에 둔 설계임을 보여준다. 플레이그라운드에서 실험해 본 뒤 엔드포인트 POST /v1/decisions로 통합하는 흐름을 권장한다.

[Hacker News에서 원문 읽기 →](https://developers.openai.com/api/docs/guides/decisions)

