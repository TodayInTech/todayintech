# ARCHITECTURE

## 프로젝트 아키텍처

Today in Tech는 수집, 처리, 생성, 빌드, 배포 단계를 분리한다. 각 단계는 독립적으로 테스트 가능해야 하며, 서비스 추가가 전체 파이프라인 수정으로 이어지지 않도록 설계한다.

```text
Official Sources
    ↓
Service Factory
    ↓
Service-specific Collector Strategy
    ↓
Normalize Articles
    ↓
Deduplicate
    ↓
Importance Scoring
    ↓
Category Classification
    ↓
Summarization
    ↓
Service Markdown Generation
    ↓
Global Summary Markdown Generation
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
│   ├── deduplicator.py
│   ├── classifier.py
│   ├── scorer.py
│   └── summarizer.py
├── generator/
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

날짜마다 하나의 브리핑 묶음을 생성한다.

```text
docs/
└── YYYY-MM-DD/
    ├── summary.md
    └── services/
        ├── hacker-news.md
        ├── github-blog.md
        ├── google-blog.md
        ├── openai-blog.md
        └── anthropic-blog.md
```

`summary.md`는 전체 브리핑의 진입점이며, `services/*.md`는 서비스별 상세 브리핑이다.

## 단계별 플로우

```text
Collector
    ↓
Processing
    ↓
Generator
    ↓
Build
    ↓
Deploy
```

## Collector

Collector 단계는 독립 실행 가능해야 하며, 각 서비스별 수집 상태와 원본 JSON을 확인할 수 있어야 한다.

1. `NewsCollector`가 `NewsSourceFactory`를 통해 MVP 서비스 구현체를 생성한다.
2. 각 서비스 구현체가 RSS/Atom, sitemap, 공식 API 등 자기 collector strategy로 정보를 수집한다.
3. 피드 항목을 공통 `Article` 모델로 정규화한다.
4. 서비스별 수집 결과를 `ServiceCollectionResult`로 묶는다.
5. URL, 제목, 발행일, 출처, 요약, 태그를 최대한 보존한다.
6. 수집 결과를 `data/raw/{YYYY-MM-DD}/` 아래에 JSON으로 저장한다.

전체 서비스 수집:

```bash
.venv/bin/python -m src.collection
```

단일 서비스 수집:

```bash
.venv/bin/python -m src.collection --service hacker-news --preview-limit 5
```

사용 가능한 서비스 키는 `NewsSourceFactory.service_keys()`가 제공한다. collector CLI는 실행 결과를 콘솔에 요약하고, 같은 결과를 `data/raw/{YYYY-MM-DD}/summary.json`과 `data/raw/{YYYY-MM-DD}/services/{service}.json`에 저장한다. 이 단계는 Markdown 생성이나 Docusaurus 빌드를 수행하지 않는다.

MVP 대상 서비스:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

Raw 수집 산출물:

```text
data/raw/YYYY-MM-DD/
├── summary.json
└── services/
    ├── hacker-news.json
    ├── github-blog.json
    ├── google-blog.json
    ├── openai-blog.json
    └── anthropic-blog.json
```

## Processing

Processing 단계는 수집된 기사 데이터를 브리핑 후보로 정리한다.

1. URL 기준 중복을 제거한다.
2. 기사 카테고리를 분류한다.
3. 중요도 점수를 계산한다.
4. 요약 데이터를 만든다.

현재 스캐폴딩은 휴리스틱 기반이다. LLM 기반 News Editor Agent는 이후 이 계층에 연결한다.

## Generator

Generator 단계는 처리 결과를 Markdown으로 저장한다.

1. 서비스별 문서를 생성한다.
2. 전체 요약 문서를 생성한다.
3. 내부 서비스 문서 링크와 원문 출처 링크를 함께 기록한다.

생성 경로:

```text
docs/{YYYY-MM-DD}/summary.md
docs/{YYYY-MM-DD}/services/{service}.md
```

## Build

Docusaurus가 `docs/` 아래 Markdown을 정적 사이트로 빌드한다.

로컬 빌드:

```bash
npm run build
```

개발 서버:

```bash
npm run start -- --host 127.0.0.1 --port 3000
```

## Deploy

GitHub Actions가 매일 브리핑 생성과 배포를 수행한다.

워크플로:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. Briefing generation
7. Docusaurus build
8. GitHub Pages artifact upload
9. GitHub Pages deploy
