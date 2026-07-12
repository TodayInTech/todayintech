---
title: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k"
sidebar_label: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k"
---

# Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

> Hacker News · 2026-07-12 · AI 개발자 툴

---

systima가 Claude Code와 OpenCode를 같은 모델·같은 기계·동일 과제에서 비교 측정한 결과를 정리한 글이다. 가장 단순한 확인에서 Claude Code는 사용자 프롬프트가 도달하기 전에 시스템 프롬프트·툴 스키마·스캐폴딩 등으로 약 33,000 토큰을 전송한 반면 OpenCode는 약 7,000 토큰을 보냈다. 모델 계열을 바꿔 재실행하면 격차가 줄어들어(Claude Fable 5에서는 대략 3.3배) 모델 의존성이 존재하지만, 전반적으로 Claude Code의 초기 베이스라인이 훨씬 크다. 툴 스키마만으로도 Claude Code는 약 24,000토큰, OpenCode는 약 4,800토큰을 차지했고, 72KB짜리 리포지토리 지침 파일 하나가 각 요청에 평균 20,000토큰을 추가하는 등 실운영 구성 요소가 비용을 크게 증폭시킨다.
캐시·세션 행동이 비용 차이를 설명하는 핵심 메커니즘으로 제시된다. OpenCode는 요청 프리픽스가 바이트 단위로 동일해 세션당 캐시를 한 번만 읽어 재사용하는 반면 Claude Code는 세션 중간에 수만 토큰을 다시 쓰는 일이 반복되어 동일 작업에서 OpenCode 대비 캐시 쓰기량이 5.9배에서 최대 54배까지 벌어졌다. 캐시 쓰기는 더 높은 요율로 과금되므로 이러한 재쓰기와 서브에이전트 팬아웃(예: 직접 실행 시 121,000토큰이 두 서브에이전트로 분산되면 513,000토큰으로 증가)으로 대시보드 상의 사용량이 급증할 수 있다. 품질 측면에서는 본 실험의 과제들에서 두 허니스가 모두 정답을 내어 토큰 차이가 동일한 결과에 대한 비용 차이라는 점을 부각한다. 측정은 API 경계에 프록시를 두고 요청 바디와 사용량 블록을 캡처·해시 체인으로 보관하는 방식으로 이뤄졌으며, 단일 머신·버전·작은 표본이라는 한계가 명시되어 있다. 운영자는 어떤 파일명을 허니스가 실제로 읽는지(예: AGENTS.md vs CLAUDE.md)를 확인하고, 모델 경로에 게이트웨이가 개입하면 실제 어떤 모델로 요청이 라우팅되는지 API 경계에서 계측할 것을 권한다.

[Hacker News에서 원문 읽기 →](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)

