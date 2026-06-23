# ENV

이 문서는 Today in Tech에서 사용하는 환경 변수를 추적한다.
환경 변수를 추가, 삭제, 이름 변경하면 `.env.example`, `src/settings.py`, 이 문서, `notes/en/harness/ENV.md`를 함께 업데이트한다.

## 관리 원칙

- 환경 변수 예시는 `.env.example`에 둔다.
- 런타임 코드는 `os.getenv()`를 직접 호출하지 않고 `src/settings.py`의 `SETTINGS` 싱글톤 객체를 사용한다.
- `SETTINGS = AppSettings.from_env()`는 import 시점에 루트 `.env`를 먼저 로드한 뒤 환경 변수를 읽는다.
- shell에 이미 설정된 환경 변수는 `.env` 값으로 덮어쓰지 않는다.
- 비어 있는 문자열은 선택 값에서 `None`으로 취급한다.
- 숫자 환경 변수는 `SETTINGS`에서 파싱하고 fallback 기본값을 제공한다.

## OpenAI / LLM 설정

| 변수 | 기본값 | 필수 여부 | SETTINGS 필드 | 설명 |
| --- | --- | --- | --- | --- |
| `OPENAI_API_KEY` | 없음 | LLM 기능 사용 시 필수 | `openai_api_key` | 중요도 평가, 요약, 인사이트 생성에 사용할 OpenAI API 키 |
| `OPENAI_MODEL` | `gpt-5-mini` | 선택 | `openai_model` | LLM Agent가 사용할 모델명 |

## Pipeline 설정

| 변수 | 기본값 | 필수 여부 | SETTINGS 필드 | 설명 |
| --- | --- | --- | --- | --- |
| `TODAYINTECH_TIMEZONE` | `Asia/Seoul` | 선택 | `timezone` | 브리핑 기준 시간대 |
| `TODAYINTECH_OUTPUT_DIR` | `docs` | 선택 | `output_dir` | 생성된 Markdown 브리핑 저장 루트 |
| `TODAYINTECH_RAW_OUTPUT_DIR` | `.var/local/raw` | 선택 | `raw_output_dir` | collector raw JSON 저장 루트 |
| `TODAYINTECH_PROCESSED_OUTPUT_DIR` | `.var/local/processed` | 선택 | `processed_output_dir` | preprocessor 후보 JSON 저장 루트 |
| `TODAYINTECH_ENRICHED_OUTPUT_DIR` | `.var/local/enriched` | 선택 | `enriched_output_dir` | enrichment 결과 JSON 저장 루트 |
| `TODAYINTECH_ENRICHMENT_CACHE_DIR` | `.var/local/enrichment-cache` | 선택 | `enrichment_cache_dir` | URL·extractor·chunker·policy 설정 기반 enrichment JSON 캐시 루트 |
| `TODAYINTECH_TRACE_OUTPUT_DIR` | `.var/local/traces` | 선택 | `trace_output_dir` | 운영 트레이싱 JSON/Markdown 저장 루트 |
| `TODAYINTECH_BRIEFED_ARTICLES_PATH` | `data/briefed_articles.json` | 선택 | `briefed_articles_path` | 이미 브리핑/발행된 원문 글 상태 파일 경로 |
| `TODAYINTECH_WRITER_AGENT` | `draft` | 선택 | `writer_agent` | Writer Agent 구현 선택. `draft` 또는 `openai`. `openai` 사용 시 `OPENAI_API_KEY` 필요 |
| `TODAYINTECH_MAX_ARTICLES_PER_SERVICE` | `5` | 선택 | `max_articles_per_service` | legacy Markdown scaffold용 서비스별 최대 기사 수. 현재 Writer 경로에서는 사용하지 않는다 |
| `TODAYINTECH_MAX_CANDIDATES_PER_SERVICE` | `10` | 선택 | `max_candidates_per_service` | preprocessor가 Agent 입력 후보로 남길 서비스별 최대 글 수. 최소값은 1 |
| `TODAYINTECH_MAX_CANDIDATES_TOTAL` | `50` | 선택 | `max_candidates_total` | preprocessor가 Agent 입력 후보로 남길 전체 최대 글 수. 최소값은 1 |
| `TODAYINTECH_ENRICHMENT_TIMEOUT_SECONDS` | `20` | 선택 | `enrichment_timeout_seconds` | 원문 HTTP 요청 timeout 초 |
| `TODAYINTECH_ENRICHMENT_MAX_ATTEMPTS` | `2` | 선택 | `enrichment_max_attempts` | timeout·네트워크 오류 원문 요청 최대 시도 횟수 |
| `TODAYINTECH_ENRICHMENT_MINIMUM_TOKENS` | `100` | 선택 | `enrichment_minimum_tokens` | 유효한 추출 본문으로 인정할 최소 token 수 |
| `TODAYINTECH_ENRICHMENT_FULL_CONTENT_MAX_TOKENS` | `4000` | 선택 | `enrichment_full_content_max_tokens` | 전체 본문을 Agent 입력으로 사용할 최대 token 수 |
| `TODAYINTECH_ENRICHMENT_CHUNK_SELECTION_MAX_TOKENS` | `8000` | 선택 | `enrichment_chunk_selection_max_tokens` | chunk selection과 evidence selection을 나누는 token 기준 |
| `TODAYINTECH_ENRICHMENT_CHUNK_MAX_TOKENS` | `1200` | 선택 | `enrichment_chunk_max_tokens` | 구조 보존 chunk 하나의 목표 최대 token 수 |
| `TODAYINTECH_ENRICHMENT_SELECTED_CHUNKS_MAX_TOKENS` | `4000` | 선택 | `enrichment_selected_chunks_max_tokens` | 긴 글에서 Writer에 전달할 선택 chunk의 최대 token 수 |

