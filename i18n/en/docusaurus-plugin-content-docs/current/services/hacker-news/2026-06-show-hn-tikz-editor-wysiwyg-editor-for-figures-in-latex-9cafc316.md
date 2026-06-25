---
title: "Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX"
sidebar_label: "Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX"
---

# Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

> Hacker News · 2026-06-23 · 개발자 도구

---

TikZ는 논문 그림을 코드로 그리는 LaTeX 패키지로, 좌표를 손으로 조정하며 재컴파일하는 방식이 흔하다. 피드에 따르면 작성자는 웹·데스크톱용 오픈소스 WYSIWYG TikZ 편집기를 공개했으며, 소스 코드와 렌더링을 동시에 보여주고 양쪽을 동기화해 사용자가 드래그로 요소를 옮기면 코드 내 좌표 숫자만 정확한 원위치에 맞춰 바꾼다고 설명한다. 작성자는 동일한 편집 환경을 제공하는 다른 사례를 알지 못한다고 덧붙였다.
피드 기준으로는 이 앱이 각 객체의 원본 소스 위치를 추적해 들여쓰기나 줄바꿈 같은 형식을 유지하면서 수치만 수정하는 점을 핵심 구현으로 삼는다. 또한 작성자는 TikZ의 상당 부분을 재구현해야 했고 SVG·pptx·ipe 변환기, 다중 행 노드를 위한 LaTeX 하이픈·줄바꿈 알고리듬 재구현, LaTeX 색 혼합 표기 지원 색상 선택기 등 부가 기능을 개발했다고 적시해, 대규모 코드 변환과 자동화 도구(작성자는 Codex 사용을 언급)를 활용한 편집기화의 기술적 함의를 보여준다.

[Hacker News에서 원문 읽기 →](https://tikz.dev/editor/)

