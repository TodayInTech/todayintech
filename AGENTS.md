# AGENTS.md

Today in Tech는 기술 뉴스 RSS/Atom 피드를 수집하고, AI 기반 News Editor Agent가 중요한 뉴스를 선별, 요약, 분석하여 정적 문서 사이트로 배포하는 기술 뉴스 브리핑 플랫폼이다.

이 문서는 프로젝트의 설계 기준과 에이전트 작업 규칙을 정의한다. 루트의 문서는 한국어를 기준으로 작성한다. 영어 문서는 다국어 지원 문서로 `notes/en/` 아래에 둔다.

## 확정된 프레임워크

- Runtime: Python 3.14 고정
- Static Site: Docusaurus
- Language: 루트 문서는 한국어, 영어 문서는 `notes/en/`
- Storage: JSON 파일 기반
- Automation: GitHub Actions
- Hosting: GitHub Pages
- LLM: OpenAI API

`pyproject.toml`의 Python 버전은 현재처럼 `>=3.14`를 유지하거나, 재현성을 더 강하게 보장해야 할 경우 `==3.14.*`에 준하는 방식으로 고정한다. GitHub Actions와 로컬 개발 환경의 Python 버전은 반드시 동일해야 한다.

## MVP 대상 서비스

MVP에서 지원하는 뉴스 서비스는 다음으로 제한한다.

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

추후 다른 서비스가 쉽게 추가될 수 있어야 하므로 서비스별 구현은 하드코딩하지 않는다.

## 핵심 아키텍처

```text
RSS/Atom Sources
    ↓
Service Factory
    ↓
Service-specific Collector
    ↓
Normalize Articles
    ↓
Deduplicate
    ↓
Importance Scoring
    ↓
Category Classification
    ↓
AI Summarization
    ↓
Service Markdown Generation
    ↓
Global Summary Markdown Generation
    ↓
Docusaurus Build
    ↓
GitHub Pages Deployment
```

Today in Tech는 날짜마다 브리핑 묶음을 만든다. 단, 날짜별로 하나의 거대한 Markdown 파일을 만들지 않는다. 각 날짜 디렉터리 안에 서비스별 Markdown 문서와 전체 요약 Markdown 문서를 함께 생성한다.

예시:

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

notes/
└── en/
    ├── AGENTS.md
    └── harness/
        ├── ARCHITECTURE.md
        ├── COMMIT_MESSAGE.md
        ├── OVERVIEW.md
        └── TECH_STACK.md
```

## 서비스 확장 설계

서비스 생성은 Factory Method와 Abstract Factory를 사용하고, 수집 알고리즘은 Strategy 패턴으로 분리한다.

목표:

- 서비스 구현체에는 서비스 메타데이터와 collector 설정만 둔다.
- RSS, sitemap, API 등 수집 알고리즘은 collector strategy에 둔다.
- 파이프라인은 구체 서비스명을 직접 알지 않도록 한다.
- 신규 서비스 추가 시 기존 파이프라인 코드를 수정하지 않고 factory 등록만으로 확장 가능해야 한다.
- RSS를 지원하지 않는 서비스는 공식 sitemap, 공식 API, HTML metadata 등 서비스별 collector strategy를 구현한다.

권장 구조:

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

설계 규칙:

- 제품과 문서에서는 사용자에게 노출되는 브리핑 단위를 `service`라고 부른다.
- 코드에서는 외부 수집 대상을 `source`, 수집 실행 계층을 `collection`으로 구분한다.
- `BaseNewsSource`는 서비스 메타데이터와 collector 설정 인터페이스를 정의한다.
- `BaseCollectorStrategy`는 수집 알고리즘 인터페이스를 정의한다.
- `RssCollector`는 RSS/Atom 수집 strategy를 제공한다.
- `SitemapCollector`는 sitemap + page metadata 수집 strategy를 제공한다.
- `CollectorStrategyFactory`는 서비스의 `collector_type`에 맞는 collector strategy를 생성한다.
- `NewsSourceFactory`는 서비스 키를 받아 구체 서비스 구현체를 생성한다.
- `AbstractNewsSourceFactory`는 서비스 제품군 확장을 위한 추상 팩토리 역할을 한다.
- 파이프라인은 `BaseNewsSource` 인터페이스에만 의존한다.
- source별 예외 처리는 가능한 경우 source 또는 collector strategy 경계에서 처리한다.

## 문서 생성 규칙

서비스별 Markdown:

- 각 서비스마다 하나의 문서를 생성한다.
- 문서는 해당 서비스에서 선별된 주요 뉴스, 요약, 중요도, 출처 링크를 포함한다.
- 모든 요약은 한국어를 기본으로 작성한다.
- 영어 문서가 필요할 경우 `notes/en/` 아래에 대응 문서를 둔다.

전체 요약 Markdown:

- 전체 브리핑의 시작점이다.
- 도메인별 시사점을 구분해서 설명한다.
- 각 도메인 또는 주요 뉴스에서 원문 출처와 내부 서비스 문서로 이동할 수 있어야 한다.
- 단순 기사 목록이 아니라 편집된 브리핑이어야 한다.

권장 구성:

```markdown
# Today in Tech

