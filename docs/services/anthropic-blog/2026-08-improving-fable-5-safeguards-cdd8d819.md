---
title: "Improving Fable 5 Safeguards"
sidebar_label: "Improving Fable 5 Safeguards"
---

# Improving Fable 5 Safeguards

> Anthropic Blog · 2026-08-07 · AI 안전·바이오

---

Anthropic은 Claude Fable 5의 생물학 안전장치를 개편해 생물학 관련 질의에서 발생하던 'fallback' 현상을 대폭 줄였다고 밝혔다. 내부 테스트에서 생물학 관련 fallback이 제품 전반에서 약 85% 감소했으며, 플랫폼별로는 Claude.ai에서 약 67%, Cowork 55%, Claude Code 17%, Claude Platform 7%의 감소를 기대한다고 명시했다. Fallback은 분류기가 작동할 때 요청을 더 낮은 능력의 모델(Opus 5)로 우회시키는 현상으로, 이번 업데이트로 일상적 건강·교육 질문(검사 해석, 증상 이해 등)과 임상의 지원에서 사용자들이 더 많은 실질적 도움을 받을 수 있게 됐다고 설명한다. 다만 바이러스학·독성학·분자설계 등 듀얼유즈(유익·유해 양면성) 영역은 여전히 Opus 5로 우회되며, 전문 연구·신약개발용으로는 아직 직접 활용할 수 없다는 한계도 분명히 했다.
안전장치는 핵심적으로 소형 자동 분류기(classifier)에 의존한다는 점을 재확인했다. 분류기는 유해하거나 듀얼유즈로 간주되는 요청을 식별해 Fable 5의 출력을 제한하고 우회시키는 역할을 한다. 초기에는 광범위한 차단을 통해 모델을 일반 사용자에게 우선 개방했으나, 최근 수주간 분류기 규범(콘스티튜션)을 재작성하고 내부·외부 전문가 피드백을 반영해 악의적 사용을 계속 차단하면서도 정상적·유익한 생물학적 질문은 허용하도록 학습 데이터를 업데이트하고 재학습을 진행했다. 그럼에도 불구하고 분류기의 안전 여지(safety margin)로 인한 거짓양성은 잔존하며, Anthropic은 신뢰할 수 있는 접근 경로(trusted access)를 통해 전방위 생물학 역량을 안전하게 개방하는 방안을 지속 개발하겠다고 밝혔다. 이 변화는 AI의 생물의학적 응용을 넓히려는 시도와 동시에 듀얼유즈 위험을 관리하려는 기술적·정책적 균형을 보여준다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)

