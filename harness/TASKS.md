# TASKS

이 문서는 Today in Tech의 현재 작업 상태를 추적한다.
기능 구현, 문서 구조, collector strategy, 배포 흐름이 변경되면 이 문서를 지속적으로 업데이트한다.

## 상태 기준

- `[x]`: 완료
- `[ ]`: 미완료
- `진행 중`: 현재 작업 중이며 아직 완료로 표시하지 않는다.
- `대기`: 이후 단계에서 진행한다.

## 현재 단계

현재 프로젝트는 `Project Init`을 완료했고, `Collector` 단계를 진행 중이다.

## 작업 체크리스트

- [x] Project Init - 완료
  - Python 3.14 기반 프로젝트 설정
  - Docusaurus 정적 문서 사이트 기본 구조 구성
  - GitHub Actions / GitHub Pages 배포 흐름 초안 구성
  - README, AGENTS, 하네스 문서 기본 구조 작성
  - 한국어 루트 문서와 영어 `notes/en/` 문서 구조 구성

- [ ] Collector - 진행 중
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
  - [x] 서비스별 수집 조건 문서화
  - [ ] `seen.json` 기반 영속 deduplication 구현
  - [ ] collector 테스트 구현

- [ ] Processing - 대기
  - deduplication 고도화
  - 중요도 점수화
  - 카테고리 분류
  - LLM 기반 요약 연결

- [ ] Generator - 대기
  - 서비스별 Markdown 생성 고도화
  - 전체 요약 Markdown 생성 고도화
  - 내부 링크와 출처 링크 검증

- [ ] Build / Deploy - 대기
  - Docusaurus 빌드 검증
  - GitHub Actions 실제 배포 검증
  - GitHub Pages 운영 설정 검증

## 다음 작업 후보

- `seen.json` 저장소와 collector deduplication 연결
- collector 단위 테스트 추가
- Anthropic sitemap collector timeout, limit, metadata fallback 정책 정리
- raw JSON schema 안정화
