---
title: "Steel Bank Common Lisp version 2.6.7"
sidebar_label: "Steel Bank Common Lisp version 2.6.7"
---

# Steel Bank Common Lisp version 2.6.7

> Hacker News · 2026-07-28 · Programming languages

---

Steel Bank Common Lisp(SBCL) 2.6.7이 발표되면서 몇 가지 실용적 변화가 도입됐다. 먼저 SB-MANUAL이라는 새 contrib 모듈이 추가돼 매뉴얼 내용을 섹션 정의의 도큐스트링으로 포함하며, Slime의 M-. 같은 개발 도구로 상호작용해 탐색할 수 있도록 했다. DOCUMENTATION이 DOC-TYPE 선언을 지원하게 되었고, 공식 Texinfo 기반 문서는 SB-MANUAL로부터 생성되는 구조를 유지하는 한편, 내부 도큐스트링은 Markdown 하위집합을 따르지만 일부 마크업은 DOCUMENTATION/DESCRIBE가 제거한다고 명시했다. 또한 외부 렌더링 대안으로 fixnum.com의 PDF·HTML·Markdown 변형이 소개되어 있어 접근성이 개선되었다.
플랫폼·성능 측면에서는 SIMD 관련 확장이 눈에 띈다. SB-SIMD contrib이 ARM64를 지원하고 x86-64에서는 AVX512 명령을 추가로 지원함으로써 ARM64·x86-64에서의 SIMD 활용 범위가 넓어졌다(기여자 크레딧 포함). ARM64에서의 잘못된 컴파일 수정을 비롯해 MIPS·LoongArch에서의 INTEGER-LENGTH 구현 개선 등 아키텍처별 버그 수정을 포함한다. 읽기 동작(*READ-SUPPRESS* T)과 CONCATENATE 관련 컴파일러 타입 오류, MULTIPLE-VALUE-CALL의 오컴파일 등 여러 정확성 버그가 고쳐졌고, 상수 복수수 전달 시 cons를 줄이는 최적화, UTF-8 변환에서의 향상된 SIMD 루틴 활용, COUNT 변환 적용 범위 확대 등 성능상 개선도 다수 이루어졌다. 문서상 오탈자·타이포 수정과 외부 함수 인터페이스 설명(배열이 행 우선임) 등 문서 품질 개선도 병행되어, SBCL을 실사용하는 개발자에게는 상호참조 가능한 매뉴얼 접근성과 플랫폼별 향상된 성능·정확성이 핵심 의미로 다가올 것이다.

[Hacker News에서 원문 읽기 →](https://sbcl.org/all-news.html?2.6.7)

