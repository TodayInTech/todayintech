---
title: "From 2,500 requests to 24: Rebuilding star history without the stargazers"
sidebar_label: "From 2,500 requests to 24: Rebuilding star history without the stargazers"
---

# From 2,500 requests to 24: Rebuilding star history without the stargazers

> GitHub Blog · 2026-10-14 · Architecture &amp; optimization

---

레포지토리 스타 기록을 시간 흐름으로 재구성하려던 기존 방식은 '누가(stargazer)와 언제(starred_at)' 정보를 페이지 단위로 읽어 모으는 설계 때문에 개인정보 노출과 데이터베이스 비용 문제를 동시에 일으켰습니다. 공개된 스타 목록을 대량으로 긁어 스팸에 악용하는 사례가 생겼고, 페이지네이션 구현 버그로 인해 각 요청이 전체 스타 집합을 세어야 해서 대형 레포지토리에서는 수천 건의 요청과 느린 카운트 쿼리가 반복되었습니다(예: react/react는 과거에는 약 2,511개의 요청이 필요). 우선 GitHub는 관리자·협업자 외에는 stargazer·watcher 목록 접근을 제한해 노출 위험과 즉각적 DB 부담을 줄였지만, 기존 도구들이 필요로 하던 '성장 곡선' 정보가 사라지자 커뮤니티와 협업해 새로운 해결책을 설계했습니다.
핵심 설계는 아이덴티티를 제거하는 것을 넘어서서 '집계 전 필터링'을 적용한 것입니다. 새 엔드포인트는 페이지와 per_page를 캘린더 주 단위의 indexed created_at 범위로 변환해 해당 범위의 행만 먼저 필터링하고, 그 범위 안에서 일별 카운트로 집계해 최대 30주를 한 번에 반환합니다. 이렇게 하면 대형 레포지토리라도 한 요청으로 최대 30주를 가져올 수 있어 react/react의 경우 약 2,511요청이 아니라 약 24요청으로 줄이고, 전체 기록을 읽을 때 각 스타를 대략 한 번만 검사하게 됩니다. 다만 매우 밀집된 주간(특정 주에 스타가 몰리는 경우)은 여전히 비용이 클 수 있다는 한계가 남아 있으며, 동일한 '온디맨드 카운트' 패턴이 발견된 웹 페이지들도 캐시된 스타 카운트로 교체해 느린 쿼리를 제거하는 등의 추가 최적화가 병행되었습니다. 이 과정은 제품팀·커뮤니티·툴 메인터이너 간 협업으로 진행되어, 유지보수자가 관심 변화를 보는 데 실용적이며 DB 부담을 낮춘 집계형 API를 얻었다는 점이 기술적으로 의미가 큽니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/architecture-optimization/from-2500-requests-to-24-rebuilding-star-history-without-the-stargazers/)

