---
title: "Show HN: GolemUI – Declarative Form Engine"
sidebar_label: "Show HN: GolemUI – Declarative Form Engine"
---

# Show HN: GolemUI – Declarative Form Engine

> Hacker News · 2026-07-01 · 웹 개발

---

GolemUI는 JSON 정의를 중심으로 동적 폼을 생성하고, 타입화된 저작 계층을 통해 작성 편의성을 높이며 여러 프레임워크에서 같은 정의를 렌더링할 수 있다는 점을 전면에 둔 오픈소스 폼 엔진입니다. 피드 요약은 JSON 엔진과 28개의 헤드리스 컴포넌트, CSS 변수로 스타일을 제어할 수 있는 방식, Material·Shoelace 등으로 대체 가능한 API, 그리고 LLM으로 생성된 정의를 검증·정형화하는 결정론적 MCP(모델 출력 검증 도구)를 주요 특징으로 제시합니다. 이 설명은 GolemUI가 정의를 DB에 저장·버전 관리하거나 LLM과 결합해 폼 정의를 자동 생성·검증하는 워크플로우를 목표로 삼고 있음을 시사합니다.
사이트에 실린 코드 예제들은 같은 가입(Signup) 폼을 React(react-hook-form 기반), Angular(signals와 schema 검증 사용), LitElement(수동 바인딩과 검증)에서 구현한 모습을 보여줍니다. 각 예제는 이메일·비밀번호 유효성, 계정 유형에 따른 조건부 필드, 숫자 범위 검사, 체크박스 검증 등 동일한 비즈니스 규칙을 각 프레임워크 스타일로 표현해 보이며, 이는 단일 정의를 여러 UI 플랫폼으로 재사용할 수 있다는 주장과 기술적으로 일치합니다. 제공된 정보만 보면 GolemUI는 폼 중복을 줄이고 저작자 경험을 개선할 잠재력이 뚜렷하지만, 실제 운영상 성능·확장성·타 프레임워크 통합 사례 등은 추가 검증이 필요합니다.

[Hacker News에서 원문 읽기 →](https://golemui.com/)

