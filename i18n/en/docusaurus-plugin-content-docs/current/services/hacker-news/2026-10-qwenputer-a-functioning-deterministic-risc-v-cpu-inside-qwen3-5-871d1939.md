---
title: "Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5"
sidebar_label: "Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5"
description: "Qwenputer는 Qwen 3.5 4B의 Gated DeltaNet 상태를 **정확한 주소지정 RAM**으로 활용해 RV32IM RISC-V CPU(작성자 주장)를 가중치에 직접 컴파일하고, 모델 내부 forward 패스만으로 C·MicroPython 실행과 512파일(약 53,000토큰) 지속 저장을 구현했다."
---

# Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5

> Hacker News · 2026-10-29 · AI/ML Research

---

Divyansh Agrawal이 공개한 **Qwenputer**는 Qwen 3.5 4B 모델의 가중치 안에 직접 컴파일된 32비트 RISC‑V 코어(RV32IM, Zba 확장 포함)와 간단한 파일시스템을 넣어, 외부 런타임이나 툴 호출 없이 모델의 순방향(forward) 연산만으로 계산과 저장을 수행할 수 있음을 보여준다. 블로그에 따르면 이 CPU는 공식 riscv-tests를 통과했고, **1800만(18,000,000) 명령을 free‑running으로 실행해 오류가 없었으며**, 출력 230,000 위치를 기준으로 레퍼런스 기계와의 불일치가 없었다.

## Gated DeltaNet를 RAM으로 사용한 방식
작성자는 Qwen 3.5의 일부 attention 레이어가 Gated DeltaNet(선형 RNN) 기반임에 주목했다. 게이트를 1로 설정하고 쓰기 강도(beta)를 1, 그리고 원-핫 키 인코딩을 사용하면 각 쓰기가 상태 행(row)을 정확히 덮어쓰게 되어 **주소지정 가능한 정확한 RAM**이 된다고 설명한다. 이 방식은 전통적 attention을 KV 캐시로 쓰는 것보다 상태 크기가 입력 길이에 무관하게 유지돼 비용이 낮다고 제시된다.

## 가중치에 컴파일한 CPU와 실행 메커니즘
CPU는 컴파일러가 각 명령을 변환해 트랜스포머 레이어 조각으로 삽입하는 방식으로 만들어졌다. 덕분에 명령 실행은 모델이 생성하는 토큰(ADDR, VAL, STEP 등)으로 표현된 실행 트레이스와 결합되어, 모델이 토큰을 생성하는 과정 자체가 CPU의 실행이 된다. 구현상 CPU는 Qwen의 32개 레이어 앞에 **11개 레이어**로 추가되며, 기본 Qwen 가중치는 그대로 둔 상태에서 추가 차원과 레이어로 컴퓨터 기능을 얹었다.

## 파일시스템과 지속성
작성자는 DeltaNet 상태에 디렉토리 영역(1,024 슬롯)을 해시 기반으로 만들고, 텍스트는 다른 헤드에 8토큰/행으로 체인 저장해 최대 **512개의 파일(약 53,000토큰)** 을 보관할 수 있다고 밝혔다. 저장한 상태는 대화 사이에 로드하면 지속되어, 이전 사실을 유지하는 실험에서 정확도가 크게 개선되는 결과를 보였다(예: 과거 대화 붙여넣기 대비 90% vs 30%).

## 성능·제약·실행 환경
작성자는 여러 벤치마크를 제시한다. 예컨대 DeepMind 테스트셋 일부에서 Qwenputer는 97.5%~100% 성능을 보였고, NUPA 장정수 연산에서는 48.6%에서 100%로 상승했다고 보고한다. 체크포인트 크기는 **약 18.8GB(대부분 제로 패딩)**로 늘어나며, 현재는 부팅과 펌웨어 적재를 위한 드라이버(RvChat)가 필요해 일반적인 generate() 호출만으로는 바로 실행되지 않는다. 또한 명령 하나가 몇 개의 디코드된 토큰을 소비해 느린 편이며(대형 계산은 밀리초가 아닌 초 단위), 벤치마크용 배치 실행기는 L4에서 약 **3,200 CPU 토큰/초**를 처리한다고 밝혔다.

## 공개와 추가 연구 지점
코드와 모델은 GitHub, Hugging Face, ModelScope에 공개되어 있으며, 작성자는 향후 MicroPython 내부 실행을 통한 python() 도구 지원과 CPU 고속화 등을 계획하고 있다. 또한 저자는 이 기술이 하이브리드 모델의 내부 상태에 논리를 숨기거나(안전성 우려) 가중치 기반의 모니터링 도구를 내장하는 연구 테스트베드가 될 수 있다고 제안한다.

이 글의 주요 내용과 수치는 블로그 게시물에 명시된 주장과 실험 결과에 기반한다. 재현 가능한 코드와 체크포인트가 공개되어 있어 기술적 검증이 가능한 수준이라는 점이 이 작업의 핵심 의미다.

[Hacker News에서 원문 읽기 →](https://divagr.com/blog/qwenputer)

