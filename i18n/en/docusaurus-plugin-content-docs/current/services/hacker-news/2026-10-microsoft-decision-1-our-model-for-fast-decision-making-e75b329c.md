---
title: "Microsoft-Decision-1, our model for fast decision-making"
sidebar_label: "Microsoft-Decision-1, our model for fast decision-making"
---

# Microsoft-Decision-1, our model for fast decision-making

> Hacker News · 2026-10-09 · AI 모델

---

마이크로소프트는 텍스트 생성용 LLM과 구분되는 ‘의사결정(decision) 모델’ 분야에서 새 모델 Microsoft-Decision-1을 공개했다. 이 모델은 라우팅, 분류, 우선순위 판단, 검증과 워크플로 제어 같은 구조화된 출력이 즉시 소프트웨어에 적용되는 작업을 목표로 설계되었으며, Microsoft Foundry와 OpenRouter를 통해 제공된다. 문서에서는 Microsoft-Decision-1이 36개 벤치마크(약 15만 질문, 학습에서 블라인드된 항목 포함)에서 최고 정확도를 기록했고, 지연 측면에서도 Quyet-1.0-Large보다 4.5배, GPT-6 Sol보다 35배 빠르다고 주장한다. 기술적 구현은 Qwen3.5-9B 기반의 단일 패스 결정 점수화 방식으로, 예/아니오·객관식·평점·루브릭 기반 채점 등을 구조화된 API로 지원하며 각 선택지에 대한 보정된 확률 값을 반환하는 점이 강조된다.
성능 검증과 운영적 고려사항도 상세히 다뤄졌다. 속도는 연쇄적 의사결정에서 지연 누적을 줄이는 핵심 요구로 제시되며, 공개된 벤치마크 전반에서의 일반화 능력과 강건성(입력 변형 8가지 방식에 대한 평균 결정 전환율 1.3%, 옵션 서술·순서 변경에는 전환 없음)을 근거로 신뢰성을 확보했다고 설명한다. 또한 확률 보정과 안전성 테스트(5,250개 요청·11개 벤치마크)를 통해 유해 요청은 거부하면서도 실용성을 유지한다고 밝힌다. 내부 적용 사례로는 XBOX의 피드백 라벨링(품질 유사, 속도 14배·비용 200배 절감), Copilot 품질 관리(경쟁 모델과 유사한 품질, 100배 빠름), 실험 재계획에서의 일관성과 속도 개선(LLM 기반 대비 46배 일관성, 3배 속도)을 제시하며, 입력 토큰 비용($0.042/백만 토큰, 출력 무료)과 향후 MAI·OpenAI 계열로의 리베이스 계획도 함께 언급되어 개발자·시스템 설계자 관점에서 의사결정 모델을 기존 에이전트·프로그래밍 워크플로에 통합할 때의 성능·비용·안전 트레이드오프를 판단하는 데 유용한 근거를 제공한다.

[Hacker News에서 원문 읽기 →](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)

