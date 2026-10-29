# 원문 근거 확보와 재확인

## 처리 흐름

```text
후보 원문 URL
  → 원본 다운로드 URL 해석 (GitHub PDF 뷰어 → raw 파일)
  → HTTP 요청 (요청당 다운로드 20 MiB 제한)
  → 일시적 네트워크/5xx/429 재시도
  → OpenAI /index 경로의 403/404는 공식 trailing-slash 경로로 재확인
  → HTML: precision 추출 → 비어 있거나 최소 토큰 미달이면 balanced 보완 추출
  → PDF: 텍스트 추출 → 페이지 단위 근거 블록
  → 기존 제목·최소 토큰·근거 선택 검증
  → Writer
```

재시도는 기존 `enrichment_max_attempts` 예산 안에서 수행한다. 401은 재시도하지 않는다. 429/5xx는 Retry-After가 숫자이고 0~5초이면 기다린 후 재시도하며, 긴 값이나 HTTP 날짜이면 즉시 재요청하지 않는다. 헤더가 없으면 1초를 기다린다. 공식 경로 재확인은 프록시나 인증·챌린지 우회가 아니다. 공식 경로에서도 403이면 `access_denied`로 남긴다.

HTML 보완 추출은 같은 응답의 실제 텍스트만 사용한다. 기존 precision 결과가 충분하면 그대로 유지하고, 결과가 짧거나 추출에 실패할 때만 balanced 결과를 비교한다. 제목 유사도와 기존 최소 토큰 정책은 낮추지 않는다. 챌린지·로그인 제목은 근거로 사용하지 않는다. `extraction_method`는 `precision`, `balanced_retry`, `pdf_text`로 기록한다. 변경된 추출기 버전은 기존 캐시와 분리한다.

PDF는 바이너리 시그니처를 검사하고 pypdf로 텍스트를 추출한다. 암호화 문서·100페이지 초과 문서·10 MiB 초과 페이지 content stream은 거절한다. 스캔 PDF에 OCR을 적용하거나 수식/표를 완전 복원하지 않는다. 근거 선택 단계의 기존 입력 예산을 그대로 적용한다. 원문 URL은 원래 출처를 유지하고 실제 다운로드 URL은 `final_url`에 기록한다.

## 지속되는 재확인 대기열

`data/evidence_requests.json`은 briefed state와 같은 디렉터리에 저장한다. 자동화가 생성한 메타데이터이며 원문 본문·PDF 바이너리·근거 chunk를 포함하지 않는다.

- `pending`: 원문 확보 실패 또는 피드 정보만 확보. 최초 재확인은 하루 뒤다.
- `ready`: 원문 근거를 확보했다. 이미 발행한 URL은 재생성하지 않는다.
- `reviewed`: 확보한 근거를 Writer가 게시·초안·게시 제외로 판단했다.
- `exhausted`: 대기열 재확인이 7회 실패했다. 수동 검토 대상이다.

전체 파이프라인은 현재 후보의 원문을 처리하고, 별도 대기열에서 기한이 지난 최대 5건을 추가 확인한다. 현재 후보 URL은 같은 실행에서 두 번 요청하지 않는다. 대기열 재확인 간격은 2, 4, 7, 7…일로 증가한다. 정상 후보 처리의 횟수 제한과는 별개다. 후보 수 제한 때문에 다음날 목록에서 빠지거나 피드에서 사라진 글도 대기열에서 재확인한다. 일반적인 후보 제한 제외 건을 모두 대기열에 넣지는 않는다.

복구한 글은 URL·서비스 내 제목·기존 문서 파일을 다시 검사한다. 아직 생성하지 않은 글만 Writer 입력에 합친다. 이미 발행/초안인 글은 원문 확보 상태만 갱신한다. Writer의 명시적인 게시 제외는 반복 생성하지 않으며, API 오류 등 실패는 다음 실행에서 다시 검토할 수 있다. 기존 공개 글을 자동으로 덮어쓰지 않는다.

전체 파이프라인은 대기열을 GitHub Actions에서 함께 커밋한다. 재확인 원문은 `.artifacts/enriched/{date}/recovery/` artifact에만 저장하고, `traces/{date}/evidence-recovery.json`에는 건수와 요청·추출 지표만 남긴다. 이미 생성된 글을 재확인하더라도 새 문서나 새 URL을 만들지 않는다.

이전 실행의 실패를 가져와 원문만 다시 확인할 수 있다.

```bash
.venv/bin/python -m src.enrichment.recovery \
  --seed .var/local/enriched/2026-10-27/enrichment.json \
  --retry-now
```

이 명령은 최대 5건을 확인하고 `.var/local/recovered/{date}/enrichment.json`을 생성한다. Agent 실행이나 공개 문서 수정은 수행하지 않는다. 기본 대기열은 briefed state 디렉터리의 `evidence_requests.json`이며 `--queue`로 격리할 수 있다. `--retry-now`는 pending 항목만 즉시 확인 대상으로 바꾸고 exhausted 항목을 되살리지 않는다.

## 2026-10-29 실제 재확인

2026-10-27 운영 artifact에서 문제 글 4건을 골라 변경된 기본 Enricher로 검사했다. 원문 접근 결과는 시점과 실행 환경에 따라 달라질 수 있다.

| 글 | 이전 문제 | 개선 후 실제 결과 |
| --- | --- | --- |
| Decisions API | 403 또는 데모 문구 62토큰 | 공식 `/` 경로 HTTP 200, balanced 본문 1,116토큰, `full_content` |
| Exponential Time Hypothesis 논문 | GitHub HTML 뷰어의 세션 문구 45토큰 | raw PDF HTTP 200, 63,222토큰 추출 후 `evidence_selection`으로 제한 |
| CodeRabbit 보안 사례 | HTTP 403 | 현재도 403, 피드 fallback 및 재확인 대기 |
| What FDE means at OpenAI | HTTP 403, 피드 49자로 fallback 불가 | 현재도 403, failed 및 재확인 대기 |

재현 산출물은 로컬 `.var/local/evidence-recovery/probe/enrichment.json`에 있다. 기존 글의 재생성이나 LLM 호출은 하지 않았다. 성공한 HTTP 추출은 GitHub Actions에서도 항상 성공한다는 보장이 아니며, 남은 접근 거부는 운영 대기열과 지표로 확인해야 한다.
