---
title: "The case for a cooldown: Why Dependabot now waits before issuing version updates"
sidebar_label: "The case for a cooldown: Why Dependabot now waits before issuing version updates"
---

# The case for a cooldown: Why Dependabot now waits before issuing version updates

> GitHub Blog · 2026-07-23 · Supply chain security

---

GitHub은 새 릴리스가 퍼져 자동화 도구로 곧바로 설치되는 '초기 창'을 막기 위해 Dependabot에 기본 3일 쿨다운을 도입했다. 글은 2025년 npm 패키지(예: chalk 등)에 대한 피싱·악성 버전 유포가 불과 몇 시간 만에 확산된 사례를 제시하면서, 자동 업데이트 도구가 새 릴리스를 즉시 PR로 열어버리는 동작이 이런 공격 경로를 키운다고 지적한다. GitHub Advisory Database의 통계(2026년 5월 기준 연간 6,500건 이상의 npm 악성코드 권고 등)와 2018~2026년 보고된 21건의 공급망 사고 검토를 근거로, 짧은 시간에 잡히는 악성 릴리스가 대다수라는 점을 들어 쿨다운의 필요성을 설명한다.
기본값은 ‘출시 후 최소 3일 대기’지만 dependabot.yml로 사용자별 조정이 가능하고, 이 설정은 커뮤니티 관행(일부 도구도 3일 채택)과의 일관성을 고려했다고 밝힌다. 동시에 쿨다운은 빠르게 퍼지는 공격 패턴만 차단할 뿐 장기 은닉형 백도어, 관리자의 악의적 행위, 빌드 시스템 손상 등에는 취약하므로 잠금 파일 사용, CI의 설치 스크립트 비활성화, 빌드 토큰 범위 제한, 업데이트 사전 검토 등 다른 방어책과 함께 써야 한다는 ‘방어의 깊이(defense in depth)’ 관점도 강조한다. 기술적 의미는 자동화 편의와 보안의 균형을 재조정해 초기 노출 창을 줄임으로써 많은 단기간 유포형 공급망 공격을 사전에 감소시킬 수 있다는 점에 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/)

