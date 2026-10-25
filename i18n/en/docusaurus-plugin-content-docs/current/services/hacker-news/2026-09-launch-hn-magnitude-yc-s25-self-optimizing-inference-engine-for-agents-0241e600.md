---
title: "Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents"
sidebar_label: "Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents"
---

# Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents

> Hacker News · 2026-09-30 · 머신러닝/추론엔진

---

피드 기준으로는 Anders와 Tom이 발표한 Magnitude는 에이전트 실행에 맞춰 스스로 성능을 최적화하는 추론 엔진을 표방한다. Mac·Linux·Windows의 다양한 하드웨어에서 동작하며 llama.cpp 대비 최대 2배 빠르다고 주장하고, 기존 엔진들이 배치 최적화·범용성·특정 하드웨어 특화의 트레이드오프를 겪는다고 진단한다. 또한 로컬에서 여러 장기 세션을 돌리는 에이전트 사용 사례를 목표로 삼고 있다.
피드에 따르면 Magnitude는 장치 내 컴파일 및 튜닝으로 하드웨어별 파라미터를 조정하고, 인기 오픈 웨이트 계열을 대상으로 튜닝 가능한 고효율 커널을 제공해 성능 한계를 끌어올리려 한다. 초기 메모리는 가중치만 예약하고 세션 확장에 따라 동적으로 힙을 늘렸다가 해제하는 동적 메모리 할당과, 동시 실행을 고려한 하이브리드 페이징 어텐션 등의 설계가 강조된다. 다만 제공된 요약만으로는 세부 벤치마크나 광범위한 호환성 검증의 범위가 충분히 드러나지 않으므로, 실제 성능과 구현 범위는 추가 근거 확인이 필요하다.

[Hacker News에서 원문 읽기 →](https://github.com/magnitudedev/magnitude)

