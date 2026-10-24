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
make build-operations
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

Operations 대시보드는 로컬 trace를 입력으로 사용하지 않는다. `make build-operations`는 `TRACE_HISTORY_DIR`로 지정한 원격 `tracing-history` checkout만 읽고, 원문 본문·선택 chunk·Agent 상세 판단 문장을 제외한 집계 metric을 `static/data/operations/trace-metrics.json`으로 생성한다. GitHub Actions는 trace history를 push한 뒤 다시 `tracing-history`를 fetch하고 Operations 데이터를 만든 다음 Docusaurus를 빌드한다.

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

Collection trace의 전체 상태는 다음 의미를 갖는다.

- `success`: 실패 또는 부분 실패 서비스가 없다.
- `partial`: 일부 서비스가 실패했거나 일부 서비스가 개별 article metadata 요청 실패 같은 복구 가능한 경고를 기록했다.
- `failed`: 모든 서비스 수집이 실패했다.

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

공개 article은 목록용 `summary_ko` 1~2문장과 상세 `article_markdown_ko`를 분리한다. 상세 본문은 기사별로 소제목·문단·목록·표·근거 기반 코드/인용문을 선택하며 고정 섹션을 강제하지 않는다. 일반 뉴스 800~1500자, 풍부한 기술 발표 1500~2500자 이상을 권장하지만 근거가 부족하면 짧게 작성한다. 원문 링크는 Generator가 추가하고 선정 이유·확신도·근거 목록은 trace에만 남긴다.

## 운영 기준

- fixture 기반 `make test`는 안정적인 개발 검증 용도이다.
- `make trace-collect`는 실제 외부 source를 호출하므로 운영 트레이싱 용도이다.
- `make trace-preprocess`는 collector raw snapshot을 기준으로 전처리 후보와 제외 사유를 기록한다.
- `make trace-enrich`는 제한된 후보의 원문 요청, 추출, 구조와 입력 전략을 기록한다.
- `make trace-write`는 Writer Agent가 후보별로 내린 게시, 제외, 실패 판단과 근거를 기록한다.
- 외부 네트워크 영향이 있으므로 trace duration은 강한 pass/fail 조건으로 사용하지 않는다.
- 서비스별 article count가 0이면 `empty_collection` warning을 기록한다.
- sitemap 기반 수집에서 개별 page metadata 요청이 실패하면 해당 URL만 제외하고 `article_metadata_fetch_failed` warning을 기록한다.
- 일부 서비스 수집 실패는 trace에 기록하되, 성공한 서비스가 하나라도 있으면 collector CLI는 성공으로 종료한다.
- 모든 서비스 수집이 실패하면 collector CLI는 실패로 종료한다.
- GitHub Actions에서는 dev 의존성을 설치하고 `PYTHON=python`을 명시해서 로컬 `.venv` 경로에 의존하지 않는다.
- GitHub Actions는 OpenAI Writer가 만든 `docs/`와 `data/briefed_articles.json`을 main에 다시 커밋해야 한다. 이 상태 파일이 다음 실행의 중복 제거 기준이다.
- Markdown generator는 RSS, Atom, sitemap 등 외부 source에서 들어온 HTML과 MDX 토큰을 안전한 텍스트로 정규화해야 한다.
- OpenAI structured output이 토큰 제한이나 JSON 파싱 문제로 실패하면 더 큰 출력 제한으로 한 번 재시도하고, 계속 실패하는 후보만 제외한다.

## UI 검증 (2026-10-16)

- B4React의 중립색 표면, 경계선, 라운드 컨트롤을 참고해 네브바·브리핑 카드·트레이스 화면을 정리했다.
- 원격 trace 입력을 유지하고 지표명, 상태명, 빈 상태를 한국어/영어로 간결하게 표시한다. 집계 범위와 발행률 정의는 지표 툴팁으로 제공한다.
- 툴팁은 키보드 포커스/탭, Escape, 외부 탭을 지원하고, 서비스 선택은 커스텀 combobox와 listbox의 방향키/Enter/Escape 탐색을 사용한다. 모션 축소 설정을 존중한다.
- 검증: 생성 문서·article Markdown·운영 메트릭 관련 기존 테스트 6개 통과, Python lint/format 및 SVG XML 검증 통과. 한국어/영어 Docusaurus 빌드 통과. 브라우저에서 밝은/어두운 테마, 390px 카드·트레이스 배치, 툴팁 열기/Escape 닫기, 서비스 필터에 따른 추이 갱신을 확인했다.

- 후속 UI 조정: 원래 브랜드 색상 복원, 아이콘 프레임 제거, 경계선 없는 네브바·사이드바, 중앙 정렬 콘텐츠, 36px 컨트롤(터치 환경 44px)과 축소한 카드 패딩을 적용했다.

- 후속 탐색 회귀 검증: 사이드바는 콘텐츠와 관계없이 200px을 유지한다. 다크 모드 토큰과 선택 페이지 배경은 기본 스타일보다 높은 명시도로 선언한다. 필터·페이지는 URL에 보존하고, 글 상단의 목록 복귀 링크는 진입 목록을 복원한다. 직접 진입한 글은 서비스 목록으로 이동한다. 빈 상태는 전체 목록 폭과 최소 144px 높이를 확보한다. 브라우저에서 Anthropic 2페이지 → 글 → 목록 복귀와 양 테마의 선택 번호 대비를 확인했다.

