# QUALITY

이 문서는 Today in Tech의 개발 검증과 운영 트레이싱 플로우를 정의한다.

## 개념 구분

- `test`: 코드가 의도대로 동작하는지 fixture와 contract로 검증한다.
- `trace`: 실제 운영 collector/preprocessor/enrichment/writer 실행 결과와 실행 시간을 기록한다.
- `quality`: `test`와 `trace`를 함께 실행해 배포 전 판단 근거를 만든다.

## Make 명령

```bash
make test
make test-unit
make test-collection
make trace-collect
make trace-preprocess
make trace-enrich
make trace-write
make fetch-trace-history
make quality
```

## 산출물

```text
.var/local/reports/
└── junit.xml

.var/local/traces/YYYY-MM-DD/
├── collection.json
├── enrichment.json
├── enrichment-summary.md
├── preprocessing.json
├── preprocessing-summary.md
├── writer-decisions.json
├── writer-decisions-summary.md
└── summary.md
```

`.var/local/reports/`와 `.var/local/traces/`는 Git에 커밋하지 않는다. GitHub Actions에서는 artifact로 업로드한다.

GitHub Actions 산출물은 로컬 산출물과 분리해서 `.artifacts/` 아래에 둔다.

```text
.artifacts/
├── raw/
├── reports/
└── traces/
```

## 트레이싱 히스토리

운영 trace는 `main` 브랜치에 커밋하지 않는다. GitHub Actions는 collector trace 실행 후 `tracing-history` 전용 브랜치에 trace 결과만 날짜별로 누적한다.

```text
tracing-history
└── traces/
    └── YYYY-MM-DD/
        ├── collection.json
        ├── enrichment.json
        ├── enrichment-summary.md
        ├── preprocessing.json
        ├── preprocessing-summary.md
        └── summary.md
```

원칙:

- `main`은 코드, 설정, 사람이 관리하는 문서만 포함한다.
- `tracing-history`는 운영 trace 장기 보관용 브랜치이다.
- raw 수집 데이터와 test report는 GitHub Actions artifact로만 보관한다.
- 같은 날짜로 workflow를 재실행하면 해당 날짜 trace 파일을 갱신하고 변경이 있을 때만 커밋한다.

로컬에서 누적 trace 데이터를 확인하려면 다음 명령을 사용한다.

```bash
make fetch-trace-history
```

기본 checkout 위치는 `.var/remote/tracing-history`이다.

## 현재 추적 지표

- 전체 collection stage 상태
- 전체 collection duration
- 서비스별 status
- 서비스별 collector strategy
- 서비스별 article count
- 서비스별 duration
- article 1개당 평균 duration
- warning code
- error message
- preprocessing duration
- preprocessing candidate count
- preprocessing excluded count
- preprocessing excluded reason count
- enrichment 전체·서비스별 usable count와 usable rate
- Writer에 즉시 전달 가능한 writer-ready count와 rate
- enrichment status와 Agent input strategy 분포
- 원문 HTTP status, MIME type, 응답 크기, fetch/extraction/selection duration
- extractor·policy 버전과 cache hit 여부
- 문서 유형과 추출 언어
- 추출 token 분포와 선택 token 비율
- section, chunk, code block, table, list item count
- title similarity와 extraction quality score
- enrichment failure reason count

Enrichment trace의 상태는 다음 의미를 갖는다.

- `enriched`: 추출한 원문 근거를 Agent 입력으로 사용할 수 있다.
- `fallback`: 원문 근거는 사용할 수 없지만 피드 메타데이터 fallback이 가능하다.
- `skipped`: 정책에 따라 enrichment 대상에서 제외했다.
- `failed`: Writer에 전달할 근거가 없다.

실패 원인은 `fetch_failed`, `fetch_timeout`, `access_denied`, `rate_limited`, `unsupported_content_type`, `empty_content`, `thin_content`, `title_mismatch`, `extraction_failed`, `selection_failed`, `policy_rejected`, `unknown`으로 정규화한다. HTTP 상태와 구체 오류는 별도 필드로 기록한다.

Enrichment trace에는 원문 본문과 chunk 텍스트를 저장하지 않는다. `content_hash`와 크기·구조·상태 지표만 저장해 원문 복제와 trace-history 비대화를 방지한다.

## 실행 로그

전체 파이프라인은 다음 4단계 로그를 출력한다.

```text
[1/4] Collector
[2/4] Preprocessor
[3/4] Enrichment
[4/4] Writer
```

Enrichment는 `make enrich` 또는 `make trace-enrich`로 독립 실행할 수도 있다.

Writer 내부에서는 Agent 편집, Markdown 작성, `briefed_articles` 상태 갱신을 다시 순서대로 기록한다. OpenAI Agent는 후보별 검토 순서, 게시/제외 결정, structured output 파싱 실패와 재시도 여부를 로그로 남긴다. Writer decision trace는 후보별 decision status, 선정/제외 이유, 판단 확신도, 요약 범위, 근거 목록을 JSON과 Markdown으로 저장한다.

published article 문서는 내부 판단 정보를 노출하지 않는다. 사용자에게는 글의 주제, 핵심 내용, 기술적 의미를 연결한 자연스러운 한국어 요약 2~3문단과 원문 링크만 제공하고, 선정 이유와 판단 근거는 Writer decision trace에서 확인한다.

## 운영 기준

- fixture 기반 `make test`는 안정적인 개발 검증 용도이다.
- `make trace-collect`는 실제 외부 source를 호출하므로 운영 트레이싱 용도이다.
- `make trace-preprocess`는 collector raw snapshot을 기준으로 전처리 후보와 제외 사유를 기록한다.
- `make trace-enrich`는 제한된 후보의 원문 요청, 추출, 구조와 입력 전략을 기록한다.
- `make trace-write`는 Writer Agent가 후보별로 내린 게시, 제외, 실패 판단과 근거를 기록한다.
- 외부 네트워크 영향이 있으므로 trace duration은 강한 pass/fail 조건으로 사용하지 않는다.
- 서비스별 article count가 0이면 `empty_collection` warning을 기록한다.
- 일부 서비스 수집 실패는 trace에 기록하되, 성공한 서비스가 하나라도 있으면 collector CLI는 성공으로 종료한다.
- 모든 서비스 수집이 실패하면 collector CLI는 실패로 종료한다.
- GitHub Actions에서는 dev 의존성을 설치하고 `PYTHON=python`을 명시해서 로컬 `.venv` 경로에 의존하지 않는다.
- GitHub Actions는 OpenAI Writer가 만든 `docs/`와 `data/briefed_articles.json`을 main에 다시 커밋해야 한다. 이 상태 파일이 다음 실행의 중복 제거 기준이다.
- Markdown generator는 RSS, Atom, sitemap 등 외부 source에서 들어온 HTML과 MDX 토큰을 안전한 텍스트로 정규화해야 한다.
- OpenAI structured output이 토큰 제한이나 JSON 파싱 문제로 실패하면 더 큰 출력 제한으로 한 번 재시도하고, 계속 실패하는 후보만 제외한다.
