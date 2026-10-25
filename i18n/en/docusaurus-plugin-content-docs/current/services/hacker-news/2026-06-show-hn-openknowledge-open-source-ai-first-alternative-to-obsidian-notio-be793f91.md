---
title: "Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion"
sidebar_label: "Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion"
---

# Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion

> Hacker News · 2026-06-25 · Developer Tools

---

OpenKnowledge는 로컬 퍼스트 WYSIWYG 마크다운 편집기이자 LLM 위키를 표방하는 오픈소스 도구로, macOS 데스크톱 앱과 웹 UI/CLI(리눅스·윈도우·인텔 맥 지원)로 제공된다. Claude, Codex, Cursor 등 에이전트와의 직접 통합을 통해 에이전트가 내장 브라우저에서 편집기를 열어 사이드바 형태로 작업할 수 있으며, MCP/CLI 연동으로 어떤 하네스에도 적용 가능하다고 소개된다. 기본 제공 기능으로는 에이전트 기반 검색(RAG), MCP와 스킬 세트, 팀 공유용 '노코드' 동기화 기능이 있으며 내부적으로는 git/GitHub를 활용해 데이터 프라이버시를 유지하는 모델을 취한다. 사용자 문서와 데스크톱 설치 방법, CLI 예제(npm을 통한 설치와 프로젝트 초기화·서빙 명령)도 공개되어 있어 실사용 진입 장벽을 낮췄다.
기술적 의미는 편집기와 마크다운 간의 상호 운용성, 협업 동기화 문제 해결에 집중한다는 점이다. ProseMirror 기반의 WYSIWYG 상태와 바이트-충실한 마크다운 표현을 상호 변환하는 파이프라인과, ProseMirror와 마크다운 상태를 동기화하는 듀얼 옵저버 CRDT 설계가 핵심 엔지니어링 과제로 제시된다. 또한 yjs(CRDT), Tiptap/ProseMirror, CodeMirror, remark/rehype 등 오픈소스 스택을 활용해 협업·버전관리(undo/redo, 에이전트별 활동 표시)와 에이전트 편집 경험을 결합하려는 시도가 눈에 띈다. GPL-3.0-or-later 라이선스로 공개되어 기여와 포크가 가능하며, 에이전트 통합과 로컬 우선 설계를 통해 팀 단위의 마크다운 중심 워크플로에 실용적 대안을 제시한다.

[Hacker News에서 원문 읽기 →](https://github.com/inkeep/open-knowledge)

