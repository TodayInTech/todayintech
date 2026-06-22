# TASKS

이 문서는 Today in Tech의 현재 작업 상태를 추적한다.
기능 구현, 문서 구조, collector strategy, 배포 흐름이 변경되면 이 문서를 지속적으로 업데이트한다.

## 상태 기준

- `[x]`: 완료
- `[ ]`: 미완료
- `진행 중`: 현재 작업 중이며 아직 완료로 표시하지 않는다.
- `대기`: 이후 단계에서 진행한다.

## 현재 단계

현재 프로젝트는 `Project Init`, `Collector`, `Preprocessor` 단계를 완료했고, `Writer` 기본 구조를 구성 중이다. 제품 방향은 날짜별 일간 브리핑에서 글 단위 누적 큐레이션 아카이브로 전환했다.

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
  - [x] Writer draft 생성 상태 기준으로 `briefed_articles` 상태 갱신 연동
  - [x] Collector 구조와 맞춘 contracts/steps/scoring/state 기반 전처리 패키지 재구성
  - [x] 전처리 pipeline factory, scorer ABC, 제외 사유 enum, ranking signal 모델, step metrics, context helper, legacy helper 제거 적용
  - [x] 서비스별 전처리 정책, 후보 품질 게이트, 점수 산정 설명 추가

- [ ] Writer - 진행 중
  - [x] Writer 패키지 구조 추가
  - [x] Draft Agent contract/schema 구현
  - [x] `docs/services/{service_key}/{slug}.md` draft 문서 생성
  - [x] 개별 article 문서의 자연스러운 브리핑형 템플릿 구성
  - [x] `docs/services/{service_key}.md` 서비스별 색인 생성
  - [x] `docs/index.md` 메인 페이지 생성
  - [x] 생성 성공 후 `briefed_articles` draft 상태 갱신
  - [x] Writer 단독 실행 CLI와 Makefile 명령 구성
  - [x] OpenAI 기반 News Editor Agent 구현
  - [x] Writer Agent 선택 설정 추가
  - [x] 서비스별 공식 브랜드 아이콘과 서비스 색인 표시 구성
  - [x] Today in Tech 전용 SVG 브랜드 아이콘과 테마별 UI 적용
  - [x] README와 조직 아이콘용 브랜드 자산 적용
  - [x] 조직 아이콘 업로드용 PNG 브랜드 자산 생성
  - [x] OpenAI Agent decision schema에 선정 이유, 근거 범위, 확신도 추가
  - [x] 공개 article 문서를 자연스러운 한국어 장문 요약 중심으로 단순화
  - [ ] 게시 상태 전환 정책 구현

- [x] Build / Deploy - 완료
  - Docusaurus 빌드 검증
  - GitHub Actions 실제 배포 검증
  - GitHub Pages 운영 설정 검증

## 다음 작업 후보

- LLM 기반 News Editor Agent 구현
- draft article을 published article로 전환하는 정책 구현
