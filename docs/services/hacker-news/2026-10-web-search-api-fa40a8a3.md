---
title: "Web Search API"
sidebar_label: "Web Search API"
---

# Web Search API

> Hacker News · 2026-10-05 · APIs

---

Cloudflare가 베타로 공개한 Web Search API는 AI 에이전트와 애플리케이션이 인터넷을 직접 검색해 실시간 정보를 근거로 답변을 만들 수 있게 해 준다. 이를 통해 모델의 학습 컷오프나 단순 URL 추측에 의존하는 방식에서 벗어날 수 있다고 설명한다. 런칭 시점에는 Ceramic.ai, Exa, Linkup 세 공급자를 선택할 수 있으며, 세 곳 모두 Cloudflare를 통해 이루어진 요청에 대해 Zero Data Retention을 지원하고 Cloudflare의 검증된 봇 크롤링 기준을 준수한다고 명시돼 있다.
기술적 통합 관점에서 Web Search API는 AI Gateway를 통해 동작해 검색 요청이 게이트웨이 로그에 기록되며, 각 공급자의 공개 API 요금표에 따라 AI Gateway 크레딧으로 청구된다고 안내한다(추가 마크업 없음). 사용자는 공급자 API 키를 직접 가져와 연결할 수도 있고, REST API 호출이나 Worker의 AI 바인딩을 통해 접근할 수 있다. 이 조합은 실시간 웹 근거를 필요한 AI 워크플로에 비교적 간단히 붙일 수 있게 하고, 로그·청구의 중앙화와 데이터 보존 정책 선택이 가능한 점에서 운영·프라이버시 요구를 동시에 고려한 설계라는 기술적 의미를 가진다. 더 자세한 사용 방법은 제공된 가이드를 참고하라고 안내하고 있다.

[Hacker News에서 원문 읽기 →](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

