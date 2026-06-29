---
title: "Qwen 3.6 27B is the sweet spot for local development"
sidebar_label: "Qwen 3.6 27B is the sweet spot for local development"
---

# Qwen 3.6 27B is the sweet spot for local development

> Hacker News · 2026-06-29 · AI/ML

---

저자는 Qwen 3.6 시리즈를 직접 시험하면서, 특히 밀집형(dense) 27B 모델이 로컬 개발 환경에서 ‘무게 대비 성능’이 뛰어나 실용적이라는 결론을 내린다. Qwen 3.6은 MoE(혼합 전문가) 방식의 35B A3B와 dense 27B 두 갈래로 나오는데, 글쓴이는 속도는 35B A3B 쪽이 빠르지만 27B가 출력 품질과 일관성 면에서 우수해 추천한다고 밝힌다. 창작(시 · 주제 혼합)과 코드 생성(예: 헥사곤 지뢰찾기) 같은 실험에서 27B가 단일 프롬프트로 쓸만한 결과를 내었고, 전반적인 온라인 여론과 벤치마크도 27B를 지지한다고 요약한다.
실무 적용 관점에서 글은 구체적 실행 절차와 성능 데이터를 제공한다. llama.cpp와 llama-server를 이용해 Hugging Face의 unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0 같은 8비트 MTP 양자화 모델을 내려받아 실행하는 예제(포트·컨텍스트 크기·플래시 어텐션 등 플래그 포함)를 소개한다. 저자가 Macbook Max M5(128GB)에서 측정한 결과는 약 30 tokens/s, GPU 95% 사용으로 48GB 내에서 동작하며, 사용자 리포트로는 RTX 5090에서 Q6_K·Q4_0 KV 양자화로 123k 컨텍스트에서 50 tokens/s를 얻었다는 사례가 나온다. 글은 8비트 양자화가 공간 절약에 유리하고 품질 저하가 크지 않다고 보면서도, 매우 공격적인 2–4비트 양자화는 품질 저하 가능성이 있음을 경계한다. 결론적으로 저자는 로컬에서의 전반적 실현 가능성, 프라이버시·맞춤화 이점, 그리고 GLM 5.2 같은 더 큰 모델도 기업 예산으로는 로컬 운용이 가능해지는 시대가 다가오고 있음을 강조한다.

[Hacker News에서 원문 읽기 →](https://quesma.com/blog/qwen-36-is-awesome/)

