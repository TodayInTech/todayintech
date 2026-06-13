# Today in Tech

Today in Tech는 기술 뉴스 RSS/Atom 피드와 공식 sitemap을 매일 수집하고, AI 기반 News Editor Agent가 의미 있는 글만 선별해 Docusaurus 문서 사이트로 누적 배포하는 기술 글 큐레이션 아카이브입니다.

현재 저장소는 MVP 기본 구조 단계입니다. 서비스별 정보 수집, raw snapshot 저장, 전처리 후보 생성, 운영 trace, Docusaurus 빌드/배포 흐름이 잡혀 있으며, LLM 기반 선별/요약은 이후 구현 예정입니다.

## 확정 스택

- Python 3.14
- Docusaurus
- GitHub Actions
- GitHub Pages
- JSON 파일 기반 저장소
- OpenAI API

## MVP 대상 서비스

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

서비스 생성은 `Factory Method + Abstract Factory` 구조를 따르고, 수집 알고리즘은 `Strategy` 패턴으로 분리합니다. 신규 서비스는 `src/sources/implementations/`에 메타데이터 구현체를 추가하고 factory registry에 등록하는 방식으로 확장합니다. RSS를 지원하지 않는 서비스는 공식 sitemap, 공식 API, HTML metadata 등 적절한 collector strategy를 선택하거나 추가합니다.

## 문서 생성 구조

사이트는 날짜별 일간 브리핑이 아니라 누적 아카이브로 구성합니다. Collector는 매일 실행되지만, 이미 브리핑된 글은 다시 Agent로 처리하지 않습니다.

```text
docs/
├── index.md
├── services/
│   ├── hacker-news.md
│   ├── github-blog.md
│   ├── google-blog.md
│   ├── openai-blog.md
│   └── anthropic-blog.md
└── articles/
    ├── hacker-news/
    ├── github-blog/
    ├── google-blog/
    ├── openai-blog/
    └── anthropic-blog/
```

`docs/articles/{service_key}/{slug}.md`는 의미 있는 원문 글 하나에 대응합니다. 같은 원문 URL로 생성된 article 문서는 다시 생성하지 않습니다. 기존 날짜 디렉터리 산출물은 초기 구조 검증용 샘플로 취급합니다.

## 환경 변수

환경 변수 예시는 [.env.example](/Users/choi-hyk/todayintech/.env.example)에 있습니다.
변수별 의미와 코드 매핑은 [harness/ENV.md](/Users/choi-hyk/todayintech/harness/ENV.md)에서 관리합니다.

로컬에서 사용할 경우:

```bash
cp .env.example .env
```

주요 변수:

- `OPENAI_API_KEY`: LLM 요약/평가에 사용할 OpenAI API 키
- `OPENAI_MODEL`: 사용할 OpenAI 모델명
- `TODAYINTECH_TIMEZONE`: 브리핑 기준 시간대
- `TODAYINTECH_OUTPUT_DIR`: Markdown 생성 위치
- `TODAYINTECH_RAW_OUTPUT_DIR`: 서비스별 수집 원본 JSON 저장 위치
- `TODAYINTECH_PROCESSED_OUTPUT_DIR`: 전처리 후보 JSON 저장 위치
- `TODAYINTECH_TRACE_OUTPUT_DIR`: 운영 트레이싱 JSON/Markdown 저장 위치
- `TODAYINTECH_BRIEFED_ARTICLES_PATH`: 이미 브리핑된 원문 글 상태 파일 위치
- `TODAYINTECH_MAX_ARTICLES_PER_SERVICE`: 서비스별 최대 기사 수
- `TODAYINTECH_MAX_CANDIDATES_PER_SERVICE`: Agent 입력 후보의 서비스별 최대 개수
- `TODAYINTECH_MAX_CANDIDATES_TOTAL`: Agent 입력 후보의 전체 최대 개수
- `TODAYINTECH_TARGET_DATE`: 재현 가능한 날짜 지정용 값
- `DOCUSAURUS_URL`: 배포 사이트 URL
- `DOCUSAURUS_BASE_URL`: GitHub Pages base URL

현재 스캐폴딩 코드는 일부 환경 변수를 아직 직접 사용하지 않습니다. 이후 LLM Agent와 배포 설정을 붙일 때 이 이름들을 기준으로 구현합니다.

## 로컬 실행

