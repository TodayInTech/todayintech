# AGENTS.md

Today in Tech는 기술 뉴스 RSS/Atom 피드와 공식 sitemap을 매일 수집하고, AI 기반 News Editor Agent가 특정 기간 동안 의미 있는 글을 선별, 요약, 분석하여 정적 문서 사이트로 누적 배포하는 기술 글 큐레이션 아카이브이다.

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

## 제품 방향

```text
RSS/Atom Sources
    ↓
Service Factory
    ↓
Service-specific Collector
    ↓
Normalize Articles
    ↓
Preprocess Candidates
    ↓
Briefed Article Filtering
    ↓
Candidate Ranking
    ↓
Writer
    ├── News Editor Agent
    └── Markdown Generator
    ↓
Docusaurus Build
    ↓
GitHub Pages Deployment
```

Today in Tech는 날짜마다 브리핑 묶음을 새로 만드는 서비스가 아니다. Collector는 매일 실행되어 외부 source의 최신 snapshot을 저장하지만, Agent는 이미 브리핑된 글을 다시 처리하지 않는다. 사이트는 날짜별 일간 뉴스레터가 아니라 서비스별 핵심 글과 전체 핵심 흐름을 누적하는 아카이브로 동작한다.

예시:

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
│   ├── news_preprocessor.py
│   ├── briefed_article_store.py
│   ├── article_candidate.py
│   ├── url_normalizer.py
│   ├── deduplicator.py
│   ├── classifier.py
│   ├── scorer.py
│   └── summarizer.py
├── writer/
│   ├── __main__.py
│   ├── news_writer.py
│   ├── agent/
│   │   ├── contracts.py
│   │   ├── draft_agent.py
│   │   └── schemas.py
│   └── generator/
│       ├── article_markdown_writer.py
│       ├── main_index_writer.py
│       └── service_index_writer.py
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

메인 페이지:

- `docs/index.md`는 전체 서비스의 핵심 글과 핵심 흐름을 보여주는 첫 진입점이다.
- 특정 기간 동안 새로 선별된 핵심 글, 도메인별 흐름, 서비스별 최근 업데이트를 연결한다.
- 모든 항목은 내부 article 문서와 원문 출처로 이동 가능해야 한다.

서비스별 Markdown:

- 각 서비스마다 하나의 문서를 생성한다.
- 문서는 해당 서비스에서 누적 선별된 핵심 글 목록, 서비스 관점 요약, 최근 브리핑 링크를 포함한다.
- 모든 요약은 한국어를 기본으로 작성한다.
- 영어 문서가 필요할 경우 `notes/en/` 아래에 대응 문서를 둔다.

글별 Markdown:

- 의미 있는 원문 글 하나당 하나의 문서를 생성한다.
- 문서 경로는 `docs/articles/{service_key}/{slug}.md`를 사용한다.
- 한 번 생성된 article 문서는 같은 원문 URL로 다시 Agent 재생성하지 않는다.
- 문서는 리포트가 아니라 자연스러운 에디토리얼 브리핑 글처럼 읽혀야 한다.
- 문서는 짧은 브리핑 본문, 핵심 포인트, 읽어볼 만한 이유, 확인할 점, 원문 링크를 포함한다.
- `DraftNewsEditorAgent`가 만든 draft 문서는 요약한 척하지 않고 작성 대기 상태, 피드 설명, 후보 판단 근거만 표시한다.

권장 글별 구성:

```markdown
# 원문 글 제목

> 서비스명 · 발행일 · 카테고리

원문 링크: [원문 글 제목](https://...)

---

자연스럽게 읽히는 브리핑 본문 2~4문단

## 핵심 포인트

- ...

## 읽어볼 만한 이유

...

## 확인할 점

- ...
```

권장 구성:

```text
docs/index.md
docs/services/{service_key}.md
docs/articles/{service_key}/{article_slug}.md
```

## News Editor Agent 책임

News Editor Agent는 뉴스레터 편집자가 아니라 기술 글 큐레이터와 리서치 에디터 역할을 수행한다.

해야 할 일:

- 신규 후보 글의 브리핑 가치 평가
- 카테고리 분류
- 중복 제거 보조
- 글 단위 상세 브리핑 생성
- 서비스별 누적 요약 갱신
- 메인 페이지의 도메인별 핵심 흐름 생성
- 원문 출처와 내부 문서 링크 보존

