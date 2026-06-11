# ARCHITECTURE

## 프로젝트 아키텍처

Today in Tech는 수집, 전처리, Agent 편집, 문서 생성, 빌드, 배포 단계를 분리한다. 각 단계는 독립적으로 테스트 가능해야 하며, 서비스 추가가 전체 파이프라인 수정으로 이어지지 않도록 설계한다.

```text
Official Sources
    ↓
Service Factory
    ↓
Service-specific Collector Strategy
    ↓
Normalize Articles
    ↓
Raw Snapshot Storage
    ↓
Preprocess Candidates
    ↓
Briefed Article Filtering
    ↓
Candidate Ranking
    ↓
News Editor Agent
    ↓
Article Markdown Generation
    ↓
Service Index Generation
    ↓
Main Index Generation
    ↓
Docusaurus Build
    ↓
GitHub Pages Deployment
```

## 주요 디렉터리

```text
src/
├── sources/
│   ├── contracts/
│   │   └── base.py
│   ├── factory.py
│   └── implementations/
│       ├── hacker_news.py
│       ├── github_blog.py
│       ├── google_blog.py
│       ├── openai_blog.py
│       └── anthropic_blog.py
├── collection/
│   ├── __main__.py
│   ├── news_collector.py
│   ├── raw_writer.py
│   ├── factories/
│   │   └── collector_strategy_factory.py
│   └── strategies/
│       ├── base.py
│       ├── rss.py
│       └── sitemap.py
├── processing/
│   ├── news_preprocessor.py
│   ├── briefed_article_store.py
│   ├── article_candidate.py
│   ├── url_normalizer.py
│   ├── deduplicator.py
│   ├── classifier.py
│   ├── scorer.py
│   └── summarizer.py
├── generator/
│   ├── article_markdown_writer.py
│   ├── service_markdown_writer.py
│   └── summary_markdown_writer.py
├── models/
│   └── article.py
└── main.py
```

## 서비스 확장 구조

서비스 생성은 Factory Method와 Abstract Factory를 따르고, 수집 알고리즘은 Strategy 패턴으로 분리한다.

- 제품과 문서에서는 사용자에게 노출되는 브리핑 단위를 `service`라고 부른다.
- 코드에서는 외부 수집 대상을 `source`, 수집 실행 계층을 `collection`으로 구분한다.
- `BaseNewsSource`: 서비스 메타데이터와 collector 설정 인터페이스
- `BaseCollectorStrategy`: 수집 알고리즘 인터페이스
- `RssCollector`: RSS/Atom 수집 strategy
- `SitemapCollector`: sitemap + page metadata 수집 strategy
- `CollectorStrategyFactory`: `collector_type`에 맞는 collector strategy 생성
- `NewsSourceFactory`: 서비스 키를 기준으로 구체 서비스 구현체 생성
- `AbstractNewsSourceFactory`: 서비스 제품군 확장을 위한 추상 팩토리

신규 서비스를 추가할 때는 기존 파이프라인을 수정하지 않는다. `src/sources/implementations/`에 서비스 메타데이터 구현체를 추가하고 factory registry에 등록한다.
RSS를 지원하지 않는 서비스는 제3자 RSS에 의존하지 않고 공식 sitemap, 공식 API, HTML metadata 등 적절한 collector strategy를 선택하거나 추가한다.

## 문서 생성 구조

문서 사이트는 날짜별 일간 브리핑이 아니라 누적 아카이브로 구성한다.

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

`index.md`는 전체 서비스의 핵심 흐름과 최근 선별 글을 보여주는 진입점이다. `services/*.md`는 서비스별 핵심 글 색인이다. `articles/{service_key}/*.md`는 원문 글 하나에 대한 상세 브리핑이다.

## 단계별 플로우

```text
Collector
    ↓
Preprocessor
    ↓
News Editor Agent
    ↓
Generator
    ↓
Build
    ↓
Deploy
```

## Collector

Collector 단계는 독립 실행 가능해야 하며, 각 서비스별 수집 상태와 원본 JSON을 확인할 수 있어야 한다. Collector는 daily snapshot 발견 계층이다. 같은 글이 여러 날짜에 반복 수집되는 것은 정상이며, 재처리 방지는 전처리 단계가 담당한다.

