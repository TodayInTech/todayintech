# OVERVIEW

## 프로젝트 목적

Today in Tech는 기술 뉴스 RSS/Atom 피드를 수집하고, AI 기반 News Editor Agent가 중요한 뉴스를 선별하여 정적 문서 사이트로 배포하는 기술 뉴스 브리핑 플랫폼이다.

이 프로젝트는 단순 RSS 리더가 아니다. 모든 기사를 저장하거나 나열하지 않고, 개발자와 기술 리더가 하루의 핵심 기술 흐름을 빠르게 파악할 수 있도록 서비스별 브리핑과 전체 요약을 생성한다.

## 핵심 목표

- 매일 최신 기술 뉴스를 자동 수집한다.
- 서비스별 주요 뉴스를 선별한다.
- 전체 요약 문서에서 도메인별 시사점을 제공한다.
- 원문 출처와 내부 서비스 문서 링크를 함께 제공한다.
- Docusaurus 기반 정적 사이트로 배포한다.

## MVP 범위

MVP는 다음 기능에 집중한다.

- RSS/Atom Feed Collection
- News Normalization
- Deduplication
- Importance Scoring
- Category Classification
- Markdown Generation
- Docusaurus Build
- GitHub Pages Deployment

LLM 기반 고품질 요약과 중요도 평가는 이후 단계에서 강화한다. 현재 스캐폴딩은 휴리스틱 기반 처리와 Markdown 생성 구조를 우선 제공한다.

## 기본 언어 정책

- 루트 문서와 하네스 문서는 한국어를 기본으로 한다.
- 영어 문서는 다국어 지원 문서로 `notes/en/` 아래에 둔다.
- 자동 생성 브리핑도 한국어를 기본 출력 언어로 한다.

## 하네스 추적 문서

- `harness/TASKS.md`: 프로젝트 단계별 작업 상태와 완료/진행 체크리스트를 추적한다.
- `harness/service/SERVICES.md`: 현재 지원 중인 서비스, 수집 방식, 수집 조건 범위를 추적한다.
- `harness/ARCHITECTURE.md`: 전체 아키텍처와 단계별 플로우를 설명한다.
- `harness/TECH_STACK.md`: 확정 기술 스택과 운영 기준을 설명한다.
- `harness/COMMIT_MESSAGE.md`: 커밋 메시지 작성 규칙을 정의한다.

서비스 구현이나 collector strategy를 변경하면 `harness/service/SERVICES.md`를 먼저 확인하고 함께 수정한다.
기능 구현 상태가 바뀌면 `harness/TASKS.md`의 체크리스트 상태를 함께 갱신한다.
