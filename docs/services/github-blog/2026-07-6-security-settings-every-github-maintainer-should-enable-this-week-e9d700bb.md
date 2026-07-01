---
title: "6 security settings every GitHub maintainer should enable this week"
sidebar_label: "6 security settings every GitHub maintainer should enable this week"
---

# 6 security settings every GitHub maintainer should enable this week

> GitHub Blog · 2026-07-01 · Security

---

GitHub 보안팀은 유지보수자가 '한 주 안에' 켤 수 있는 여섯 가지 무료 설정을 묶어 빠르게 보안 태세를 향상시킬 수 있다고 권한다. 우선 SECURITY.md로 리포터가 취약점 신고 경로를 알게 하고, 비공개 취약점 리포팅(PVR)을 활성화해 공개 이슈 대신 기밀 Advisory로 triage할 것을 권장한다. 이어서 시크릿 스캐닝과 푸시 보호로 로컬에서 키·토큰이 리포지토리로 올라가는 것을 차단하고, Dependabot과 의존성 리뷰로 패키지 의존성의 알려진 취약점을 PR 수준에서 검사하도록 구성하라 권한다. 코드스캐닝은 CodeQL 엔진을 기본 쿼리팩으로 한 번의 설정으로 PR마다 정적분석을 실시하며, 마지막으로 기본 브랜치에 병합 정책(풀 리퀘스트, 최소 승인자 등)을 적용해 단일 크리덴셜 탈취나 실수로 인한 직접 푸시를 막으라고 제안한다.
제안된 설정들은 개별적으로는 간단하지만 상호작용해 효과를 증폭한다는 점을 강조한다: 브랜치 보호가 있어야 Dependabot 알림이나 코드스캐닝 결과가 실제 병합 차단으로 연결되어 실질적 방어가 된다. 또한 GitGuardian 통계(2025년에 공개 GitHub에서 2,865만 건의 시크릿 누출 보고, AI 보조 커밋이 누출 비율을 두 배로 높임)와 IBM의 데이터 유출 평균 비용 수치 등을 인용해 자동화된 기본 방어가 왜 필요한지 근거를 제시한다. 유지보수자 상당수가 보안 전담이 아니기 때문에 문서는 'Protect Your Project' 가이드 흐름과 함께 30분 이내로 설정을 끝낼 수 있다고 안내하며, 이들 조치는 '완전한 무결성'을 보장하진 않지만 '쉬운 출입구'를 닫아 프로젝트와 그 종속성을 의미 있게 더 안전하게 만든다고 결론 내린다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/)

