---
title: "Mistral's Robostral Navigate: a state of the art robotics navigation model"
sidebar_label: "Mistral's Robostral Navigate: a state of the art robotics navigation model"
---

# Mistral's Robostral Navigate: a state of the art robotics navigation model

> Hacker News · 2026-07-08 · robotics/embodied AI

---

Mistral이 발표한 Robostral Navigate는 8B 파라미터 크기의 내비게이션 모델로, 단 하나의 RGB 카메라와 자연어 지시만으로 로봇이 복합 환경을 자율 주행하도록 설계되었다고 소개합니다. R2R-CE 검증 unseen에서 76.6% 성공률을 기록해 단일 카메라 최선 접근법보다 9.7포인트, 깊이·다중 카메라를 쓴 최고 시스템보다 4.5포인트 높은 성능을 냈다는 점을 전면에 내세우며, validation seen에서는 79.4%를 보고합니다. 모델은 휠·다리·비행형 로봇 등 다양한 플랫폼과 카메라 내재성 차이를 견디도록 일반화되며, 실세계에서 보여주지 않은 사람과 장애물에도 적응해 장기간 지시를 완수할 수 있다고 주장합니다.
기술적으로는 시뮬레이션으로 생성한 약 40만 개의 궤적(6,000개 장면)으로 전량 학습을 진행했고, 외부 오픈소스 VLM에 의존하지 않고 자체 비전-언어 모델을 초기화점으로 삼아 위치 추정(포인팅) 능력을 기반으로 이동 결정을 내립니다. 포인팅으로 이미지 좌표와 도착 시 원활한 자세를 예측하고, 시야 밖 목표에 대해서는 로컬 좌표계의 거리·회전 명령으로 보완합니다. 학습 효율을 높이기 위해 prefix-caching과 트리 기반 어텐션 마스킹으로 전체 에피소드를 하나의 시퀀스로 압축해 토큰 수를 22배 줄였고, 감독학습 이후 CISPO라는 온라인 강화학습 단계로 시행착오를 통해 성능을 추가로 3.2% 향상시켰다고 밝힙니다. 이 조합은 소형 모델과 단일 RGB 센서로도 고성능의 임베디드 내비게이션을 달성할 수 있음을 보여주며, 내비게이션을 통합된 임베디드 에이전트의 기초 역량으로 삼겠다는 향후 방향성을 제시합니다.

[Hacker News에서 원문 읽기 →](https://mistral.ai/news/robostral-navigate/)

