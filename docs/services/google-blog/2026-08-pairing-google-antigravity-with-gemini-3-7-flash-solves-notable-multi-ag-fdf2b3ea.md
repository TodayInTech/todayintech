---
title: "Pairing Google Antigravity with Gemini 3.7 Flash solves notable multi-agent math and engineering problems."
sidebar_label: "Pairing Google Antigravity with Gemini 3.7 Flash solves notable multi-agent math and engineering problems."
---

# Pairing Google Antigravity with Gemini 3.7 Flash solves notable multi-agent math and engineering problems.

> Google Blog · 2026-08-31 · Developer tools

---

Google Antigravity는 자율 에이전트 팀이 수 시간에서 수일에 걸쳐 협업·비판·반복 작업을 수행하도록 하는 Teamwork 프레임워크 업데이트와 Gemini 3.7 Flash 모델을 결합해 여러 분야에서 의미 있는 성과를 냈다고 보고했다. 수학 및 이론 컴퓨터과학 분야에서는 FOCS·JMLR급 학회에 해당하는 일곱 개의 미해결 문제를 해결했다고 밝히며, 그중 Knuth의 Cycles 추측을 Lean으로 40쪽이 넘는 증명으로 검증한 사례를 포함했다. 또한 희소 볼록 최적화, 증명 가능한 LLM 양자화, 접두사-행렬 분해 등 다양한 이론적 과제를 해결했고, TCSBench에서 71% 성능을 기록했다.
시스템 측면에서는 사이클 정확도(cycle-accurate)를 목표로 한 비순차 RISC-V CPU 시뮬레이터를 처음부터 구현해 xv6 운영체제를 셸까지 부팅시키는 데 성공했고, 하드웨어 기준 대비 0.71%의 사이클 정렬 오차를 보고했다. 오픈소스 기여도 병행되어 Eigen에 SIMD 경로 최적화, ParlayHash에는 삽입 처리량 2배·메모리 25% 절감 등 핵심 라이브러리 성능 개선이 메인라인에 반영됐다. 이 사례들은 고성능 대형 모델을 다수의 자율 에이전트와 조합하면 형식적 증명·정밀 시뮬레이션·라이브러리 최적화 등 서로 다른 기술 스택에서 실질적 개발 성과를 만들어낼 수 있음을 보여주며, 연구 재현성·엔지니어링 생산성 측면에서 주목할 만한 시사점을 제공한다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/antigravity-teamwork-multi-agent/)