## 개요

오늘의 핵심 기술 흐름 요약

## 도메인별 시사점

### AI

- 주요 변화
- 관련 서비스 문서: [OpenAI Blog](./services/openai-blog.md)
- 원문 출처: ...

### Developer Tools

...

## 서비스별 브리핑

- [Hacker News](./services/hacker-news.md)
- [GitHub Blog](./services/github-blog.md)
- [Google Blog](./services/google-blog.md)
- [OpenAI Blog](./services/openai-blog.md)
- [Anthropic Blog](./services/anthropic-blog.md)
```

## News Editor Agent 책임

News Editor Agent는 뉴스레터 편집자 역할을 수행한다.

해야 할 일:

- 뉴스 중요도 평가
- 카테고리 분류
- 중복 제거 보조
- 서비스별 주요 뉴스 요약
- 전체 요약 문서의 도메인별 시사점 생성
- 원문 출처와 내부 문서 링크 보존

하지 말아야 할 일:

- 원문 전체를 재작성하지 않는다.
- 원문에 없는 사실을 단정하지 않는다.
- 모든 수집 기사를 문서에 포함하지 않는다.
- 출처 링크 없이 요약만 제공하지 않는다.

## 처리 워크플로

각 단계는 지속적인 개발과 디버깅을 위해 독립 실행 가능해야 한다.

- Collector 단계는 `.venv/bin/python -m src.collection`로 실행한다.
- 특정 서비스 수집은 `.venv/bin/python -m src.collection --service {service_key}`로 확인한다.
- Collector 단계는 `data/raw/{YYYY-MM-DD}/summary.json`과 `data/raw/{YYYY-MM-DD}/services/{service}.json`만 생성하고 Markdown 생성이나 Docusaurus 빌드를 수행하지 않는다.
- 전체 파이프라인은 `.venv/bin/python -m src.main`으로 실행한다.
- 이후 Processing, Generator 단계도 독립 실행 엔트리포인트를 제공하는 방향으로 확장한다.

1. Factory가 MVP 서비스 구현체를 생성한다.
2. `NewsCollector`가 각 서비스 구현체의 collector strategy로 정보를 수집한다.
3. 수집 데이터를 공통 `Article` 모델로 정규화한다.
4. 서비스별 수집 결과를 `data/raw/{YYYY-MM-DD}/services/{service}.json`에 저장한다.
5. `seen.json`과 URL canonicalization으로 중복을 제거한다.
6. Agent가 중요도 점수와 카테고리를 산출한다.
7. 서비스별 Top News를 요약한다.
8. `docs/{YYYY-MM-DD}/services/{service}.md`를 생성한다.
9. 모든 서비스 결과를 모아 `docs/{YYYY-MM-DD}/summary.md`를 생성한다.
10. Docusaurus를 빌드한다.
11. GitHub Actions가 GitHub Pages에 배포한다.

## 오류 처리 원칙

- 특정 서비스 수집 실패는 로그에 남기고 가능한 경우 나머지 서비스 처리를 계속한다.
- 모든 서비스가 실패하면 문서 생성을 중단하고 CI를 실패 처리한다.
- 필수 필드가 없는 기사는 제외한다.
- LLM 응답은 schema 검증을 통과해야 한다.
- LLM 실패 시 RSS summary 기반 fallback 요약을 사용할 수 있다.
- 배포 전 Docusaurus build가 반드시 성공해야 한다.

## 유지보수 원칙

- 신규 서비스 추가 시 기존 파이프라인을 수정하지 않는다.
- 서비스 구현체와 factory 등록만 추가하는 구조를 유지한다.
- 루트 문서는 한국어를 기준으로 유지한다.
- 지원 언어 문서는 같은 변경 안에서 함께 업데이트한다.
- 현재 지원 언어는 한국어와 영어이다.
- 영어 문서는 `notes/en/`에 동일 주제 문서로 관리한다.
- 영어 AGENTS 문서 경로는 `notes/en/AGENTS.md`이다.
- 영어 하네스 문서 경로는 `notes/en/harness/`이다.
- 한국어 하네스 문서를 수정하면 대응하는 `notes/en/harness/*.md`도 함께 수정한다.
- 작업 상태가 바뀌면 `harness/TASKS.md`와 `notes/en/harness/TASKS.md`를 함께 업데이트한다.
- 서비스 수집 방식이나 수집 조건이 바뀌면 `harness/service/SERVICES.md`와 `notes/en/harness/service/SERVICES.md`를 함께 업데이트한다.
- 자동 생성 문서와 사람이 작성한 설계 문서를 명확히 구분한다.
- 브리핑 품질은 수집량보다 선별 품질을 우선한다.
