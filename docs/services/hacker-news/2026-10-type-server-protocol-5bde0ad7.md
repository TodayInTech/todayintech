---
title: "Type Server Protocol"
sidebar_label: "Type Server Protocol"
description: "Pylance 저장소에 공개된 Type Server Protocol(TSP)은 Python 타입 분석을 위한 JSON-RPC 규격으로, 스냅샷 기반 일관성, 0.x 버전 규칙, 및 선택적 멀티-커넥션(ipc) 읽기 전용 채널 협상 방식 등을 명확히 규정합니다. (업데이트: Pylance 2026.4.1 기준)"
---

# Type Server Protocol

> Hacker News · 2026-10-26 · Developer Tools / Language Server

---

마이크로소프트의 Pylance 저장소에 Type Server Protocol(TSP) 명세가 정리되어 공개됐다. TSP는 Python 타입 분석 데이터를 질의하기 위한 **JSON-RPC 기반 프로토콜**로, 워크스페이스의 타입 분석 상태를 유지하는 타입 서버가 프로토콜 버전, 스냅샷, 파이썬 검색 경로, 임포트 해석, 계산·선언·예상 타입 질의를 처리하도록 규정한다. (문서의 마지막 갱신은 Pylance 2026.4.1과 정렬됨.)

## 버전 정책과 호환성
TSP는 시맨틱 버전 문자열을 사용하며 현재 0.x 라인에 있다. 문서에 따르면 **0.x의 마이너 버전 변경은 파괴적일 수** 있고 패치 버전은 동일 마이너 라인 내에서 후방호환을 유지한다. 클라이언트는 typeServer/getSupportedProtocolVersion 호출로 서버가 반환하는 semver가 호환되는지 확인해야 한다.

## 스냅샷(분석 시점) 모델과 오류 처리
스냅샷은 비음수 정수로 타입 서버의 시점(view)을 식별한다. 타입 객체와 핸들(IDs)은 요청에 사용한 스냅샷에만 유효하며 응답 간에 비교하면 안 된다. 서버는 분석 결과가 무효화될 때마다 스냅샷을 진행해야 하고, 클라이언트가 오래된 스냅샷으로 요청하면 **ServerCancelled(-32802)** 같은 취소 오류로 재시도하도록 유도해야 한다.

## 멀티-커넥션(성능용 읽기 전용 IPC 채널)
TSP는 선택적 멀티-커넥션을 통해 추가 로컬 채널을 열어 **읽기 전용** TSP 요청을 병렬로 처리할 수 있게 한다. 이 기능은 고빈도 타입 질의나 백그라운드 워커에 유리하지만 필수는 아니다(서버는 단일 연결에서도 동작해야 함).

핵심 제약 및 협상 메커니즘:
- 멀티-커넥션은 LSP의 initialize 단계에서 capabilities.experimental.typeServerMultiConnection로 광고하고, 양측이 공통 지원 전송(supportedTransports)을 가질 때만 활성화된다.
- 현재 문서에서 지원하는 추가 연결 전송은 **ipc**이다.
- 추가 채널은 메인 연결이 소유한 초기화·워크스페이스 상태·문서 동기화·상태 변경 알림 등은 다루지 못하고, LSP 트래픽이나 상태 변경 요청을 거부해야 한다.

예시 협상/연결 제어(JSON-RPC 페이로드):
&#123; "capabilities": &#123; "experimental": &#123; "typeServerMultiConnection": &#123; "supportedTransports": \["ipc"\] &#125; &#125; &#125; &#125;

추가 채널을 여는 요청(메인 연결에서 전송):
&#123; "type": "open", "kind": "ipc", "args": \["&lt;ipc-endpoint&gt;"\] &#125;

닫기 요청:
&#123; "type": "close", "kind": "ipc", "args": \["&lt;ipc-endpoint&gt;"\] &#125;

서버는 연결 수락 시 &#123; success: true &#125;를, 실패 시 &#123; success: false, message? &#125;를 반환한다. 플랫폼 IPC가 단방향만 제공할 경우 args에 입력/출력 엔드포인트 두 개를 전달한다.

## 타입 객체와 메시지 표준
타입은 JSON-직렬화 가능한 태그 객체로서 numeric kind(예: BuiltIn=0, Declared=1, Function=2 등), id, flags를 가진다. TypeReference(kind=9)를 통해 응답 내에서 재사용과 순환 그래프를 처리한다. 문서에 메시지 목록과 각 메시지의 방향/파라미터/결과 형태가 명시되어 있으며, 주요 요청으로는 getSupportedProtocolVersion, getSnapshot, getPythonSearchPaths, resolveImport, getComputedType, getDeclaredType, getExpectedType 등이 있다.

## 실무적 의미
이 명세는 LSP 클라이언트와 Python 타입 서버(예: Pylance) 통합자에게 구체적 구현 지침을 제공한다. 특히 멀티-커넥션 협상, 메인 연결의 상태 소유권, 스냅샷 유효성 검사와 오류 코드 사용 규칙은 동시성 설계와 클라이언트의 재시도 로직, 그리고 IPC 기반 추가 채널 구현에 직접적인 영향을 준다. 문서에 정의된 페이로드 형태와 메시지 유효성은 프로토콜 구현체가 상호운용성을 확보하는 데 핵심이다.

출처: Pylance 저장소의 Type Server Protocol 문서(문서 본문: typeServerProtocol.ts, tsp.json, tsp.schema.json에 상응하는 정의).

[Hacker News에서 원문 읽기 →](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)

