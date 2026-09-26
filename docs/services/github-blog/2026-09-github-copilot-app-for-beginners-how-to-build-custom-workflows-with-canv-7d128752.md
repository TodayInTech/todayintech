---
title: "GitHub Copilot app for Beginners: How to build custom workflows with canvases"
sidebar_label: "GitHub Copilot app for Beginners: How to build custom workflows with canvases"
---

# GitHub Copilot app for Beginners: How to build custom workflows with canvases

> GitHub Blog · 2026-09-25 · GitHub Copilot

---

많은 도구가 고정된 화면을 제공해 사용자가 도구에 맞춰야 하는 반면, GitHub Copilot 앱의 '캔버스'는 먼저 원하는 워크플로우를 설명하면 인터페이스가 그에 맞춰 만들어지는 접근을 제안한다. 캔버스는 칸반 보드, 이슈 분류판, 릴리스 체크리스트, 대시보드나 스프레드시트처럼 작업 방식에 맞춘 UI로 구성되며, /create-canvas 스킬을 실행하고 워크플로우, 사용자 인터페이스에서 할 수 있는 일, 에이전트가 수행해야 할 일을 평범한 영어 설명으로 입력하면 에이전트가 우측 패널에 바로 인터페이스를 생성한다. 코딩이나 레이아웃 수작업 없이 초기 버전을 얻을 수 있고, 생성한 캔버스는 확장(extension)으로 저장해 프로젝트 단위나 개인용으로 재사용할 수 있다.
캔버스의 핵심은 실시간 양방향 상태 공유다. 사용자가 버튼을 누르거나 카드를 이동하면 상태가 즉시 갱신되어 에이전트가 별도 동기화 없이 같은 상태를 보고 같은 조작(항목 추가·이동·업데이트)을 수행할 수 있다. 레이아웃 메뉴가 고정돼 있지는 않지만 워크플로우를 설명하면 에이전트가 반복적으로 수정·개선해 줄 수 있어, 열 추가·필터 적용·오픈 PR 연동이나 일일 체크리스트 전환 등 실무적 변형이 가능하다. 커뮤니티의 기존 캔버스(예: 릴리스 노트 도구, 칸반, 이슈 트리아지)를 설치해 기본으로 삼고 에이전트에게 맞춤화를 맡기는 방식으로 시작해도 된다. 이 방식은 도구 적응 비용을 낮추고 에이전트와 사용자 간의 공동 조작을 통해 작업 흐름을 자동화·가속화할 수 있다는 점에서 실무적 의미가 크다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/)

