---
title: "Lean verification of the Riemann Hypothesis"
sidebar_label: "Lean verification of the Riemann Hypothesis"
description: "Levent Alpöge가 2026-11-20에 제출한 리만 가설 증명이 **Lean 라이브러리(17,000,000행)** 형태로 공개되어 Lean·Mathlib 커뮤니티와 연합체들이 컴파일·명제 비교·여러 독립 체커로 검증해 정확성을 공식 인증했습니다."
---

# Lean verification of the Riemann Hypothesis

> Hacker News · 2026-11-21 · formal verification / mathematics

---

Levent Alpöge가 2026-11-20에 제출한 리만 가설 증명이 **Lean 라이브러리(약 17,000,000행)** 형태로 공개되었고, Lean 커뮤니티 및 Mathlib Initiative와 Lean FRO의 연합 성명이 이 증명과 명제의 정확성을 공식 인증했습니다. 커뮤니티는 증명 코드를 Mathlib에만 직접 의존하도록 구성된 라이브러리로 관리했고, 수십 명이 직접 컴파일을 재현해 빌드 오류 없이 동일한 원시 증명 내보내기 파일이 생성됨을 보고했습니다.

## 검증 방식과 핵심 확인점

- 명제의 일치: 리만 가설 명제가 Mathlib 안의 RiemannHypothesis 항목으로 포함되어 있으며, 커뮤니티가 분리한 파일은 Mathlib만 임포트해 해당 명제와 Alpöge의 증명에서 사용된 정리가 정확히 일치하는지 비교했습니다. 두 개의 독립 도구(comparator와 con-leche –compare)가 **증명에서 사용된 정리가 Mathlib의 명제와 정확히 동일함**을 확인했습니다.

- 컴파일과 체커 검증: 라이브러리는 오류 없이 컴파일되었고, 내보낸 원시 증명은 Lean 공식 커널, con-leche, con-ron 및 여러 제3자 구현 체커들에 의해 확인되었습니다. 특히 con-leche와 con-ron은 집합론에 상대화된 형식적 보증을 갖추고 있어 잘못된 증명을 받아들일 수 없음을 형식적으로 보장한다고 명시되어 있습니다.

- 안전성: 검증은 증명 소스의 실행 가능한 코드가 아닌 '비활성화된(exported) 원시 증명' 상에서 이루어졌다고 밝혀, 가설적 악성 코드가 검증 결과에 영향을 주었을 가능성을 낮추려는 조치를 취했습니다.

## 기술적 의미와 실무적 영향(해석)

사실로 확인된 점은 '리만 가설의 정리적 명제와 그에 대한 형식화된 증명이 Lean 체계 안에 정리되어 있고, 여러 독립 도구로 검증되었다'는 것입니다. 이 결과는 형식증명(formal proof) 도구와 커뮤니티 기반 검증 워크플로우가 아주 복잡한 수학적 정리를 대규모 코드베이스로 정리·검증할 수 있음을 보여줍니다. 또한 증명 내보내기(export)와 독립 체커의 조합이 수학적 증명의 신뢰성을 높이는 실무적 패턴으로 자리잡을 가능성을 제시합니다.

다만 이 문건은 근거에서 제시된 검증 절차와 도구에 대한 사실을 보고할 뿐, 증명의 수학적 내용(아이디어 전개·중간 보조정리의 직관적 해석 등)을 설명하지는 않습니다. 커뮤니티 성명은 향후 수학계의 추가 해설과 재검토 활동이 이어질 것이라고 밝혔습니다.

[Hacker News에서 원문 읽기 →](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

