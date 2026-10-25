---
title: "Show HN: Gemini 4 Argon plays StarCraft"
sidebar_label: "Show HN: Gemini 4 Argon plays StarCraft"
---

# Show HN: Gemini 4 Argon plays StarCraft

> Hacker News · 2026-10-16 · AI 벤치마크

---

StarSkirmish Bench v0.2는 LLM이 1시간의 실시간(벽시계) 동안 C++로 스타크래프트: 브루드워 프로토스 봇을 작성해 경쟁하는 벤치마크로, 이번 업데이트는 OpenAI·Anthropic·Google·Meta·Muse의 플래그십 모델들을 각사의 1st‑party CLI 하니스에서 실행해 결과를 비교했다. 각 모델은 BWAPI 4.4.0과 OpenBW 위에서 동일한 고정 로스터(인간 작성 경쟁 봇과 데모 봇)에 대해 5회 실행한 평균 승률로 점수를 매겼고, GPT‑6 Astra가 1위, GPT‑6.1 Sol이 2위, Gemini 4 Argon이 3위에 올랐다. 그럼에도 최상위 인간 봇들(Stardust, PurpleWave, BananaBrain)과의 격차는 크며, GPT‑6 Astra조차도 이들에 대해 평균 7% 승률에 불과해 한 시간 제약 하에서의 한계가 분명하다.
v0.2는 동일 로스터·평균 승률 방식, 각 실험실의 CLI 하니스와 모델별 최고 추론 설정(단, Gemini 4는 ‘high’)을 적용해 이전 버전과 차이를 뒀다. 실험은 시작 코드(채광만 하는 골격 봇), 데모 봇 소스, FAP·BWEM 라이브러리, 컴파일/연습경기 도구를 제공하고 모델이 연습한 횟수가 성능의 강력한 예측자라는 점을 확인했다. 모델별 런간 변동성은 상당해(예: Gemini 4의 최고·최저 런 차가 18점), 일부 모델은 강한 상대를 일찍 많이 연습해 성능을 끌어올렸고 비용 대비 효율성에서는 GPT‑6.1 Sol이 눈에 띄는 값 우위를 보였다. 또한 컨텍스트는 약 25만 토큰 수준으로 압축 기능을 쓰며 웹 액세스는 차단됐다. 이러한 결과는 장기적 계획과 에러 허용을 요구하는 ‘에이전트형 코딩’ 능력의 실전적 차이를 드러내며, 1시간 제한과 특정 맵·조건으로 인한 제한이 있어 토너먼트 환경 전체를 바로 대체하지는 못한다는 점도 함께 시사한다.

[Hacker News에서 원문 읽기 →](https://starskirmish.com/bench/v0-2/)

