# Today in Tech

Today in Tech는 기술 뉴스 RSS/Atom 피드를 수집하고, AI 기반 News Editor Agent가 중요한 뉴스를 선별해 Docusaurus 문서 사이트로 배포하는 기술 뉴스 브리핑 플랫폼입니다.

현재 저장소는 MVP 기본 구조 단계입니다. 서비스별 정보 수집, 서비스별 Markdown 생성, 전체 요약 Markdown 생성, Docusaurus 빌드 흐름이 잡혀 있으며, LLM 기반 중요도 평가와 요약은 이후 구현 예정입니다.

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

브리핑은 날짜마다 하나의 묶음으로 생성됩니다. 날짜별 디렉터리 안에 전체 요약 문서와 서비스별 문서가 함께 들어갑니다.

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

`docs/2026-06-03/` 아래의 현재 문서는 구조 검증을 위해 생성한 샘플 산출물입니다.

## 환경 변수

환경 변수 예시는 [.env.example](/Users/choi-hyk/todayintech/.env.example)에 있습니다.

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
- `TODAYINTECH_MAX_ARTICLES_PER_SERVICE`: 서비스별 최대 기사 수
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
.venv/bin/python -m src.collection
```

특정 서비스만 확인할 수도 있습니다.

```bash
.venv/bin/python -m src.collection --service hacker-news --preview-limit 5
```

실행 시 콘솔에는 서비스별 상태, 수집 개수, 기사 미리보기가 출력되고 각 서비스별 수집 결과가 JSON으로 저장됩니다.

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

전체 파이프라인을 실행하여 수집 결과와 날짜별 브리핑 Markdown을 함께 생성합니다.

```bash
.venv/bin/python -m src.main
```

Docusaurus 개발 서버를 실행합니다.

```bash
npm run start -- --host 127.0.0.1 --port 3000
```

정적 사이트 빌드를 검증합니다.

```bash
npm run build
```

## 주요 디렉터리

```text
src/
├── sources/       # 외부 수집 대상 계약, 구현체와 source factory
├── collection/    # 수집 오케스트레이션, collector strategy와 raw writer
├── processing/    # 중복 제거, 분류, 점수화, 요약
├── generator/     # Markdown 생성기
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
5. 브리핑 Markdown 생성
6. Docusaurus 빌드
7. GitHub Pages 배포

GitHub Actions에서 `OPENAI_API_KEY`는 repository secret으로 설정해야 합니다.

## 현재 한계

- LLM 기반 요약/중요도 평가는 아직 실제 구현 전입니다.
- 현재 요약, 분류, 점수는 MVP 휴리스틱입니다.
- `seen.json` 파일은 준비되어 있지만 영속 deduplication 로직은 아직 단순 URL 중복 제거 수준입니다.
- Docusaurus 보안 감사에서 Node 의존성 경고가 있을 수 있습니다. 필요 시 `npm audit` 기준으로 별도 처리합니다.
