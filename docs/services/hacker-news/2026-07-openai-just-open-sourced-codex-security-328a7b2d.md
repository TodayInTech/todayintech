---
title: "OpenAI just open-sourced Codex Security"
sidebar_label: "OpenAI just open-sourced Codex Security"
---

# OpenAI just open-sourced Codex Security

> Hacker News · 2026-07-28 · security

---

OpenAI가 공개한 @openai/codex-security는 코드베이스의 취약점을 찾아 검증하고 수정하는 데 쓰이는 CLI와 TypeScript SDK입니다. 레포지토리 스캔, 변경사항 검토, 발견사항의 시간 추적 기능을 제공하며 CI 파이프라인에서 보안 검사를 실행할 수 있도록 설계되어 있어 개발 흐름에 직접 통합할 수 있습니다. 배포 자료는 Node.js 22 이상과 Python 3.10 이상, 그리고 Codex Security 접근 권한이 필요하다고 명시합니다.
설치와 인증, 사용 예시도 간단히 제시되어 있어 빠른 도입이 가능합니다. npm으로 패키지를 설치한 뒤 npx codex-security login으로 인증하고 npx codex-security scan . 명령으로 스캔을 실행할 수 있으며, CI 환경에서는 로그인 대신 OPENAI_API_KEY를 설정해 사용하도록 안내합니다. 코드 예시로는 TypeScript 환경에서 CodexSecurity 객체를 생성해 run('.')을 호출하고 결과 리포트 경로를 출력한 뒤 close()로 종료하는 흐름이 제시되어 있어 자동화와 통합 관점에서 실무 적용 방식을 바로 확인할 수 있습니다. 추가 설치·인증·스캔 옵션과 CI 설정은 공식 문서를 참고하라는 안내가 함께 제공됩니다.

[Hacker News에서 원문 읽기 →](https://github.com/openai/codex-security)

