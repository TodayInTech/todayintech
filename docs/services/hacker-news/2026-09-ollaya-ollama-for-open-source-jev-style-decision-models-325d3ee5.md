---
title: "Ollaya – Ollama for open-source, Jev-style decision models"
sidebar_label: "Ollaya – Ollama for open-source, Jev-style decision models"
---

# Ollaya – Ollama for open-source, Jev-style decision models

> Hacker News · 2026-09-25 · AI/ML

---

Ollaya는 '결정(decision) 모델'을 로컬 환경에서 동작시키도록 설계된 오픈 소스 런타임으로, 텍스트나 JSON에 대해 타입화된 질문을 던지면 보정된 확률과 선택지를 단일 포워드 패스에서 밀리초 단위로 반환한다고 설명한다. 문서에는 예시 응답과 함께 'laya' 등 모델을 이용한 다섯 질문 요청이 로컬 GPU에서 HTTP API 경로를 통해 대략 8–10ms(또는 약 10ms) 수준으로 처리된다고 적혀 있으며, 호스팅 API의 중간 응답(236–276ms)과 비교해 로컬 실행의 속도 이점이 강조되어 있다. 또한 /v1/systemone, /v1/models 같은 TypeSafe 호환 엔드포인트를 제공해 기존 TypeSafe Python SDK를 변경 없이 사용할 수 있음을 보인다(예시 curl 요청과 'invoice' 선택 응답의 확률·confidence 필드 포함).
제품은 여러 공개 모델을 모아 제공하는데, laya(가장 빠름), decider(정확도 우수), von(8k 토큰 컨텍스트), qwen3guard(안전성 판정) 등 용도별 모델을 나열하고 각 모델의 정확도·속도를 안내한다. 가중치는 원저자의 Hugging Face 리포지토리에서 커밋 고정·sha256 검사로 내려받고 Ollaya가 가중치를 재호스팅하지 않는다고 명시하며, 런타임은 Apache-2.0이다. 로컬 기본은 127.0.0.1 리스닝이며 ONNX Runtime을 통해 CPU 또는 NVIDIA GPU(WSL2, CUDA 13 등)를 지원하고 macOS·Windows·Linux용 데스크톱 앱과 커맨드라인, Docker 이미지를 제공해 실제 배포 환경에 맞춰 설치하기 쉽다고 밝힌다. 과금 없이 하드웨어 한도까지 처리할 수 있고(토큰별 비용 없음), 모델별 보정된 확률과 라벨 데이터로 재적합하는 Modelfile 기능을 통해 사후 임계값 설정이 가능해 프라이버시가 중요한 분류·안전성 검사 파이프라인이나 비용 제약이 있는 로컬 배포에 실용적이라는 기술적 함의를 가진다.

[Hacker News에서 원문 읽기 →](https://ollaya.dev/)

