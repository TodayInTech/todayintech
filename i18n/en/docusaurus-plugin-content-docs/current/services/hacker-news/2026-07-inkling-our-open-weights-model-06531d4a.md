---
title: "Inkling: Our Open-Weights Model"
sidebar_label: "Inkling: Our Open-Weights Model"
---

# Inkling: Our Open-Weights Model

> Hacker News · 2026-07-15 · AI 모델 공개

---

Thinking Machines가 공개한 Inkling은 전체 가중치를 제공하는 Mixture-of-Experts(MoE) 계열의 멀티모달 기초모델로, 총 975B 파라미터(활성 41B), 최대 1M 토큰 문맥을 지원하며 텍스트·이미지·오디오·비디오 등 45조 토큰 규모의 학습 데이터를 사용해 사전학습됐습니다. 경량형 변형인 Inkling‑Small(276B, 활성 12B)도 함께 예고되었고, 두 모델은 파인튜닝 친화성·멀티모달 능력·컨트롤 가능한 사고(Thinking Effort)로 공개 가중치 기반 커스터마이징의 출발점이 되기를 목표로 합니다. Inkling은 오늘부터 Tinker에서 파인튜닝 가능하며 Playground로 개발자가 직접 체험해볼 수 있고, 전체 체크포인트는 Hugging Face에 NVFP4 등 효율화된 포맷으로 공개되어 여러 인퍼런스·배포 파트너와 통합되어 있습니다.
기술적으로 Inkling은 256개의 라우티드 전문가와 토큰당 6개 활성 전문가를 쓰는 MoE 구조, 시그모이드 기반 라우터, 5:1 비율의 슬라이딩윈도우·글로벌 어텐션 혼합(8 KV 헤드), 상대적 위치 임베딩과 단기 컨볼루션 적용 등 장문 컨텍스트와 효율성을 겨냥한 설계를 채택했습니다. 훈련은 Muon/Adam 하이브리드 옵티마이저와 NVIDIA GB300 NVL72에서 진행되었고, 비동기 RL을 3천만 롤아웃 이상으로 확장해 사고 효율과 추론 스타일 변화를 학습시켰습니다. 실사용 관점에서는 Nemotron 3 Ultra 대비 동일 성능을 내기 위해 토큰 사용량을 3분의1로 줄이는 등 비용·지연 측면의 이점이 강조되지만, 안전성 평가는 외부 테스터와 내부 스펙으로 검증되는 반면 Cognition의 일부 평가에서는 검열 불복종(censorship non-compliance) 패턴이 관찰되었다는 점도 명시하고 있어, 커스터마이징 전후의 안전 거버넌스와 벤치마크 선택이 중요한 실무 고려사항으로 남습니다.

[Hacker News에서 원문 읽기 →](https://thinkingmachines.ai/news/introducing-inkling/)

