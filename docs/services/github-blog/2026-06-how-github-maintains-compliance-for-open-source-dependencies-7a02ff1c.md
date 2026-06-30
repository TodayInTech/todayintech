---
title: "How GitHub maintains compliance for open source dependencies"
sidebar_label: "How GitHub maintains compliance for open source dependencies"
---

# How GitHub maintains compliance for open source dependencies

> GitHub Blog · 2026-06-30 · Governance &amp; compliance

---

GitHub은 자사 플랫폼과 내부 애플리케이션에서 매일 새로운 오픈소스 의존성을 도입하며, 이에 따른 라이선스 의무 준수를 위해 Open Source Program Office(OSPO)가 새로 공개한 GitHub License Compliance 기능으로 수천 개의 의존성을 관리하고 있다. 전통적으로 수동 검토나 서드파티 도구에 의존하던 라이선스 검토 프로세스를 PR 단계로 끌어와, 풀리퀘스트에서 새로 추가되는 직접 및 전이적 의존성의 라이선스를 스캔해 정책 위반을 알리는 방식이다. 초기 정책은 내부에서 사용하던 허용 라이선스 목록(MIT, Apache-2.0, BSD-3-Clause 등)으로 시작했고, 기능을 도입할 때는 한동안 “Evaluate” 모드로 운영해 개발 생산성을 저해하지 않으면서 기존 도구와 병행해 동작 차이를 점검했다. 내부 도입은 약 두 달 전에 이루어졌고, 빠르게 피드백을 주며 엔터프라이즈 수준의 요구사항을 충족시키는 데 기여했다.
라이선스 검사는 규칙셋(ruleset)과 리포지토리 대상 지정(custom property)으로 동작하며, 조건값으로 “Active” 또는 “Evaluate” 모드를 전환할 수 있다. 위반이 감지되면 PR에 패키지별 경고가 달리고, 개발자는 코드를 수정하거나 풀리퀘스트를 닫아 의존성을 제거하거나 예외 요청을 제출해 지정된 팀의 판단을 받을 수 있다. 정책팀은 전 세계 시차를 고려해 분산 배치되어 있으며, 실제로 요청 트리아지 응답은 몇 시간 내로 이뤄지는 경우가 많다. 승인 시에는 라이선스·패키지 허용 여부와 적용 범위를 엔터프라이즈 수준 또는 특정 리포지토리 수준 중에서 결정하고, 내부 패키지에 대해 와일드카드 예외(@github-ui/* 등)를 적용해 일괄 허용하는 기능도 활용한다. 긴급 상황을 위한 일시적 강제 해제(‘break glass’)는 커스텀 속성 값을 토글해 시행할 수 있으며, 실사용에서는 한 번만 사용했다고 밝혔다. 이 기능은 GHAS Code Security 라이선스가 활성화된 GitHub Enterprise Cloud 고객이 사용할 수 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/enterprise-software/governance-and-compliance/how-github-maintains-compliance-for-open-source-dependencies/)

