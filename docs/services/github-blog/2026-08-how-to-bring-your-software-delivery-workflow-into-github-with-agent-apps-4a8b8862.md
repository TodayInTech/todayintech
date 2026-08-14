---
title: "How to bring your software delivery workflow into GitHub with agent apps"
sidebar_label: "How to bring your software delivery workflow into GitHub with agent apps"
---

# How to bring your software delivery workflow into GitHub with agent apps

> GitHub Blog · 2026-08-14 · Developer Tools / Software Delivery

---

GitHub 블로그 글은 에이전트 앱을 통해 소프트웨어 전달 워크플로를 GitHub 안으로 직접 가져오는 방법을 실무 사례로 풀어냅니다. 글은 온보딩 흐름에서 '팀 초대' 단계를 수정하는 예를 따라 네 단계—사전 검증, 개발 중 점검, 점진적 롤아웃, 배포 전 위험평가—로 나눠 설명합니다. 사전 검증 단계에서는 GitHub의 Agents 탭이나 PR 코멘트에서 @amplitude 에이전트를 호출해 세그먼트별로 해당 단계가 유의미한지 쿼리하고, 결과에 따라 솔로 사용자엔 단계를 유예하고 팀에는 유지하는 리스코핑을 결정합니다. 개발 단계에서는 Endor Labs 에이전트가 PR에서 변경된 의존성을 식별해 알려진 취약점과 패키지 위험을 검사하고, 문제가 없으면 '청정' 리포트를 남겨 CI 실패 후 대처 대신 사전 확인을 가능하게 합니다.
롤아웃 과정에서는 LaunchDarkly 에이전트에 의해 기능 플래그가 생성되고 코드 커밋이나 승인 요청이 PR에 추가되어 수동 코드 전달과 별도의 도구 이동 없이 롤아웃 설정이 이루어집니다. 배포 전에는 PagerDuty 에이전트가 레포지토리와 서비스 매핑, 활성 인시던트 및 과거 90일 이력 비교, PR 파일과 과거 인시던트 연관성 분석을 수행해 위험을 평가합니다. 글은 에이전트 앱이 동일 플랫폼(Copilot 클라우드 에이전트와 같은 기반) 위에서 동작해 컨텍스트 전환을 줄이고, 검증을 코드와 PR 흐름 안으로 앞당기며 인간의 최종 판단(승인)은 유지한다고 정리합니다. 또한 Packfiles, Miro, Bright Security, SonarQube, Octopus Deploy 등 초대된 초기 에이전트들을 통해 백로그·보안·분석·배포 문제도 GitHub 안에서 다룰 수 있음을 제시합니다. 기술적으로는 툴 연동의 지연을 줄여 피드백 루프를 단축하고, 자동화된 선검사로 위험을 앞당겨 발견하는 점이 핵심적 의미입니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/how-to-bring-your-software-delivery-workflow-into-github-with-agent-apps/)

