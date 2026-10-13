---
title: "GitHub Copilot app for Beginners: How to teach Copilot about your codebase"
sidebar_label: "GitHub Copilot app for Beginners: How to teach Copilot about your codebase"
---

# GitHub Copilot app for Beginners: How to teach Copilot about your codebase

> GitHub Blog · 2026-10-12 · AI &amp; ML

---

코드베이스 맥락은 AI 도구의 유용성을 크게 좌우한다는 전제로 글은 Copilot을 레포지토 수준에서 ‘가르치는’ 네 가지 수단을 제시한다. 우선 저장소 전반의 규칙을 정의하는 .github/copilot-instructions.md와 파일 경로별로 적용할 수 있는 .github/instructions의 applyTo를 통해 Copilot이 기본 아키텍처·네이밍·테스트 기대치를 자동으로 참조하게 할 수 있다. 반복되는 절차는 .github/skills 아래의 스킬 폴더로 묶어 SKILL.md에 “언제 이 스킬을 써야 하는지”, 실행할 테스트·린트 스크립트, 실패 시 대처법 등을 명시하면 해당 절차를 수행할 때 Copilot이 필요한 자원과 과정을 불러온다. 더 넓은 작업에는 .github/agents로 정의한 커스텀 에이전트를 써서 접근성 검토처럼 여러 파일과 도구를 넘나드는 역할을 부여할 수 있다. 외부 도구 연동은 MCP 서버로 확장된다. 문서 서버나 Playwright 같은 MCP를 연결하면 Copilot이 브라우저를 열어 애플리케이션을 직접 상호작용하며 동작을 검증할 수 있다.
이들 도구는 각각의 문제를 해결하지만 조합할 때 효과가 커진다는 점이 기술적 요지다. 규칙은 인스트럭션으로, 반복 작업은 스킬로, 복합적 역할은 에이전트로, 런타임 확인은 MCP로 나누어 설계하면 Copilot이 매번 같은 설명을 요구하지 않고도 팀의 방식으로 코드 변경·테스트·검증을 수행한다. 실무 권고로는 먼저 한 가지 규칙을 .github/copilot-instructions.md에 추가해 적용 결과를 관찰한 뒤 자주 반복되는 절차를 스킬로 정형화하고, 필요하면 에이전트와 MCP를 도입해 범위를 넓혀가라는 점을 제시한다. 또한 커뮤니티에서 공유되는 Awesome Copilot 리소스를 참고해 기존 워크플로에 맞춘 구성요소를 가져와 적응시키는 접근을 권한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-teach-copilot-about-your-codebase/)

