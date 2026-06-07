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
make quality
```

## 산출물

```text
reports/
└── junit.xml

data/traces/YYYY-MM-DD/
├── collection.json
└── summary.md
```

`reports/`와 `data/traces/`는 Git에 커밋하지 않는다. GitHub Actions에서는 artifact로 업로드한다.

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
