---
title: "Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use"
sidebar_label: "Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use"
description: "작성자의 역공학·실행 테스트에서 Windows 11의 MissionControlAggregator.dll이 codex.exe·copilot.exe 등 코딩 에이전트와 python·gcc 같은 개발 도구 사용을 감지해 비트맵 형태로 로컬에 저장하고, **선택적 진단 데이터(AllowTelemetry=3)**가 허용된 경우 Segments.SubCohorts 이벤트로 Microsoft에 업로드하는 것으로 확인됐습니다."
---

# Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use

> Hacker News · 2026-11-16 · Privacy / Windows telemetry

---

Windows 11의 진단 컴포넌트가 어떤 개발 도구·코딩 에이전트를 관찰하는지, 그리고 그 관찰 결과가 어떻게 보고되는지를 역공학과 실행 테스트로 확인한 조사 결과를 정리합니다. 소스는 역공학자(cwaffles)의 분석이며, 검사된 환경은 Windows 11 ARM64 VM(빌드 **26200.9974**)입니다.

## MissionControlAggregator가 관찰하는 항목
역공학으로 발견된 실행파일 이름 목록에는 **codex.exe, claude.exe, copilot.exe, cursor.exe** 등 코딩 에이전트와 **python.exe, dotnet.exe, gcc.exe, clang.exe, gdb.exe, javac.exe, devenv.exe, code.exe** 등 익숙한 개발 도구가 포함되어 있습니다. 이들 이름은 MissionControlAggregator.dll 내부의 일치 검사(matcher)에서 사용되며, 일부 슬롯은 퍼블리셔 검증(예: Node.js Foundation, Python Software Foundation, Microsoft Corporation)을 추가로 수행합니다. 조사 대상 DLL 버전은 **10.0.26100.9818**입니다.

## 수집 경로와 보고 방식
이 컴포넌트는 직접 프로세스 스캔을 하지 않고 Windows 이벤트를 구독해 정보를 얻습니다. 구체적으로는 KernelProcess.AppStateChangeSummary, Win32kTraceLogging.AppInteractivitySummary, WSL의 Microsoft.Windows.Lxss.Manager.Exec/ExecCritical 같은 원본 이벤트를 파싱해 매처에 전달합니다. 매칭이 성공하면 내부 상태의 특정 슬롯(bit)을 설정하고, 이후 **ReportCohorts&lt;12,4,5&gt;** 흐름을 통해 **Segments.SubCohorts**라는 이름의 ETW(TraceLogging) 이벤트로 변환·전송합니다. 보고서는 개별 실행 파일 이름을 반복 전송하지 않고, **카테고리별 비트맵(예: Codex CLI 비트 = 1&lt;&lt;2 = 4, 컴파일러/디버거 카테고리 = 1&lt;&lt;3 = 8)**으로 저장·표현합니다.

영향을 확인한 실행 경로 예시: DiagTrack(Connected User Experiences and Telemetry) 서비스가 AggregatorHost.exe를 시작하고 해당 프로세스가 MissionControlAggregator.dll을 로드합니다. 관찰 상태는

C:\\ProgramData\\Microsoft\\Diagnosis\\AggregatorStorage\\MissionControlAggregator$

에 영구 저장됩니다.

## 보고가 외부로 전송되는 조건
핵심적 발견은 이 보고가 **'선택적(옵션) 진단 데이터'로 분류**되며, 조사한 미국 설정의 깨끗한 설치에서 **기본값으로 선택적 진단이 허용(AllowTelemetry = 3)** 되어 있어 DiagTrack의 업로드 큐에 해당 이벤트가 실제로 들어가는 것을 확인했다는 점입니다. 업로드 큐에 기록된 항목의 예시는 다음과 같습니다:

&#123; "name": "Microsoft.Windows.MissionControlAggregator.Segments.SubCohorts", "ext": &#123; "privacy": &#123; "isRequired": false &#125; &#125;, "data": &#123; "Version": "0.1.5", "CliAgentSubCohorts": \[4\], "DesktopAgentSubCohorts": \[0\], "FlushedFromSave": true &#125; &#125;

다만 조사자는 공개 ISO의 기본 VM 이미지에서는 해당 기능이 비활성화된 경우도 확인했으므로, 모든 설치에서 자동으로 활성화되는 것은 아니라고 명시합니다.

## 실무적 의미
- 수집 형식은 **개별 실행 파일의 이름 대신 카테고리·에이전트 비트맵**이므로 로그에 원본 파일명을 대량 저장하지는 않지만, 어떤 종류의 코딩 에이전트(예: Codex, Copilot)나 도구 집단(예: 컴파일러/디버거)이 사용되는지는 기기 단위로 식별 가능합니다. 이는 도구 사용 패턴과 환경(예: AI 에디터 사용 여부)을 드러낼 수 있어 개인정보·업무 보안 관점에서 고려할 사항입니다.
- 보고 전송은 사용자의 진단 설정에 달려 있습니다. 설치 시 '선택적 진단 데이터 포함(Include Optional)'를 허용한 경우 데이터가 업로드됩니다. 끄려면 Settings → Privacy &amp; security → Diagnostics &amp; feedback에서 'Send optional diagnostic data'를 비활성화하면 됩니다.

## 확인된 기술적 세부값(핵심 근거)
- 검사된 Windows 빌드: **26200.9974**
- MissionControlAggregator.dll 버전: **10.0.26100.9818**
- 기능명/ID: **CLICodingAgentUsage, 62580080**
- 보고명: **Microsoft.Windows.MissionControlAggregator.Segments.SubCohorts**
- 저장 위치: C:\\ProgramData\\Microsoft\\Diagnosis\\AggregatorStorage\\MissionControlAggregator$
- 일부 매처는 퍼블리셔 검증을 수행

위 내용은 제공된 역공학·실행 검증 결과를 바탕으로 정리한 것입니다. 조사자는 동작 확인을 위해 자체 VM에서 실험을 수행했고, 모든 Windows 설치에서 동일하게 동작한다고 단정할 근거는 제시하지 않았습니다.

[Hacker News에서 원문 읽기 →](https://xusheng.dev/posts/windows-coding-agent-telemetry/)

