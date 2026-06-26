---
title: "Show HN: Smart model routing directly in Claude, Codex and Cursor"
sidebar_label: "Show HN: Smart model routing directly in Claude, Codex and Cursor"
---

# Show HN: Smart model routing directly in Claude, Codex and Cursor

> Hacker News · 2026-06-26 · AI 인프라 / 개발자 도구

---

Weave가 공개한 라우터는 Anthropic·OpenAI·Gemini 호환 엔드포인트를 흉내내는 드롭인 프록시로, 요청별로 최적 모델을 골라 보내는 기능을 제공합니다. 로컬 또는 호스팅 형태로 동작하며 Claude Code, Codex, opencode, Cursor 등 코딩 에이전트와 즉시 연동되도록 설치 스크립트(npx @workweave/router)와 self-hosted용 make 흐름을 제공합니다. 라우터는 Anthropic Messages, OpenAI Chat Completions, Gemini 네이티브 등의 API를 말하고 스트리밍·툴·비전까지 지원하며, OpenRouter를 통해 DeepSeek, Kimi, GLM, Qwen, Llama, Mistral 같은 OSS 모델도 이용할 수 있습니다. 운영 측면에서는 BYOK(키는 로컬에 암호화 저장), OTLP 트레이스와 대시보드(로컬 UI), 토큰 수 세기·라우팅 디시전 조회용 /v1/route 등 실무에 필요한 엔드포인트와 토글 방식이 상세히 문서화되어 있습니다.
기술적 핵심은 요청 단위 라우팅 전략으로, 문서에 따르면 Avengers-Pro 계열의 클러스터 스코어러와 온박스 임베더를 활용해 모델 선택을 결정합니다. 피드 요약에는 수만 건의 에이전트 트레이스에 RL 보상 신호를 학습시켜 유효한 모델 선택에 보상을 주었다고 밝히며, 내부 사용 결과 토큰 비용을 약 40% 절감했다고 주장합니다. 이런 접근은 프런티어 모델을 필요한 경우에만 쓰고 경량·저비용 모델로 반복 작업을 처리해 비용-지연 트레이드를 관리하려는 팀에 실질적 이득을 줄 수 있습니다. 소스 가용성(Elastic License 2.0)과 호스팅 옵션(weaverouter.com)도 함께 제공되어 바로 실험해볼 수 있는 점이 실무적 의미를 높입니다.

[Hacker News에서 원문 읽기 →](https://github.com/workweave/router)

