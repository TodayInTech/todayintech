---
title: "GLM-5.2 – How to Run Locally"
sidebar_label: "GLM-5.2 – How to Run Locally"
---

# GLM-5.2 – How to Run Locally

> Hacker News · 2026-06-22 · 모델·인프라

---

Z.ai의 GLM-5.2을 Unsloth가 공개한 문서에 따르면, 이 모델은 744B 파라미터(활성 40B)와 1,048,576 토큰의 최대 컨텍스트를 지원하며 Unsloth Dynamic GGUF 포맷으로 로컬에서 실행할 수 있도록 배포됐다. 문서는 GLM-5.2가 일부 벤치마크에서 Claude 4.8 Opus, GPT-5.5, Gemini 3.1 Pro와 동등한 수준의 성능을 보인다고 주장하며, 2-bit(UD-IQ2_M) 양자화는 239GB 디스크를 사용해 256GB 통합메모리 Mac이나 1×24GB GPU + 256GB RAM 구성에서 동작한다고 구체적으로 안내한다. 또한 'thinking' 모드(High/Max/비활성화)와 reasoning 설정을 --chat-template-kwargs 또는 llama.cpp의 --reasoning on/off로 제어하는 방법, 추천 추론 파라미터와 GGUF 파일 경로 등 로컬 실행에 필요한 실무적 지침을 담고 있다.
문서는 동적 양자화의 성능-크기 절충을 수치로 보여준다: 1-bit 동적 양자화는 약 76.2% top-1 정확도를 유지하면서 모델 크기를 86% 줄였고, 2-bit는 약 82% 정확도에 84% 축소를 기록한다고 설명한다. KLD(평균 KL 발산) 샘플링을 통해 양자화 품질을 평가하며, 동적 양자화는 중요 레이어를 더 높은 비트로 남겨두는 방식으로 큰 손실 없이 용량을 줄일 수 있다고 밝힌다. 장기 컨텍스트를 위해서는 KV 캐시 양자화(q4_0, q4_1 등)를 활용하면 컨텍스트 길이를 수배로 늘릴 수 있다는 구체적 제안도 포함되어 있어, 대용량 컨텍스트와 로컬 하드웨어 제약을 고려하는 엔지니어에게 즉시 적용 가능한 실무적 가이드라인을 제공한다.

[Hacker News에서 원문 읽기 →](https://unsloth.ai/docs/models/glm-5.2)

