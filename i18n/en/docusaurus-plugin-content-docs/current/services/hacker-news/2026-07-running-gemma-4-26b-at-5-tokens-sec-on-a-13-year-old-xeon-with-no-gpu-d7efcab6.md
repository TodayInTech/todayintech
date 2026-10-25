---
title: "Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU"
sidebar_label: "Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU"
---

# Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

> Hacker News · 2026-07-15 · ML 인프라

---

저자는 13년 된 Ivy Bridge Xeon E5-2690 v2(AVX1, GPU 없음) 서버에서 Google의 Gemma 4 26B-A4B(MoE)를 CPU 전용으로 구동해 약 5 tokens/sec(디코드)와 ~16 tok/s(프롬프트 평가)를 얻어낸 과정을 상세히 정리했다. 출발점은 ik_llama.cpp 포크에서 AVX2·FMA3 가정을 거는 최적화 때문에 빌드와 실행이 실패한 점이다. 단순히 GPU를 빌리기보다 오래된 장비를 살려 쓰려는 목적에서 시작해, Claude 에이전트의 진단과 저자의 실험 반복으로 문제의 원인과 해결책을 찾아냈다. 결과는 비용 대비 효율(박스 비용 약 $300)과 운영상 대안성(유료 API 장애 시 로컬 모델 대체) 측면에서 의미가 있다.
문제의 핵심은 GGML_USE_IQK_MULMAT 관련 경로가 AVX2를 전제로 설계돼 그래프 빌더가 AVX1 빌드에서 실행 경로를 누락시켰고, 그로 인해 많은 FFN 텐서가 계산되지 않아 숨겨진 상태가 초기화되지 않은 값으로 채워지는 현상이었다. 패치는 세 축으로 정리된다: 비-AVX2 환경에서 컴파일이 가능하도록 스칼라 루프로의 수정과 누락 include 보완, 그래프 빌더가 AVX1에서도 계산 경로를 내보내도록 ggml_moe_up_gate와 ggml_fused_up_gate 처리 변경, 그리고 CI용 스텁 정비다. 단, --run-time-repack 옵션은 AVX2 전용 가중치 레이아웃(Q8_0_R8)을 만들기 때문에 이 실험에서는 제외했다. 전체 수정은 PR(ikawrakow/ik_llama.cpp#2138)에 올려져 있으며, 글은 오래된 서버에서 현대 MoE 모델을 돌릴 때 생기는 실제 한계와 그 우회법을 기술적으로 연결해 보여준다.

[Hacker News에서 원문 읽기 →](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/)

