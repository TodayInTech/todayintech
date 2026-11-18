---
title: "Building the Agent Host Protocol for sessions that continue across devices"
sidebar_label: "Building the Agent Host Protocol for sessions that continue across devices"
description: "GitHub은 에이전트 세션을 에디터·앱·폰·클라우드에서 이어 쓰게 하는 오픈 표준 **Agent Host Protocol(AHP)**을 발표했다. AHP는 URI 기반 채널과 리듀서 상태로 재접속·재생을 지원하며 VS Code(TypeScript)와 GitHub(Rust) 두 구현으로 상호운용성이 검증됐다."
---

# Building the Agent Host Protocol for sessions that continue across devices

> GitHub Blog · 2026-11-17 · 개발자 도구

---

GitHub은 에이전트 세션을 한 애플리케이션에 묶지 않고 여러 클라이언트에서 이어서 사용할 수 있게 하는 **Agent Host Protocol(AHP)**을 설계·공개했다. AHP는 세션 연속성(한 기기에서 시작한 작업을 다른 기기에서 이어감)을 목표로 하며, 네트워크 단절·재접속·동시 접속 시 상태 재생(replay)을 용이하게 하도록 설계되었다.

## 채널과 리듀서 기반 상태 모델

AHP의 핵심은 URI로 식별되는 "채널"(channels)과 각 채널 내부의 리듀서 기반 상태 객체다. 모든 서버는 **root, session, chat 채널을 반드시 구현**해야 하며, 터미널 지원이나 OTel 보고 같은 추가 채널은 선택적으로 제공할 수 있다. 클라이언트는 서버가 소유한 상태(state)에 대해 액션(action) 시퀀스를 보내어 상태를 변형하거나 부작용(예: 채팅 메시지 전송)을 트리거한다. 이 구조 덕분에 클라이언트가 큐에 담긴 액션을 재전송해 서버가 이를 조정·확인하면 네트워크가 불안정한 환경에서도 올바른 상태를 복원할 수 있다. GitHub은 이 설계가 React 같은 UI 프레임워크와도 잘 맞는다고 설명했다.

## 두 독립 구현으로 검증된 상호운용성

AHP는 VS Code 쪽 구현(타입스크립트)과 GitHub Agent Host(러스트)라는 **서로 다른 요구와 언어로 개발된 두 호스트**로 병행 운영되고 있다. VS Code의 기존 Copilot Chat 확장은 윈도우 수명주기에 묶여 있었고 약 **400,000줄의 TypeScript** 코드베이스를 갖고 있었으나, AHP 채택을 위해 에이전트 호스트 기반 스택으로 재구성했다. GitHub 호스트는 클라우드와 다양한 인프라·보안 제약을 겨냥해 별도 구현이 필요했고, 이런 이중 구현이 프로토콜의 진정한 이식성을 검증하는 역할을 했다고 밝혔다. 개발 과정에서 두 구현이 각자 확장한 메커니즘(예: _metadata, 커스텀 메서드)을 점검하면서 프로토콜의 공백이나 잘못된 가정을 찾아 고쳤다(예: PTY가 없는 셸 출력 표현 문제, 세션 URI 구조 가정 등).

## 개발자 실무 영향과 사용법

AHP용 클라이언트/서버 라이브러리는 **Rust, TypeScript, Kotlin, Swift, .NET, Go**로 제공돼 다양한 환경에서 구현 가능하다. GitHub은 Copilot 앱과 VS Code에서 같은 에이전트 세션을 공유하도록 이미 적용했다고 밝혔다. 직접 연결 방법으로는 Copilot 앱에서 `Experimental > Direct Connections` 활성화 후 Environments &gt; Add Agent Host Protocol Host를 사용하고, VS Code에서는 Agents 창의 "Add Remote Agent Host"를 통해 연결할 수 있다. 또한 로컬 호스트를 띄우거나 엔드포인트를 확인하는 명령어 예시는 다음과 같다:

code agent host

code agent endpoints

이 설계는 각 클라이언트가 별도의 맞춤형 통합을 만들지 않아도 동일한 에이전트, 이전 대화 기록, 상태를 공유할 수 있게 한다는 점에서 중요하다. 재접속·재생(replay) 특성은 불안정한 네트워크 환경이나 다중 클라이언트 동시 수정을 다루는 실무에 직접적인 이득을 주며, 프로토콜이 에이전트 내부 행위를 강제하지 않는다는 점은 빠르게 진화하는 에이전트 도메인에 유연성을 남긴다.

GitHub은 AHP를 오픈 표준으로 제시하며 질문과 제안을 GitHub에서 받겠다고 알려왔다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/)

