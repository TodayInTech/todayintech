---
title: "Getting the most out of Opus 5.5 in Claude and Claude Code"
sidebar_label: "Getting the most out of Opus 5.5 in Claude and Claude Code"
---

# Getting the most out of Opus 5.5 in Claude and Claude Code

> Hacker News · 2026-10-03 · AI 도구/모델 사용 가이드

---

Opus 5.5는 이전 Opus 모델과 달리 긴 다단계 작업을 스스로 길게 수행하고, 작업 진행을 더 명료한 문장으로 보고하며, 응답 전 '얼마나 생각할지' 스스로 결정한다는 점이 핵심이다. 이 가이드는 Claude 앱과 Claude Code에서 Opus 5.5를 쓸 때 실무자가 바로 적용할 수 있는 행동 지침을 모아둔다. 한 번에 전체 작업을 하나의 메시지로 주고 완료 조건(예: 테스트 통과, 모든 엔드포인트 마이그레이션)을 명확히 적어 두면 모델이 목적을 향해 오래 달릴 수 있고, “think step by step” 같은 문구는 빼라는 권고는 응답 시작 시간을 줄이면서 품질 저하를 막는 사례로 제시된다. 또한 중간에 기억을 추가하거나 디자인 선호를 구체적 패턴으로 나열해 기본 스타일을 바꾸는 등 긴 실행을 관리하는 실무 팁을 담고 있다.
긴 런을 다루는 구체적 방법도 제시된다. 장기 작업 목록을 TASKS.md로 관리해 컨텍스트 창이 채워져도 진행 상황을 잃지 않도록 하고, CLAUDE.md에 언제 멈추고 질문할지(파괴적 조치 전 등) 규칙을 적어두면 불필요한 정지를 줄일 수 있다. 대규모 감사나 마이그레이션은 서브에이전트로 분할해 병렬 검사 후 증거를 검토하도록 권장하며, 차트·스크린샷 판독과 스프레드시트·문서 생성 품질이 개선된 점, fast 모드(연결 미리보기·비용 상향) 사용법, 그리고 Fable 수준의 바이오·사이버 안전장치로 인해 특정 요청이 이전 모델로 전환될 수 있음을 보고받는 절차과 대처 방법도 담겨 있다. 전반적으로 실무자가 Opus 5.5의 장기 실행 특성을 받아들이고 프로젝트별 규칙을 설계해 안정성과 생산성을 높이도록 돕는 실용서다.

[Hacker News에서 원문 읽기 →](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

