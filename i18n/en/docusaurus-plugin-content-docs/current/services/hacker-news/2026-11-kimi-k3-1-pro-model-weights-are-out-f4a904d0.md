---
title: "Kimi K3.1 Pro model weights are out"
sidebar_label: "Kimi K3.1 Pro model weights are out"
description: "Moonshot의 Kimi K3.1 Pro 가중치가 공개됐다. **총 2.8T, 활성화 104B, 1백만 토큰(context length 1,048,576)** 지원하는 MoE 기반 멀티모달 에이전트 모델로, OpenAI/Anthropic 호환 API와 플랫폼 배포가 제공된다."
---

# Kimi K3.1 Pro model weights are out

> Hacker News · 2026-11-04 · AI 모델/프레임워크

---

Moonshot의 Kimi K3.1 Pro 모델 가중치가 공개되었다. 공개 페이지에 따르면 K3.1 Pro는 **오픈 가중치(open-weight)**로 배포되는 '네이티브 멀티모달 에이전트' 모델이며, 회사는 이를 자사 기준에서 가장 능력있는 **3T급 모델**이라고 소개한다.

## 설계와 주요 사양
- **총 파라미터 2.8T**, 활성화(activated) 파라미터 **104B**. 레이어 수는 **93**.
- 문맥 길이는 **1,048,576 토큰(약 1백만 토큰)**으로 매우 긴 컨텍스트를 지원한다.
- 아키텍처는 Mixture-of-Experts(MoE)를 채택: **전문가(Experts) 수 896**, 토큰당 선택 전문가 수 **16**, 공유 전문가 수 **2**.
- 어텐션 구성은 **KDA와 Gated DSA(DeepSeek Sparse Attention)** 혼합을 사용하며, Kimi K3 대비 Gated MLA 레이어를 Gated DSA로 교체해 장문 컨텍스트 효율을 개선했다고 명시된다.
- 비전 인코더는 **MoonViT-V2(401M 파라미터)**이며, 모달리티는 텍스트·이미지 둘 다 지원.
- 활성화 함수는 **SiTU-GLU**, 어텐션 헤드 수 **96**, 어텐션 히든 차원 **7168** 등 세부값이 공개되어 있다.
- 양자화는 **MXFP4(가중치) / MXFP8(활성화)** 형태로 양자화 인지 학습(quantization-aware training)을 거쳤다고 표기된다.

## API·사용 방식 및 호환성
Kimi K3.1 Pro는 웹 플랫폼(https://platform.kimi.ai)에 API로 배포되며, **OpenAI/Anthropic 호환 API**를 제공한다고 명시된다. 모델의 사고(추론) 과정을 제어하는 최상위 요청 필드로 **reasoning_effort**("low"/"high"/"max", 기본 "max")를 지원한다.
특히 멀티턴 대화나 도구 호출(tool calls)을 사용하는 경우, API는 어시스턴트 메시지의 **reasoning_content와 tool_calls를 포함한 전체 응답(assistant message)을 그대로 messages로 다시 전달**할 것을 요구한다. 문서에 포함된 간단한 예시는 다음과 같다:

&#105;mport openai

def chat_with_preserved_thinking(client: openai.OpenAI, model_name: str):
    messages = \[
        &#123; "role": "user", "content": "Tell me three random numbers." &#125;,
        &#123; "role": "assistant", "reasoning_content": "I'll start by listing five numbers: 473, 921, 235, 215, 222, and I'll tell you the first three.", "content": "473, 921, 235" &#125;,
        &#123; "role": "user", "content": "What are the other two numbers you have in mind?" &#125;
    \]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        max_tokens=4096,
        reasoning_effort="max",
    )
    print(f"response: &#123;response.choices\[0\].message.reasoning&#125;")
    return response.choices\[0\].message.content

이 예시는 어시스턴트의 내부 추론(reasoning_content)을 응답 흐름 안에 보존하고 재전달해야 모델이 기대한 동작을 계속 재현함을 보여준다.

## 평가와 비교·운용 주의점
공개 문서는 K3.1 Pro 성능을 다양한 벤치마크(예: Terminal-Bench, ProgramBench, DeepSWE, BenchCAD, ExploitBench 등)에서 제시하지만, 평가마다 사용한 하니스(harness)와 심사 모델이 다르다고 명시한다. 예를 들어 여러 비교에서는 Claude Code 또는 Kimi Code를 사용해 평가했고, 일부 내부 평가는 서로 다른 GPU(H20 vs H100)에서 수행되었다. 따라서 표에 제시된 점수는 **각 벤치마크의 평가 설정과 비교 조건을 함께 살펴봐야 한다**.

또한 Kimi K3.1 Pro는 **Kimi K3.1 Pro License**로 배포되며, 문의는 support@moonshot.ai로 안내되어 있다. 공개 페이지의 다운로드 수는 최근 한 달 **797회**로 표기되어 있다.

근거에 기반한 사실만을 정리하면, Kimi K3.1 Pro는 긴 컨텍스트·멀티모달·에이전트 워크플로를 전제로 한 고사양 MoE 모델로 설계되었고, API 사용 시 내부 추론 표현을 보존하는 것과 같은 운영·호환성 요구가 존재한다. 벤치마크 수치는 문서에 제시된 평가 환경에 따라 달라지므로, 실제 비교·도입을 검토할 때는 해당 벤치마크의 하니스와 설정을 함께 확인해야 한다.

[Hacker News에서 원문 읽기 →](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

