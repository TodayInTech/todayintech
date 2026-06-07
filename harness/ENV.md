# ENV

이 문서는 Today in Tech에서 사용하는 환경 변수를 추적한다.
환경 변수를 추가, 삭제, 이름 변경하면 `.env.example`, `src/settings.py`, 이 문서, `notes/en/harness/ENV.md`를 함께 업데이트한다.

## 관리 원칙

- 환경 변수 예시는 `.env.example`에 둔다.
- 런타임 코드는 `os.getenv()`를 직접 호출하지 않고 `src/settings.py`의 `SETTINGS` 싱글톤 객체를 사용한다.
- `SETTINGS = AppSettings.from_env()`는 import 시점에 환경 변수를 읽는다.
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
| `TODAYINTECH_TRACE_OUTPUT_DIR` | `.var/local/traces` | 선택 | `trace_output_dir` | 운영 트레이싱 JSON/Markdown 저장 루트 |
| `TODAYINTECH_MAX_ARTICLES_PER_SERVICE` | `5` | 선택 | `max_articles_per_service` | Markdown 생성 시 서비스별 요약 대상 최대 기사 수. 최소값은 1 |

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

- `src/main.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.max_articles_per_service`, `SETTINGS.output_dir`, `SETTINGS.raw_output_dir`
- `src/collection/__main__.py`: `SETTINGS.resolve_target_date()`, `SETTINGS.raw_output_dir`

## 추가 시 체크리스트

- [ ] `.env.example`에 구분 주석과 함께 변수 추가
- [ ] `src/settings.py`의 `AppSettings` 필드와 `from_env()`에 반영
- [ ] 이 문서의 변수 표 업데이트
- [ ] `notes/en/harness/ENV.md` 동시 업데이트
- [ ] 필요한 경우 README와 GitHub Actions secret 문서 업데이트