1. `NewsCollector`가 `NewsSourceFactory`를 통해 MVP 서비스 구현체를 생성한다.
2. 각 서비스 구현체가 RSS/Atom, sitemap, 공식 API 등 자기 collector strategy로 정보를 수집한다.
3. 피드 항목을 공통 `Article` 모델로 정규화한다.
4. 서비스별 수집 결과를 `ServiceCollectionResult`로 묶는다.
5. URL, 제목, 발행일, 출처, 요약, 태그를 최대한 보존한다.
6. 수집 결과를 `.var/local/raw/{YYYY-MM-DD}/` 아래에 JSON으로 저장한다.
7. 서비스별 수집 범위는 source 설정으로 제한할 수 있다. OpenAI처럼 feed가 과도하게 큰 source는 `collection_limit` 또는 `lookback_days` 설정을 추가한다.

전체 서비스 수집:

```bash
make collect
```

단일 서비스 수집:

```bash
make collect SERVICE=hacker-news COUNT=5
```

날짜 지정 수집:

```bash
make collect SERVICE=hacker-news DATE=2026-06-07 COUNT=5
```

사용 가능한 서비스 키는 `NewsSourceFactory.service_keys()`가 제공한다. collector CLI는 실행 결과를 콘솔에 요약하고, 같은 결과를 `.var/local/raw/{YYYY-MM-DD}/summary.json`과 `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`에 저장한다. 이 단계는 Markdown 생성이나 Docusaurus 빌드를 수행하지 않는다.

MVP 대상 서비스:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

Raw 수집 산출물:

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

## Preprocessor

Preprocessor 단계는 수집된 snapshot을 Agent 입력 후보로 정리한다.

1. URL을 canonical form으로 정규화한다.
2. 필수 필드가 없는 항목을 제외한다.
3. 현재 실행 내 URL/title fingerprint 중복을 제거한다.
4. `briefed_articles` 상태와 기존 article 문서를 기준으로 이미 브리핑된 글을 제외한다.
5. 발행일, source priority, popularity signal, editorial keyword를 기준으로 후보를 랭킹한다.
6. Agent 입력 개수를 제한한다.
7. 전처리 trace를 생성한다.

현재 스캐폴딩은 휴리스틱 기반이다. LLM 기반 News Editor Agent는 전처리된 신규 후보만 받는다.
`src.main`의 전체 파이프라인은 Collector 실행 직후 Preprocessor를 실행하고, 전처리 결과를 `.var/local/processed/{YYYY-MM-DD}/preprocessing.json`에 저장한다.

전처리 실행:

```bash
make preprocess
make preprocess DATE=2026-06-07
make preprocess RAW_DIR=.var/local/raw PROCESSED_DIR=.var/local/processed
```

전처리 산출물:

```text
.var/local/processed/YYYY-MM-DD/
└── preprocessing.json
```

전처리는 `Pipeline + Strategy + Repository` 조합으로 구성한다. `NewsPreprocessor`는 단계별 `PreprocessingStep`을 순서대로 실행하고, 후보 점수화는 교체 가능한 scorer strategy로 둔다. `BriefedArticleStore`는 이미 브리핑된 원문 글 상태를 조회하는 저장소 역할을 한다.

## News Editor Agent

Agent는 신규 후보 중 의미 있는 글만 선택하고, 선택된 글마다 하나의 상세 브리핑을 생성한다. 이미 브리핑된 원문 URL은 다시 처리하지 않는다.

## Generator

Generator 단계는 처리 결과를 Markdown으로 저장한다.

1. 글별 상세 브리핑 문서를 생성한다.
2. 서비스별 색인 문서를 갱신한다.
3. 전체 메인 페이지를 갱신한다.
4. 내부 article/service 문서 링크와 원문 출처 링크를 함께 기록한다.

생성 경로:

```text
docs/index.md
docs/services/{service_key}.md
docs/articles/{service_key}/{slug}.md
```

## Build

Docusaurus가 `docs/` 아래 Markdown을 정적 사이트로 빌드한다.

로컬 빌드:

```bash
make build
```

개발 서버:

```bash
npm run start -- --host 127.0.0.1 --port 3000
```

## Deploy

GitHub Actions가 매일 source snapshot 수집, 신규 후보 처리, 아카이브 문서 갱신, 배포를 수행한다.

워크플로:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. `make generate`를 통한 collection, preprocessing, Markdown scaffold generation
7. `make build`를 통한 Docusaurus build
8. GitHub Pages artifact upload
9. GitHub Pages deploy

수동 배포:

```bash
make deploy
make deploy DATE=2026-06-07
make deploy-status
```
