---
title: "We want you to build the next Git platform on Cloudflare"
sidebar_label: "We want you to build the next Git platform on Cloudflare"
---

# We want you to build the next Git platform on Cloudflare

> Hacker News · 2026-10-03 · 클라우드 플랫폼/개발자 도구

---

Cloudflare는 인간 개발자가 아닌 '에이전트'가 대규모로 코드 작업을 수행하는 시대를 대비해 기존의 GitHub식 모델을 재고할 필요가 있다고 제안한다. 이를 위해 회사는 Git과 호환되는 버전형 파일시스템인 Artifacts를 오픈 베타로 공개했고, 레포지토리를 프로그래밍 가능한 원시(primitives)로 설계해 에이전트별·세션별·작업별로 레포를 생성·포크하고 에이전트 컨텍스트를 저장할 수 있도록 했다. 다수의 에이전트가 동시 작업할 때 충돌 관리, 변경 이유 추적, 검토 워크플로우 같은 상위 레이어를 개발자가 구축할 수 있게 하는 것이 목표다.
기능적으로 Artifacts는 Workers와 긴밀히 통합되어 레포를 Workers Builds로 연결하면 푸시 시 자동 빌드·프로덕션·프리뷰 배포가 가능하고, Workers에서 Artifacts 바인딩을 통해 레포 생성·포크·파일·커밋 검사와 레포 범위의 Git 토큰 발급을 코드로 제어할 수 있다. 또한 레포 생성·포크·푸시 등 이벤트를 구독해 CI나 코드리뷰 워크플로우를 자동으로 시작할 수 있고, 레포별 메트릭 대시보드와 EU/US 데이터 관할권 설정을 제공한다. 아티팩츠는 사용량 기반 과금으로 2026년 10월 15일부터 과금이 시작되며, Cloudflare는 이 플랫폼을 활용해 '차세대 Git 플랫폼'을 만드는 경진대회를 열어 소스 코드(허용 라이선스: MIT/Apache/BSD)와 5–10분 데모 영상을 요구하고, 1위 팀에 크레딧과 행사 초대 등을 제공한다. 기술 관점에서 이번 발표는 에이전트 주도의 자동화·격리·검토 파이프라인을 인프라 수준에서 지원하려는 실질적 발걸음으로, 클라우드 네이티브 워크플로우를 재설계하려는 개발자·연구자에게 유의미한 플랫폼 기회를 제시한다.

[Hacker News에서 원문 읽기 →](https://blog.cloudflare.com/next-git-platform-on-cloudflare/)

