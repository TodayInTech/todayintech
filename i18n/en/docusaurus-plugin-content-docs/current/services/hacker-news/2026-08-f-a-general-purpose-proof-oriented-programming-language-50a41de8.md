---
title: "F*: A general-purpose proof-oriented programming language"
sidebar_label: "F*: A general-purpose proof-oriented programming language"
---

# F*: A general-purpose proof-oriented programming language

> Hacker News · 2026-08-02 · 프로그래밍 언어·형식검증

---

F*는 의존형 타입의 표현력과 SMT 기반 자동 증명 및 전술 기반 상호작용적 정리 증명을 결합한 범용 증명지향 프로그래밍 언어로, 순수 함수형과 효과 지향 프로그래밍을 모두 지원합니다. 기본적으로 OCaml로 컴파일되지만, F#·C·Wasm(KaRaMeL)·어셈블리(Vale) 등 다양한 대상로 추출할 수 있는 점과 Low*라는 C로 컴파일 가능한 저수준 부분집합을 제공하는 점이 특징입니다. Microsoft Research와 Inria, 커뮤니티가 활발히 개발 중이며 Apache 2.0으로 배포되어 설치·실습용 온라인 교재와 튜토리얼, 강의 자료가 준비되어 있다는 점도 눈에 띕니다 (바이너리·OPAM·Docker·Nix 등 설치 경로 제공).
실무 적용과 연구 성과가 긴밀히 연결되어 있다는 점이 F*의 핵심 기술적 의의입니다. Project Everest와 HACL*, ValeCrypt, EverCrypt, EverParse 등에서 검증된 암호 구현과 파서 생성기가 생성 코드로 생산 환경(예: Firefox, 리눅스 커널, Python, mbedTLS, Tezos, ElectionGuard, Wireguard, Azure Hyper-V 등)에 투입된 사례가 다수 확인됩니다. 또한 Dijkstra 모나드, 단조 상태 로직, SteelCore·PulseCore 등 고급 효과·병행성 논리 관련 연구들이 F* 위에 구현·검증되어 왔고, TLS·QUIC·DICE·FastVer·StarMalloc 등 보안·시스템·파싱·컴파일 검증 사례가 연계되어 있어, 정리 증명과 자동화된 추출을 통해 고신뢰성 소프트웨어를 실무 수준으로 연결하는 플랫폼으로서 의미가 큽니다.

[Hacker News에서 원문 읽기 →](https://fstar-lang.org/)

