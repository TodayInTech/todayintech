---
title: "Your contributors are AI-first now. Is your project?"
sidebar_label: "Your contributors are AI-first now. Is your project?"
---

# Your contributors are AI-first now. Is your project?

> GitHub Blog · 2026-08-12 · Open Source / Maintainers

---

AutoGPT의 사례는 유지관리자가 ‘에이전트 기여자’와 공존하려면 문서만으로는 부족하다는 현실을 보여준다. AutoGPT는 수만 개의 스타와 수백 개의 오픈 PR을 마주하면서 에이전트가 리포지토리의 어느 디렉터리에서든 바로 읽을 수 있는 AGENTS.md·CLAUDE.md 같은 파일을 코드 옆에 두고, 커밋 트레일러로 에이전트 제출을 식별하도록 만드는 방식으로 문제에 대응했다. 또한 스킬(skill)과 트리거 문구를 통해 자동화가 특정 작업(예: Storybook 테스트 생성, test PR 스킬의 브라우저 실행)을 실제로 수행하게 하여 에이전트가 단순 텍스트를 채우는 수준을 넘어 코드를 실행·검증하게 만들었다.
실용적 게이트도 핵심이다. PR 템플릿 강제화는 에이전트의 행동을 바꾸는 효과를 냈고, CI 커버리지 체크를 ‘벽’으로 설정하면 에이전트가 테스트를 추가하도록 유도된다. CLA나 코드 오브 컨덕트 등 사람 인증 절차는 에이전트의 자동 제출을 걸러내는 인간 감지 장치로 작동한다. 한편 잘못 배치된 AGENTS.md는 오히려 문맥을 오염시키고, GraphQL 레이트 리밋·리뷰 툴 비용·남은 권한 잔류 등 운영상의 문제도 발생하므로 GitHub App 인증과 권한 감사가 권장된다. 핵심은 판단은 유지관리자에게 남겨두되, 규칙을 코드 옆에 두어 에이전트와 기여자가 ‘같은 장소’를 보게 하는 것이다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/open-source/maintainers/your-contributors-are-ai-first-now-is-your-project/)

