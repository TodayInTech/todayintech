---
title: "How GitHub gave every repository a durable owner"
sidebar_label: "How GitHub gave every repository a durable owner"
---

# How GitHub gave every repository a durable owner

> GitHub Blog · 2026-07-09 · Governance &amp; compliance

---

GitHub은 조직 내 14,000여 개 리포지토리 가운데 절반도 채 명확한 소유자가 없다는 문제를 해결하기 위해 45일 이내에 모든 활성 리포지토리의 소유권을 검증하고, 사용되지 않는 약 8,000개 리포지토리를 아카이브하는 작업을 수행했다. 핵심 설계는 리포지토리별 소유권을 1차 시민권으로 삼는 것이었다. 저장소 내 파일 대신 조직 전체에서 질의 가능한 GitHub 커스텀 프로퍼티(ownership-type, ownership-name)를 도입했고, ownership-type은 Service Catalog, 개인(허버), 팀의 세 가지 값을 허용했다. 허버 핸들·팀 존재·서비스 카탈로그 항목 등을 앱에서 직접 검증해 잘못된 입력을 걸러냈고, 기존 서비스와 연동된 약 1,500개 리포지토리는 Service Catalog 동기화로 즉시 커버했다. 자동화는 쿠버네티스 크론잡으로 구동되는 GitHub 앱이 담당했고, 초기에는 30일 유예 후 아카이브 정책을 적용했으며 이후 생성 시 필수화와 함께 소유권 상실 시 1시간 이내로 플래그되도록 강화를 진행했다.
운영 과정에서의 실무적 교훈도 구체적이다. 아카이브로 인해 Datadog 이슈 생성이 실패하면서 알림 체계의 허점이 드러났고, 이를 보완하기 위해 리포지토리 관리자 멘션과 쓰기 권한자 할당을 추가했다. 또한 Service Catalog의 장애나 손상된 데이터로 인해 대량 아카이브를 막기 위해 '로우 워터 마크'를 두어 한 번에 처리할 항목 수가 임계치를 넘으면 작업을 중단하도록 했고, 카탈로그 접근 불가 시에는 독립적으로 검증 가능한 항목만 검사하도록 설계했다. 결과적으로 활성 리포지토리는 약 3,000개로 줄고 아카이브는 11,000개에 달했으며, 이 과정은 시크릿 스캐닝 등 조직 전체에 퍼지는 보안·조치 워크플로우의 전제 조건을 마련했다. 게시글은 유사한 체계를 고민하는 조직에 대해 소유권 분류·조직 레벨 프로퍼티·카탈로그 동기화·유예·가드레일 설계 등 실무 지침을 제시한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/application-security/how-github-gave-every-repository-a-durable-owner/)

