---
title: "Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives"
sidebar_label: "Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives"
description: "Google Chrome·Edge·Firefox·MDN이 공동 관리하는 Modern Web Guidance가 npx 기반 로컬 CLI로 공개됐다. 200여 개 가이드를 에이전트 문맥에 삽입해 로컬 검색·retrieve로 현대 웹 API 사용을 유도하며, 자동화 평가에서 여러 에이전트의 성공률을 크게 높였습니다."
---

# Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives

> Hacker News · 2026-11-10 · Web 개발 도구

---

Google Chrome, Microsoft Edge, Mozilla Firefox, MDN 팀이 공동으로 관리하는 **Modern Web Guidance**가 npx 기반 로컬 CLI 형태로 배포됐다. 이 스킬은 코딩 에이전트의 컨텍스트에 웹 플랫폼 전문 지식과 구현 가이드를 직접 삽입해, 에이전트가 오래된 JavaScript 패턴 대신 네이티브 웹 솔루션을 선택하도록 돕는다.

## 에이전트에 직접 임베디드되는 가이드

설치·검색·가이드 호출은 CLI로 이루어진다. 예시 커맨드로는 다음이 제공된다:

npx modern-web-guidance@latest install

npx modern-web-guidance@latest search "animate a dialog modal backdrop"

npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"

또한 코드베이스 스캔을 통한 레거시 패턴 탐색을 위한 legacy-scan 명령이 있다. 가이드는 약 200건의 실사용 사례(문서 내 '203 real-world developer use cases' 표기)를 포함하며, CSS·레이아웃·성능·접근성·네이티브 컴포넌트 등 광범위한 주제를 다룬다.

## 로컬·오프라인 검색과 안전성 제어

현대 웹 지식은 로컬 시맨틱 검색(제로-의존 임베딩 모델과 BM25)을 사용해 네트워크 호출이나 API 키 없이 조회된다. 패키지는 오프라인·프라이빗 실행을 목표로 설계되었고, npx를 통해 최신 버전을 가져와 사용하도록 권장한다.

실험적 Origin Trial API나 엔진별 불안정 기능은 검색으로는 발견되지만, 가이드를 실제로 가져오는 retrieve 단계에서 명시적 동의가 필요하도록 게이트되어 있다. 프로젝트 또는 사용자 수준 설정 파일(.mwgrc)을 통해 allowOriginTrials 및 allowVolatileFeatures 옵션을 켤 수 있다.

## 자동화 평가: 수치로 확인된 효과

팀은 에이전트 성능을 비교하는 자동화 평가 파이프라인을 개발해 가이드를 계량적으로 검증했다. 문서에 제시된 일부 결과는 다음과 같다:

- antigravity_cli (gemini-4-argon), 214 과제: **58% → 94%** (+36pp)
- codex_cli (gpt-6.1-sol), 215 과제: **54% → 82%** (+28pp)
- claude_code (opus-5-5), 215 과제: **57% → 88%** (+31pp)

평가 시스템은 Playwright 기반 그레이더로 구현되어 소스 패턴, 계산된 스타일, 런타임 DOM 동작과 접근성 상태를 검사한다. 가이드가 불필요하다고 판단되는 경우(에이전트가 이미 잘 알고 있는 항목)는 내용을 가지치기하는 절차도 운영된다.

## 실무적 고려사항

- 텔레메트리: Google은 익명화된 사용 통계를 수집한다고 명시하며(설치 수, 호출한 에이전트 이름, 조회된 가이드 ID 등), 원치 않으면 DISABLE_TELEMETRY=1로 비활성화 가능하다.

- 라이선스: 코드 기반은 Apache License 2.0, guides 문서는 CC-BY 4.0 하에 배포된다.

- 통합 경로: npx 외에도 여러 에이전트·플러그인 생태계용 설치 경로(예: GitHub CLI, plugin 명령 등)가 문서에 제시되어 있어 다양한 개발 환경에 연결할 수 있다.

Modern Web Guidance는 에이전트가 실무에서 더 적합한 플랫폼 네이티브 API와 경량 폴백을 선택하도록 돕는 도구다. 문서와 자동화 평가에 근거하면, 적절히 통합된 경우 여러 상용/연구용 에이전트에서 실행 가능한 코드의 품질과 접근성 준수도를 눈에 띄게 개선한 것으로 나타난다.

[Hacker News에서 원문 읽기 →](https://github.com/GoogleChrome/modern-web-guidance)

