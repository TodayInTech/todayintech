---
title: "Stacked sessions and pull requests in the GitHub Copilot app"
sidebar_label: "Stacked sessions and pull requests in the GitHub Copilot app"
---

# Stacked sessions and pull requests in the GitHub Copilot app

> GitHub Blog · 2026-07-30 · AI &amp; ML

---

Cassidy Williams는 10년 넘은 개인 앱을 현대화하면서 GitHub Copilot 앱의 '스택된 세션'과 이를 바탕으로 한 연쇄적인 풀 리퀘스트 워크플로우를 사용한 경험을 공유한다. 오래된 의존성(React 15, Less, 오래된 react‑bootstrap 등)과 얽힌 변경들을 한 번에 바꾸려다 실패한 뒤, Plan 모드에서 AI(예: Claude Opus, GPT 리뷰)를 활용해 설계·검토를 반복했고, 초기 일괄 갱신 시도는 불완전하게 끝났지만 Copilot 앱이 세션을 분리해 작업을 이어가게 하면서 문제를 해결했다. 또한 콘솔에서 발견한 findDOMNode·componentWillReceiveProps 같은 오래된 API 의존성은 라이브러리 교체를 권하는 플랜으로 이어졌다.
실무적 핵심은 ‘스택’의 개념이다. Copilot 앱은 현재 진행 중인 변경에 대해 풀 리퀘스트를 만들고, 그 위에 이어질 작업을 별도 세션으로 쌓아 이전 세션의 브랜치를 대상으로 하는 연속된 PR 체인을 자동으로 구성했다. 저자는 이렇게 분리된 세션 덕분에 범위를 조절하고 기존 배포(예: dev 브랜치)에 안전하게 변경을 적용할 수 있었으며, 대규모 단일 PR에서 오는 범위 확장과 혼란을 피할 수 있었다고 평가한다. 이 사례는 레거시 코드 현대화나 단계적 마이그레이션을 계획하는 개발자에게 스택된 세션·PR이 왜 유용한지, 그리고 도구가 실제로 어떻게 개발 흐름을 단순화하는지 실무적으로 보여준다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/)

