---
title: "Mistral's Shieldstral: 3B open-weights model for multimodal moderation"
sidebar_label: "Mistral's Shieldstral: 3B open-weights model for multimodal moderation"
---

# Mistral's Shieldstral: 3B open-weights model for multimodal moderation

> Hacker News · 2026-08-04 · 모델/콘텐츠 모더레이션

---

Mistral이 공개한 Shieldstral은 3B 파라미터의 오픈 웨이트 멀티모달 안전 분류기로, 실행 시점에 자연어 정책을 질문 형태로 주면 단일 토큰의 yes/no 로그릿으로 보정된 안전 점수를 반환하는 방식으로 동작한다. 이 '질문응답형' 접근은 텍스트와 이미지, 프롬프트·응답 쌍 등 다양한 입력을 하나의 인터페이스로 통합하고, 정책을 가중치에 고정하지 않아 재학습 없이 다른 배포 환경에 즉시 재타깃팅할 수 있다는 점이 핵심이다. 공개 평가는 텍스트 안전성, 거부 감지, 정책 적응성 및 멀티모달 벤치마크에서 최대 7배 큰 모델과 견주어 동등하거나 더 나은 성능을 보였고, 단일 16GB GPU에서 효율적으로 구동되며 Apache 2.0으로 공개되었다고 밝히고 있다.
기술적 구현은 이 모델의 주장에 힘을 실어준다. 서로 다른 라벨링 규약과 데이터 형태를 instruction–query–document 포맷으로 통합하고, 출처별 엄격도를 조정해 결정 경계를 보정하는 한편, 유사 정책들 사이에서 구별하도록 LLM으로 대조적(contrastive) 리라이트를 생성해 기계가 '구체적 정책 위반'을 판별하도록 훈련했다. 시각 데이터 부족 문제는 일반 이미지 집합을 고품질 네거티브로 보강하고 비전·언어 재랭커로 노이즈를 걸러 보완했으며, LoRA 미세조정과 SLERP 병합으로 공통의 보정·적응성과 기본 지시 수행 능력을 하나의 체크포인트로 결합했다. Forge 플랫폼을 통해 인프라와 분산훈련을 관리했으며, 다국어·긴 문서·확장된 멀티모달 안전성 분야에서 추가 작업을 예고하고 있어, 정책 가변성을 중시하는 제품 환경에서 실용적 대안이 될 가능성이 있다.

[Hacker News에서 원문 읽기 →](https://mistral.ai/news/shieldstral/)

