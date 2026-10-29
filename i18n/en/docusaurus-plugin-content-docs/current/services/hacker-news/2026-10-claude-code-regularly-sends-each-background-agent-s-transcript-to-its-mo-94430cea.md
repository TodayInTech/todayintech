---
title: "Claude Code regularly sends each background agent’s transcript to its model"
sidebar_label: "Claude Code regularly sends each background agent’s transcript to its model"
description: "Flamerix AI는 Claude Code(2.1.257–2.1.312)가 백그라운드 에이전트의 전체 대화를 매 ~30초마다 모델(Opus 등)으로 보내 짧은 요약을 요청하도록 기본 활성화되어 있으며, 이 호출이 OpenTelemetry에서 상당한 비용(대략 16% 수준)과 요청 비중을 차지하므로 운영자는 제공된 Bun preload 훅으로 차단하거나 OpenTelemetry로 검증해야 한다고 밝혔습니다."
---

# Claude Code regularly sends each background agent’s transcript to its model

> Hacker News · 2026-10-29 · AI/ops/security

---

Flamerix AI의 조사에 따르면 Claude Code(테스트 범위: 2.1.257–2.1.312)는 **백그라운드 에이전트마다 약 30초 간격으로 그 에이전트의 전체 대화(transcript)를 모델(주로 Opus)에 전송**해 "최근 행동을 3–5단어로 설명"하도록 요청한다. 이 요약 요청은 에이전트 패널의 상태 줄만 갱신할 뿐 대화 스레드에는 노출되지 않는다고 보고서가 명시한다. (보고자: Flamerix AI)

## 주기적 에이전트 요약 호출의 증거와 범위

- 해당 동작은 **2.1.232(2026-08-13)**부터 기본으로 켜졌으며 조사 대상 버전 범위는 **2.1.257–2.1.312**이다. (근거: chunk-0001, chunk-0003)
- OpenTelemetry 집계에서 query_source = agent_summary 항목이 전체 비용(Flamerix의 추정 cost_usd 기준)에서 **약 16%**를 차지했고 API 요청 중 비중은 약 **19.7%**로 보고되었다. 독립 측정(4건)은 18–26% 범위를 기록했다. (근거: chunk-0001)
- 이러한 요청은 세션 로그(디스크)에 기록되지 않으며, OpenTelemetry에서만 포착된다. (근거: chunk-0003)

## 운영상 의미 (비용·토큰·검증)

- Flamerix는 이 호출이 구독 기반 이용자의 경우 직접 청구 항목이 아니라 **rate-limit(할당) 여유를 잠식**할 수 있다고 명시한다. 또한 약 98%는 캐시에서 읽어 비용이 낮지만 일부 냉캐시가 전체 비용의 상당 부분을 끌어간다고 보고한다. (근거: chunk-0003)
- 서버 플래그로만 동작을 조절할 수 있어 클라이언트 설정만으로 완전히 끌 수 없는 구조이며, SDK 옵션(agentProgressSummaries=false)은 번들 내 코드 경로에서는 무력하다고 기술되어 있다. (근거: chunk-0003)

## 즉시 적용 가능한 차단 방법과 한계

Flamerix는 Linux에서 동작하는 Bun preload 훅(no-agent-summary.js, 약 80줄)을 공개해 요약 타이머를 무력화하는 방법을 제시한다. 핵심 동작은 다음과 같다. (근거: chunk-0001, chunk-0002)

- Function.prototype.toString로 타이머 콜백의 소스 텍스트를 검사해 요약 관련 앵커(예: "\[AgentSummary\] Timer fired")가 포함된 setTimeout/setInterval 콜백만 인식하고, 해당 타이머를 2^31−1 ms(사실상 무기한) 지연을 주는 비활성 핸들로 바꾼다.
- 설치: no-agent-summary.js를 사용자 경로에 저장하고, BUN_OPTIONS="--preload /abs/path/no-agent-summary.js"를 전역 환경에 설정한 뒤 데몬을 재시작(claude daemon stop --any)해 모든 Claude Code 프로세스에 적용한다. (근거: chunk-0001, chunk-0002)

한계와 검증 포인트

- 훅은 **콜백 내부의 문자열 매칭에 의존**하므로 업데이트로 로그 라인이 바뀌거나 콜백이 bind/wrapper로 전달되면 매칭이 실패하고 요약이 되살아난다. 따라서 업데이트 후에 반드시 Verify 단계를 재실행해야 한다. (근거: chunk-0002)
- 플랫폼 검증은 Linux에서만 수행되었고 macOS·Windows는 미검증(Windows에서는 /$bunfs/ 경로로 인해 훅이 설치되지 않을 가능성 있음). (근거: chunk-0002)
- 적용 후 OpenTelemetry에서 query_source = agent_summary가 0인지 확인하는 것이 유일하게 모든 실패 모드를 잡아내는 검증 방법이다. (근거: chunk-0002)

## 다른 관련 기술적 포인트

- 2.1.300(2026-10-14)부터는 서버에서 간격(30–240초)을 조정할 수 있고, 2.1.310(2026-10-23)에는 'short' 모드(트랜스크립트 대신 약 2k 토큰 노트 사용)가 추가됐지만 기본값은 여전히 전체 전송이고 short 모드는 서버 플래그 없이는 활성화되지 않는다. (근거: chunk-0003)
- Flamerix가 훅을 적용한 시스템(예: 2.1.301)에서는 OpenTelemetry에 agent_summary 요청이 0으로 내려갔음을 보고했다. (근거: chunk-0002)

실무적 시사점은 직접적이다: 운영자는 (1) 내부 OpenTelemetry나 메트릭을 점검해 agent_summary 호출 비중과 비용 영향을 확인하고, (2) 즉시 차단이 필요하면 Flamerix의 Bun preload 훅을 검토·시험 적용하며, (3) Claude Code의 업데이트마다 훅의 유효성을 재검증해야 한다는 점이다. 제공된 훅은 운영자가 선택적으로 적용할 수 있는 임시 방편으로서 유효하지만, 플랫폼 간 호환성·업데이트 내성·공식 지원 여부는 근거 문서에 포함되어 있지 않으므로 추가 확인이 필요하다.

참고: 원문 조사는 Flamerix AI(MIT License)가 제공했으며, 모든 명령·설정·버전 정보는 그들의 근거 문서(chunk-0001~0003)를 따랐습니다.

[Hacker News에서 원문 읽기 →](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)

