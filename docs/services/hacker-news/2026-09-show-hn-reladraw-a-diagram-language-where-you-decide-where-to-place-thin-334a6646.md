---
title: "Show HN: Reladraw – A diagram language where you decide where to place things"
sidebar_label: "Show HN: Reladraw – A diagram language where you decide where to place things"
---

# Show HN: Reladraw – A diagram language where you decide where to place things

> Hacker News · 2026-09-26 · Developer Tools / Visualization

---

reladraw는 좌표 대신 ‘무엇이 어디에 있는지’를 문장으로 적어 다이어그램을 서술하는 텍스트 언어다. Mermaid나 Graphviz처럼 전적으로 자동 배치를 맡기지 않고, Draw.io·Figma처럼 절대 좌표로 손수 배치하는 쪽도 아닌 중간 지점을 겨냥한다. 파일에는 위/아래·왼쪽/오른쪽·사이 등 관계만 쓰여 있고 엔진이 그 관계들로부터 모든 거리를 결정한다는 점이 핵심이다. 저장소에는 브라우저에서 바로 써볼 수 있는 플레이그라운드와 npm 전역 설치 예시(예: npm install -g reladraw, reladraw diagram.reladraw -o diagram.svg), 그리고 에이전트 스킬 설치 커맨드(npx skills add reladraw/reladraw -g, -a 옵션 사용 가능)가 포함되어 있다. 이름·로고는 라이선스 범위에서 제외된다는 점도 명시되어 있다.
기술적으로는 파서, 결정론적 리졸버(최소 거리 제약을 받아 최단 해를 찾는 방식—최장 경로 알고리즘 이용), 정적 SVG 렌더러가 구현되어 있으며(이들이 v0.5.0에 포함), CLI로 텍스트 파일을 받아 독립형 SVG를 출력한다. 겹침 방지와 배치 결정은 파일에 명시된 관계에서 유도되며, 엔진은 자동 배치처럼 예측 불가능한 그림을 만들어내는 자유를 거부한다. 반면 아직 구현되지 않은 부분도 분명하다: 진단 리포트의 완전한 제공, 노드를 회피하는 고급 에지 라우팅, 아이콘·타이포그래피 개선 등이 남아 있고 문법은 안정화되지 않은 상태다. 에이전트 관점에서 중요한 설계 선택은 ‘파일 자체가 의도를 표현하고 에이전트가 그 파일을 다시 읽어 편집한다’는 흐름으로, 렌더링-비전-픽셀 계산을 거치지 않고 텍스트 수준에서 다이어그램을 변경·확인할 수 있게 한다는 점이다.

[Hacker News에서 원문 읽기 →](https://github.com/reladraw/reladraw)

