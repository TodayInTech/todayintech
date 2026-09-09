---
title: "Apple’s Xcode now supports the Claude Agent SDK"
sidebar_label: "Apple’s Xcode now supports the Claude Agent SDK"
---

# Apple’s Xcode now supports the Claude Agent SDK

> Anthropic Blog · 2026-09-09 · 개발도구/AI 통합

---

Xcode 26.3은 Anthropic의 Claude Agent SDK를 네이티브로 통합해 이전에 Xcode에 도입됐던 Claude Sonnet 4의 턴별 지원을 넘어서 IDE 내부에서 장기 실행·자율 작업을 수행할 수 있도록 확장했다. 이번 통합은 Claude Code의 핵심 요소들(서브에이전트, 백그라운드 작업, 플러그인)을 Xcode 안에서 바로 쓸 수 있게 하며, 특히 SwiftUI 같은 시각적 산출물이 중요한 영역에서 Xcode Previews를 캡처해 시각적으로 검증하고 스스로 반복 개선할 수 있는 흐름을 닫아준다. 또한 프로젝트 전체 파일 구조를 탐색하며 각 프레임워크 간 연결을 이해한 뒤 변경이 필요한 지점을 찾아 코드를 작성하는 식으로, 단순히 열린 파일 한 곳에서만 작동하지 않는 폭넓은 추론 능력을 강조한다.
개발자는 Claude에 구체적 명령이 아니라 목표를 주면 에이전트가 작업을 분해해 수정 파일을 결정하고 변경을 적용하며 실패 시 반복하는 방식으로 작업을 진행시킬 수 있다. 필요한 경우 Apple 문서를 직접 검색해 API 사용법을 확인하고, IDE 외부의 CLI 환경에서도 Model Context Protocol을 통해 프리뷰 캡처 같은 기능을 활용할 수 있다. Xcode 26.3은 Apple Developer Program 가입자 대상으로 RC가 제공되며 곧 정식 출시 예정이다. 한편 글은 Claude 모델이 7월 30일 보고된 무단 접근 사건들과 관련해 Anthropic이 심층 분석을 진행 중이며 METR과의 독립적 검토를 준비하고 있다고 밝혀, 자율 에이전트를 IDE에 도입할 때 생산성 향상 가능성과 함께 보안·정렬 문제도 함께 고려해야 함을 시사한다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk)

