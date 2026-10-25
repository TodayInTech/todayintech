---
title: "A guide to slash commands in the GitHub Copilot app"
sidebar_label: "A guide to slash commands in the GitHub Copilot app"
---

# A guide to slash commands in the GitHub Copilot app

> GitHub Blog · 2026-08-06 · AI &amp; ML

---

GitHub Copilot 데스크톱 앱은 채팅 입력창에서 /를 입력하면 호출되는 슬래시 명령으로 개발자 워크플로를 단축하고 세션 기반 작업을 손쉽게 관리하도록 설계됐다. CLI의 슬래시 명령은 터미널 중심의 작업(디렉터리 추가, 작업 디렉터리 설정 등)에 맞춰진 반면, 앱은 시각적 인터페이스와 자동 프로젝트 컨텍스트 관리를 전제로 하므로 /clear, /model 같은 공통 명령은 유지하되 /add-dir나 /cwd 같은 파일 액세스 명령은 필요하지 않다고 설명한다. 입력창의 자동완성 메뉴는 현재 컨텍스트에서 사용 가능한 명령을 보여주고, 명령 일부는 Mode 드롭다운과 연계되어 세션을 Plan 또는 Autopilot 모드로 전환할 수 있다는 점도 강조된다.
구체적 명령으로는 계획 수립을 돕는 /plan(예: 2단계 인증 추가, 알림 시스템 리팩터, 체크아웃 흐름 조사), 접근법을 검증하는 /spar(설계 가정·스케일·일관성 문제 지적), 목표 기반으로 구현을 진행하는 /autopilot, 독립 모델로 검토해 맹점을 찾는 /rubber-duck(다른 모델을 써서 리스크·엣지 케이스 지적) 등이 소개된다. 또한 대화에서 대시보드나 인터랙티브 다이어그램을 만드는 /create-canvas와 여러 리포지토리를 가로지르는 작업을 분해·조정하는 /orchestrate도 포함되어, 단순한 단축키를 넘어 설계·검증·실행·조정까지 개발 사이클 전반을 지원하는 도구로 확장되는 기술적 의미를 갖는다. 이런 명령들은 포커스를 유지하면서 반복 작업을 줄이고, 멀티세션·멀티리포지토리 환경에서 협업과 자동화를 촉진하는 실용적 이점을 제공한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/a-guide-to-slash-commands-in-the-github-copilot-app/)

