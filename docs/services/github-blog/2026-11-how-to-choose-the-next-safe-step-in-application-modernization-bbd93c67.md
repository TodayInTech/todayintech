---
title: "How to choose the next safe step in application modernization"
sidebar_label: "How to choose the next safe step in application modernization"
description: "GitHub는 레거시 현대화를 위해 먼저 '증거(inventory) 확보'로 현재 동작을 캡처하고, 최소 영향의 처리 순서(keep→upgrade→swap→wrap→rewrite)와 L0~L4 안전 등급을 적용해 단계적 실험을 권한다. 이 절차를 'doc-and-modernize' Copilot 스킬로 파일화해 재사용 가능하게 만들었다."
---

# How to choose the next safe step in application modernization

> GitHub Blog · 2026-11-25 · Application Modernization / GitHub Copilot

---

**증거 우선(evidence-first) 절차와 재현 가능한 에이전트 스킬**

GitHub 블로그 글은 애플리케이션 현대화에서 흔히 기술 선택으로 곧장 달려가지 말고, 먼저 무엇이 아직 작동하는지 '증거'를 모아야 한다고 제안합니다. 저자는 매니페스트·락파일·엔트리포인트, 설치·빌드·테스트·실행 명령, 런타임 고정값, 외부 계약(API·DB·파일 포맷·사용자 워크플로)과 EOL(수명 종료) 종속성 등으로 구성된 소규모 증거 인벤토리를 만들라고 권합니다. 불확실성은 'documented / inferred / unverified'로 기록하라고 명시합니다 (chunk-0001).

## 최소 교란 우선 순서와 증명 가능성

컴포넌트별로 **keep → upgrade → swap → wrap → rewrite** 순으로 덜 파괴적인 선택을 먼저 고려하되, 결정 근거로서 '어떤 증거가 필요한지' 묻습니다. 또 시간 상자(time-box) 기반의 가용성 확인으로 '구식 코드가 실제로 실행되는지'를 판별하고, 실행이 가능하면 '행동 캡처 후 업그레이드', 불가능하면 '작은 최신화 슬라이스를 먼저 만들기' 경로로 나눕니다 (chunk-0001).

## 안전 등급(L0~L4)

저자는 스킬에서 사용하는 안전 수준을 제시합니다. 요약하면: L0은 회귀망 없음(문서가 사양), L1은 소규모 되돌림 가능 변경·스모크 체크, L2는 입력·출력 캡처(스냅샷 등), L3는 자동화 검사로 부분 커버, L4는 lint·단위·행동·E2E를 합친 CI 게이트입니다. 각 레벨별로 '무엇을 증명할 수 있는지'를 명확히 하도록 요구합니다 (chunk-0001).

## 사례: PiggyMetrics와 ADempiere

PiggyMetrics 사례에서는 Java 8, Spring Boot 2.0.3, Spring Cloud Finchley, Zuul, Hystrix, spring-security-oauth2 같은 오래된 스택을 조사했습니다. feasibility 체크에서 mvn -pl config -am compile(Exit code 0)과 mvn -pl account-service -am test(14 tests ran: five passed and nine errored)이 기록되었고, 오류는 embedded MongoDB 다운로드의 HTTP 403와 i386 바이너리 핀 문제로 이어졌습니다. 이로써 전체 재설계 대신 **테스트 의존성 교체(Testcontainers로 교체)** → CI(GitHub Actions)에 베이스라인 등록 → Java 8→Java 21, Spring Boot 3.3으로 이동 → Zuul→Spring Cloud Gateway, Hystrix→Resilience4j, spring-security-oauth2→Spring Authorization Server+JWT로 대체하는 순서로 진행했습니다. 모듈 수는 인스코프 빌드에서 **9개에서 7개로 감소**했습니다(구체 수치는 실험 결과를 기술한 것임) (chunk-0002).

ADempiere 대형 사례에서는 빌드를 재현하고 JDK 21로 런타임을 이동시키며 SOAP 계약을 유지하면서 XFire→CXF와 Jakarta 전환, 일부 사용자에게 현대적 웹 경로 도입까지 수행했습니다. 여기서는 30개의 머지된 현대화 PR과 **102,587.72 재구성된 Copilot 크레딧**이라는 실험적 측정치가 보고되었고, 저자는 이 수치가 달러 비용을 의미하지 않음을 명시했습니다. 또한 POC 수준에서 멈춘 이유는 기술적 증명이 완료되었기 때문이라고 적었습니다(실제 제품 전환은 추가 결정 필요) (chunk-0002).

## 절차를 코드로: .github/skills/doc-and-modernize

이 방법은 단순 가이드가 아니라 **GitHub Copilot 에이전트 스킬(.github/skills/doc-and-modernize/)** 형태로 파일화되어 있습니다. SKILL.md에 이름·설명·명령·검사 포인트·안전 레벨·에비던스 요구사항·페이즈 게이트 등이 포함되며, 스킬은 절차를 드러내지만 정책(허용 런타임·보안·승인자 등)은 조직이 제공해야 한다고 명확히 구분합니다. 또한 gh skill 명령은 현재 퍼블릭 프리뷰 상태임을 안내합니다(gh skill 설치 가이드는 별도 확인 필요) (chunk-0003).

## 실무적 의미

이 글이 제공하는 핵심 실무 가치는 '먼저 무엇을 증명할 수 있느냐'에 기반해 변경의 범위와 증명 방법을 제한한다는 점입니다. 구체적 사례와 명확한 체크포인트(Testcontainers로 대체해 CI에서 베이스라인 확보, 모듈·버전 변경 내역, 안전 등급 분류)는 팀이 무리한 재설계를 피하고, 변경을 검증 가능한 단계로 나누도록 돕습니다. Copilot 스킬로 절차를 보존하면 프로젝트별로 파일 리뷰로 정책·승인자를 결합해 재현 가능하게 운영할 수 있습니다.

이 글의 권고는 절차·사례·파일 배치 방식에 대한 실무 지침을 제공하며, 특정 버전 선택(예: Java 21, Spring Boot 3.3)은 사례 실험을 설명한 것이므로 각 조직의 지원 요구에 맞춰 목표를 정하라고 명시되어 있습니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/)

