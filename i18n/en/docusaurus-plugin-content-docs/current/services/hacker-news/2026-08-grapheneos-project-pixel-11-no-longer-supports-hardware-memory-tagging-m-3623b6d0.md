---
title: "GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)"
sidebar_label: "GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)"
---

# GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)

> Hacker News · 2026-08-29 · 모바일 OS / 보안

---

GrapheneOS 프로젝트는 일주일가량의 작업 끝에 Pixel 11 시리즈에 대한 부분 포팅을 구현했으나, 포팅을 완료하지 못했다고 밝혔다. 그 이유로는 소프트웨어와 펌웨어, 그리고 거의 확실히 하드웨어 측면에서 ARM 하드웨어 메모리 태깅(MTE)에 대한 지원이 부족하다는 점을 들었다. 게시글은 이 보안 기능이 빠진 상태가 포팅을 막는 직접적 원인이라고 명시하며, 구글이 비용 절감을 이유로 중요한 보안 기능을 제거한 것으로 보인다고 지적했다.
이번 공지는 단순한 기기 호환성 문제를 넘어서 보안 기능의 설계·제거가 서드파티 운영체제의 개발 가능성과 보안 태세에 즉각적인 영향을 줄 수 있음을 드러낸다. GrapheneOS 측의 설명에 따르면 MTE 지원 부재는 소프트웨어·펌웨어·하드웨어 전반에 걸친 호환성 결여로 포팅 작업을 중단하게 만든 핵심 제약이며, 해당 문제는 Pixel 11 시리즈에서의 보안 설계 변경이 모바일 OS 생태계에 미치는 실무적 함의를 보여준다. 제공된 글은 포팅 시도와 그 중단 사유를 직접 보고하는 형식이므로, 구체적 기술적 세부사항(예: MTE의 구체적 동작 방식 등)은 게시글 내에 명확히 설명되지 않았음을 유념해야 한다.

[Hacker News에서 원문 읽기 →](https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22e)

