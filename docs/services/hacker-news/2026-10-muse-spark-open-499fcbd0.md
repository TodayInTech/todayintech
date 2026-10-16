---
title: "Muse Spark Open"
sidebar_label: "Muse Spark Open"
---

# Muse Spark Open

> Hacker News · 2026-10-15 · 인공지능(대형모델)

---

Meta가 공개 가중치로 내놓은 Muse Spark Open은 데스크톱에서의 강력한 에이전시(Agentic) 역량을 목표로 한 멀티모달 대형모델이다. 문서에 따르면 총 8160억 파라미터(활성 파라미터 420억) 구조에 100만 토큰의 컨텍스트 창을 지원하며, 장기간 작업·복잡한 소프트웨어 엔지니어링·다단계 추론에 최적화되어 있다. 특히 두 대의 Apple M5 Ultra Mac Studio와 최신 MLX 프레임워크를 통해 개인 환경에서 전체 모델이 구동될 수 있다고 설명하는데, M5 Ultra의 통합 메모리(각 기기 최대 512GB)를 활용하면 두 대가 하나의 테라바이트 통합 메모리처럼 동작해 토큰 단위 슬라이스를 빠르게 읽어 처리할 수 있다는 점을 강조하고 있다. Muse Code를 이용해 오픈소스 iOS 클라이언트의 빌드·버그 수정·기능 추가를 온디바이스로 수행하거나, DaVinci Resolve의 프레임별 리뷰·수직 크롭까지 전 과정 에이전트 워크플로를 돌린 테스트를 사례로 제시한다.
배포 측면에서 Muse Spark Open은 Baseten·Fireworks AI·Groq·Modal·Nebius·OpenRouter·Together AI 같은 API 플랫폼을 통해 이용 가능하며, 모델 가중치는 Amazon SageMaker, Google Cloud Model Garden, Hugging Face, Microsoft Foundry Models에서 내려받을 수 있다. 추론 엔진 호환성도 넓어 SGLang, vLLM, TensorRT-LLM, Hugging Face Transformers, Apple MLX, llama.cpp, Unsloth 등에서 구동되며 AMD·Apple·Intel·NVIDIA용 최적화가 마련되어 있다. 또한 Helion GPU 커널을 통해 NVIDIA/AMD에서 커널 수준 1.03–3.95배 속도 향상과 AMD MI350에서 3%의 엔드투엔드 개선을 보고했으며, PyTorch 기반의 추가 튜닝도 지원된다. 공개 가중치 배포에 따른 안전성 고려를 위해 후처리 안전성 작업과 Meta Superintelligence Scaling Framework에 따른 위험 평가를 거쳤고, Muse Model License에 따른 제한적 상업 이용 조건으로 제공된다고 밝히고 있어 개발자·연구자에게 실무적 사용성과 위험 관리 관점에서 의미 있는 정보들을 함께 제공한다.

[Hacker News에서 원문 읽기 →](https://research.meta.ai/blog/muse-spark-open)