## Local 재현성 설정

| 변수 | 기본값 | 필수 여부 | SETTINGS 필드 | 설명 |
| --- | --- | --- | --- | --- |
| `TODAYINTECH_TARGET_DATE` | 오늘 날짜 | 선택 | `target_date` | 로컬 재현 실행 또는 특정 날짜 산출물 생성을 위한 `YYYY-MM-DD` 값 |

## Docusaurus / GitHub Pages 설정

| 변수 | 기본값 | 필수 여부 | SETTINGS 필드 | 설명 |
| --- | --- | --- | --- | --- |
| `DOCUSAURUS_URL` | `https://example.com` | 배포 시 필요 | `docusaurus_url` | Docusaurus 사이트 URL |
| `DOCUSAURUS_BASE_URL` | `/` | 배포 시 필요 | `docusaurus_base_url` | GitHub Pages 하위 경로 배포용 base URL |

## 현재 코드 사용 지점

- `src/main.py`: Collector, Preprocessor, Enrichment, Writer의 입출력 경로와 enrichment 정책 설정
- `src/collection/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`
- `src/processing/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`, `SETTINGS.processed_output_dir`, `SETTINGS.briefed_articles_path`, `SETTINGS.max_candidates_per_service`, `SETTINGS.max_candidates_total`
- `src/enrichment/__main__.py`: enrichment 출력·캐시 경로, HTTP 요청, token budget, chunk 크기 설정
- `src/writer/__main__.py`: `SETTINGS.resolve_target_date()`, Writer Agent 설정, `SETTINGS.enriched_output_dir`, `SETTINGS.output_dir`, `SETTINGS.briefed_articles_path`

## 추가 시 체크리스트

- [ ] `.env.example`에 구분 주석과 함께 변수 추가
- [ ] `src/settings.py`의 `AppSettings` 필드와 `from_env()`에 반영
- [ ] 이 문서의 변수 표 업데이트
- [ ] `notes/en/harness/ENV.md` 동시 업데이트
- [ ] 필요한 경우 README와 GitHub Actions secret 문서 업데이트
