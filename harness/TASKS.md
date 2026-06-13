# TASKS

이 문서는 Today in Tech의 현재 작업 상태를 추적한다.
기능 구현, 문서 구조, collector strategy, 배포 흐름이 변경되면 이 문서를 지속적으로 업데이트한다.

## 상태 기준

- `[x]`: 완료
- `[ ]`: 미완료
- `진행 중`: 현재 작업 중이며 아직 완료로 표시하지 않는다.
- `대기`: 이후 단계에서 진행한다.

## 현재 단계

현재 프로젝트는 `Project Init`, `Collector`, `Preprocessor` 단계를 완료했다. 제품 방향은 날짜별 일간 브리핑에서 글 단위 누적 큐레이션 아카이브로 전환했다.

## 작업 체크리스트

- [x] Project Init - 완료
  - Python 3.14 기반 프로젝트 설정
  - Docusaurus 정적 문서 사이트 기본 구조 구성
  - GitHub Actions / GitHub Pages 배포 흐름 초안 구성
  - README, AGENTS, 하네스 문서 기본 구조 작성
  - 한국어 루트 문서와 영어 `notes/en/` 문서 구조 구성

- [x] Collector - 완료
  - [x] source 메타데이터 구현체 분리
  - [x] `sources`와 `collection` 상위 패키지 경계 분리
  - [x] `NewsSourceFactory` 기반 source 생성 구조 구성
  - [x] `CollectorStrategyFactory` 기반 collector strategy 생성 구조 구성
  - [x] RSS collector 구현
  - [x] Sitemap collector 구현
  - [x] 서비스별 raw JSON 저장 구조 구성
  - [x] collector 단독 실행 CLI 구성
  - [x] Makefile 기반 collector 실행 명령 구성
  - [x] Makefile 기반 lint, format, build, verify 명령 구성
  - [x] Makefile 기반 GitHub Actions 수동 배포 트리거 구성
  - [x] 최소 테스트 플로우와 운영 트레이싱 산출물 구성
  - [x] `tracing-history` 브랜치 기반 운영 trace 누적 흐름 구성
  - [x] 서비스별 수집 조건 문서화
  - [x] collector 기본 contract 테스트 구현
  - [x] daily snapshot 수집 정책 문서화
  - [x] RSS collector의 `collection_limit` / `lookback_days` source 설정 지원
  - [x] Hacker News points/comments/rank metadata 추출

- [x] Preprocessor - 완료
  - [x] URL canonicalization
  - [x] 필수 필드 validation
  - [x] 현재 실행 내 URL/title fingerprint deduplication
  - [x] `briefed_articles` 기반 이미 발행된 글 제외
  - [x] 후보 랭킹과 Agent 입력 개수 제한
  - [x] Writer 입력용 `candidate_id`, `url_hash`, `suggested_doc_key`, `suggested_article_path` 생성
  - [x] preprocessing trace 생성
  - [x] Preprocessor 단독 실행 CLI 구성
  - [x] Makefile 기반 preprocessor 실행 명령 구성
  - [x] `src.main` 파이프라인에 Collector 이후 Preprocessor 단계 연결
  - [ ] Generator 발행 완료 시 `briefed_articles` 상태 갱신 연동

- [ ] News Editor Agent - 대기
  - 신규 후보 글 선별
  - 글 단위 상세 브리핑 생성
  - 서비스별 요약과 메인 페이지 인사이트 생성
  - LLM 응답 schema 검증과 fallback 정책

- [ ] Generator - 대기
  - `docs/articles/{service_key}/{slug}.md` 생성
  - `docs/services/{service_key}.md` 서비스별 색인 생성
  - `docs/index.md` 메인 페이지 생성
  - 내부 링크와 출처 링크 검증

- [x] Build / Deploy - 완료
  - Docusaurus 빌드 검증
  - GitHub Actions 실제 배포 검증
  - GitHub Pages 운영 설정 검증

## 다음 작업 후보

- Writer 발행 완료 시 `briefed_articles` 상태 갱신 연동
- 날짜 기반 generator를 article archive generator로 전환
