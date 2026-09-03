---
title: "GitHub Copilot app for Beginners: Run several agents at once"
sidebar_label: "GitHub Copilot app for Beginners: Run several agents at once"
---

# GitHub Copilot app for Beginners: Run several agents at once

> GitHub Blog · 2026-09-03 · AI &amp; ML

---

여러 AI 에이전트를 같은 코드베이스에서 동시에 돌리면 통제가 어렵다고 느끼기 쉽지만, GitHub Copilot 앱은 각 작업을 독립된 '세션'으로 관리해 그 걱정을 덜어준다. 세션 뷰에서는 각 작업 카드가 제목과 진행 상태를 보여주며, 각 세션은 서로 간섭하지 않고 언제든 새 세션을 시작할 수 있다. 저자는 이를 세탁소의 여러 세탁기 비유로 설명하며, 각 세탁기가 독립된 설정으로 동시에 돌아가도 서로 영향을 주지 않는다고 말한다. 실무적으로 중요한 부분은 각 세션이 자체 Git worktree에서 동작한다는 점으로, 이로 인해 세션 간 격리가 물리적(파일 트리 관점)으로 보장되어 병렬 실행이 가능해진다.
이런 구조는 개발 흐름에서 '지켜보기' 대신 '검토와 의사결정'에 시간을 더 쓰게 해준다. 예시로는 tailspin-toys 저장소에서 funded sort 추가, 접근성 검토, 테스트 실행을 각각 별도 세션으로 동시에 돌려 결과를 세션 뷰에서 확인하는 과정이 제시된다. 각 세션이 자체 컨텍스트를 유지하므로 작업 전후에 상태를 재설명할 필요가 없고, 컨텍스트 전환 비용이 줄어든다. 저자는 두 개의 작은 작업부터 병렬 세션을 시도해 보라고 권하며, 개발 생산성 관점에서 병렬 에이전트 세션과 Git worktree 분리는 실무적 이점을 제공한다고 결론짓는다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/)

