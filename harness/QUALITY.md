# QUALITY

이 문서는 Today in Tech의 개발 검증과 운영 트레이싱 플로우를 정의한다.

## 개념 구분

- `test`: 코드가 의도대로 동작하는지 fixture와 contract로 검증한다.
- `trace`: 실제 운영 collector 실행 결과와 실행 시간을 기록한다.
- `quality`: `test`와 `trace`를 함께 실행해 배포 전 판단 근거를 만든다.

## Make 명령

```bash
make test
make test-unit
make test-collection
make trace-collect
make fetch-trace-history
make quality
```

## 산출물

```text
.var/local/reports/
└── junit.xml

.var/local/traces/YYYY-MM-DD/
├── collection.json
└── summary.md
```

`.var/local/reports/`와 `.var/local/traces/`는 Git에 커밋하지 않는다. GitHub Actions에서는 artifact로 업로드한다.

GitHub Actions 산출물은 로컬 산출물과 분리해서 `.artifacts/` 아래에 둔다.

```text
.artifacts/
├── raw/
├── reports/
└── traces/
```

## 트레이싱 히스토리

운영 trace는 `main` 브랜치에 커밋하지 않는다. GitHub Actions는 collector trace 실행 후 `tracing-history` 전용 브랜치에 trace 결과만 날짜별로 누적한다.

```text
tracing-history
└── traces/
    └── YYYY-MM-DD/
        ├── collection.json
        └── summary.md
```

원칙:

- `main`은 코드, 설정, 사람이 관리하는 문서만 포함한다.
- `tracing-history`는 운영 trace 장기 보관용 브랜치이다.
- raw 수집 데이터와 test report는 GitHub Actions artifact로만 보관한다.
- 같은 날짜로 workflow를 재실행하면 해당 날짜 trace 파일을 갱신하고 변경이 있을 때만 커밋한다.

로컬에서 누적 trace 데이터를 확인하려면 다음 명령을 사용한다.

```bash
make fetch-trace-history
```

기본 checkout 위치는 `.var/remote/tracing-history`이다.

## 현재 추적 지표

- 전체 collection stage 상태
- 전체 collection duration
- 서비스별 status
- 서비스별 collector strategy
- 서비스별 article count
- 서비스별 duration
- article 1개당 평균 duration
- warning code
- error message

## 운영 기준

- fixture 기반 `make test`는 안정적인 개발 검증 용도이다.
- `make trace-collect`는 실제 외부 source를 호출하므로 운영 트레이싱 용도이다.
- 외부 네트워크 영향이 있으므로 trace duration은 강한 pass/fail 조건으로 사용하지 않는다.
- 서비스별 article count가 0이면 `empty_collection` warning을 기록한다.
