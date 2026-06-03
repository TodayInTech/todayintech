# ARCHITECTURE

## 프로젝트 아키텍처

Today in Tech는 수집, 처리, 생성, 빌드, 배포 단계를 분리한다. 각 단계는 독립적으로 테스트 가능해야 하며, 서비스 추가가 전체 파이프라인 수정으로 이어지지 않도록 설계한다.

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
├── services/
│   ├── base.py
│   ├── factory.py
│   ├── rss_service.py
│   ├── hacker_news.py
│   ├── github_blog.py
│   ├── google_blog.py
│   ├── openai_blog.py
│   └── anthropic_blog.py
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

서비스 구현은 Factory Method와 Abstract Factory를 따른다.

- `BaseNewsService`: 모든 뉴스 서비스 구현체가 따라야 하는 공통 인터페이스
- `RssNewsService`: 일반 RSS/Atom 기반 서비스의 기본 구현
- `NewsServiceFactory`: 서비스 키를 기준으로 구체 서비스 구현체 생성
- `AbstractNewsServiceFactory`: 서비스 제품군 확장을 위한 추상 팩토리

신규 서비스를 추가할 때는 기존 파이프라인을 수정하지 않는다. `src/services/`에 구현체를 추가하고 factory registry에 등록한다.

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

Collector 단계는 서비스 구현체가 담당한다.

1. `NewsServiceFactory`가 MVP 서비스 구현체를 생성한다.
2. 각 서비스 구현체가 RSS/Atom 피드를 수집한다.
3. 피드 항목을 공통 `Article` 모델로 정규화한다.
4. URL, 제목, 발행일, 출처, 요약, 태그를 최대한 보존한다.

MVP 대상 서비스:

- Hacker News
- GitHub Blog
- Google Blog
- OpenAI Blog
- Anthropic Blog

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
