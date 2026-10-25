---
title: "Highlights from Git 2.55"
sidebar_label: "Highlights from Git 2.55"
---

# Highlights from Git 2.55

> GitHub Blog · 2026-06-29 · Git / 오픈소스

---

Git 2.55는 대형 저장소 관리와 메타데이터 유지비용을 줄이기 위한 실용적 개선에 초점을 맞췄다. 가장 큰 변화 가운데 하나는 증분 멀티팩 인덱스(incremental MIDX)를 직접 쓰도록 git repack을 확장한 것으로, --write-midx=incremental 모드에서 기본적으로는 기존 레이어를 건드리지 않고 새 레이어를 덧붙이는 append-only 동작을 제공한다. 여기에 기하학적(geometric) 리패킹을 결합하면 repack.midxSplitFactor와 repack.midxNewLayerThreshold 규칙에 따라 인접 레이어를 메타데이터 수준에서만 합치는 컴팩션을 수행해 체인의 크기를 로그 규모로 유지할 수 있다. 이 설계는 전체 MIDX를 자주 다시 쓰지 않으면서도 최근 소규모 레이어를 더 자주 합쳐 관리비용을 낮추는 절충을 제공하며 기존의 repack 흐름과 통합된다.
그 외에도 개발자 워크플로우와 성능 관련 유용한 기능들이 다수 추가되었다. git history에 fixup 서브명령이 생겨 인덱스에 스테이징된 변경을 특정 이전 커밋에 합치는 의도 기반 작업이 가능해졌고(비교적 보수적으로 동작해 충돌 시 중단하고 베어 리포지토리에서는 동작하지 않음), 구성 기반 훅은 병렬 실행을 허용해 훅 처리 시간을 단축할 수 있다. Linux용 내장 FS 모니터가 inotify로 구현되어 성능을 개선하지만 디렉토리당 워치 수 제한(fs.inotify.max_user_watches)을 조정해야 할 수 있다. 리치빌리티 비트맵 생성 경로도 불필요한 트리 재귀를 피하고 캐싱·정렬 전략을 도입해 대형 저장소의 비트맵 생성 시간을 약 612초에서 약 294초로 줄였고, 의사-머지(pseudo-merge) 비트맵은 탐색 속도 이점을 유지하면서 생성 오버헤드를 크게 낮췄다. 또한 --path-walk와 필터 조합 지원, 입력 파이프용 git format-rev 실험적 명령, fetch 협상에서 참조 포함/제한 옵션 등 부분 클론·팩 크기·스크립팅 유연성을 향상하는 변경들이 포함되어 저장소 유지관리와 자동화 파이프라인에 즉시 적용 가능한 개선을 다수 제공한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/open-source/git/highlights-from-git-2-55/)

