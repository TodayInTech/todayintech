---
title: "Build once, run on any agent: A practical guide to agent skills"
sidebar_label: "Build once, run on any agent: A practical guide to agent skills"
description: "GitHub은 에이전트 업무를 재사용 가능한 'agent skill'로 구조화하는 실무 가이드를 공개했다. SKILL.md 중심의 버전 디렉터리, 프로젝트 매니페스트 분리, 독립 검증자(Proof Agent)와 CI 연동, 클라이언트별 패키징(node scripts/package.mjs 등)을 통한 이식성 확보가 핵심이다."
---

# Build once, run on any agent: A practical guide to agent skills

> GitHub Blog · 2026-11-12 · AI &amp; ML / Developer Tools

---

Andrea Griffiths가 GitHub 블로그에 올린 'Build once, run on any agent: A practical guide to agent skills'는 에이전트가 수행하는 반복적 엔지니어링 판단을 파일로 캡처해 팀에서 검토·재사용하도록 하는 실무 패턴을 제시한다. 핵심은 **SKILL.md 기반의 버전화된 지침 디렉터리**와 이를 보완하는 **프로젝트 매니페스트**다.

## SKILL.md와 버전화된 지침
GitHub는 에이전트 스킬을 SKILL.md를 중심으로 하는 버전 디렉터리로 정의한다. SKILL.md는 작업의 이름, 목적, 입력·출력, 그리고 언제 호출할지(When to Verify) 같은 실행 규칙을 담는다. 예시로 Proof Agent의 frontmatter는 다음과 같다:

--- name: proof-agent description: Adversarial verification of AI-generated work. Spawns an independent verifier to check for false claims, broken code, and security issues. ---

저자는 "자기검증은 검증이 아니다(self-verification is not verification)"라는 원칙을 강조하며, 검증자가 원본 요청과 코드 변경만 받아 내부 에이전트의 평가를 참조하지 않도록 설계해야 한다고 설명한다.

## 프로젝트 매니페스트로 환경 의존성 분리
실행 환경·프로젝트별 이름·엔진 선택 등은 스킬에 하드코딩하지 말고 매니페스트로 분리하라고 권한다. 예시 매니페스트:

project:
  name: "support-desk"
  store_name: "support_metric_store"
  platform:
    engine: "duckdb"
    pipeline_framework: "spark_python"
    duckdb_dir: "warehouse"

매니페스트는 어떤 엔진을 사용할지 선택할 뿐, DuckDB CLI 설치나 데이터베이스 접근 권한 부여 등은 호스트와 사용자 책임으로 남는다.

## 독립 검증자(Proof Agent)와 CI 연동
Proof Agent 데모는 검증자를 분리해 원본 요청과 변경된 코드만 주고받게 한다. 검증 결과는 PASS / FAIL / PARTIAL로 반환되며, GitHub Actions가 diff의 정적 검토만 수행하도록 데모를 구성했다. 워크플로우 설정 예시에서는

block-on-fail: false

로 데모에서는 실패를 권고로 처리하지만, 기본 동작은 FAIL이 체크 실패로 간주되어 병합을 차단할 수 있다. 저자는 테스트 결과와 병합 규칙을 리포지토리의 CI 검사와 규칙으로 관리하라고 권고한다.

## 클라이언트별 패키징과 설치 검증
여러 에이전트 클라이언트를 지원할 때는 스킬 원본(skills/*/SKILL.md)을 기반으로 클라이언트별 메타파일을 생성하는 패키징 단계가 필요하다. 예시 출력 파일들:

skills/*/SKILL.md
.claude-plugin/plugin.json
.cursor-plugin/plugin.json
.github/agents/*.agent.md

패키징 스크립트 예: node scripts/package.mjs --check

설치 후에는 각 클라이언트가 해당 스킬을 인식하는지, 참조 자료를 로드하는지, 필요한 도구와 권한을 사용할 수 있는지, 스킬이 요구하는 증거(evidence)를 반환하는지를 검증해야 한다고 명시한다.

## 실무적 의미
GitHub의 가이드는 에이전트 기반 자동화에서 '판단'을 어떻게 코드화할지에 대한 실용적 규칙을 제공한다. 중요한 제약으로는 스킬이 권한을 부여하지 않으며(데이터 접근·CLI 설치는 호스트 책임), 일부 검증은 정적 검토에 머문다는 점이 있다. 실무적으로는 반복 작업을 SKILL.md로 문서화해 재사용성을 높이고, 매니페스트로 환경 차이를 분리하며, 검증·승인 포인트와 CI 검사를 리포지토리 규칙으로 연계하는 방식이 실무 적용의 핵심이다.

원문은 GitHub Universe 2026 세션과 Data Forge·Proof Agent 데모를 예로 들며 구체적 파일 구조와 워크플로우 동작을 설명한다. 기사 본문에서 제시된 실습 요소(node scripts/package.mjs, manifest 예시, block-on-fail 설정 등)는 개발팀이 직접 따라해볼 수 있는 실행 단서로 활용할 수 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/)

