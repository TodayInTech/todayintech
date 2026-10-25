---
title: "Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks"
sidebar_label: "Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks"
---

# Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks

> GitHub Blog · 2026-06-25 · AI &amp; ML

---

GitHub는 Copilot SDK의 공용 구성요소인 'agentic harness'가 여러 제품(예: Copilot CLI, 앱, 코드 리뷰)에 공통으로 적용되며, 도구·컨텍스트·워크플로를 조율해 속도·토큰 효율성·예측 가능성을 높이는 역할을 한다고 설명한다. 글은 Claude Sonnet 4.6·Opus 4.7, GPT‑5.4·GPT‑5.5 등 주요 모델을 대상으로 SWE-bench, SWE-bench Pro, SkillsBench, TerminalBench, Win‑Hill 등 공개·사내 벤치마크와 실사용 지표를 통해 하니스 성능을 반복적으로 평가한 결과를 제시한다. 동일 모델·동일 작업 조건에서 비교할 때 Copilot 하니스는 작업 해결률은 모델 벤더 하니스와 대체로 동등한 수준을 유지하면서 대부분 구성에서 토큰 소비는 더 낮게 나타났고, 이는 토큰 비용 절감과 멀티모델 유연성이라는 실용적 이점을 의미한다.
보고서는 특히 TerminalBench 2.0의 변동성 분석을 통해 결과 재현성(다중 실행의 1σ 범위)과 비용 대비 해결률 간 트레이드오프를 보여준다. GPT 계열 모델은 낮은 비용에서 우수한 가성비를 제공하고, Claude Opus는 높은 해결률을 프리미엄으로 제공하는 등 모델 선택에 따라 효율성과 품질 간 균형을 조정할 수 있다고 밝힌다. 또한 20개 이상의 프런티어 모델을 지원하고 BYO키를 허용하며, 교차모델 비판(예: Rubber Duck) 같은 하니스 수준의 기능을 활용해 단일 모델 기반 하니스보다 확장된 전략을 쓸 수 있다고 정리한다. 방법론적 통제(동일 컨텍스트 창·토큰 한도·추론 노력 설정, 비대화형 단일 턴, 웹 도구 비활성화, 2시간 타임아웃, 각 조합 최소 5회 실행 등)를 명시해 비교의 공정성과 재현성을 확보하려는 의도도 분명히 드러난다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/)

