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
