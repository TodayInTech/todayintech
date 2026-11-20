---
title: "Introducing Tool Retrieval in the Gemini API"
sidebar_label: "Introducing Tool Retrieval in the Gemini API"
description: "Google은 2026-11-19 발표로 Gemini API Interactions에 'Tool Retrieval' 프리뷰를 도입했습니다. 도구의 파라미터 스키마를 필요 시에만 불러와 토큰 사용량·지연·도구 선택 정확도를 개선하도록 설계되었습니다."
---

# Introducing Tool Retrieval in the Gemini API

> Google Blog · 2026-11-19 · Developer tools

---

**Gemini API에 'Tool Retrieval'이 도입됐다 (프리뷰, Interactions API)**

Google은 2026-11-19자 블로그에서 Gemini API에 **Tool Retrieval**을 도입했다고 발표했다. 이 기능은 에이전트가 수십~수백 개의 도구를 연결할 때 매 요청마다 모든 파라미터 스키마를 보내는 비용(입력 토큰, 지연, 도구 선택 정확도 저하)을 줄이는 것이 목적이다.

## 어떻게 작동하나: tool_search와 defer_loading

요청에 tool_search 타입 도구를 추가하고, 미리 로드하지 않을 도구에 `defer_loading: true`를 설정하면 된다. 모델은 각 도구의 이름과 설명은 보지만 파라미터 스키마는 컨텍스트에서 제외된다. 필요할 때 모델이 도구 이름으로 요청하면 API가 그 스키마를 로드하고 같은 요청 내에서 함수 호출이 이뤄진다. 인터랙션 로그에는 다음과 같은 단계가 남아 디버깅이 가능하다:

"tool_search_call" → "tool_search_result" → "function_call"

자주 쓰는 도구는 앞에서 유지하고 장기 라이브러리(롱테일)는 지연 로드하는 방식으로 구성할 수 있다.

## 클라이언트 측 검색과 MCP 서버와의 통합

자체 도구 레지스트리나 임베딩 인덱스를 운영한다면 `"execution": "client"`로 tool_search를 선언해 앱 쪽에서 검색을 수행할 수 있다. 이 경우 검색당 한 번의 왕복이 추가된다는 점을 Google이 명시했다. 또한 원격 MCP 서버 도구를 `defer_loading: true`로 설정하면 그 서버가 노출하는 도구들을 필요 시에만 불러올 수 있다.

## 비용·모델 지원

Tool Retrieval 자체의 별도 요금은 없고, 입력·출력 토큰은 호출한 모델의 표준 요금으로 청구된다. tool_search 는 작은 고정량의 입력 토큰을 추가하고, 모델이 로드한 각 스키마는 대화의 나머지 기간 동안 입력으로 청구된다. Google은 **Gemini 3.6 이상 모델(모든 Gemini 4 포함)**에서 Interactions API를 통해 지원된다고 밝혔다.

## 실무적 의미

Google 설명에 따르면 이 방식은 별도의 인덱스 구축·호스팅 없이 서버 측에서 검색을 수행하므로 구현 부담을 줄인다. 장점으로는 프롬프트 시작부의 스키마를 제거해 캐시된 프리픽스가 회전되지 않게 하고, 불필요한 스키마를 보내지 않아 토큰·지연을 절감할 수 있다는 점이 있다. 다만 Google은 절감 효과가 실제로 발생하려면 '절대 불러오지 않는 스키마가 불러오는 스키마보다 많을 때'임을 명확히 해, 각 서비스 트래픽 패턴에 맞춰 측정할 것을 권장한다.

근거: Google 블로그 게시물(2026-11-19).

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)

