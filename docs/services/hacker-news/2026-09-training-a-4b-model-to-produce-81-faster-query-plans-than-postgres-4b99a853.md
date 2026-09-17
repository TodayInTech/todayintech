---
title: "Training a 4B model to produce 81% faster query plans than Postgres"
sidebar_label: "Training a 4B model to produce 81% faster query plans than Postgres"
---

# Training a 4B model to produce 81% faster query plans than Postgres

> Hacker News · 2026-09-16 · 데이터베이스·머신러닝

---

쿼리 플래너는 조인 순서와 스캔·조인 알고리듬 조합의 조합 폭 때문에 여전히 어려운 문제이며, 실행 시간이라는 단일 검증 축이 존재한다는 점에서 언어모델을 활용해 ‘빠른 실행’을 직접 최적화하는 접근이 가능하다고 저자는 제시한다. 저자는 pg_hint_plan로 Postgres에게 힌트를 주는 형식으로 문제를 재구성하고, SFT와 에이전트형 강화학습(RL)을 결합해 소형 4B 모델을 후학습시킨 실험을 설명한다. 하이라이트로는 113개의 조인 중심 JOB 쿼리에서 44.7% 평균 지연 감소를 달성했고, 초기엔 99개 쿼리에 대해 플랜을 생성하지 못하던 모델이 개선되었다는 점, 소음 최소화를 위한 측정 리그 구성, 노이즈 환경에 맞춘 GRPO 변형 설계, vLLM과 H100 노드로 학습을 분산한 점, GPT-6 Astra 궤적을 이용한 오프폴리시 증류 등이 제시된다.
실험에서는 반복 실행되는 분석(analytic) 쿼리를 최적화 대상으로 삼는 점을 명확히 하며, 단발성 쿼리 대비 여러 번 실행되는 배치에 대한 기댓값을 올리는 게 목표였다. 측정 안정화를 위해 Postgres 튜닝(예: shared_buffers 2GB, work_mem 4MB)을 고정해 기본 플랜의 실행 시간 자체도 빨라졌고, 평가 지표로 쿼리별 평균을 보는 기하평균 속도 개선과 전체 작업량을 합산해 보는 총 작업 속도 개선을 병행 사용했다. 소형 모델을 선택한 배경엔 저자의 개인 장비(2×RTX 3090) 제약이 있으며, 소형 모델로도 적절한 학습·에이전트 설계와 정밀한 측정이 결합되면 반복적 분석 워크로드에서 Postgres 기본 계획을 실질적으로 능가할 수 있음을 보여준다는 점이 기술적 의의다.

[Hacker News에서 원문 읽기 →](https://rohanbansal.com/qorl)

