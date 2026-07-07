---
title: "Expanding Managed Agents in Gemini API: background tasks, remote MCP and more"
sidebar_label: "Expanding Managed Agents in Gemini API: background tasks, remote MCP and more"
---

# Expanding Managed Agents in Gemini API: background tasks, remote MCP and more

> Google Blog · 2026-07-07 · Developer tools

---

구글은 Gemini API의 Managed Agents에 백그라운드 실행, 원격 MCP 서버 통합, 커스텀 함수 호출, 네트워크 인증 갱신 등 실무 중심의 기능 확장을 발표했다. Managed Agents는 단일 엔드포인트로 샌드박스 내에서 추론, 코드 실행, 패키지 설치, 파일 관리, 웹 정보 수집을 처리하도록 설계되어 있으며, 예제는 @google/genai JavaScript SDK와 npx skills add 명령을 통해 제공된다. 이러한 업데이트는 개발자 피드백과 제품 요구를 반영해 신뢰성 있는 프로덕션 에이전트를 만드는 데 초점을 맞춘다.
기술적으로 눈에 띄는 점은 비동기 백그라운드 실행(background:true)인데, API는 즉시 작업 ID를 반환하고 클라이언트는 상태 폴링이나 진행 스트리밍으로 원격에서 완료되는 작업을 추적할 수 있다. 또한 interaction 시 mcp_server 도구를 전달하면 원격 Model Context Protocol 서버와 직접 연결해 내부 API나 프라이빗 데이터베이스에 안전하게 접근할 수 있으며, 내장 샌드박스 도구와 외부 도구를 혼합해 사용할 수 있다. 커스텀 함수는 스텝 매칭에 따라 requires_action 상태로 전환되어 클라이언트 쪽 비즈니스 로직을 실행하게 하고, 인증 갱신은 기존 environment_id에 새 네트워크 구성을 전달하면 즉시 규칙이 교체되며 샌드박스의 파일시스템·설치된 패키지·클론된 레포는 유지된다. 이로써 Managed Agents는 애플리케이션을 블로킹하지 않는 비동기 작업자처럼 동작하며, 커스텀 에이전트 정의와 환경 설정을 통해 실제 개발 환경에서 더 안정적인 자동화 워크플로를 구성할 수 있다. 자세한 내용은 Gemini Interactions API 개요와 Managed Agents 퀵스타트를 참고한다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/)

