---
title: "Show HN: Wyzer Programming Language"
sidebar_label: "Show HN: Wyzer Programming Language"
---

# Show HN: Wyzer Programming Language

> Hacker News · 2026-08-07 · Programming Languages

---

Wyzer는 메모리·동시성·네트워크의 안전 문제를 하나의 소유권 규칙으로 다루려는 정적 타이프·컴파일형 언어입니다. 설계자는 Rust가 프로세스 내 메모리 안전을 보장하지만 분산 교착이나 서비스 간 프로토콜 불일치 등은 다루지 못한다고 지적하며, 이를 해결하기 위해 choreographic programming(합의된 전역 흐름을 바탕으로 각 노드 코드를 생성)과 Perceus 참조 카운팅을 결합했다고 설명합니다. 언어적 특징으로는 불변이 기본인 let/var/const 구분, struct와 match/Result 기반의 명시적 오류 처리, async/await 같은 숨겨진 제어 흐름을 배제한 단순한 모델을 표방하며, Perceus는 러스트의 복잡한 빌림 검사 대신 더 단순한 참조 카운팅 접근이라 소개합니다.
기술적 의미는 소유권 개념을 메모리에 국한하지 않고 네트워크 메시지와 하드웨어 인터럽트, 스레드까지 일반화하려는 점입니다. 컴파일러가 소유권 정보를 바탕으로 네트워크 규약을 유도·검증해 교착이나 메시지 손실을 컴파일 타임에 잡아내는 것을 목표로 하며, choreography 아이디어를 스레드와 인터럽트에도 적용한다고 명시합니다. 동시에 개발자는 이 접근이 연구 초기 단계이며 미해결 과제가 남아 있음을 솔직히 밝히고 기여를 권장하고 있습니다(피드에 따르면 곧 v0.1.0 공개 예정). 커밋 메시지·리서치·브랜딩에 AI를 보조적으로 사용했다는 점도 명시되어 있어 프로젝트의 현재 상태와 한계가 투명하게 드러납니다.

[Hacker News에서 원문 읽기 →](https://github.com/Wyzer-Lang/wyzer)

