---
title: "How genome mapping can help researchers better understand disease"
sidebar_label: "How genome mapping can help researchers better understand disease"
description: "Google DeepMind의 AlphaGenome은 부분 서열(100만 염기)로 수천 예측을 생성하고 모든 단일 염기 변이 90억 건의 영향을 예측해 AVI 점수로 우선순위를 제공한다. AlphaGenome 2는 세포 유형 특이성 문제를 해결하려는 모델입니다."
---

# How genome mapping can help researchers better understand disease

> Google Blog · 2026-11-17 · Genomics · AI

---

AlphaGenome은 유전체를 '읽기'에서 변이의 영향을 대규모로 '예측'하는 단계로 옮겼다. Google DeepMind는 2025년 6월에 AlphaGenome을 출시했고, **9억?** — 주의: 원문은 "9 billion"(90억)으로 표기 — 단일 염기 변이(각 염기에 가능한 교체 조합 90억 건)에 대한 예측을 생성해 **AlphaGenome Atlas**라는 대규모 데이터셋으로 공개했다고 밝혔다. 모델은 부분 서열 100만 염기(base pairs)를 입력으로 받아 수천 건의 예측을 산출할 수 있다.

## AlphaGenome Atlas와 AVI 점수

AlphaGenome이 계산한 변이 영향은 **AVI(AlphaGenome Variant Impact) 점수**로 제공되어 연구자가 수백만~수십억 건의 후보 변이 가운데 우선순위를 빠르게 매길 수 있도록 돕는다. 원문 근거로는 연구자가 10억 건의 변이를 좁혀 상위 1%에 주목해 BMI(체질량지수)와 연관된 19개 변이 그룹을 식별한 사례와, Broad Institute 연구진이 AVI 점수를 통해 신경발달장애 관련 유전자의 중요 변이를 찾아 후속 연구(사례 해결)에 결정적 증거를 제공한 사례가 제시돼 있다(chunk-0001).

## AlphaGenome 2: 세포 유형 특이성

AlphaGenome의 한계로 지목됐던 부분은 **세포 유형(cell-type) 특이성**이다. 첫 모델은 주로 전체 조직 또는 세포주(whole tissues or cell lines) 데이터를 기반으로 학습되어 조직 평균에 대한 예측을 제공했다. Google DeepMind는 이를 개선한 **AlphaGenome 2**를 도입해 개별 세포 유형에서 변이가 어떻게 작동하는지를 예측하려 한다고 밝혔다. 이는 질병의 세포 수준 발병 기전을 특정하는 데 중요한 진전이 될 수 있다고 제시된다(chunk-0001).

## 한계와 신뢰도 고려사항

원문은 유전체의 많은 부분이 비암호화 영역(유전자 발현을 조절하는 이른바 'dark matter')으로 남아 있어 실험적 검증(습식 연구, wet-lab)이 필수적이며 비용·시간 부담이 크다고 지적한다. 또한 DeepMind는 모델의 예측 신뢰도를 수치화하는 방법을 적극 연구 중이며, 초기 분석에서는 **강하게 예측된 변이들이 높은 수준의 정확도**를 보인다고 밝혔다. 하지만 그 자체로 확정적 결론을 내리기보다는 다른 근거와 함께 해석해야 한다고 명시되어 있다(chunk-0001, chunk-0002).

## 실무적 의미

AlphaGenome Atlas와 AVI 점수는 희귀질환 원인 변이 탐색, 후보 표적의 우선순위 매김, 약물발견 초기 단계 등에서 '사전 필터' 역할을 할 수 있다. AlphaGenome 2의 세포 유형 예측 능력이 정교해지면 조직 평균으로는 잡히지 않던 세포 특이적 병인 기전 추적에 유용할 가능성이 있다. 다만 DeepMind 스스로도 모델 예측을 보완할 실험적 검증과 신뢰도 지표 개발이 필요함을 밝히고 있어, 당장 임상적 결정에 단독으로 사용하기보다는 연구 가설을 좁히는 도구로 보는 것이 근거에 부합한다(chunk-0001, chunk-0002).

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-disease-research/)

