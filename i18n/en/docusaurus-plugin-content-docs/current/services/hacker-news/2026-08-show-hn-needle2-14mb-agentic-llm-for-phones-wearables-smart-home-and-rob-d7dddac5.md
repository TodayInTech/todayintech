---
title: "Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots"
sidebar_label: "Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots"
---

# Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots

> Hacker News · 2026-08-10 · Edge AI / On-device LLM

---

Cactus의 Needle 2는 ‘작고 특화된’ 에이전트형 LLM을 지향하며, 단일 14MB 바이너리와 28MB 세션 RAM 한도 안에서 동작하도록 설계된 모델입니다. 모델은 45M 파라미터에 Cactus Quants로 훈련된 손실 없는 2비트 표현을 사용하고, 라즈베리파이5에서 초당 수백~천 단위 토큰 처리 성능을 보이며(예: Pi5 decode 500+ tok/s), 파일 크기·메모리·연산량을 낮추기 위해 Hadamard MLP, 해시된 n-gram 엔그램, 멀티레인 잔차 스트림 같은 구조적 절약 기법을 채택합니다. 툴 호출·기기 제어를 '함수 호출과 타입화된 매개변수' 문제로 재정의해 세계지식과 자유문장 생성을 배제하고, 256토큰 슬라이딩 윈도우·영구 고정된 도구 선언으로 상태 메모리를 고정하는 설계로 MCU 계열 하드웨어까지 현실적으로 동작하게 만든 점이 핵심 주장입니다.
평가에서는 LFM2.5(230M, f16) 등 더 큰 일반 모델들과 도구 호출 정확도에서 엎치락뒤치락하는 결과를 보이지만, Needle 2는 동일 엔진 구성에서 실제 배포 환경과 동일한 CQ2-bit 설정으로 측정되었다는 점을 강조합니다. 아키텍처·엔진 최적화(2비트 코드의 레지스터 확장, int8 산술 유지, 문법 기반 출력 후보 축소)로 인해 전통적 트랜스포머 대비 MFLOPs/토큰을 대폭 줄였고(예: 동일 형상 트랜스포머 164→Needle 70 MFLOPs/토큰), 저전력·저지연·오프라인 개인비서처럼 항상 켜진 서비스의 전력 예산을 절감한다고 주장합니다. 다만 저자도 Needle이 기기 제어·구조화된 추출에 특화되어 있어 범용 함수 호출·프로그래밍 언어 카테고리에서는 분포 차이가 성능 격차로 이어진다는 점을 명확히 밝히고 있어, 모바일·임베디드 제품에 직접 통합하는 실무적 대안으로서의 기술적 의미가 분명합니다.

[Hacker News에서 원문 읽기 →](https://cactuscompute.com/needle)

