---
title: "Using the GitHub Copilot SDK for Java"
sidebar_label: "Using the GitHub Copilot SDK for Java"
---

# Using the GitHub Copilot SDK for Java

> GitHub Blog · 2026-08-10 · AI &amp; ML

---

GitHub의 새 SDK는 Java 진영에서 AI 에이전트를 ‘자바스럽게’ 다룰 수 있도록 설계됐다. 글은 Copilot SDK for Java가 프레임워크에 종속되지 않는 최초의 방식이며, BYOK(자체 모델 제공자 구성) 지원으로 OpenAI·Azure·Anthropic 등 직접 모델 제공자와 연동해 Copilot 구독 없이도 사용할 수 있다고 설명한다. 동시에 데모와 예제는 Maven 의존성(com.github:copilot-sdk-java:1.0.7-preview.1), JDK 17 또는 25 권장, Copilot CLI와(데모 전제) 같은 구체적 전제조건을 명시해 실제 도입 경로를 제시한다. 어노테이션(@CopilotTool, @CopilotToolParam)을 통한 툴 선언, 람다·JSON Schema 방식의 툴 정의, SystemMessage의 섹션 단위 커스터마이즈, 한 줄짜리 agent 루프(sendAndWait(...))와 같은 핵심 API를 예제로 보여주며 SDK가 CompletableFuture·람다·가상 스레드 등 자바 기존 패턴과 자연스럽게 결합함을 강조한다.
샘플 애플리케이션은 Jakarta EE 11 기반의 부동산 리드 관리 파이프라인으로, 각 문의를 가상 스레드 상의 독립된 Copilot 세션으로 처리하고 Jakarta WebSocket으로 실시간 진행 상태를 브라우저에 푸시한다. 기술적으로는 ManagedThreadFactory(virtual=true)를 통해 컨테이너 컨텍스트가 전파되는 가상 스레드를 Executor로 만들어 콜백에서 CDI·JPA 리포지토리를 바로 활용하게 하고, session.on(...) 이벤트 구독으로 도구 호출·모델 응답을 실시간으로 관찰하게 한다. 또한 ToolSet과 SessionConfig를 통한 세션별 도구 권한 제한, 어노테이션 프로세서 설정(-Acopilot.experimental.allowed=true 및 annotationProcessorPath) 등 운영·보안 측면 실무 고려사항도 상세히 다뤄 개발자가 SDK를 시험하고 프로덕션에 적용할 때 유의할 점을 제시한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)

