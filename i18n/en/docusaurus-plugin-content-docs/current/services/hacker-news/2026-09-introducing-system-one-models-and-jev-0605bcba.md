---
title: "Introducing System One Models and Jev"
sidebar_label: "Introducing System One Models and Jev"
---

# Introducing System One Models and Jev

> Hacker News · 2026-09-15 · 인공지능/머신러닝

---

TypeSafe AI가 발표한 'System One' 모델 계열과 첫 공개 모델 Jev는 기존의 생성형 LLM과는 다른 설계 철학을 내세웁니다. Jev는 문자열 생성을 포기하는 대신 사전에 정의된 타입-안전(타입 안전 출력) 구조와 교정된 확률(모든 출력에 신뢰도 표기)을 반환하도록 최적화되어 소프트웨어가 그대로 소비할 수 있는 결정값을 내보냅니다. 이를 위해 병렬 샘플러와 새로운 학습법인 Reinforcement Learning for Calibrated Decisions(RLCD)을 도입했고, 그 결과 응답 속도는 70ms–500ms 수준으로 같은 수준의 ‘System One’ 지능을 내는 기존 모델 대비 40×–200× 빠르다고 주장합니다. 비용 모델과 토큰 단가(입력 $0.042/MTok 등)도 공개해 실무 적용 가능성을 강조합니다.
평가 측면에서 TypeSafe는 코드 내 워크플로우 성능을 비교하는 별도의 워크플로우 평가를 도입해 GPT-6 Astra와 Fable 5.1의 평균을 기준 참조로 삼았습니다. 이 평가에서 Jev는 Pareto 전선을 점유하며 최대 수백 배의 속도·비용 이점을 보고했으나, 저자가 스스로 인정하듯 데모와 평가의 일부는 자사 환경(서부 해안 노트북)과 평가팀 설계 영향, 참조 모델 평균에 따른 편향 가능성 등 한계가 있습니다. 또한 Jev는 문자열 유연성을 포기하는 대신 환각(hallucination)과 타입 오류를 제거했다고 주장하지만, 이들 주장의 일부는 수학적 보장 또는 비공개·초기검증 방식에 의존하므로 도입 전 실제 워크로드에서의 검증이 필요합니다. 이 기술은 실시간 UX, 대규모 데이터 맵리듀스, 자동화된 의사결정·검증 파이프라인 등에서 특히 의미가 클 것으로 보입니다.

[Hacker News에서 원문 읽기 →](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

