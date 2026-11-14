---
title: "Introducing Claude 3.5 Sonnet"
sidebar_label: "Introducing Claude 3.5 Sonnet"
description: "Anthropic은 **Claude 3.5 Sonnet**을 공개했다. Claude 3 Opus 대비 2배 속도, 200K 토큰 컨텍스트, 입력 $3/백만·출력 $15/백만 토큰 가격으로 Claude.ai·iOS·API·Bedrock·Vertex AI에서 이용 가능하다."
---

# Introducing Claude 3.5 Sonnet

> Anthropic Blog · 2026-11-13 · AI 모델 발표

---

Anthropic은 새로운 Claude 3.5 계열의 첫 버전인 **Claude 3.5 Sonnet**을 발표했다. 이번 릴리스는 성능과 처리 속도, 적용 편의성을 동시에 끌어올린 점을 핵심 혁신으로 내세운다.

## 성능·속도·가격·가용성
Anthropic에 따르면 Claude 3.5 Sonnet은 여러 표준 평가에서 기존 모델과 경쟁사 모델을 능가하며, 특히 대학원 수준 추론(GPQA), 학부 수준 지식(MMLU), 코딩(HumanEval)에서 개선을 보였다. **Claude 3 Opus 대비 2배 속도**를 제공하며, **컨텍스트 윈도우는 200K 토큰**이다. 가격은 **입력 $3/백만 토큰, 출력 $15/백만 토큰**으로 제시됐다. Sonnet은 Claude.ai와 Claude iOS 앱에서 무료로 사용 가능하며, Claude Pro·Team 구독자는 더 높은 레이트 리밋으로 접근할 수 있다. 개발자·기업용 경로로는 Anthropic API, Amazon Bedrock, Google Cloud Vertex AI를 통해서도 이용할 수 있다 (출처: Anthropic).

## 코드 능력과 실무적 영향
내부 에이전틱 코딩 평가에서 Sonnet은 **문제 64% 해결**, Claude 3 Opus는 **38% 해결**로 보고됐다. 이 평가는 자연어로 주어진 개선 요구를 바탕으로 오픈소스 코드베이스에 버그 수정이나 기능 추가를 수행하는 능력을 테스트한 것이며, Sonnet은 주어진 도구와 지시 하에 코드를 작성·수정·실행해 문제를 해결하는 역량이 향상되었다고 Anthropic은 설명한다. 이 성능은 레거시 애플리케이션 업데이트, 코드베이스 마이그레이션, 컨텍스트 민감한 고객지원과 다단계 워크플로 오케스트레이션 같은 실무 영역에서 즉시 활용 가능성이 있다(출처: Anthropic).

## 비전 기능과 Artifacts 워크스페이스
Sonnet은 시각적 추론 능력에서도 개선을 보였고, 특히 차트·그래프 해석 같은 작업과 불완전한 이미지의 텍스트 전사에서 우수하다고 Anthropic은 밝혔다. 또한 Claude.ai에 **Artifacts**라는 새 기능을 추가해 코드 스니펫·문서·웹 디자인 등 생성 결과물을 대화창 옆 별도 창에 표시하고 실시간 편집·구축할 수 있는 작업 공간을 제공한다. Anthropic은 이를 대화형 AI에서 협업형 작업 환경으로의 진화 초석으로 설명하며, 향후 팀·조직 단위의 중앙화된 지식·문서 관리 기능으로 확장할 예정이라고 밝혔다 (출처: Anthropic).

## 안전·프라이버시·외부 평가
Anthropic은 Sonnet이 내부 레드팀 평가 결과 **ASL-2** 수준을 유지한다고 보고했으며, 외부 전문가 의견을 모델 평가에 반영했다고 명시했다. 구체적으로 영국 AI 안전 연구기관(UK AISI)에 Sonnet을 사전배포해 평가를 받았고, 그 결과를 미국 AI 안전 연구기관(US AISI)과 공유했다고 밝혔다. 또한 아동 안전 전문단체인 Thorn의 피드백을 반영해 분류기와 미세조정에 반영했다고 명시되어 있다. Anthropic은 사용자 제출 데이터는 명시적 허가가 있을 때만 학습에 사용한다고 밝혔다 (출처: Anthropic).

## 여파와 남은 관측점
Sonnet은 높은 컨텍스트 용량과 개선된 문제 해결 능력, 빠른 응답 속도를 결합해 대화형 AI의 실무 적용 범위를 넓힐 가능성이 있다. 다만 공개 근거는 Anthropic의 평가와 외부 협업 사실을 제시하고 있으나, 독립적·장기적 운영 환경에서의 비용-성능 검증이나 대규모 배포 시의 통합 상세(레이트 리밋 수준, 엔터프라이즈 통합 사례 등)는 근거에 포함되어 있지 않다. Anthropic은 올해 Claude 3.5 Haiku와 Claude 3.5 Opus를 추가로 출시할 예정이며, 개인화 기억 기능(Memory) 등 기업용 기능을 연구 중이라고 밝혔다 (출처: Anthropic).

(근거: Anthropic 블로그 발표 본문 — chunk-0001)

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/claude-3-5-sonnet)

