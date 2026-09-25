---
title: "Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design"
sidebar_label: "Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design"
---

# Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design

> Hacker News · 2026-09-24 · Developer Tools

---

Whiteboard는 사람과 코딩 에이전트가 하나의 작업 공간에서 소프트웨어를 설계하도록 돕는 오픈소스 데스크톱 앱입니다. 에이전트를 연결해 캔버스 위에 그리듯 설계 설명을 주고받을 수 있도록 SDK를 제공하며, 시퀀스 다이어그램이나 ERD 같은 시각화에서 클릭 한 번으로 기저의 코드로 이동할 수 있게 해 설계·구현 간 손실을 줄입니다. 에디터 경험은 Code OSS(벤더 포함)를 기반으로 키바인딩과 LSP 지원을 제공해 기존 개발 도구와의 연계를 유지하고, 추천 모델(GPT-6 Sol, Claude Opus 5.5 등)에 대한 언급을 통해 성능·비용 균형을 고려한 사용을 권장합니다.
기술적으로는 러스트로 작성한 AST 인식 시맨틱 디프 뷰어를 통해 노이즈가 많은 원시 디프 대신 의미 있는 변경만 골라 보여주고, 큰 함수는 의사코드로 요약하거나 테스트·문서 변경을 접어둘 수 있게 했습니다. 이 기능들은 WASM 기반 플러그인으로 커스터마이즈 가능해 확장성이 높습니다. 또한 에이전트의 자동 결정과 트레이스를 연결해 요구사항이 어떻게 구현됐고 에이전트가 어떤 결정을 내렸는지 추적하는 의사결정 로그를 제공해 변경의 근거를 파악하기 쉽게 합니다. 현재는 파일 직접 편집 기능과 멀티 리포지토리 리뷰 지원이 제한적이고, 공유된 리뷰는 이후 업데이트가 자동 반영되지 않는 등 제약이 명시되어 있으며 익명 텔레메트리는 코드나 프롬프트 등 민감 정보를 포함하지 않도록 설계되어 있습니다. MIT 라이선스로 자가 호스팅이 가능하고 향후 팀용 호스팅 제품이 계획되어 있어 오픈소스 기반으로 내부 워크플로우에 통합해 실험해볼 만한 툴로 보입니다.

[Hacker News에서 원문 읽기 →](https://github.com/devdotfast/whiteboard)

