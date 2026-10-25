---
title: "I built non-autoregressive decision models with RL a year ago"
sidebar_label: "I built non-autoregressive decision models with RL a year ago"
---

# I built non-autoregressive decision models with RL a year ago

> Hacker News · 2026-09-19 · 모델 출시·연구

---

작성자는 2025년부터 강화학습 기반의 비자기회귀(non-autoregressive) 결정 모델을 연구해온 결과물로서 'Laya'라는 오픈 소스 System 1 계열 모델군을 공개했다. 이 접근은 텍스트 생성을 하지 않고 구조화된 스키마에 대해 확률분포를 빠르게 예측하는 것을 목표로 하며, 핵심은 PPO 등 RL을 이용한 학습과 이후 제안된 RLCD 프레임워크에 있다. 생성형 LLM을 단순 분류·루팅·가드레일 용도로 쓰는 것은 과도한 비용과 지연, 그리고 '위험한' 확신 점수(토큰 예측에 불과한 confidence)를 낳기 때문에, 저자는 응답을 텍스트가 아닌 확률과 숫자로만 반환하는 세 가지 원시(primitive)—choice, score, noul—을 도입해 환각을 물리적으로 배제했다고 설명한다. 또한 모델은 Apache 2.0으로 공개되어 자체 호스팅이 가능하고 허깅페이스·GitHub·PyPI 등으로 배포된다.
기술적 의의는 실용성에 맞춘 속도·보정·다국어 라우팅에 있다. bidirectional 인코더 기반의 체크포인트들은 단일 GPU에서 P50 32.8ms(배치 시 질문당 7.2ms)로 동작해, 저자가 인용한 TypeSafe Jev보다 6–8배 빠르며(제3자 및 회사 보고서 비교), 여러 공개 벤치마크에서의 우수한 정확도(예: typed-decisions 0.766 vs Jev 0.727, AG News 0.950 vs 0.910)와 더 나은 캘리브레이션(ECE 0.081 vs 0.246)을 제시한다. 다만 한계도 솔직히 제시되어 있는데, 선택지 수가 20개를 넘으면 성능 저하(예: Banking77 스트레스 테스트)와 제로샷 한계(기본 모델은 타겟 벤치마크에서 약 0.35) 등으로 실제 배치 시 미세조정·온도 보정·계층적 라우팅 설계가 권장된다. 입력 스크립트를 사전 감지해 모델을 선택하는 라우터(22개 알파벳 감지, preload로 콜드스왑 제거)와 구체적 실행 예제·데모·파인튜닝 노트북도 함께 제공되어, 대량의 구조화된 의사결정·가드레일·티켓 라우팅 등 실무용 빠른 추론 계층으로서 의미있는 대안임을 보여준다.

[Hacker News에서 원문 읽기 →](https://laya.convaiinnovations.com/)

