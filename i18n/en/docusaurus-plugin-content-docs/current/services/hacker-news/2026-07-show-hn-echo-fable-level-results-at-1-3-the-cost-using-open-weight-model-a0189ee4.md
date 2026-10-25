---
title: "Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models"
sidebar_label: "Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models"
---

# Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models

> Hacker News · 2026-07-23 · AI 모델 오케스트레이션

---

Echo는 단일 모델을 모든 작업에 고정으로 쓰지 않고, 오픈 가중치 모델 풀에서 요청별로 어떤 모델을 참여시킬지와 얼마만큼의 계산을 할당할지를 결정해 출력들을 조합하는 실험적 시스템이다. 작성자는 GLM-5.2, Kimi K2.7 등 여러 모델을 동일한 평가에 돌려 '어떤 문제에 어떤 모델이 유용한지 미리 알고 적절히 결합한다면'이라는 가정의 가상 시스템이 개별 모델보다 훨씬 우수하다는 사실을 확인했고, Echo는 그런 이점을 실제로 사전 정보 없이 어느 정도 회복하려는 시도다. 구현상 일부 프롬프트는 적은 추론만으로 충분하고 다른 요청은 여러 모델의 분업이 유리하다고 보고되며, 흥미롭게도 전반적으로 약한 모델도 특정 문제나 조합에서 유용하게 작동하는 상보성이 발견됐다.
초기 평가에서는 Echo가 풀 내 최상 개별 모델을 일관되게 능가했고, 비교 대상 중 하나인 Fable과 유사한 집계 성능을 대략 1/3 수준의 추론 비용으로 달성했다고 보고한다. 다만 잘못된 계산 배분이나 조합 결정을 내리는 사례가 남아 있어 실패 원인 분석에 집중하고 있으며, 코딩이나 에이전트적 작업처럼 각 결정의 품질을 정량화하기 어려운 영역에서 이 방식이 얼마나 잘 유지되는지 검증하는 작업도 진행 중이다. 실사용 검증을 위해 채팅 인터페이스와 OpenAI 호환 API를 공개했고 평가 방법론 및 개별 모델 결과·비용·제한 사항을 문서화해 외부 테스트와 피드백을 받고자 한다.

[Hacker News에서 원문 읽기 →](https://news.ycombinator.com/item?id=49026810)

