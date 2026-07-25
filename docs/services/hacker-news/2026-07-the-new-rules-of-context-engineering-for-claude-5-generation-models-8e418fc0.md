---
title: "The new rules of context engineering for Claude 5 generation models"
sidebar_label: "The new rules of context engineering for Claude 5 generation models"
---

# The new rules of context engineering for Claude 5 generation models

> Hacker News · 2026-07-25 · 인공지능

---

Anthropic의 글은 최신 Claude 5 계열 모델에서 관찰된 능력 향상이 맥락 엔지니어링의 관행을 어떻게 바꿔야 하는지를 실무적으로 정리한다. 핵심 발견은 Claude Code의 시스템 프롬프트를 80% 이상 제거해도 코드 관련 평가에서 유의미한 성능 저하가 나타나지 않았다는 점이다. 과거에는 삭제나 부적절한 출력 같은 최악의 경우를 막기 위해 과도하게 규칙을 부여하거나 예시를 반복하고, 많은 정보를 시스템 프롬프트와 CLAUDE.md에 집약해 두는 일이 필요했지만, 최신 모델은 더 나은 판단력과 점진적 맥락 로딩(progressive disclosure)을 활용해 제한을 완화해도 올바른 결정을 내린다. 글은 '규칙을 주기보다 판단에 맡기기', '예시 대신 인터페이스 설계', '모든 걸 앞쪽에 두지 말고 점진적으로 드러내기', '반복 대신 간단한 도구 설명' 같은 대조적 원칙들을 제시한다.
실무 적용 측면에서 권장하는 변화도 구체적이다. 시스템 프롬프트는 제품 맥락을 정의하는 핵심 위치로 남기되 과도한 세부 규칙은 피하고, CLAUDE.md는 가벼운 개요와 코드베이스의 특이점(gotchas)에 토큰을 집중하라. 스킬(Skills)은 필요할 때 불러오는 경량 가이드로 설계하고, 큰 스킬은 분할해 점진적 로딩을 활용하라고 권한다. 참조 자료는 가능한 코드나 HTML 같은 고충실도 아티팩트를 우선하고, 루브릭(rubrics)과 검증 에이전트를 통한 동적 검증도 추천한다. 또한 자동 메모리와 artifacts, Task 도구의 지연 로딩 같은 새로운 인프라를 활용해 컨텍스트를 선택적으로 불러오는 전략을 권장하며, 이를 돕는 명령어로 claude doctor를 소개한다. 저자는 Thariq Shihipar(Anthropic)로, 제시된 권고는 Claude Code 운영 경험을 바탕으로 최신 모델 특성에 맞춰 맥락 설계를 단순화하고 더 표현력 있는 도구 설계를 촉진하려는 실무적 제안이다.

[Hacker News에서 원문 읽기 →](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)

