---
title: "The harness is all you need (mostly)"
sidebar_label: "The harness is all you need (mostly)"
---

# The harness is all you need (mostly)

> GitHub Blog · 2026-07-27 · AI &amp; ML

---

AI 도구 과다에 압도당하는 대신 ‘하네스(harness)’를 이해하고 일관된 워크플로우를 따르는 것이 생산성 향상에 더 큰 효과를 준다는 주장이 중심이다. 저자는 GitHub Copilot의 다양한 접점(CLI, 앱, VS Code 등)에서 공통으로 작동하는 하네스를 익히라고 권하며, 실무에서는 /allow-all(‘YOLO mode’)로 에이전트에 자율성을 주되 민감한 작업은 Codespaces나 개발 컨테이너 같은 샌드박스에서 실행하라고 권고한다. 초기는 시각적·다양한 변형을 빠르게 만들어보는 프로토타이핑을 통해 요구사항과 미묘한 설계 문제를 드러내고, 그 결과를 바탕으로 계획(/plan) 모드에서 엣지케이스를 체계적으로 질문하며 구현 방향을 다듬는 흐름을 제시한다.
구현 단계에서는 Autopilot이 계획 항목을 반복적으로 완료하도록 하여 모델이 파일 탐색 등 필요한 작업을 수행할 때는 적절한 서브에이전트와 모델을 자동으로 선택한다고 설명한다. 실전에선 중간 규모 모델(예: GPT 5.6 Terra, Claude Sonnet)과 ‘중간(reasoning) 설정’을 추천하고, 동일 모델·이성 수준을 유지하면 프롬프트 캐싱으로 토큰 비용을 절감할 수 있다고 밝힌다. 마지막으로 사람의 심미·품질 판단을 넣어 반복 검토하고, 다른 계열 모델로 검토하는 Rubber Duck 절차로 숨은 문제를 찾아내며 필요하면 Autopilot과 결합해 루프를 돌리라고 권한다. 전반적으로 복잡한 기능이나 최신 기술을 쫓기보다 하네스를 익혀 단순하고 반복 가능한 고품질 결과를 얻으라는 실용적 메시지가 기술적 실무자에게 의미 있는 지침을 제공한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/)