Python 가상환경을 만들고 의존성을 설치합니다.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
```

Docusaurus 의존성을 설치합니다.

```bash
npm install
```

Collector 단계만 실행하여 서비스별 수집 결과를 확인합니다.

```bash
make collect
```

특정 서비스만 확인할 수도 있습니다.

```bash
make collect SERVICE=hacker-news COUNT=5
```

날짜를 지정하려면 `DATE` 값을 함께 넘깁니다.

```bash
make collect SERVICE=hacker-news DATE=2026-06-07 COUNT=5
```

실행 시 콘솔에는 서비스별 상태, 수집 개수, 기사 미리보기가 출력되고 각 서비스별 수집 결과가 JSON으로 저장됩니다.

```text
.var/local/raw/YYYY-MM-DD/
├── summary.json
└── services/
    ├── hacker-news.json
    ├── github-blog.json
    ├── google-blog.json
    ├── openai-blog.json
    └── anthropic-blog.json
```

Preprocessor 단계만 실행하여 수집 결과를 Agent 입력 후보로 정리합니다.

```bash
make preprocess
```

날짜나 입출력 경로를 지정할 수 있습니다.

```bash
make preprocess DATE=2026-06-07
make preprocess RAW_DIR=.var/local/raw PROCESSED_DIR=.var/local/processed
```

전처리 결과는 URL 정규화, 실행 내 중복 제거, `briefed_articles` 상태 필터링, 휴리스틱 후보 점수화, Writer 입력용 후보 식별자 생성을 거쳐 저장됩니다.

```text
.var/local/processed/YYYY-MM-DD/
└── preprocessing.json
```

전체 파이프라인을 실행하여 수집, 전처리, Markdown scaffold 생성을 함께 수행합니다. 현재 Markdown 생성기는 legacy scaffold이며, 다음 단계에서 article archive generator로 전환합니다.

```bash
.venv/bin/python -m src.main
```

Docusaurus 개발 서버를 실행합니다.

```bash
npm run start -- --host 127.0.0.1 --port 3000
```

정적 사이트 빌드를 검증합니다.

```bash
make build
```

프로젝트 규칙을 검증합니다.

```bash
make check
make verify
```

테스트와 운영 트레이스를 함께 실행합니다.

```bash
make quality
```

산출물:

```text
.var/local/reports/
└── junit.xml

.var/local/traces/YYYY-MM-DD/
├── collection.json
├── preprocessing.json
├── preprocessing-summary.md
└── summary.md
```

배포 워크플로를 GitHub Actions에서 수동 실행합니다.

```bash
make deploy
make deploy DATE=2026-06-07
```

## 주요 디렉터리

```text
src/
├── sources/       # 외부 수집 대상 계약, 구현체와 source factory
├── collection/    # 수집 오케스트레이션, collector strategy와 raw writer
├── processing/    # 후보 정리, 중복 제거, briefed article filtering, 점수화
├── generator/     # article/service/index Markdown 생성기
├── models/        # Pydantic 데이터 모델
└── main.py        # 파이프라인 진입점
```

## GitHub Actions

워크플로 파일은 [.github/workflows/daily-briefing.yml](/Users/choi-hyk/todayintech/.github/workflows/daily-briefing.yml)에 있습니다.

현재 워크플로는 다음 순서로 동작합니다.

1. Python 3.14 설정
2. Node 20 설정
3. Python 의존성 설치
4. Node 의존성 설치
5. `make generate`로 수집, 전처리, Markdown scaffold 생성
6. `make build`로 Docusaurus 빌드
7. GitHub Pages 배포

GitHub Actions에서 `OPENAI_API_KEY`는 repository secret으로 설정해야 합니다.
수동 배포는 `workflow_dispatch`의 `target_date` 입력 또는 `make deploy DATE=YYYY-MM-DD`로 날짜를 지정할 수 있습니다.

## 현재 한계

- `make generate`는 전처리 결과를 사용하지만, article archive Markdown 생성기는 아직 전환 전입니다.
- LLM 기반 요약/중요도 평가는 아직 실제 구현 전입니다.
- 현재 요약, 분류, 점수는 MVP 휴리스틱입니다.
- `briefed_articles` 상태는 전처리 필터로 사용되며, Writer 단계에서 발행 완료 상태 갱신이 추가되어야 합니다.
- Docusaurus 보안 감사에서 Node 의존성 경고가 있을 수 있습니다. 필요 시 `npm audit` 기준으로 별도 처리합니다.
