---
title: "Introducing Agent Skills | Claude by Anthropic"
sidebar_label: "Introducing Agent Skills | Claude by Anthropic"
---

# Introducing Agent Skills | Claude by Anthropic

> Anthropic Blog · 2026-07-22 · AI 플랫폼

---

Anthropic은 Claude에 'Skills'라는 개념을 도입해 특정 업무에서의 성능을 개선할 수 있게 했다. 스킬은 지침, 스크립트, 리소스를 담은 폴더 단위로 구성되며, Claude는 작업 맥락에서 관련성이 있을 때만 필요한 최소 정보와 파일을 로드해 처리 속도와 효율을 유지한다. 스킬은 조합(composable)되어 Claude가 여러 스킬을 자동으로 식별·조정하고, 포터블한 단일 형식으로 Claude 앱·Claude Code·API 전반에서 재사용할 수 있다. 또한 스킬은 실행 가능한 코드도 포함할 수 있어 토큰 생성에 의존하는 전통적 접근보다 신뢰성 있는 처리가 가능하다고 설명한다. 2025년 12월 업데이트로 조직 단위 관리, 파트너 제작 스킬 디렉토리, 크로스플랫폼 이식성을 위한 오픈 표준 등도 추가되었다.
실무 적용 측면에서 스킬은 이미 Claude 앱에서 스프레드시트·프레젠테이션 생성 등에서 사용되며, 사용자는 직접 스킬을 만들고 공유할 수 있다. Pro/Max/Team/Enterprise 이용자에 대해 제공되며, 팀·엔터프라이즈는 관리자 승인으로 조직 전반에 활성화해야 한다. 개발자용으로는 /v1/skills 엔드포인트와 메시지 API 연동, 스킬 버전 관리 기능이 제공되고 스킬은 Code Execution Tool 베타 환경에서 실행된다. Claude Code에서는 플러그인 마켓플레이스(anthropics/skills)나 ~/.claude/skills 경로로 설치·공유할 수 있고, 콘솔에서 버전 업그레이드가 가능하다. Anthropic은 스킬 생성 흐름 간소화와 엔터프라이즈 배포 기능 개선을 예고하면서도, 스킬이 코드 실행 권한을 요구하기 때문에 신뢰할 수 있는 출처 사용을 권고한다. 전반적으로 스킬은 조직의 전문 지식을 패키징해 Claude를 특정 업무의 전문가로 만드는 도구로, 크로스플랫폼 재사용성과 실행 코드 통합이라는 기술적 의미가 분명하다.

[Anthropic Blog에서 원문 읽기 →](https://claude.com/blog/skills)

