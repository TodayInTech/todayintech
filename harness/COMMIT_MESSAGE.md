# COMMIT_MESSAGE

## 커밋 메시지 스타일

커밋 메시지는 Conventional Commits 스타일을 따르되, 설명 문장은 한국어로 작성한다.

기본 형식:

```text
<type>(<scope>): <한국어 요약>

- 작업 개요

## 작업 내용
- 
- 
- 

## 영향 받은 파일
- 
- 
- 
```

예시:

```text
feat(service): Google Blog RSS 서비스 추가

- Google Blog 피드를 MVP 수집 대상에 포함하기 위한 서비스 구현체를 추가한다.

## 작업 내용
- Google Blog 서비스 클래스를 추가한다.
- 서비스 팩토리 registry에 google-blog 키를 등록한다.
- 서비스별 브리핑 생성 경로와 연결되는 service_key를 정의한다.

## 영향 받은 파일
- src/services/google_blog.py
- src/services/factory.py
- harness/ARCHITECTURE.md
```

## Type

- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 변경
- `refactor`: 동작 변경 없는 구조 개선
- `test`: 테스트 추가 또는 수정
- `chore`: 빌드, 설정, 의존성, 기타 유지보수
- `ci`: GitHub Actions 등 CI/CD 변경

## Scope

권장 scope:

- `service`
- `processing`
- `generator`
- `models`
- `docs`
- `harness`
- `config`
- `ci`

## Summary 규칙

- 한국어로 작성한다.
- 마침표를 붙이지 않는다.
- 72자 이내를 권장한다.
- 무엇을 했는지 짧고 구체적으로 쓴다.

좋은 예:

```text
feat(service): Anthropic Blog RSS 서비스 추가
fix(generator): 날짜별 요약 문서 링크 수정
docs(harness): 프로젝트 플로우 문서 추가
chore(config): Ruff 포맷팅 규칙 설정
```

피해야 할 예:

```text
fix: 수정
update: 이것저것 변경
feat(service): 작업함
```

## 본문 작성 규칙

커밋 본문은 아래 구조를 사용한다.

```text
- 작업 개요

## 작업 내용
- 변경한 구현 또는 문서 내용을 항목으로 작성
- 하나의 항목에는 하나의 변경 사항만 작성
- 자동 생성 산출물이 포함되면 명시

## 영향 받은 파일
- 변경된 주요 파일 경로
- 생성된 주요 파일 경로
- 설정 또는 워크플로 파일 경로
```

본문은 변경 이유와 영향 범위를 빠르게 파악하기 위한 문서다. 단순히 파일 목록만 반복하지 말고, 왜 변경했는지와 어떤 동작이 달라졌는지를 적는다.

## 커밋 분리 원칙

- 프로젝트 초기 단계에서는 기능 변경과 관련 문서 변경을 같은 커밋에 포함한다.
- 기능을 추가하거나 구조를 바꾸면 `README.md`, `AGENTS.md`, `harness/` 문서 중 영향 받는 문서를 함께 갱신한다.
- 자동 생성 브리핑 문서 변경은 코드 변경과 섞지 않는다.
- 설정 변경은 `chore` 또는 `ci`로 분리한다.
- 대규모 리팩터링은 기능 추가와 같은 커밋에 넣지 않는다.
