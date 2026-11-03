---
title: "Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app"
sidebar_label: "Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app"
description: "Momentic은 에이전트 기반 자동 QA 플랫폼 'Mo'를 정식 출시했다. 웹·iOS·Android를 직접 탐색해 버그를 재현·분류하고 자가 치유·트리아지와 PR/CI 연동, plain‑English YAML 테스트로 테스트 유지비를 낮추는 것이 핵심 변화입니다."
---

# Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app

> Hacker News · 2026-11-02 · Product Launch / QA Automation

---

Momentic은 에이전트형 자동 QA 플랫폼의 핵심 엔진 **Mo를 베타를 졸업하고 정식 배포**했다고 밝혔다. Mo는 앱을 직접 탐색해 기능 결함을 재현하고, 실패 원인을 그룹화(트리아지)해 제안된 수정을 커밋하거나 PR로 올리는 등 QA 작업을 에이전트 루프 안으로 집약하는 데 초점을 맞췄다.

## Mo의 작동 방식과 기술적 변화
Momentic의 새 에이전트(v3)는 실행 전에 흐름을 계획하고(플랜), 해석한 단계들을 캐시한 뒤 실패 시 스스로 복구(자가치유)한다. 에이전트는 실행 중에 DAG(직접 비순환 그래프)를 구성해 탐색을 조직하고, 각 단계별로 재시도·캐시·상태 검사 같은 복구 동작을 적용한다. 테스트 정의는 사람이 읽을 수 있는 YAML(fileType: momentic/test/v2)로 작성해 에디터에서 버전 관리하고, 성공한 AI 동작은 재사용·버전화할 수 있다.

## CI/개발자 워크플로 통합
Mo는 PR 코멘트, 라벨, CLI에서 세션을 시작해 PR의 프리뷰 배포를 테스트하고 결과를 리뷰로 남기며 Mo 커밋 체크를 설정한다. 트리아지 에이전트는 실패를 범주화하고, 자동으로 수정할 수 없는 항목은 격리(quarantine)한다. 또한 테스트 실행의 구조화된 JSON 출력과 라이브 진행상황, 캐시 상태·재시도·루프 등 실행 진단을 제공하는 Run Viewer를 통해 수동 디버깅을 돕는다.

## 모바일·네트워크·환경 지원
웹뿐 아니라 Android와 iOS를 호스팅된 에뮬레이터/시뮬레이터에서 실행하고 화면 녹화, 네트워크 요청 기록·모킹(request recording &amp; mock route) 등 모바일 특유의 문제를 다룬다. Android는 호스트에 Android Studio나 SDK, adb가 없어도 호스팅 에뮬레이터에서 테스트를 돌릴 수 있다. 모바일 테스트에서도 단계별 계획·캐시·자가치유가 동일하게 동작한다.

## 실무적 의미
Momentic은 기존 Playwright·Selenium 같은 프레임워크에서 요구하던 XPath·텍스트 하드코딩을 줄이고, UI 변화에 따라 선택자를 재탐색하거나 영구 보수 제안(diff)을 생성해 테스트 유지비를 낮추려 한다. 회사의 주장대로 동일한 평가에서 **Mo가 약 269개의 라벨된 버그를 찾았고, 경쟁 에이전트는 약 86개**를 찾았다는 결과도 제시되어 있어(근거 자료에 따른 수치) 탐지 재현 능력에 무게를 둔 설계임을 알 수 있다.

## 엔터프라이즈·보안·운영
Momentic은 SOC 2 Type 2 인증을 언급하며 SAML/OIDC SSO, 관리자·멤버 역할, 감사 로그와 같은 엔터프라이즈 기능을 제공한다. 실행은 클라우드에서 이루어지며 조직의 MCP 서버와 시크릿을 세션에 연결할 수 있다. 또한 결과를 로컬로 열람하는 'results view' 기능도 제공해 업로드 없이 내부 검토가 가능하다.

증거로 제시된 기능 목록은 플랫폼이 엔드투엔드 흐름 검증을 자동화하고, 실패를 재현·분류해 개발 주기에서 바로 조치하도록 설계되었음을 보여준다. 제공된 근거 범위에서 가격·계약 상세나 실제 성능 비교의 추가 검증 자료는 없으므로, 도입 전에는 자체 평가(프리뷰 배포에서의 재현율·오탐률·비용)를 권장한다.

[Hacker News에서 원문 읽기 →](https://momentic.ai/)

