---
title: "A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth"
sidebar_label: "A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth"
description: "Unsloth Desktop과 양자화된 Qwen·Inkling 모델을 이용하면 **RTX 5090(32GB)** 같은 소비자 GPU에서 개인 로컬 AI를 설치해 LAN으로 공유할 수 있다. 문서는 VRAM별 모델·양자화 추천, 컨텍스트 설정(예: 128K)과 LAN 접근 설정 절차를 상세히 제시한다."
---

# A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth

> Hacker News · 2026-11-22 · AI/Local AI

---

Unsloth Desktop과 오픈 가중치 모델(예: Qwen, Inkling)을 조합하면 개인 PC에서 비교적 간단히 '로컬 AI' 챗 인터페이스를 띄울 수 있다. 글쓴이는 비용·프라이버시·클라우드 제약을 이유로 자체 호스팅을 선택했고, Windows 환경에서 10–15분(다운로드 시간 제외) 내 기본 구성 가능하다고 보고한다.

## 모델·VRAM·양자화: 어떤 조합을 고를지

문서는 GPU VRAM을 기준으로 권장 모델을 정리한다. 예를 들어 **8–12GB** 카드는 Qwen3.5-9B 같은 소형 모델(UD-Q4_K_S/Q4_K_M, 컨텍스트 8K–16K), **16GB** 카드는 Qwen3-14B·MoE 계열(16K–32K), **24GB**는 Qwen3.8-27B·Inkling 2 Mini(UD-Q4_K_M 등), **32GB+** 환경은 Qwen3.8-27B·Inkling 2 Mini의 더 큰 컨텍스트(64K–128K+)를 권장한다(chunk-0002).

양자화(quantization)는 모델을 낮은 정밀도로 압축해 VRAM에 맞추는 방법이다. Qwen3.8-27B의 원본은 약 **56GB**(16-bit)지만 Unsloth가 제공하는 UD-Q4_K_XL 같은 4-bit 파일은 약 **~18GB**로 줄어들어 **RTX 5090(32GB)** 같은 소비자 카드에서 모델과 큰 컨텍스트를 함께 운용할 수 있다(chunk-0001, chunk-0004). 글쓴이는 예시로 Qwen3.8-27B(U D-Q4_K_XL)와 **128K 컨텍스트**를 사용했다.

## Inkling 2 Mini와 Inkling 2 Small 차이

Inkling 2 Mini는 **26.4B 매개변수**, Apache 2.0 라이선스, **1M 토큰 컨텍스트**를 지원하며 Unsloth의 UD-Q4_K_XL 파일은 **17.6GB**로 보고된다(Thinking Machines Lab 공개, Unsloth 문서). 이에 반해 Inkling 2 Small은 모델 규모가 **594B**, 최소 배포 파일이 **171.7GB**로 소비자 GPU로는 현실적이지 않다(chunk-0002, chunk-0003, chunk-0004).

## 설치와 공유: 실무적 절차

기본 흐름은 세 단계다: Unsloth Desktop 설치 → 양자화된 모델 다운로드(모델 드롭다운에서 선택, 기어 아이콘으로 컨텍스트 설정) → 컨텍스트 크기 지정. Unsloth는 GGUF·MLX 형식 모델을 지원하고, 최신 빌드가 필요할 수 있다(예: Inkling 2 지원).

로컬 네트워크 공유는 Unsloth의 'Remote &amp; LAN' 설정을 통해 가능하다. 원격 비밀번호를 설정한 뒤 LAN 접근을 시작하면 홈 네트워크 내에서 브라우저로 접속 가능한 주소가 제공되며, 접속자는 'unsloth' 계정과 해당 비밀번호로 로그인한다. 이 방식은 외부 인터넷 접근을 기본으로 제공하지 않으므로 현재로선 동일 네트워크 내 사용에 국한된다(chunk-0001, chunk-0003).

## 실무적 의미와 제약

근거에 따르면 소비자용 하드웨어에서도 **양자화된 모델**과 적절한 컨텍스트 설정만으로 개인용 대화형 AI를 운영할 수 있다. 다만 모델 파일 크기·컨텍스트 설정·시스템 RAM 사용(특히 MoE 모델의 경우)이 성능과 사용성에 직접적인 영향을 미친다. 예를 들어 MoE 모델은 활성 파라미터가 상대적으로 작아 시스템 RAM으로 일부를 처리할 수 있어 작은 VRAM 카드에서도 동작이 가능하다(chunk-0002, chunk-0003).

원문은 설치·공유 절차, 모델 선택과 양자화·컨텍스트의 실제 수치(예: 파일 크기, 권장 VRAM, 컨텍스트 값)를 구체적으로 제시하고 있어 실습용 가이드로 유용하다. 다만 인터넷 공개 접근(원격 공개)은 별도 터널링·구성 없이 바로 사용할 수 없다는 점과, Inkling 2 Small처럼 소비자 환경에 맞지 않는 모델이 존재한다는 사실도 함께 제시된다(chunk-0003, chunk-0004).

출처: Unsloth 데스크톱 문서, Unsloth 모델 파일 설명, Qwen·Inkling 모델 카드(문서 근거에 따라 인용).

[Hacker News에서 원문 읽기 →](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)

