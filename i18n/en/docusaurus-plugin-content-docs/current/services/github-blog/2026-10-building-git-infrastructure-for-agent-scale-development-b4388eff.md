---
title: "Building Git infrastructure for agent-scale development"
sidebar_label: "Building Git infrastructure for agent-scale development"
---

# Building Git infrastructure for agent-scale development

> GitHub Blog · 2026-10-06 · Architecture &amp; optimization

---

GitHub은 에이전트와 개발자가 동시에 수백만 건의 변경을 만드는 ‘에이전트 시대’에 맞춰 Git 인프라를 재구축하고 있다. 제공된 근거에 따르면 지난 해(2025년 9월~2026년 8월) Git 활동은 월별 이벤트가 218.2000억에서 473.3000억으로 두 배 이상 증가했고, 2026년 9월 한 달에만 73.8억 커밋이 발생했다. 최상위 저장소는 한 달에 약 10억 요청을 받는 등 부하 분포의 꼬리가 매우 길다. 현재 아키텍처는 Spokes라 불리는 파일서버의 로컬 디스크 복제본들이 내구성과 읽기 용량을 동시에 담당해 왔는데, 모든 복제본이 쓰기 작업에 참여하기 때문에 읽기 복제를 늘리면 쓰기가 느려지는 근본적 한계가 드러났다. 또한 에이전트는 거의 모든 동작 뒤에 커밋을 수행해 단일 푸시 지연이 병목이 되고, 머지·병합 참조 하나에 경합이 집중되며 CI 팬아웃으로 동일 브랜치 팁에 대한 수천 건의 읽기가 발생하는 등 설계적 문제를 지적한다.
GitHub이 제시한 해결책은 내구성과 스케일을 분리하고 조율을 최소화하는 것이다. 참조 업데이트처럼 합의가 꼭 필요한 부분만 임계 경로에 두고, 객체 저장·검증·시크리트 스캐닝 등은 병렬로 처리한다. 컴팩션·가비지콜렉션 같은 무거운 유지보수 작업을 서비스 경로에서 분리해 별도 워커가 내구 스토리지에 대해 처리하도록 하며, 권한 있는 저장소 복사는 Azure Blob Storage에 두고 읽기는 경량 캐시 워커로 확장한다. 이 접근은 컴퓨트와 스토리지를 독립적으로 확장해 장애 복구와 버스트 대응을 개선하며, 내부 벤치마크에서는 최대 35배 높은 쓰기 처리량을 보였다고 밝힌다. 사용자가 기대하는 브랜치 보호·심사·감사 로그 같은 제어권도 유지하겠다는 점을 강조해, 대규모 동시성 환경에서 실용성과 신뢰성을 함께 끌어올리려는 설계적 전환을 제시한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/architecture-optimization/building-git-infrastructure-for-agent-scale-development/)

