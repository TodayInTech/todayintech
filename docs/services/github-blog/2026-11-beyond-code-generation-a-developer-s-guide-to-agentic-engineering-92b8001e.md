---
title: "Beyond code generation: A developer’s guide to agentic engineering"
sidebar_label: "Beyond code generation: A developer’s guide to agentic engineering"
description: "GitHub은 Copilot을 중심으로 계획(Plan)·구현(Build)·검증(Verify)·관찰(Observe)을 잇는 'agentic engineering' 워크플로를 제시하며, **1주간 12억+ 커밋(전년 대비 400% 증가)**과 PR 검토 지연(441% 증가)을 근거로 세션 지속성, 클라우드 실행, 자동 코드·보안 검사, Agent Merge 등 실무 기능을 소개했다."
---

# Beyond code generation: A developer’s guide to agentic engineering

> GitHub Blog · 2026-11-06 · AI &amp; Developer Tools

---

GitHub은 개발자의 작업 흐름 전체를 에이전트가 보조하는 'agentic engineering'으로 재구성하는 방법을 제안한다. 원문은 증가한 코드 생성량(“**이번 10월, GitHub은 1주간 12억 건이 넘는 커밋—전년 대비 400% 이상**”)과, AI 도입이 늘어날 때 발생하는 검토 병목(“Faros AI 연구: 검토 대기 시간이 **441%** 증가”)을 근거로, Plan·Build·Verify·Observe 네 단계에서 Copilot과 연계된 구체적 도구·패턴을 설명한다 (원문 근거: chunk-0001, chunk-0002).

## Plan: 흩어진 맥락을 한 곳으로

GitHub은 Copilot을 Slack·Teams 등 협업 공간과 연결해 설계·요구사항·기존 PR 근거를 한데 모으고, 합의된 요구사항을 GitHub 이슈로 전환하도록 권한다. 또한 GitHub Agentic Workflows로 이슈 라벨링·복잡도 추정 등을 자동화해 반복적 트리아지를 줄이고, Plan Mode에서 접근법을 비교해 검토·승인한 뒤 에이전트에게 구현을 넘길 것을 권장한다 (chunk-0001).

## Build: 세션 지속성과 클라우드 실행

Copilot은 세션 연속성으로 여러 기기에서 같은 작업을 이어갈 수 있고, 클라우드 샌드박스에서 작업을 실행해 로컬 환경에 부담을 주지 않는다. 작업별로 격리된 리포지토리 복사본을 제공해 서로 다른 작업의 편집이 섞이지 않게 하며, 저장된 리포지토리 지침과 공유 메모리(Shared memory)를 통해 팀 규약과 반복 지식을 유지한다. Copilot Fusion을 통해 모델과 추론 수준을 선택해 품질·비용·응답시간 균형을 조절할 수 있고, Enterprise 관리 설정은 회사 정책을 일관되게 적용한다 (chunk-0001).

## Verify: 사람의 주의를 절약하는 자동화

대형 단일 PR이 검토 병목을 악화한다는 지적을 바탕으로, GitHub은 **작고 집중된 PR(스택 PR)** 전략을 권장한다. 또한 GitHub Code Quality로 조직 규칙을 사전점검하고, Copilot 코드 리뷰는 변경 규모에 맞춰 자동 피드백을 제공한다. 보안·비밀 검출 측면에서는 AI Scan과 AI secret detection이 CodeQL의 범위를 넘는 언어·파일을 검사하고, 라이선스 준수 검사와 함께 npm에 대해 공개 프리뷰인 GitHub package firewall로 정책 위반 다운로드를 차단할 수 있다. Agentic Autofix와 Agent Merge는 보안 이슈 수리·실패한 체크·머지 충돌을 자동으로 처리하고, 설정 시 검증이 통과하면 PR을 자동 병합할 수 있다 (chunk-0002).

## Observe: 배포 후 증거를 합치기

관찰 단계에서는 Fabric 등 커넥터를 통해 운영 지표와 비즈니스 데이터를 연동해 어느 요청·고객군이 영향을 받는지 조사하도록 제안한다. 조사 결과는 Copilot에게 이슈 초안과 회귀 테스트 기준으로 남기게 하고, Copilot Dreaming은 세션·리포지토리 활동을 사용해 메모리·스킬·검토 가이드를 개선하도록 돕는다 (chunk-0002).

## 실무적 의미와 적용 포인트

원문은 사람의 판단이 여전히 필요하다고 전제하면서도, **반복적 검색·트리아지·형식적 검사·충돌 해결 같은 작업을 에이전트가 맡기** 쉬운 영역으로 규정한다. 기술적으로는 세션 격리·클라우드 실행·공유 메모리·모델 선택 같은 메커니즘이 협업과 일관성 향상에 직접 연결된다. 보안·라이선스 정책은 AI 검사와 패키지 방화벽으로 보완되지만, 공개 프리뷰 상태(예: npm 대상 패키지 방화벽)임을 근거로 도입 범위와 정책 적용은 검증이 필요하다 (chunk-0002).

시작 방법으로는 이미 진행 중인 작업 한 건을 선택해 에이전트에 맡겨보고, 점진적으로 워크플로 전반으로 확대할 것을 권한다. GitHub Universe 2026에서의 라이브 세션('Agentic Engineering: Past the Pilot')도 같은 맥락에서 다뤄졌다 (chunk-0002).

(근거: GitHub Blog 게시글, chunk-0001·chunk-0002)

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/)

