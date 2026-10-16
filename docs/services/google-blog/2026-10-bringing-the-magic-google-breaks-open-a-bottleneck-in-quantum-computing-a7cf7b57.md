---
title: "Bringing the magic: Google breaks open a bottleneck in quantum computing"
sidebar_label: "Bringing the magic: Google breaks open a bottleneck in quantum computing"
---

# Bringing the magic: Google breaks open a bottleneck in quantum computing

> Google Blog · 2026-10-15 · Quantum computing

---

구글 Quantum AI는 ‘매직 상태 재배양(magic state cultivation)’을 실제 하드웨어에서 구현해 양자컴퓨팅의 주요 병목을 실험적으로 해소했다고 발표했습니다. 매직 상태는 보편적 양자연산을 가능하게 하지만 높은 품질로 생성·오류교정하려면 시스템 자원의 대부분이 소모된다는 문제가 있어왔습니다. 연구팀은 2024년 이론을 바탕으로 재배양 개념을 실험적으로 다듬어, 잡음을 포함한 초기 상태를 작은 칩 영역에 주입한 뒤 정교한 측정 연쇄로 결함을 걸러냄으로써 매우 순도 높은 상태를 ‘재배양’하는 방식을 적용했습니다. 그 결과 구글의 Willow 프로세서에서 비재배양 상태 대비 오류를 약 40배 줄였고, T-상태의 논리적 충실도를 99.99%라는 기록 수준으로 달성했다고 보고서에 적시되어 있습니다.
실제 적용 과정에서는 이론을 장비 제어·계측과 맞추는 상당한 공학적 난제가 드러났습니다. 연구진은 측정법 가정에서 비롯된 전기 장비 드리프트와 온도 변동에 따른 잡음을 찾아내어 제어를 추가하고, 재배양을 자체적으로 활용하는 새로운 벤치마크 기법으로 문제를 근본적으로 해결했다고 설명합니다. 또한 거리-3 컬러 코드에서 거리-5 서피스 코드로 상태를 이식(그래프팅)하는 시연을 통해 재배양으로 얻은 정화된 상태가 실무적 오류교정 아키텍처들과 연계될 가능성도 제시합니다. 여전히 대규모 적용과 추가 기술적 과제가 남아 있지만, 이 성과는 매직 상태 생성의 자원 부담을 크게 낮춰 실용적 오류교정 양자컴퓨터에 한걸음 더 가까워졌음을 의미합니다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/)