하지 말아야 할 일:

- 원문 전체를 재작성하지 않는다.
- 원문에 없는 사실을 단정하지 않는다.
- 모든 수집 기사를 문서에 포함하지 않는다.
- 출처 링크 없이 요약만 제공하지 않는다.
- 이미 `briefed_articles` 상태에 등록된 글을 다시 브리핑하지 않는다.

## 처리 워크플로

각 단계는 지속적인 개발과 디버깅을 위해 독립 실행 가능해야 한다.

- Collector 단계는 `make collect`로 실행한다.
- 특정 서비스 수집은 `make collect SERVICE={service_key}`로 확인한다.
- Collector 단계는 `.var/local/raw/{YYYY-MM-DD}/summary.json`과 `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`만 생성하고 Markdown 생성이나 Docusaurus 빌드를 수행하지 않는다.
- Collector는 daily snapshot을 저장한다. 같은 글이 여러 날짜에 반복 수집될 수 있으며, 이는 정상 동작이다.
- Preprocessor 단계는 `make preprocess`로 실행한다.
- Preprocessor는 URL 정규화, 현재 실행 중복 제거, 이미 브리핑된 글 제외, 후보 랭킹, Writer 입력용 후보 식별자 생성을 수행한다.
- Writer 단계는 `make write`로 실행한다.
- Writer는 Agent와 Generator를 포함한다. Agent는 편집 결과를 만들고 Generator는 Markdown 파일만 쓴다.
- 기본 Writer는 요약을 생성하지 않는 `DraftNewsEditorAgent`를 사용한다.
- `TODAYINTECH_WRITER_AGENT=openai` 또는 `make write WRITER_AGENT=openai`를 사용하면 `OpenAINewsEditorAgent`를 사용한다.
- OpenAI Agent는 원문 전체를 크롤링하지 않고, Collector와 Preprocessor가 제공한 제목, 피드 설명, 태그, 메타데이터, ranking signals만 사용한다.
- 전체 파이프라인은 `.venv/bin/python -m src.main`으로 실행하며, 현재는 Collector, Preprocessor, Writer draft 생성까지 연결되어 있다.

1. Factory가 MVP 서비스 구현체를 생성한다.
2. `NewsCollector`가 각 서비스 구현체의 collector strategy로 정보를 수집한다.
3. 수집 데이터를 공통 `Article` 모델로 정규화한다.
4. 서비스별 수집 결과를 `.var/local/raw/{YYYY-MM-DD}/services/{service}.json`에 저장한다.
5. Preprocessor가 URL canonicalization과 현재 실행 중복 제거를 수행한다.
6. `briefed_articles` 상태와 기존 article 문서로 이미 발행된 글을 제외한다.
7. Preprocessor가 `candidate_id`, `url_hash`, `suggested_doc_key`, `suggested_article_path`를 포함한 Writer 입력 후보를 만든다.
8. Writer Agent가 신규 후보를 편집 결과로 변환한다. 현재 Draft Agent는 요약/인사이트를 생성하지 않는다.
9. Writer Generator가 `docs/articles/{service_key}/{slug}.md`를 생성한다.
10. `docs/services/{service_key}.md`를 서비스별 색인으로 갱신한다.
11. `docs/index.md`를 전체 진입 페이지로 갱신한다.
12. 생성 성공 후 `briefed_articles` 상태를 draft 또는 published로 업데이트한다.
13. Docusaurus를 빌드한다.
14. GitHub Actions가 GitHub Pages에 배포한다.

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
- 환경 변수나 설정 로딩 방식이 바뀌면 `harness/ENV.md`와 `notes/en/harness/ENV.md`를 함께 업데이트한다.
- 테스트, 운영 트레이싱, 품질 산출물이 바뀌면 `harness/QUALITY.md`와 `notes/en/harness/QUALITY.md`를 함께 업데이트한다.
- 자동 생성 문서와 사람이 작성한 설계 문서를 명확히 구분한다.
- 브리핑 품질은 수집량보다 선별 품질을 우선한다.
- 날짜별 일간 문서 구조를 새로 추가하지 않는다. 사이트의 기본 단위는 서비스와 article이다.
- 원문 URL 하나는 article 문서 하나에만 대응해야 한다.
