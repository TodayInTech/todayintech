---
title: "Redesigning source control at Anthropic"
sidebar_label: "Redesigning source control at Anthropic"
---

# Redesigning source control at Anthropic

> Hacker News · 2026-10-13 · Developer Infrastructure

---

Anthropic은 에이전트(Claude)가 대규모로 코드를 생성하면서 기존 인간 규모에 맞춰진 git 기반 인프라가 병목이 됨을 경험하고, 이를 해결하기 위해 자체 분산형 버전관리 시스템 Scion을 설계·배포했습니다. 하루 병합 건수가 5월 약 2,500건에서 9월 3만 건 이상으로 폭증하면서 메인 브랜치 히스토리만 100GB, 작업 복사본 25GB가 되어 기존의 미러·시드 기반 우회책이 운영 부담을 감내하지 못했습니다. Scion은 "클라이언트는 항상 온라인"이라는 전제와 클라이언트-서버 비대칭성을 채택해 서버가 히스토리 조회·커밋 생성·머지 등을 담당하고, 클라이언트는 필요한 트리와 블롭만 재귀적으로 요청하는 방식으로 설계됐습니다. 이 접근은 부분적·가상화된 체크아웃을 자연스럽게 지원하고, 전송이 단일 대형 팩파일에 의존하지 않아 중단 복구와 캐시 계층에 적합합니다.
기술적 실행은 scn 클라이언트→노드의 scion-daemon→지역 scion-cache→권한자 scion-server로 이어지는 계층형 캐시 토폴로지로 구성되어 있으며, 각 계층이 동일한 RPC를 제공해 클라이언트가 캐시 구조를 알 필요가 없습니다. 이 구조로 캐시 적중률은 99% 이상을 유지하고, CPU·메모리 면에서 이전 git 미러링 대비 인프라 발자국을 200배 축소했으며 체크아웃 속도는 수 분에서 수 초대로 개선되어 CI에서만 25%의 CPU 여유를 확보했다고 보고합니다. 또한 Claude는 인제스트 파이프라인을 20배 적은 메모리와 4배 빠른 성능으로 자동 재작성하는 등 개발 속도와 최적화를 크게 끌어올렸고, 사람 엔지니어들은 설계·제약 설정과 오버엔지니어링 방지 역할을 수행했습니다. Scion은 모든 조직에 바로 적용 가능한 대체제가 아니지만, 서버 중심 RPC·계층형 캐시·부분적 체크아웃 같은 개념은 기존 git 플랫폼과 병행해 확장성 문제를 완화하는 실용적 단서로 읽힙니다.

[Hacker News에서 원문 읽기 →](https://www.anthropic.com/engineering/redesigning-source-control)

