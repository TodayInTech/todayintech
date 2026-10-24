---
title: "DiffusionGemma: 4x faster text generation"
sidebar_label: "DiffusionGemma: 4x faster text generation"
description: "Google이 Apache 2.0으로 공개한 26B MoE 모델 DiffusionGemma는 256토큰 병렬 생성과 반복적 정제를 통해 로컬 GPU에서 최대 4배 빠른 텍스트 생성(예: H100 1000+ tps, RTX 5090 700+ tps)을 목표로 한다. 활성화 시 3.8B 파라미터를 사용하며 품질은 Gemma 4보다 낮아 연구·인터랙티브 작업에 적합하다."
---

# DiffusionGemma: 4x faster text generation

> Google Blog · 2026-06-10 · AI / Models

---

Google이 실험용 오픈 모델 DiffusionGemma를 공개했다. 이 모델은 기존의 토큰 순차 생성(자기회귀) 대신 텍스트 디퓨전 방식을 채택해 전체 텍스트 블록을 병렬로 생성함으로써 로컬 GPU 추론에서 최대 4배 빠른 출력 속도를 목표로 한다. 모델은 Apache 2.0으로 배포된 26B Mixture of Experts(MoE) 구조이며, 추론 시에는 3.8B 파라미터만 활성화된다.

## 병렬 생성과 텍스트 디퓨전 방식
DiffusionGemma는 한 번에 256토큰을 병렬로 생성하고, 랜덤 플레이스홀더 토큰(캔버스)에서 시작해 여러 차례 반복적으로 전체 블록을 정제해 나간다. 각 반복에서 모델은 전체 문단을 평가하고 잘못된 토큰을 고치는 방식으로 자기수정(intelligent self-correction)을 수행한다. 이 접근은 토큰 간 양방향(attention) 관계를 모두 활용할 수 있어 인라인 편집, 코드 인필링, 비선형 텍스트 구조(예: 수학적 그래프, 아미노산 서열) 같은 작업에서 이점이 있다.

## 성능·하드웨어 수치
공식 근거에 따르면 전용 GPU에서 최대 4x 속도 향상을 제공하며, 벤치마크 예시는 NVIDIA H100에서 1000+ 토큰/초, NVIDIA GeForce RTX 5090에서 700+ 토큰/초다. 모델은 양방향 병렬 디코딩으로 디코드 병목을 메모리 대역폭에서 연산으로 이동시키며, 양자화하면 고급 소비자 GPU의 18GB VRAM 한계 내에서 구동 가능하다고 명시돼 있다.

## 품질-속도 트레이드오프와 권장 용도
Google은 DiffusionGemma가 속도와 병렬 레이아웃을 우선하다 보니 전체 출력 품질은 표준 Gemma 4보다 낮다고 명시했다. 따라서 최대 품질이 필요한 프로덕션 애플리케이션에는 Gemma 4 사용을 권장한다. 반대로 지연(latency)과 상호작용성이 중요한 로컬·저동시성 환경(예: 실시간 편집, 빠른 반복 실험, 퍼즐·비선형 문제 해결)에서는 DiffusionGemma의 장점이 뚜렷하다. 예시로 Unsloth가 수도쿠 해결에 파인튜닝해 활용한 사례가 소개되어 있다.

## 배포·최적화 경로
모델 가중치는 Hugging Face에 공개되어 있으며, MLX, vLLM(레드햇 통합 지원), Hugging Face Transformers를 통한 서빙을 권장한다. 파인튜닝 도구로는 JAX 기반의 Hackable Diffusion, Unsloth, NVIDIA NeMo 예제가 제공된다. NVIDIA와 협력해 GeForce RTX 5090·4090용 양자화 최적화와 엔터프라이즈용 Hopper·Blackwell에서 NVFP4(4-bit floating-point) 커널 최적화를 적용했으며, NVFP4는 거의 손실 없는 정확도로 연산 처리량을 높이는 역할을 한다. 또한 Gemini Enterprise Agent Platform Model Garden과 NVIDIA NIM을 통한 클라우드 실행이 가능하고, llama.cpp에 대한 공식 지원은 곧 제공될 예정이다.

## 실무적 의미
DiffusionGemma는 로컬 단일 가속기 환경에서의 응답성 개선을 목표로 설계됐다. 고빈도 다중 요청(고 QPS) 클라우드 환경에서는 자기회귀 모델의 배치 이점 때문에 DiffusionGemma의 상대적 이점이 줄어들 수 있다는 점도 문서에 명시돼 있다. 따라서 개발자와 연구자는 용도(저지연 인터랙션 vs 고품질 대량 서빙)에 따라 DiffusionGemma와 Gemma 4 중 적절한 모델을 선택하고, 필요시 공개된 파인튜닝 경로와 하드웨어 최적화(NVFP4, 양자화)를 활용해 성능을 조정하면 된다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)

