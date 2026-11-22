---
title: "Inkling-2-Mini in 5.4 GB Memory"
sidebar_label: "Inkling-2-Mini in 5.4 GB Memory"
description: "LookAtMyQuant 컴파일러가 Inkling-2-Mini를 5.38GB(1.65 bpp)까지 압축해 Apple 실리콘용 여러 빌드를 공개했다. 12.76GB 빌드는 원본 BF16 교사와 동일한 벤치마크 점수를 유지하며, 5.38GB 빌드는 성능 저하가 확인됩니다."
---

# Inkling-2-Mini in 5.4 GB Memory

> Hacker News · 2026-11-21 · 모델 압축/양자화

---

LookAtMyQuant가 Inkling-2-Mini와 여러 대형 모델을 **실사용 수준으로 고밀도 양자화해 Apple 실리콘용 빌드로 공개**했다. 리포지토리 설명과 결과 파일은 압축된 여러 용량(12.76GB, 11.18GB, 8.87GB, 5.38GB)과 각 빌드의 정확도·속도·메모리 수치를 담고 있다.

## 무엇이 달라졌나 — 압축 산출물과 핵심 결과
LookAtMyQuant는 Inkling-2-Mini(물리 26.4B / 활성 5.4B MoE)를 텍스트 가중치만 압축해 네 가지 Apple Silicon MLX 빌드를 만들었다: **12.76GB(3.92 bpp)**, **11.18GB(3.43 bpp)**, **8.87GB(2.72 bpp)**, **5.38GB(1.65 bpp)**. 리포지토리의 표에 따르면 12.76GB 빌드는 원본 BF16 교사와 동일한 벤치마크 성적(총 349/349 pooled)을 보였고, 11.18GB·8.87GB는 98.9% 수준을 유지했다. 반면 **5.38GB 빌드는 GSM8K 176/200(88.0%), HumanEval 116/164(70.7%)로 의미 있는 성능 저하가 관찰**된다.

## 사용된 기술(공식 설명 기준)
- **코드 전략:** 4KB SRAM 해시드 블록-벡터 trellis 코드(ht2/ht3), 행 단위 trellis(rtr1/rtr4), tr2 꼬리층 처리 등 복합적인 코드 조합을 사용. 일부 고감도(expert) 버킷은 NVFP4 네이티브 패스스루로 0.0 에러를 유지한 빌드도 있음(11.2GB, 12.8GB).
- **최적화·보정:** Fisher 정보로 행별 비트 할당, 모델 자체의 작업(예: 수학 풀이)으로 보정한 후 4,000스텝 증류를 거쳐 층별로 재양자화.
- **파이프라인:** lamq 컴파일러(측정→할당→빌드)와 runtime_mlx/lamq 런타임을 통해 단일 Metal 커널로 디코드·사전채우기·샘플링을 수행.

위 절차와 구성은 리포지토리의 실행·빌드 예시와 측정·할당·빌드 명령어에 기술되어 있다.

## 성능·속도·운영 메모리(Apple M5 Max 기준)
리포지토리 표에 명시된 주요 수치:
- 12.8GB 빌드: T=512 prefill 2,016 tok/s, serial 60.5 tok/s, median drafted 112.7 tok/s, 활성 RAM 약 12.72GB.
- 11.2GB 빌드: prefill 2,032 tok/s, serial 62.4 tok/s, median 103.7 tok/s, 활성 RAM 약 11.13GB.
- 8.9GB 빌드: serial 63.5 tok/s, median 106.0 tok/s, 활성 RAM 약 9.41GB.
- 5.4GB 빌드: prefill 1,807 tok/s, serial 75.3 tok/s, median 124.4 tok/s, 활성 RAM 약 5.98GB.

수치 출처는 리포지토리의 결과 표이며, 빌드별로 추론 처리량과 활성 메모리 점유가 명확히 다르다.

## 실무적 접근: 설치와 간단한 사용법
리포지토리는 MIT 라이선스이며(명시), Apple 실리콘에서 바로 사용할 수 있는 런타임과 예시 명령을 제공한다. 예:

pip install git+https://github.com/ShinMegamiBoson/lookatmyquant.git

로컬 클론에서

pip install -e .
python -m runtime_mlx

또는 lamq 명령으로 모델을 지정해 생성·채팅을 시도할 수 있다(예시가 리포지토리에 포함).

## 제한 사항
리포지토리 자체가 제공하는 메타데이터에 따르면 벤치마크에 사용된 ‘dense weights’ 원본 파일과 per-problem 상세 결과 일부(및 16-bit drafter 훈련 파일)는 공개되지 않았다. 또한 특정 수치(예: 속도·정확도)는 제공된 실험 환경(Apple M5 Max, 설정값)에 기반한다.

리포지토리와 관련 빌드는 Github에 올라와 있으며, 자세한 명령 예시·빌드 파일명·벤치마크 표는 소스에 직접 기재되어 있다(참조: 리포지토리 파일들과 results/ 디렉터리).

[Hacker News에서 원문 읽기 →](https://github.com/ShinMegamiBoson/lookatmyquant)

