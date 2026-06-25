---
title: "VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO"
sidebar_label: "VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO"
---

# VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO

> Hacker News · 2026-06-23 · Artificial Intelligence

---

VibeThinker-3B는 3억이 아닌 30억(3B) 파라미터 규모의 조밀한(sparse가 아닌 dense) 소형 언어모델로, ‘검증 가능한 추론(verifiable reasoning)’을 소형 모델 계열에서 어디까지 끌어올릴 수 있는지를 실험적으로 탐구한 기술 보고서의 중심 주제입니다. 저자들은 Spectrum-to-Signal 후처리(post-training) 패러다임을 바탕으로, 커리큘럼 기반의 감독 미세조정(curriculum SFT), 멀티도메인 강화학습(multi-domain RL), 오프라인 자기증류(offline self-distillation)를 결합한 최적화 파이프라인을 제시하고, 이를 통해 소형 모델이 복잡한 검증형 과제를 처리할 수 있음을 보이고자 합니다.
실험 결과는 구체적 수치로 제시되어 있습니다. AIME26에서 94.3점을 기록했고, 주장 수준의 테스트타임 스케일링(claim-level test-time scaling)을 적용하면 97.1로 개선되며, LiveCodeBench v6에서는 Pass@1 80.2를 달성했습니다. 최근 미공개 LeetCode 콘테스트에 대한 OOD(분포 밖) 일반화 관찰에서는 96.1%의 수락율을 보였고, IFEval 93.4점은 엄격한 지시(instruction) 제어성도 해치지 않았음을 시사합니다. 보고서는 이러한 성과를 기반으로 ‘Parametric Compression-Coverage Hypothesis’를 제안하며, 검증 가능한 추론은 압축 가능한(reasoning cores) 반면, 개방형 지식과 장기 꼬리(long-tail) 시나리오는 광범위한 파라미터 커버리지가 필요하다고 주장합니다. 제공된 근거만 보면 이 연구는 소형 모델이 배포 효율성뿐 아니라 추론 성능 면에서도 일군의 대형 모델들과 경쟁하거나 이를 능가할 수 있다는 실증적 근거를 제시해, 소형 모델 설계와 훈련 전략을 재검토하게 만드는 기술적 함의를 갖습니다.

[Hacker News에서 원문 읽기 →](https://arxiv.org/abs/2606.16140)

