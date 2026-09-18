---
title: "Claude Code now reads AGENTS.md if there is no Claude.md"
sidebar_label: "Claude Code now reads AGENTS.md if there is no Claude.md"
---

# Claude Code now reads AGENTS.md if there is no Claude.md

> Hacker News · 2026-09-18 · 개발자 도구/AI 인프라

---

최근 공개된 Claude Code 체인지로그는 프로젝트 구성과 게이트웨이 동작, 관찰성, 권한·세션 안정성 측면에서 현실적인 개선을 다수 담고 있습니다. 우선 프로젝트 지침 파일 처리에서 CLAUDE.md가 없을 때 AGENTS.md를 대신 읽도록 했고(설정은 /config, Bedrock·Vertex·Foundry에는 아직 미적용), 프록시 환경을 위한 CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1 변수를 추가해 포워드 프록시에 호스트명을 전달하도록 변경했습니다. 게이트웨이 업스트림에 정적 헤더를 보낼 수 있는 headers: map 옵션이 추가되어 프록시 앞에 자체 제공자를 두는 구성에서 유용합니다. 또한 EndConversation 도구 추가와 장기 실행 도구 호출에 대한 주기적 진행 상태(heartbeat)는 악용·탈출(jailbreak) 대응과 장시간 작업의 가시성 개선을 목적으로 합니다.
안정성과 운영성 개선도 광범위합니다. 세션·플러그인 설치·업데이트 검사·파일 편집·툴 호출 등에서 여러 크래시와 교착 상태를 수정했고, WebFetch/WebSearch 거부 사유를 더 명확히 전달하도록 바꿨습니다. 관찰성 측면에서는 message.uuid, client_request_id, tool_source 같은 OpenTelemetry 이벤트 속성이 추가되고, OTel 콘텐츠 길이 제한을 제어하는 CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH가 도입되어 로그 상관과 툴 출처 추적이 쉬워집니다. 문맥 비용 절감(내장 claude-api 스킬을 동적 로딩해 ~200k+ 토큰에서 ~25k로 축소), 세션별 WebSearch·서브에이전트 생성 상한과 같은 루프 방지 제한, 권한 프롬프트·원격 제어 동작 개선 등은 운영 환경에서의 안전성과 비용 효율성에 직접적인 영향을 줍니다. 전반적으로 이번 릴리스는 실무적 신뢰성·가시성·제어성을 높이는 여러 실용적 수정을 포함합니다.

[Hacker News에서 원문 읽기 →](https://code.claude.com/docs/en/changelog)

