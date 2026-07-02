---
title: "Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory"
sidebar_label: "Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory"
---

# Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

> Hacker News · 2026-07-02 · Security

---

제목에 따르면 Linux 6.9에서부터 LUKS(디스크 암호화) 관련 동작이 바뀌어 시스템 suspend(절전) 과정에서 메모리 내 암호화 키를 지우지 않게 된 것으로 보입니다. 제공된 정보만 보면 원문은 mathstodon에 올라온 IngoBlechschmid의 게시물이고, Hacker News에서 포인트 368·댓글 176으로 큰 관심을 모았습니다. 다만 메타데이터만으로는 어떤 커널 변경이 정확히 원인인지, 의도된 수정인지 등 세부 내용은 확인되지 않습니다.
이 제목이 시사하는 문제는 suspend·resume 처리와 키 삭제 타이밍의 교차로 인해 암호키 잔류 가능성이 생길 수 있다는 점에서 보안적으로 의미가 있습니다. 서버, 노트북, 임베디드 장치 등 환경별 영향이 달라질 수 있고, 커뮤니티 반응은 우려를 반영하지만 실제 취약성 여부와 대응 방안은 관련 패치·리뷰와 원문 분석을 통해 확인해야 합니다.

[Hacker News에서 원문 읽기 →](https://mathstodon.xyz/@iblech/116769502749142438)

