---
title: "Google's DeepCrossAttention achieves comparable model quality up to 3x faster"
sidebar_label: "Google's DeepCrossAttention achieves comparable model quality up to 3x faster"
description: "Google Research의 DeepCrossAttention(DCA)는 층 간 출력을 깊이별 교차어텐션으로 동적으로 결합해 정보 희석을 완화하고, 동일 품질을 최대 3배 빠르게 달성하거나 특정 벤치마크에서 최대 5배 적은 학습 스텝을 보였으며 파라미터·층 수를 실질적으로 줄였습니다."
---

# Google's DeepCrossAttention achieves comparable model quality up to 3x faster

> Hacker News · 2026-11-27 · AI/ML 모델 아키텍처

---

Google Research가 발표한 DeepCrossAttention(DCA)는 전통적인 트랜스포머의 잔차(residual) 연결을 **층 단위의 깊이별 교차어텐션(depth-wise cross-attention)** 모듈로 일반화해, ‘초기층 정보의 희석(information dilution)’ 문제를 해결하는 접근이다. ICML 2025 논문과 블로그 설명을 통해 DCA는 동일한 모델 품질을 더 빠르게 달성하고 학습 효율을 높인다는 구체적 결과를 제시한다.

## 핵심 변화: 정적 합산에서 동적 선택으로
전통적 잔차 연결은 각 층의 출력에 입력을 점별 합(point-wise summation)해 전달한다. Google은 이 방식이 모든 이전 표현을 동일 가중치로 취급해 깊은 네트워크에서 초기층의 고해상도 특징이 평균화·왜곡되는 ‘정보 희석’을 낳는다고 진단했다. DCA는 각 층에 **경량의 레이어별 모듈**을 추가해 토큰 단위로 어떤 이전 층 표현을 얼마나 반영할지 동적으로 선택·결합한다. 결과적으로 잔차 스트림을 단순 합에서 ‘동적 라우팅’ 문제로 재구성한다.

## 성능·효율성 근거(원문 수치)
- 동일 품질을 얻는 데 **최대 3배 빠름**(블로그 요약). 특정 대규모 텍스트 벤치마크(C4, LM1B)에서는 **최대 5배 적은 학습 스텝**으로 표준 트랜스포머 성능에 도달했다고 보고했다.
- LM1B에서 &lt;14 perplexity를 얻기 위해 표준 트랜스포머는 **42층**가 필요했으나, DCA는 **30층**으로 동일하거나 더 낮은 퍼플렉시티를 달성해 **깊이·파라미터를 29%** 줄였다고 기술했다.
- DCA 자체는 전체 모델 크기에 **0.2% 미만**의 소량 파라미터만 추가하지만, 설계상 더 적은 깊이/파라미터로 동일 성능을 내도록 돕는다. 사전학습 모델에 DCA를 적용해 짧게 추가 학습을 한 경우 LM1B에서 **퍼플렉시티가 0.19 감소**했으며, 동일 조건에서 표준 잔차로 이어 학습한 변화는 **0.02**에 불과했다.

## 기술적 메커니즘과 변형
DCA는 깊이별 출력을 보존해 레이어 간 고해상도 특징을 선택적으로 불러온다. 관련 접근으로 Moonshot AI의 ‘attention residuals’는 레이어별 의사-쿼리(pseudo-query)와 소프트맥스 기반 가중치로 이전 표현을 선택하고, 메모리 비용을 낮추기 위해 블록 단위로 나누는 "Block AttnRes" 변형을 제안했다. Thinking Machines의 Inkling 2도 DCA의 Q/K/V 분리 교차어텐션 메커니즘을 채택했다.

또한 잔차 스트림을 다중 채널로 확장하는 ‘hyper-connections’가 설명되며, 이 방식은 혼합 행렬(mixing matrices)을 통해 정보를 섞어 더 큰 메모리 표현을 제공한다. 다만 무제한 혼합은 신호 증폭·감쇠를 일으켜 불안정해질 수 있어, 이를 완화하기 위해 Sinkhorn–Knopp 알고리즘으로 행렬을 **이중확률(doubly stochastic)** 제약 위에 놓는 ‘manifold-constrained hyper-connections’가 안정적 신호 전달을 복원한다고 보고했다.

## 실무적 함의
- 학습 효율: 같은 학습 예산에서 더 낮은 퍼플렉시티를 얻거나, 동일 품질을 더 적은 스텝으로 달성할 수 있어 대형 모델 학습 비용·시간 최적화에 직접적 이점이 있다(블로그의 수치 근거).
- 마이그레이션: DCA는 표준 잔차 동작으로 초기화할 수 있어 기존 사전학습 모델에 **레트로핏(계속학습)** 방식으로 적용 가능하며, 블로그는 짧은 추가 학습만으로 의미 있는 개선을 확인했다고 기술한다.
- 연산·메모리: DCA는 파라미터 증가가 미미하나, 블로그는 ‘메모리 대역폭’ 증가를 명시했다—이는 레이어별 표현을 보존·제시하기 때문이며, 실제 배포 시 메모리 접근 패턴과 대역폭 고려가 필요함을 시사한다.

원문은 DCA의 실험 결과와 변형 사례(Attention residuals, Block AttnRes, manifold-constrained hyper-connections)를 근거로 동적 라우팅이 다음 세대 트랜스포머 설계에서 중요한 역할을 할 것이라고 전망한다. 기술 독자·엔지니어는 제시된 수치(학습 스텝 비율, 층·파라미터 감소, 퍼플렉시티 개선 등)를 바탕으로 대규모 모델 학습 전략과 사전학습 모델의 레트로핏 적용 가능성을 검토할 만하다.

[Hacker News에서 원문 읽기 →](https://research.google/blog/supercharging-transformer-residual-connections/)

