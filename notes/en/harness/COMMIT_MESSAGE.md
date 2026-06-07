# COMMIT_MESSAGE

## Commit Message Style

Commit messages follow Conventional Commits, but the project standard for explanations is Korean. This English document mirrors the Korean rule document.

Default format:

```text
<type>(<scope>): <Korean summary>

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

Example:

```text
feat(service): Google Blog RSS 서비스 추가

- Google Blog 피드를 MVP 수집 대상에 포함하기 위한 서비스 구현체를 추가한다.

## 작업 내용
- Google Blog 서비스 클래스를 추가한다.
- 서비스 팩토리 registry에 google-blog 키를 등록한다.
- 서비스별 브리핑 생성 경로와 연결되는 service_key를 정의한다.

## 영향 받은 파일
- src/sources/implementations/google_blog.py
- src/sources/factory.py
- harness/ARCHITECTURE.md
```

## Type

- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation change
- `refactor`: structural improvement without behavior change
- `test`: test addition or update
- `chore`: build, configuration, dependency, or maintenance change
- `ci`: CI/CD change such as GitHub Actions

## Scope

Recommended scopes:

- `service`
- `processing`
- `generator`
- `models`
- `docs`
- `harness`
- `config`
- `ci`

## Summary Rules

- Write the summary in Korean.
- Do not end with a period.
- Keep it within 72 characters where possible.
- Be short and specific about what changed.

Good examples:

```text
feat(service): Anthropic Blog RSS 서비스 추가
fix(generator): 날짜별 요약 문서 링크 수정
docs(harness): 프로젝트 플로우 문서 추가
chore(config): Ruff 포맷팅 규칙 설정
```

Bad examples:

```text
fix: 수정
update: 이것저것 변경
feat(service): 작업함
```

## Body Rules

Use this structure for the commit body.

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

The body should explain why the change was made and what behavior or structure changed.

## Commit Splitting Rules

- During the early project phase, include feature changes and related documentation changes in the same commit.
- When adding features or changing structure, update affected documents among `README.md`, `AGENTS.md`, and `harness/`.
- Do not mix automatically generated briefing document changes with code changes.
- Separate configuration changes under `chore` or `ci` where appropriate.
- Do not mix large refactors with feature additions.
