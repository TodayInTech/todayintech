---
title: "Chinese frontier AI models carry the fingerprint of export-controlled GPUs"
sidebar_label: "Chinese frontier AI models carry the fingerprint of export-controlled GPUs"
description: "Unemployment Labs의 포렌식 분석은 DeepSeek, Moonshot AI, MiniMax, Ant Group의 최근 모델 여섯 개에서 NVIDIA Blackwell(B200/B300, GB200/GB300)과 일치하는 초기화 지문을 발견했다. 이 증거는 Blackwell급 GPU에 대한 접근을 시사하지만, 위치·획득 경위나 수출통제 위반 여부는 증명하지 않는다."
---

# Chinese frontier AI models carry the fingerprint of export-controlled GPUs

> Hacker News · 2026-11-12 · AI 포렌식 / 수출통제

---

Unemployment Labs(Will DePue)가 2026년 11월 12일 공개한 포렌식 보고서는 일부 중국 프런티어 AI 모델의 공개 가중치에서 **NVIDIA Blackwell 계열 GPU의 초기화(초기 가중치) 지문**을 검출했다고 밝혔다. 이 분석은 모델 자체에 남아 있는 초기화 패턴을 복원해, 어느 하드웨어 레이아웃(스레드 수/SM 수)이 초기값 생성에 쓰였는지를 역추적하는 방식으로 진행됐다.

## 어떤 결과가 나왔나

보고서는 다음 여섯 모델에서 Blackwell 계열과 일치하는 지문을 보고한다(원문 표와 날짜 표기 보존).

- DeepSeek-V4-Flash (Apr 2026) — NVIDIA Blackwell B200/B300 (148 SM)
- DeepSeek-V4-Pro (Apr 2026) — NVIDIA Blackwell GB200/GB300 (152 SM)
- Moonshot AI Kimi K3 (Jul 2026) — NVIDIA Blackwell GB200/GB300 (152 SM)
- Moonshot AI Kimi K3.1-Pro (Nov 2026) — NVIDIA Blackwell GB200/GB300 (152 SM)
- MiniMax-M3 (Jun 2026) — NVIDIA Blackwell B200/B300 (148 SM)
- Ant Group Ling-3.1-flash (Oct 2026) — NVIDIA Blackwell GB200/GB300 (152 SM)

보고서는 또한 이전 세대 모델(예: DeepSeek-V3, Moonshot K2.5, MiniMax-M2.7, Ant의 Ling-3.0-flash 등)은 Hopper 계열(132 SM fingerprint)에 해당한다고 보고한다. 일부 기업(Alibaba의 Qwen, Zhipu GLM, Tencent, Xiaomi 등)은 최신 공개 모델에서 Hopper 지문을 유지하고 있으며 Meituan의 LongCat-2.0은 NVIDIA 지문이 없었다고 기록한다.

## 방식과 근거 수준

분석팀은 공개된 가중치에서 ‘보존된’ 초기화 행(row)과 훈련으로 약하게 남은 초기값 흔적을 비교했다. PyTorch의 초기화 구현이 GPU 스레드 레이아웃에 따라 특정 위치에 값을 배치하므로, 적절한 시드(seed)와 스레드(또는 SM) 수 조합으로 시작값을 재현할 수 있다고 설명한다. 실제 칩의 스레드 수 예시는 다음과 같다(보고서 기준):

- Hopper(H100 SXM/H200/H800): 132 SM → 270,336 threads
- Blackwell B200/B300: 148 SM → 303,104 threads
- Blackwell GB200/GB300: 152 SM → 311,296 threads

보고서는 DeepSeek-V4-Flash와 Kimi K3에 대해 물리적 Blackwell 칩에서도 매칭을 확인했고, 통계적 유의성은 매우 높아(보고서 부록: 어떤 검사들은 8σ를 넘지 못할 가능성도 배제했으며, 최저 Blackwell 결과도 20σ 수준) 우연 가능성이 극히 낮다고 결론낸다. 또한 공개적으로 하드웨어를 명시한 24건의 사례와 본 분석 결과는 모두 일치한다고 보고한다.

## 한계와 해석의 범위

보고서는 중요한 제약을 명확히 제시한다. 이 방법은 공개된 가중치가 있어야만 작동하며, PyTorch 초기화에서 패턴이 남는 경우에만 식별 가능하다. Baidu의 ERNIE-5.5는 시드(2760)를 복구했으나 PaddlePaddle 초기화는 칩 레이아웃 지문을 남기지 않아 하드웨어 식별이 불가능했다. 또한 CPU 초기화(예: 일부 Qwen3 모델)나 AI ASIC 초기화(예: Meituan의 LongCat-2.0)도 GPU 지문을 남기지 않는다. 보고서는 이 결과들이 **초기화가 해당 하드웨어에서 이루어졌음을 강하게 시사**하지만, **해당 칩들이 어디에 있었는지, 어떻게 접근했는지, 또는 수출통제 위반이 있었는지**는 입증하지 못한다고 명시한다.

또한 보고서는 대안 설명으로 특별 구성된 AMD 하드웨어(수출 통제 대상)를 고려했으나 DeepSeek-V4-Flash에 대해서는 배제했고 다른 다섯 모델에 대해서도 가능성이 낮다고 판단한다고 적시한다.

## 정책·실무적 함의(증거 기반 해석)

보고서 근거만 보면 이번 결과는 **최신 상용급 GPU(Blackwell 계열)에 대한 접근을 시사하는 기술적 증거**를 제공한다는 점에서 중요하다. B200/B300/GB200/GB300는 중국 수출에 대해 미국 라이선스가 필요한 분류에 속하며(보고서 부록 근거), 해당 칩이 사용됐다는 기술적 신호가 공개 가중치에서 복원됐다는 사실 자체가 정책·규제 논의의 근거가 될 수 있다. 다만 보고서가 법적 위반을 입증하지는 못하므로 규제 측면의 판단은 별도 조사(장비 위치·이력·수출 서류 등)를 필요로 한다.

근거: Will DePue, “Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs,” Unemployment Labs, 2026-11-12(보고서 본문 및 부록, 원문 chunk-0001, chunk-0003, chunk-0006, chunk-0008).

(기술 독자는 보고서의 재현 스크립트·행 고정(row fixtures)·테스트 출력을 요청해 검토할 수 있다고 보고서가 밝히고 있음을 참고하기 바란다.)

[Hacker News에서 원문 읽기 →](https://unemploymentlabs.com/checkpoint-forensics)

