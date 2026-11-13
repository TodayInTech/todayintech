---
title: "Introducing Claude 4"
sidebar_label: "Introducing Claude 4"
description: "Anthropic이 Claude Opus 4와 Claude Sonnet 4를 발표했다. 두 모델은 '확장적 사고(extended thinking)'와 병렬 도구 사용, 로컬 파일 기반 메모리 기능을 지원하며 Claude Code의 IDE 통합과 API용 코드 실행 도구·Files API 등 새로운 개발자 기능을 함께 공개했다."
---

# Introducing Claude 4

> Anthropic Blog · 2026-11-12 · AI 모델 출시

---

Anthropic이 Claude 4 세대를 공개하며 **Claude Opus 4**와 **Claude Sonnet 4**를 동시에 내놨다. 회사는 Opus 4를 “세계 최고 수준의 코딩 모델”로 규정하면서 장시간·수천 단계가 필요한 작업에서의 지속적 성능과 에이전트 워크플로 강화를 핵심 개선점으로 제시한다. Sonnet 4는 Sonnet 3.7 대비 지시 준수와 코딩·추론 능력이 향상된 실무형 모델로 설명된다.

## 확장적 사고와 도구 사용

두 모델은 베타로 제공되는 **확장적 사고(extended thinking)에서 도구 사용**을 지원한다. 모델은 추론과 도구 호출을 번갈아가며 사용할 수 있고, 도구를 병렬로 실행하는 기능도 공개됐다. Anthropic은 확장적 사고를 64K 토큰까지 활용한 벤치마크 결과를 일부 제시했으며, 벤치마크 결과는 확장적 사고 사용 여부를 구분해 보고했다.

## 메모리·요약·안전성

로컬 파일 접근을 허용하는 애플리케이션에서는 Opus 4가 **'메모리 파일'**을 생성·유지해 장기적 과제 인식과 일관성을 높인다고 밝혔다. 또한 긴 내부 추론을 축약해 보여주는 **thinking summaries**를 도입했으며, 필요한 경우 원시 사고 사슬(chain of thought)을 유지하는 Developer Mode도 별도 제공한다고 명시했다. 보안·안전 측면에서 Anthropic은 ASL-3 수준 등급을 포함한 테스트를 도입했고, 모델이 과도한 지름길(shortcuts)·루프홀을 이용하는 행동은 Sonnet 3.7 대비 **65% 감소**했다고 보고했다.

## 코드 워크플로 통합 — Claude Code 일반 제공

Claude Code가 일반 이용 가능(GA)으로 전환되며 IDE 통합(새로운 VS Code·JetBrains 확장 베타), GitHub Actions를 통한 백그라운드 작업 지원, VS Code·JetBrains 내 인라인 편집 제안 등 실무적 협업 기능을 확장했다. 또한 Claude Code SDK와 GitHub용 예제(베타)를 공개해 PR 태깅, CI 오류 수정 등의 자동화가 가능하다. 설치 명령 예시로 /install-github-app가 문서에 포함되어 있다.

## API·가격·가용성

새로운 API 기능으로는 **코드 실행 도구, MCP 커넥터, Files API, 프롬프트 1시간 캐시** 등이 추가됐다. 모델은 API, Amazon Bedrock, Google Cloud Vertex AI에서 제공되며 요금은 **Opus 4 $15/$75**(백만 토큰 입력/출력 기준), **Sonnet 4 $3/$15**로 이전 모델과 동일한 가격 구조를 유지한다고 명시되어 있다. Pro·Max·Team·Enterprise 요금제에는 두 모델과 확장적 사고가 포함되며 Sonnet 4는 무료 사용자도 이용 가능하다.

## 성능·벤치마크와 비교 지점

Anthropic은 SWE-bench(예: Opus 4 72.5%), Terminal-bench(Opus 4 43.2%), Sonnet 4의 SWE-bench 72.7% 등 구체 수치를 공개했다. 또한 고성능 설정에서의 점수(고컴퓨트·병렬 시도·내부 스코어러 사용)를 별도로 보고해 Opus 4·Sonnet 4의 수치는 **79.4%·80.2%**로 제시된다. 블로그는 일부 벤치마크에서 확장적 사고 사용 여부를 구분해 보고했으므로 결과 해석 시 사용 모드와 고컴퓨트 절차의 차이를 고려해야 한다는 사실을 명시한다.

실무적 의미는 분명하다. Opus 4는 장시간 연속 작업, 복잡한 리팩터링, 다파일 변경을 필요로 하는 에이전트형 제품에 초점을 맞추며 Sonnet 4는 더 가벼운 실무·인터랙티브 사용에서 성능·비용 균형을 제공한다. Anthropic의 설명과 벤치마크는 확장적 사고·병렬 도구 호출·로컬 파일 기반 메모리 같은 새로운 운영 매커니즘이 모델의 장기 과제 수행 능력을 끌어올렸다고 주장한다(근거: Anthropic 블로그).

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/claude-4)

