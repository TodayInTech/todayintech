---
title: "EmbeddingGemma 2: an open, lightweight multimodal embedding model"
sidebar_label: "EmbeddingGemma 2: an open, lightweight multimodal embedding model"
---

# EmbeddingGemma 2: an open, lightweight multimodal embedding model

> Google Blog · 2026-10-06 · 모델 출시/멀티모달 임베딩

---

EmbeddingGemma 2는 텍스트 전용이던 이전 버전에서 확장되어 코드·이미지·비디오·오디오를 단일 임베딩 공간으로 통합한 경량 멀티모달 임베딩 모델입니다. Gemma 4 아키텍처를 기반으로 하며 Apache 2.0 라이선스 하에 배포되는 이 모델은 총 7억4천만 파라미터로 설계되었고, 텍스트 전용 2억7천만 파라미터부터 시각·오디오 인코더를 선택적으로 더해 완전한 멀티모달 구성을 만들 수 있도록 모듈화되어 있습니다. 저자는 MRL(Matryoshka Representation Learning) 기법을 통해 768차원 임베딩을 512·256·128차원으로 동적으로 잘라 저장·메모리 비용을 최대 6배까지 줄일 수 있다고 제시하며, 정량화 적용 시 Google Pixel 11 Pro에서 텍스트 전용은 약 191MB, 전체 멀티모달은 약 567MB의 활성 RAM으로 동작 가능한 등 실제 온디바이스 성능 수치도 공개했습니다.
성능 측면에서 EmbeddingGemma 2는 서브 1B 파라미터 범주에서 텍스트·비전·오디오·코드 벤치마크 성능이 우수하다고 주장하며, 특히 코드 성능에서 MTEB Code 기준으로 68.76에서 78.68로 약 9.92점 향상된 결과를 제시합니다. 8K 토큰(이전 대비 4배) 컨텍스트를 지원해 최대 5.5분 오디오, 29장 이미지, 58개 비디오 프레임 또는 이들의 혼합 입력을 로컬에서 처리할 수 있고, Gemma 4와 토크나이저·오디오 인코더를 공유해 온디바이스 RAG 파이프라인 구성 시 전체 메모리 부담을 낮출 수 있다고 안내합니다. 모델 가중치는 Hugging Face·Kaggle에서 제공되며 LiteRT, MediaPipe, transformers.js·WebGPU 등 다양한 배포 생태계와의 연동 방법, Qdrant 등 벡터 DB 저장·Unsloth의 파인튜닝 가이드 같은 실무 적용 정보도 포함되어 개발자들이 즉시 시도해볼 수 있도록 구성되어 있습니다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)

