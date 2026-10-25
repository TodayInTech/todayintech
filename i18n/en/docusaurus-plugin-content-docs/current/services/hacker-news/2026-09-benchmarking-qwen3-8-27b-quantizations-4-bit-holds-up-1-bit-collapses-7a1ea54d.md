---
title: "Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses"
sidebar_label: "Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses"
---

# Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses

> Hacker News · 2026-09-08 · Model Quantization

---

Qwen3.8 27B를 실사용 환경에서 어느 정도까지 메모리를 줄일 수 있는지 검증한 글이다. 원저자는 BF16 전체 모델(약 55GB)이 대부분 소비자 하드웨어 범위를 벗어난다고 지적한 뒤, 17GB인 4비트 Q4_K_M이 대표적 벤치마크인 Terminal-Bench 2.1에서 BF16과 동등한 결과를 낸다는 점을 강조한다. GPQA Diamond와 IFBench까지 포함한 여러 벤치에서 저자는 BF16 결과를 재현했고, F16 KV-cache(약 32k 토큰당 2.3GB)를 고정으로 사용했다는 점과 Modal GPU로 약 3,000달러 규모의 비용이 들었다는 실행상의 세부도 함께 제시한다. 또한 Unsloth의 양자화 파일(v2는 2/4/8비트, v3는 1비트)을 사용했으나 일부 파일은 교체되어 정확한 복제에 제약이 있음을 밝힌다.
핵심 발견은 실용적이다. 4비트(Q4_K_M)는 여러 벤치에서 거의 차이가 없고 RTX 4090과 같은 24GB 카드에 얹어도 약 64k 토큰의 컨텍스트 여유를 둔다는 점에서 로컬 실행에 현실적인 선택이라는 결론이다. 2비트(예: UD-Q2_K_XL)는 성능이 떨어지지만 여전히 쓸만한 수준을 유지하는 경우가 있고, 같은 작업을 풀 때 턴 수는 비슷하나 생성 토큰은 약 25% 더 필요했다. 반면 1비트 양자화는 지식·추론 성능이 급격히 떨어져 GPQA에서 무작위 추측 수준으로 내려가고 장시간 추론에서는 빈 출력으로 귀결되는 경우가 많았다. 글은 양자화의 비용·메모리 절감과 품질 저하 사이의 비선형적 트레이드오프를 보여주며, 실장비에서 가능한 한 큰 모델을 사용하되 Q4_K_M처럼 실무에 적합한 4비트 옵션을 우선 고려하라고 권한다. 증거는 제공된 벤치마크와 실험 설정에 한정되므로 다른 작업이나 양자화 구현에서는 결과가 달라질 수 있다.

[Hacker News에서 원문 읽기 →](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/)

