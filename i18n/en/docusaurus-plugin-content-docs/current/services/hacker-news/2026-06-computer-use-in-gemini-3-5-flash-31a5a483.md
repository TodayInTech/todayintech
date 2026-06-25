---
title: "Computer use in Gemini 3.5 Flash"
sidebar_label: "Computer use in Gemini 3.5 Flash"
---

# Computer use in Gemini 3.5 Flash

> Hacker News · 2026-06-24 · Generative AI / Agents

---

Gemini 3.5 Flash에 'computer use' 기능이 기본 내장되어, 이전의 독립형 모델(Gemini 2.5) 방식에서 메인 Flash 모델로 통합되었다. 이 통합으로 모델은 브라우저·모바일·데스크톱 환경을 넘나들며 관찰(see), 추론(reason), 행동(action)을 수행하는 커스텀 에이전트를 보다 신뢰성 있게 구현할 수 있게 되었고, 함수 호출과 Search·Maps 같은 내장 도구 활용에서 이미 강점을 보이던 점이 확장된다. 글은 특히 장기적·엔터프라이즈 자동화 시나리오—지속적 소프트웨어 테스트나 전문 애플리케이션 전반에 걸친 지식 작업—에서 성능 개선이 기대된다고 설명하며, 구체적 활용 예로 Gemini 앱을 분석해 기능을 분류하거나 자체 문서의 접근성 문제를 감사하는 사례를 제시한다.
안전성 측면에서는 라이브 환경에서 동작하는 에이전트를 위한 리스크 저감책을 강조한다. 타깃형 적대적 훈련(targeted adversarial training)을 도입했고, 기업용으로는 민감·되돌릴 수 없는 행동에 사용자 확인을 요구하거나 간접적 프롬프트 인젝션을 식별하면 작업을 자동 중단하는 두 가지 선택적 안전장치를 제공한다. 또한 샌드박싱, 휴먼 인 더 루프 검증, 엄격한 접근 통제 등 다층 방어(defense-in-depth)를 병행할 것을 권장한다. 개발자는 Browserbase에서 제공하는 데모로 기능을 시험해보고 Gemini API와 Gemini Enterprise Agent Platform의 레퍼런스 구현과 문서를 통해 바로 빌드를 시작할 수 있다. 이 변화는 에이전트형 작업의 적용 범위를 넓히고 엔터프라이즈 도입 문턱을 낮출 수 있으나, 글 자체도 안전 기능의 결합 사용과 운영 환경 통제가 중요하다는 점을 분명히 하고 있다.

[Hacker News에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

