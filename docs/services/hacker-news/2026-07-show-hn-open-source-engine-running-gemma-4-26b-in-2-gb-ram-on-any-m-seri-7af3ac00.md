---
title: "Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac"
sidebar_label: "Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac"
---

# Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac

> Hacker News · 2026-07-29 · on-device ML / 모델 인퍼런스

---

TurboFieldfare는 Apple 실리콘(macOS 26·Metal 4)에서 Gemma 4 26B-A4B(지침 튜닝)를 약 2GB의 RAM 예산으로 구동하도록 설계된 오픈소스 Swift+Metal 런타임입니다. 핵심 기법은 모델의 공유(.shared) 파트와 FP16 KV 캐시(약 1.35GB)는 메모리에 상주시킨 뒤, 토큰 생성 시 필요한 라우티드(routed) 전문가(expert) 가중치만 SSD에서 스트리밍하는 방식입니다. 라우터는 8비트, 가중치는 4비트 MLX 양자화가 적용되어 전체 설치 용량은 약 14.3GB이고, 설치 과정은 Hugging Face에서 범위 요청으로 바이트 범위를 바로 .gturbo 레이아웃으로 재포장해 디스크에 완전 체크포인트를 만들지 않습니다. 이로써 8GB M2 맥북 에어에서 5–6 tok/s, 24GB M5 Pro에서 31–35 tok/s 수준의 실측 결과를 보고합니다.
구현 측면에서 TurboFieldfare는 Metal 커널(양자화 GEMV·어텐션·MoE·정규화·RoPE 등), 제한된 크기의 전문가 캐시, bounded parallel pread를 활용한 비동기 I/O와 GPU 연산 중복으로 SSD 읽기 지연을 상쇄합니다. 네이티브 Mac 앱·CLI·로컬 OpenAI 호환 루프백 서버(도구 호출은 클라이언트가 승인해야 함)를 제공하며, 텍스트 전용으로 동작합니다. 문서와 코드에는 103개의 실험 기록과 벤치마크, 시스템 디자인(.gturbo 레이아웃, 프리필 전략, 라우터 핸드오프 등)이 포함되어 있어 재현과 타 플랫폼 벤치마크 참여가 가능합니다. 라이선스는 Apache 2.0이며 모델 가중치는 포함되지 않습니다. 전반적으로 이 프로젝트는 MoE·양자화·SSD 스트리밍을 조합해 제한된 메모리 환경에서 대형 모델을 실행하는 실용적 설계와 측정된 성능을 제시한다는 점에서 온디바이스 AI 연구자와 시스템 엔지니어에게 유의미한 사례를 제공합니다.

[Hacker News에서 원문 읽기 →](https://github.com/drumih/turbo-fieldfare)

