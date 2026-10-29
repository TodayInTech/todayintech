---
title: "Build and manage Connected Apps in one place"
sidebar_label: "Build and manage Connected Apps in one place"
description: "Google은 Search와 Gemini 앱에서 작동하는 'Connected Apps Platform' 미리보기를 공개했다. 개발자는 MCP 서버 또는 Android MCP와 AppFunctions APIs로 통합하고 Google Connected Console로 등록·테스트·배포해 Search·Gemini 양쪽에 앱을 노출할 수 있다."
---

# Build and manage Connected Apps in one place

> Google Blog · 2026-10-28 · Developer tools

---

**통합 Connected Apps Platform 미리보기 공개(2026-10-28)**

Google는 Search와 Gemini 앱에서 작동하는 **Connected Apps Platform**의 미리보기를 공개했다고 밝혔다. Google은 블로그에서 개발자가 "한 번 빌드해(Search와 Gemini) 고의도(high-intent) 사용자에게 도달"할 수 있다고 설명했다. 공개된 흐름은 클라우드 호스티드 MCP 서버 또는 Android MCP와의 통합, AppFunctions APIs 사용, 그리고 Google Connected Console을 통한 등록·테스트·제출 절차로 구성된다.

## 개발자 통합 흐름과 관리 기능

블로그에 따르면 개발자는 MCP(클라우드 호스티드 MCP 서버 또는 Android MCP)를 통해 앱 기능을 노출하고, AppFunctions APIs로 동작을 연결한다. 이후 Google Connected Console에서 앱을 등록하고 테스트한 뒤 제출할 수 있다. 제출 전에는 앱을 Search, Gemini 앱, 또는 두 곳 모두에만 공개할지 선택할 수 있다. 라이브 이후에는 트래픽, 지연(latency), 오류율을 추적할 수 있으며, **검증된 로고(verified logos)** 와 인증된 계정을 포함해 브랜드 정체성을 통제할 수 있다.

## 단계적 접근과 파트너 현황

Google은 접근을 단계적으로 개방할 예정이며 향후 더 많은 개발자, 시장, Google 제품을 추가할 계획이라고 밝혔다. 현재까지 Search와 Gemini 간에 걸쳐 **50개 이상의 Connected Apps**가 출시되었고, Adobe·Experian·Localiza·Peloton 등 파트너 통합이 Gemini에서 라이브 상태라고 명시되어 있다. 또한 Calm과의 통합은 Search와 Gemini 양쪽에서 곧 출시될 예정이라고 밝혔다. 미리보기 참여와 문서 확인은 developers.google.com/connected-apps에서 할 수 있다.

## 실무적 의미(분석)

사실: Google의 공지에 따르면 플랫폼은 구체적 API(MCP, AppFunctions)와 관리 콘솔을 통해 개발자에게 배포·관리를 제공한다. 이는 개발자가 동일한 통합 방식으로 두 제품군(검색 인터페이스와 대화형 Gemini 앱)에 앱 기능을 노출할 수 있다는 점에서 배포·유지관리 측면의 작업 중복을 줄여준다. 또한 콘솔에서 지표(트래픽·지연·오류)를 바로 확인하고 브랜드 자산을 통제할 수 있다는 점은 운영·신뢰성 관리에 직접적인 도움을 준다.

제한: Google은 접근을 단계적으로 개방한다고 밝히며, 구체적 시장 범위·심사 기준·요구 권한 범위 등은 공지문에 상세히 기술되지 않았다. 따라서 실제 적용 가능 시점이나 지역별 가용성은 신청 후 문서와 구체 안내를 확인해야 한다.

(근거: Google 블로그 공지 — Build and manage Connected Apps in one place, chunk-0001)

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)

