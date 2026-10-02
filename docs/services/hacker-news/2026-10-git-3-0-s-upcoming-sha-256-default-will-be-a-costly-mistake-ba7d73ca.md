---
title: "Git 3.0's upcoming SHA-256 default will be a costly mistake"
sidebar_label: "Git 3.0's upcoming SHA-256 default will be a costly mistake"
---

# Git 3.0's upcoming SHA-256 default will be a costly mistake

> Hacker News · 2026-10-01 · Developer Tools / Version Control

---

스콧 체이콘은 Git 3.0이 기본 해시 알고리즘을 SHA-1에서 SHA-256으로 바꾸려는 계획이 실용적 이득 없이 전 세계적으로 큰 비용과 혼란을 야기할 것이라고 경고한다. 글은 먼저 Git이 콘텐츠 주소 저장소로서 SHA-1을 어떻게 사용해 왔는지, 그리고 SHA-1에 대해 공개된 충돌 연구가 "수학적으로 약화"를 의미하지만 우발적 충돌은 사실상 불가능에 가깝다고 설명한다. 충돌(collision)과 두 번째-원본(second-preimage) 공격의 차이를 짚으며, 후자는 널리 사용되는 해시 함수들에서 실무적으로 거의 문제가 되지 않는다고 정리한다.
체이콘은 실제 공격 벡터 관점에서 해시 자체가 근본적 신뢰의 근거가 아니라고 주장한다. 신뢰는 어디서 코드를 가져오는지에 달려 있고, 사회공학·패키지 관리자의 권한 탈취 같은 현실적 공격이 해시 충돌보다 훨씬 쉽고 흔하다고 본다. 또한 SHA-256 기본 전환이 가져올 실무적 문제들—새 리포지토리의 포맷 불일치로 인한 푸시 실패, 서브모듈·툴링·서명 호환성 파괴, 링크·토론 기록의 해시 교체 필요 등—을 구체적으로 지적하며 대규모 에코시스템 전환이 복잡하고 비용이 크다고 경고한다. 결론적으로 체이콘은 대부분 환경에서는 해시를 신뢰의 근거로 삼지 않는 편이 현실적이며, 필요한 소수의 사례에 한해 더 간단한 대응책을 쓰는 편이 낫다고 제안한다.

[Hacker News에서 원문 읽기 →](https://blog.gitbutler.com/git-3-sha-256)

