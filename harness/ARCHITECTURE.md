# ARCHITECTURE

## 프로젝트 아키텍처

Today in Tech는 수집, 전처리, Writer, 빌드, 배포 단계를 분리한다. 각 단계는 독립적으로 테스트 가능해야 하며, 서비스 추가가 전체 파이프라인 수정으로 이어지지 않도록 설계한다.

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
Candidate Enrichment
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
│   ├── __main__.py
│   ├── context.py
│   ├── enums.py
│   ├── models.py
│   ├── news_preprocessor.py
│   ├── processed_writer.py
│   ├── contracts/
│   │   └── base.py
│   ├── factories/
│   │   └── preprocessing_pipeline_factory.py
│   ├── identity/
│   │   ├── candidate_identity.py
│   │   └── url_normalizer.py
│   ├── policies/
│   │   ├── base.py
│   │   └── service_policy.py
│   ├── scoring/
│   │   ├── base.py
│   │   └── default.py
│   ├── state/
│   │   └── briefed_article_store.py
│   ├── steps/
│   │   ├── validation.py
│   │   ├── url_normalization.py
│   │   ├── candidate_identity.py
│   │   ├── run_deduplication.py
│   │   ├── briefed_article_filter.py
│   │   ├── candidate_scoring.py
│   │   ├── candidate_quality_gate.py
│   │   └── candidate_limiting.py
├── enrichment/
│   ├── __main__.py
│   ├── content_enricher.py
│   ├── context.py
│   ├── models.py
│   ├── contracts/
│   ├── factories/
│   ├── fetchers/
│   ├── extractors/
│   ├── chunking/
│   ├── policies/
│   ├── steps/
│   ├── state/
│   ├── storage/
│   └── tokenization/
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
│   ├── hacker-news/
│   ├── github-blog.md
│   ├── github-blog/
│   ├── google-blog.md
│   ├── google-blog/
│   ├── openai-blog.md
│   ├── openai-blog/
│   ├── anthropic-blog.md
│   └── anthropic-blog/
```

`index.md`는 전체 서비스의 핵심 흐름과 최근 선별 글을 보여주는 진입점이다. `services/*.md`는 서비스별 핵심 글 색인이다. `services/{service_key}/*.md`는 원문 글 하나에 대한 상세 브리핑이다.
개별 article 문서는 리포트 형식보다 자연스러운 브리핑 글 형태를 우선한다.

## 단계별 플로우

```text
Collector
    ↓
Preprocessor
    ↓
Writer
    ├── Agent
    └── Generator
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
7. Writer가 사용할 `candidate_id`, `url_hash`, `suggested_doc_key`, `suggested_article_path`를 생성한다.
8. 전처리 trace를 생성한다.

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

전처리는 `Pipeline + Strategy + Repository` 조합으로 구성한다. `PreprocessingPipelineFactory`가 기본 step 목록을 조립하고, `NewsPreprocessor`는 단계별 `BasePreprocessingStep`을 순서대로 실행한다. 각 단계 구현은 `processing/steps/`에서 명시적으로 이 ABC를 상속한다. 후보 점수화는 `processing/scoring/`의 `BaseCandidateScorer` 기반 strategy로 두며, URL/문서 identity 생성은 `processing/identity/`가 담당한다. 서비스별 최소 품질 기준은 `processing/policies/`의 `ServicePreprocessingPolicy`로 정의하고, `CandidateQualityGateStep`이 scoring 이후 limit 이전에 낮은 품질 후보를 제외한다. `BriefedArticleStore`는 `processing/state/`에 위치하며 Writer가 문서 생성 성공 후 기록한 원문 글 상태를 조회하는 저장소 역할을 한다. 제외 사유는 `ExcludedReason`, 점수 근거는 `RankingSignals`, 사람이 읽을 수 있는 점수 설명은 `ranking_reasons_ko`, 단계별 실행 결과는 `PreprocessingStepMetrics`로 구조화한다.

전처리 산출물의 `ArticleCandidate`는 Writer 입력 패킷이다. 이 패킷은 요약이나 인사이트를 만들지 않고, Writer Agent가 발행 여부와 편집 내용을 판단하는 데 필요한 식별자와 근거만 제공한다.

## Enrichment

Enrichment는 Preprocessor가 제한한 후보를 대상으로 원문 근거를 준비하는 별도 stage이다. `ContentEnricher`는 `BaseEnrichmentStep` pipeline을 실행하고, fetcher·extractor·chunker·token counter는 Strategy, 구현 선택은 Factory, token budget 결정은 Policy, 결과 재사용은 Repository 패턴으로 분리한다.

1. 원문 요청 결과와 최종 URL을 기록한다.
2. 본문을 추출하되 제목, 섹션, 코드, 표, 목록 구조를 보존한다.
3. 추출 토큰 수와 구조에 따라 `full_content`, `chunk_selection`, `evidence_selection` 중 Agent 입력 전략을 선택한다.
4. 추출 실패 시 정책에 따라 `feed_metadata_only` fallback 또는 실패로 처리한다.
5. 원문 전체나 선택된 chunk 본문은 trace-history에 저장하지 않는다.

Enrichment 상태는 `enriched`, `fallback`, `skipped`, `failed`로 구분한다. Agent 입력 전략은 `full_content`, `chunk_selection`, `evidence_selection`, `feed_metadata_only`, `none`으로 구분한다. Trace는 후보별 HTTP 상태, MIME type, 응답 크기, 실행 시간, extractor와 policy 버전, 캐시 여부, 문서 유형, 추출·선택 토큰 수, 구조 개수, 제목 유사도, 품질 점수, 실패 원인을 기록한다.

초기 policy는 100토큰 미만을 정보 부족으로 처리하고, 4,000토큰 이하는 전체 본문을 선택한다. 4,001~8,000토큰은 `chunk_selection`, 8,000토큰 초과는 `evidence_selection` 대상으로 표시한다. 후자의 두 전략은 의미 기반 Agent selector가 연결되기 전까지 임의로 chunk를 선택하지 않는다.

```bash
make enrich
make enrich DATE=2026-06-23
make trace-enrich
```

산출물:

```text
.var/local/enriched/YYYY-MM-DD/
└── enrichment.json

.var/local/enrichment-cache/
└── {cache_key}.json
```

## Writer

Writer 단계는 현재 Preprocessor가 만든 `ArticleCandidate`를 받아 문서화 결과를 만든다. Enrichment stage가 연결되면 원문 근거가 추가된 후보를 입력으로 받는다. Writer 내부는 Agent와 Generator로 나뉜다.

- Writer Agent: 후보 중 문서화할 글을 선택하고 편집 결과를 만든다.
- Writer Generator: Agent 결과만 받아 Markdown 파일을 쓴다.
- Writer는 모든 Markdown 생성이 성공한 뒤 `briefed_articles` 상태와 누적 index를 갱신한다.
- 메인 index와 서비스 index는 누적된 `briefed_articles` 상태를 기준으로 우선순위 브리핑과 전체 누적 목록을 함께 보여준다.
- GitHub Actions는 생성된 `docs/`와 `data/briefed_articles.json`을 main에 커밋해 다음 실행의 중복 제거 기준으로 사용한다.
- 기본 구현은 `DraftNewsEditorAgent`를 사용한다. Draft Agent는 요약, 왜 중요한가, 개발자 인사이트를 생성하지 않고 `editorial_status=draft` 문서만 만든다.
- `TODAYINTECH_WRITER_AGENT=openai`를 사용하면 `OpenAINewsEditorAgent`가 structured output으로 게시 여부, 선정/제외 이유, 판단 확신도, 요약 근거 범위, 근거 목록, 자연스러운 한국어 장문 요약을 생성한다.
- 공개 article 문서는 요약 2~3문단과 원문 링크만 표시한다. 선정 이유, 판단 확신도, 근거 범위, 근거 목록은 Writer trace에만 남긴다.
- OpenAI Agent는 full text crawling을 하지 않고, 전처리 후보의 제목, 피드 설명, 태그, 메타데이터, ranking signals만 사용한다.

Writer 실행:

```bash
make write
make write DATE=2026-06-07 PROCESSED_DIR=.var/local/processed OUTPUT_DIR=docs
make write WRITER_AGENT=openai
make generate-openai
```

## News Editor Agent

Agent는 신규 후보 중 의미 있는 글만 선택하고, 선택된 글마다 하나의 상세 브리핑을 생성한다. 이미 브리핑된 원문 URL은 다시 처리하지 않는다.

## Generator

Generator 단계는 처리 결과를 Markdown으로 저장한다.

1. 글별 상세 브리핑 문서를 자연스러운 에디토리얼 본문 형태로 생성한다.
2. 서비스별 색인 문서를 갱신한다.
3. 전체 메인 페이지를 갱신한다.
4. 내부 article/service 문서 링크와 원문 출처 링크를 함께 기록한다.

개별 article 문서 권장 구성:

```text
# 원문 글 제목

> 서비스명 · 발행일 · 카테고리

원문 링크

글의 주제와 배경을 설명하는 자연스러운 요약 문단

핵심 내용과 기술적 의미를 이어서 설명하는 문단
```

Draft 문서는 요약이나 중요성 판단을 생성하지 않고, 작성 대기 상태와 피드 설명, 후보 판단 근거만 표시한다.

생성 경로:

```text
docs/index.md
docs/services/{service_key}.md
docs/services/{service_key}/{slug}.md
```

## Build

Docusaurus가 `docs/` 아래 Markdown을 정적 사이트로 빌드한다.

로컬 빌드:

```bash
make build
```

개발 서버:

```bash
make serve
make serve HOST=127.0.0.1 PORT=3000
```

빌드 결과 미리보기:

```bash
make serve-build
```

## Deploy

GitHub Actions가 매일 source snapshot 수집, 신규 후보 처리, 아카이브 문서 갱신, 배포를 수행한다.

워크플로:

1. Repository checkout
2. Python 3.14 setup
3. Node 20 setup
4. Python dependency install
5. Node dependency install
6. `make ci-quality`를 통한 테스트와 운영 trace 실행
7. trace 결과를 `tracing-history` 브랜치에 누적
8. `make generate-openai`를 통한 collection, preprocessing, OpenAI Writer 문서 생성
9. `make build`를 통한 Docusaurus build
10. GitHub Pages artifact upload
11. GitHub Pages deploy

GitHub Actions 자동 배포는 `OPENAI_API_KEY` repository secret이 필요하다.

수동 배포:

```bash
make deploy
make deploy DATE=2026-06-07
make deploy-status
```
