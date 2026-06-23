# TECH_STACK

## Runtime

- Python 3.14
- Node.js 20

Python 버전은 `.python-version`과 GitHub Actions에서 동일하게 유지한다.

## Python Libraries

- `feedparser`: RSS/Atom 파싱
- `httpx`: HTTP 요청
- `trafilatura`: HTML 원문 본문과 metadata 구조 추출
- `tiktoken`: Agent 입력 정책을 위한 `o200k_base` token 계산
- `pydantic`: 데이터 모델 검증
- `openai`: LLM API 연동
- `jinja2`: Markdown 템플릿 렌더링 확장용
- `ruff`: Python lint/format

## Static Site

- Docusaurus
- React
- GitHub Pages

Docusaurus는 `docs/` 디렉터리를 문서 루트로 사용한다. 브리핑 Markdown은 Python 파이프라인이 생성하고, Docusaurus는 이를 정적 사이트로 빌드한다.

## Automation

- GitHub Actions
- Makefile

워크플로는 `.github/workflows/daily-briefing.yml`에 둔다.
로컬 실행, 규칙 검증, 빌드, GitHub Actions 수동 배포 트리거는 루트 `Makefile`에서 관리한다.

## Storage

- JSON 파일 기반 저장소
- `briefed_articles` 상태 파일로 이미 브리핑/발행된 원문 글을 추적한다.
- raw 수집 데이터는 로컬 `.var/` 또는 GitHub Actions artifact로만 보관한다.
- 운영 trace는 `tracing-history` 브랜치에 누적한다.

MVP에서는 별도 DB 서버, 검색엔진, Vector DB를 사용하지 않는다.

## Environment Variables

환경 변수 예시는 `.env.example`에 둔다. 변수별 의미, 기본값, 코드 사용 지점은 `harness/ENV.md`에서 관리한다.

주요 변수:

- `OPENAI_API_KEY`
- `OPENAI_MODEL`
- `TODAYINTECH_TIMEZONE`
- `TODAYINTECH_OUTPUT_DIR`
- `TODAYINTECH_RAW_OUTPUT_DIR`
- `TODAYINTECH_ENRICHED_OUTPUT_DIR`
- `TODAYINTECH_ENRICHMENT_CACHE_DIR`
- `TODAYINTECH_TRACE_OUTPUT_DIR`
- `TODAYINTECH_MAX_ARTICLES_PER_SERVICE`
- `TODAYINTECH_TARGET_DATE`
- `DOCUSAURUS_URL`
- `DOCUSAURUS_BASE_URL`
