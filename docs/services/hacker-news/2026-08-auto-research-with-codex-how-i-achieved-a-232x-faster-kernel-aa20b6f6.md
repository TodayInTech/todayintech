---
title: "Auto-research with codex: How I achieved a 232x Faster Kernel"
sidebar_label: "Auto-research with codex: How I achieved a 232x Faster Kernel"
---

# Auto-research with codex: How I achieved a 232x Faster Kernel

> Hacker News · 2026-08-15 · GPU 커널 최적화 / Auto-research

---

GPU Mode의 auto-research형 콘테스트에서 배치형 정사각형 FP32 행렬에 대해 compact Householder 방식의 QR 분해를 구현하는 과제가 주어졌고, 저자는 baseline 대비 232배 빠른 커널을 만들어 183명 중 12위를 차지했다(chunk-0001). 핵심은 패널(panel)에서 발생하는 직렬 행렬-벡터 작업을 작게 유지하고, 오른쪽의 트레일링 블록을 GEMM으로 처리하는 블록드(Blocked) 하우스홀더 구조를 채택한 점이다(chunk-0003). 대회는 다양한 행렬 크기(32부터 4096까지)와 조건수 분포를 포함했고 내부 연산에 저정밀(FP16/FP8/NVFP4) 사용은 허용되나 최종 체크는 FP32 기준으로 이루어졌다(chunk-0001, chunk-0003).
도구와 워크플로 측면에서는 Codex(GPT-5.5)를 중심으로 한 에이전트 루프를 적극 활용했고 popcorn CLI와 Modal 프로파일링을 통해 수천 번의 제출과 성능 기록을 반복했다는 점이 인상적이다(chunk-0003). 저자는 /goal, /btw 같은 루프 제어로 모델을 장시간 자동 실행시키고 필요시 간헐적으로 개입하는 방식으로 성능을 끌어올렸다(chunk-0003). 반면 저정밀 처리의 안정성, 다양한 배치·크기 대응(작은 n을 묶는 패킹), 트레일링 행렬을 FP16에 계속 상주시키는 등 도메인 전문성이 성능을 더 끌어올릴 여지가 있었다고 평가하며, 상위 솔루션들이 라이브러리 함수 의존을 줄이고 커스텀 삼각 역행렬 등을 도입한 점을 교훈으로 제시한다(chunk-0007). 이 사례는 자동화된 에이전트 루프와 도메인 지식의 조합이 GPU 커널 최적화에서 실질적 이득을 줄 수 있음을 보여준다.

[Hacker News에서 원문 읽기 →](https://sankalp.bearblog.dev/autoresearch/)

