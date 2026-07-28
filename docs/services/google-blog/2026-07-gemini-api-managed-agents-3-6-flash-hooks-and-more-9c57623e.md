---
title: "Gemini API Managed Agents: 3.6 Flash, hooks, and more"
sidebar_label: "Gemini API Managed Agents: 3.6 Flash, hooks, and more"
---

# Gemini API Managed Agents: 3.6 Flash, hooks, and more

> Google Blog · 2026-07-28 · Developer tools

---

Gemini API의 관리형 에이전트 기능이 환경 훅(environment hooks), 모델 선택, 무료 티어 접근, 예산·스케줄 제어 등으로 확장됐다. 기본 에이전트 antigravity-preview-05-2026은 코드 변경 없이 Gemini 3.6 Flash를 기본 모델로 사용하며, agent_config.model로 gemini-3.5-flash-lite 등 다른 모델을 명시적으로 고정할 수 있다. .agents/hooks.json에 pre_tool_execution·post_tool_execution 핸들러를 넣어 코드 실행·파일 쓰기 등 툴 호출 전후에 커스텀 스크립트나 HTTP 핸들러를 실행하고, matcher 필드의 정규식으로 대상 툴을 넓게 지정할 수 있다(예: gate.py로 보안 게이트, auto_lint.py로 포맷 검사). 예시처럼 후처리 훅을 원격 샌드박스 내부에서 돌려 이미지 검증이나 품질 파이프라인을 완결할 수 있다는 점이 핵심이다.
비용과 운영 측면에서도 변화가 있다. 무료 티어 프로젝트에서 관리형 에이전트를 실험할 수 있고, agent_config.max_total_tokens로 입력·출력·사고 토큰 전체를 상한해 과다 소비를 방지할 수 있다. 제한에 도달하면 실행은 안전하게 일시중지되고 상태가 "incomplete"로 반환되며 previous_interaction_id를 주어 이어서 실행할 수 있다. 또한 트리거를 등록해 크론 스케줄로 반복 작업을 자동화하고 동일 샌드박스를 재사용해 파일을 영속화하거나 Environments API로 세션을 조회·정리할 수 있다. 이 업데이트들은 원격 샌드박스에서 검증·자동화 파이프라인을 내부적으로 실행하면서 비용·스케줄 관리를 통합하는 방향으로 실무 적용성을 높인다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/)

