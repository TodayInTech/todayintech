---
title: "Advancing chip design with OpenAI models"
sidebar_label: "Advancing chip design with OpenAI models"
description: "OpenAI 모델이 Jalapeño 실리콘에서 벡터·매트릭스 블록 표준셀 면적을 각각 약 13%·10% 줄였고, AMD 플래그십 GPU에서 최대 14% PPA 개선을 확인했다. GPT‑6.2 Astra는 RISC‑V 평가에서 최고 점수를 기록했으며 Synopsys와 함께 EDA 통합 모델(GPT‑Synopsys)을 개발 중이다."
---

# Advancing chip design with OpenAI models

> OpenAI Blog · 2026-11-18 · Semiconductors

---

OpenAI는 자사 최전선 모델들이 실제 칩 설계에서 실질적인 면적·성능(PPA) 개선을 만들어냈다고 밝혔다. Jalapeño 설계의 벡터·매트릭스 블록에서 모델 제안 변경으로 **벡터 유닛 표준셀 면적 약 13%**, **매트릭스 유닛 약 10%**의 절감이 산출되었고, 일부 곱셈기(multiplier) 재설계는 합성 단계에서 **셀 면적 약 15% 감소**와 지연을 **2클록→1클록**으로 줄이는 결과를 냈다. 별도 덧셈기(adder) 재설계도 약 **15% 면적 절감**을 보고했다. 이 최적화들은 Jalapeño의 실리콘 브링업 과정에서 검증되었다.

## RTL 재작성과 EDA 연동으로 얻은 PPA 개선
OpenAI 모델은 SystemVerilog RTL을 재작성해 연산·제어·데이터 이동 회로를 변경했고, Synopsys 도구를 사용해 동작 보존 여부를 검증하면서 전력·성능·면적 트레이드오프를 평가했다고 밝혔다. AMD와의 협업에서는 모델이 제안한 일부 변경을 최근 제조용 설계에 포함했고, 다른 변경은 향후 버전용 생산 설계 파일에 추가되었다. AMD 플래그십 GPU IP에서 **최대 14% PPA 개선**을 관측했고, AMD의 차세대 CPU 주요 블록에서도 단일 자릿수 퍼센트 수준의 이득을 확인했다고 보고했다.

## RISC‑V 평가: 세대 간 능력 향상과 조건
OpenAI는 세대별 모델 성능을 두 개의 오픈소스 32비트 RISC‑V 코어(PicoRV32, Ibex)로 비교했다. 각 모델에 원래 하드웨어 기술서(아키텍처)나 요구사항 기반 설계를 주고 처리량(초당 수행 명령 수)을 측정했다. 측정은 시뮬레이션 출력 검증, 최대 클럭 추정(Yosys), 숨겨진 워크로드의 IPC 기하평균을 곱해 도출했으며, 실패하거나 원래 면적의 16배를 초과하면 점수 0을 부여했다. 약 112,000 토큰 예산의 실행에서 **GPT‑6.2 Astra가 두 코어 모두에서 평균 점수 최고**를 기록했고, GPT‑6.1 Sol과 GPT‑5.6 Sol 사이에도 진전이 있었다. 전체 평가는 총 **9,881회 채점(run)** 을 포함한다.

## Synopsys 통합 모델(GPT‑Synopsys)
OpenAI는 설계 검증 툴 체인과의 연동을 확장하기 위해 Synopsys와 협력해 **GPT‑Synopsys**를 훈련, EDA 도구를 ‘전문 설계자처럼’ 사용하도록 하는 작업을 진행 중이라고 밝혔다. 이는 모델 제안의 자동 검증·트레이드오프 분석을 도구 파이프라인 안에서 수행하려는 시도다.

실무적으로 이번 결과는 모델이 RTL 수준에서 의미 있는 설계 변경을 제안하고, 상용 EDA 툴로 검증해 PPA 개선을 도출할 수 있음을 보여준다. 단, 평가에서는 원본 코어의 일부 부가 기능(성능 카운터 등)을 생략할 수 있었고, 면적·타이밍 제약을 더 엄격히 하거나 물리 합성 후 타이밍 확인을 포함하면 생산환경을 더 잘 반영할 것이라는 점도 원문에 명시되어 있다.

[OpenAI Blog에서 원문 읽기 →](https://openai.com/index/advancing-chip-design-with-our-models)