- 공통 DateCard는 메인 업데이트·브리핑 카드·원문 문서 메타데이터·trace 업데이트/실행/테이블 날짜에 사용한다. 기존 Markdown의 날짜 및 피드 추출 형식은 유지하고 MDX 렌더링에서 날짜 컴포넌트로 표시한다. 카드의 브랜드 아이콘/이름 정렬을 맞추고 하단 문구를 제거했다. 트레이스 서비스 선택은 커스텀 combobox/listbox로 변경하고, 툴팁은 라이트 모드에서 검은 배경·다크 모드에서 흰 배경으로 표시한다. 브라우저에서 키보드 선택과 양 테마 툴팁 색상, 내부 글 날짜 표시를 확인했다. 생성/운영 관련 기존 테스트 6개와 Python lint/format 검증이 통과했다.

- 운영 테이블은 날짜·서비스·상태를 왼쪽, 수치와 비율은 오른쪽에 맞춘다. 헤더/본문의 동일 열 정렬, 수직 중앙 정렬, 얇은 가로 구분선을 사용한다. 전체 서비스는 아이콘 없이 텍스트로 표시한다.

- 날짜는 아이콘·테두리 없는 작은 배경형 표시로 통일하고, 글의 목록 복귀 링크는 상단 하나만 제공한다. 테이블 상태는 캡슐 배경 없이 색상과 굵기로 강조한다.

- 메인 서비스 필터는 mode=all 리스트에만 적용한다. 추천/새로운 글은 고정 서비스 범위를 유지한다. 필터/페이지 변경 전에 해당 결과 영역 높이를 확보해 짧은 결과로 문서 높이가 줄어 스크롤이 이동하는 현상을 막는다. 창 크기 변경 시 확보 높이를 초기화한다. 네브바 활성 항목은 배경·테두리 없이 글자 색과 굵기로만 구분한다.

- 브리핑 카드는 16rem 고정 높이, 제목 2줄과 요약 3줄의 고정 공간을 사용한다. 메인 하단 필터 변경 전후 상단 추천/새로운 글 링크 목록이 일치하고, 키보드 기간 전환 시 스크롤 위치가 유지되는 것을 현재 3100 서버에서 확인했다.

- 최종 검증: make check의 Ruff lint/format과 전체 테스트 67개, 한국어/영어 정적 빌드가 통과했다. 페이지네이션은 첫/마지막 페이지와 현재 페이지 양옆 번호를 표시하며 26/30에서 1 … 25 26 27 … 30을 확인했다. 모든 카드 높이 256px과 제목 영역 48px을 실제 브라우저에서 확인했다.

- 사이드바 호버 회귀 확인: Infima의 카테고리 링크 `background: none !important` 충돌을 재현하고 수정했다. 한국어·영어 빌드와 실제 브라우저에서 서비스 6개 항목의 라이트/다크 호버, 선택된 서비스, 키보드 포커스 및 트레이스 6개 항목의 호버를 확인한다.

- 동적 아티클 생성: `make check`의 Ruff lint/format 및 전체 테스트 70개가 통과했다. 동일 보관 근거 3건을 기존/개선 프롬프트로 실제 생성해 분량·소제목·수치·근거 ID를 비교했다. 한국어/영어 Docusaurus 빌드와 실제 상세 페이지의 780px 읽기 영역·소제목·원문 링크, Markdown 표/목록/인용/코드 보존 및 HTML/MDX/위험 링크 비활성화를 확인했다. 상세 결과와 표본 한계는 [아티클 생성 검증](ARTICLE_GENERATION.md)에 기록한다.

- 상세 글 제목 정렬/목차: 한국어·영어 빌드와 브라우저에서 H1~H6 왼쪽 정렬 규칙, 우측 200px 고정 목차, 섹션 클릭·현재 항목 강조를 확인했다. 390px 화면에서는 접이식 목차를 유지하고 가로 넘침이 없으며, 메인 제목 중앙·섹션 제목 왼쪽 정렬은 유지한다.

- 강조 표현: 상세 아티클의 핵심 변화·수치·제약만 짧은 `**볼드 구절**`로 선택하도록 안내한다. 문단 전체·모든 수치·같은 정보의 반복 강조를 피하고, Markdown 안전 처리에서 볼드 표기가 보존되는 것을 검증한다.

- 글 이동: `node --test tests/site/briefing-navigation.test.mjs`의 3개 검증이 통과했다. 정렬은 브리핑일(없으면 원문 발행일) 최신순 → 점수 내림차순 → 문서 경로순으로 목록/사이드바에서 공유한다. 같은 서비스 순서에서 이전은 앞 항목, 다음은 뒤 항목이며 서비스 경계에서는 링크를 생략한다. 한국어·영어 빌드 HTML 총 2,326개 상세 페이지에서 모든 인접 링크와 순서·경계를 대조했고, 메인/서비스 색인/트레이스 24개 페이지에 문서 페이지네이션이 없는 것을 확인했다.

- 목록 동기화: 일일 배포의 `git add`에 카드 JSON과 영어 생성 문서가 빠져 있던 원인을 수정했다. Agent/본문 재생성 없이 보관 상태로 목록을 1,163건·2026-10-24 기준으로 갱신하고 모든 카드의 서비스별 순서와 실제 상세 이동 링크가 일치하는 것을 대조했다.
