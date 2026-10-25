---
title: "How to continue a GitHub Copilot app session in VS Code"
sidebar_label: "How to continue a GitHub Copilot app session in VS Code"
---

# How to continue a GitHub Copilot app session in VS Code

> GitHub Blog · 2026-10-19 · AI &amp; ML / GitHub Copilot

---

GitHub Copilot 앱에서 에이전트가 대규모 변경을 완료한 뒤 세부 구현을 직접 검토하고 로컬에서 실행해보고 싶을 때, 세션을 그대로 VS Code로 열어 이어서 작업할 수 있다는 사용 가이드입니다. 세션은 단순한 파일 모음이 아니라 작업 목표, 계획, 대화 내역을 모두 보존하므로 별도로 요약하거나 새 채팅으로 옮길 필요 없이 ‘Open in VS Code’로 선택하면 해당 세션의 워크트리와 연동된 VS Code가 열리고 Copilot 사이드바에 기존 세션이 그대로 표시됩니다. 이렇게 하면 변경 내역을 소스 컨트롤 뷰에서 라인 단위로 검토하고, 사이드바에서 그대로 Copilot에 추가 요청을 하거나 질문을 던져 구현 의도를 확인할 수 있습니다.
검토 후에는 VS Code에서 직접 파일을 편집하고 통합 터미널로 프로젝트의 일반적인 검증 흐름(예: npm install, npm test, npm run lint, npm run dev)을 실행해 동작을 확인할 수 있습니다. 개발 서버의 로컬 URL을 브라우저나 통합 브라우저로 열어 UI 변경을 다양한 뷰포트에서 점검하는 것까지 권장하며, 최종적으로는 소스 컨트롤 뷰나 터미널로 git add/commit/push를 수행하면 세션과 연동된 브랜치에 그대로 반영되어 기존 풀 리퀘스트를 재연결할 필요가 없습니다. 글은 또한 GitHub의 맥락 인식 비밀 탐지기 성능 개선 수치(검출 품질 향상 11.5%, 중간 스캔 시간 86% 단축)와 리포지토리용 커스텀 지침·스킬·에이전트 연결 가능성 등 다른 AI 관련 기능들도 함께 언급합니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/)

