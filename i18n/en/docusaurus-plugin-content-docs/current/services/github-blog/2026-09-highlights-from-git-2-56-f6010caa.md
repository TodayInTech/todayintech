---
title: "Highlights from Git 2.56"
sidebar_label: "Highlights from Git 2.56"
---

# Highlights from Git 2.56

> GitHub Blog · 2026-09-28 · Open Source / Git

---

오픈소스 Git의 새 버전 2.56이 발표되며 충돌 처리, 병합 기반 탐색, 리포지터리 재패킹 등 실무에 바로 도움이 되는 여러 개선이 포함됐다. 우선 충돌을 해결한 파일만 안전하게 스테이징하도록 돕는 git add --resolved가 추가돼, 병합 중 관련 없는 로컬 변경을 실수로 스테이징하는 위험을 줄인다. 병합 베이스 탐색 구현도 개선되어 한쪽에만 남은 고유 커밋이 더 이상 새 후보를 만들어낼 수 없다는 점을 판별해 조기 종료할 수 있게 되었고, 대형 모노레포에서 0.68초→0.01초 같은 극적인 속도 향상이 관측됐다. 리눅스 커널 비교 사례에서도 트래버설 스텝과 시간이 크게 줄었다는 구체적 수치가 제시된다.
저장 공간 측면에서는 --path-walk 재패킹의 적용 제약을 제거해 리포지터리 호스팅 환경에서 비트맵과 델타 아일랜드 규칙을 유지하면서도 경로 기반 델타 탐색의 이점을 활용할 수 있게 했다. 예시 벤치마크에서 패키지 크기가 약 558.5MB에서 164.4MB로 약 71% 줄었다. 대용량 객체 관리를 위한 수동 정리 명령(예: --filter=blob:limit=1m --drop-filtered)과 함께 실험적 기능들도 확장됐다(git history drop, git refs로의 레퍼런스 관리 통합, bulk --delete-merged, git bisect의 --reset-when-found, git replay --linearize 등). 또한 git log --follow의 경로 추적이 부모별로 분리되어 비선형 히스토리에서도 더 안정적으로 동작하고, 내부 자료구조 개선으로 reftable·패키지 로딩·작업 트리 비교 성능이 대폭 향상되어 몇 초·몇 분 단위 작업이 수 밀리초 수준으로 단축된 사례가 보고된다. 보다 자세한 변경 목록은 릴리스 노트를 통해 확인할 수 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/open-source/git/highlights-from-git-2-56/)

