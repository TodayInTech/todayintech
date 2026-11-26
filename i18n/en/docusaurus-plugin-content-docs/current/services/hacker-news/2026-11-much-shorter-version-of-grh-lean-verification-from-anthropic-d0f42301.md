---
title: "Much shorter version of GRH Lean verification from Anthropic"
sidebar_label: "Much shorter version of GRH Lean verification from Anthropic"
description: "Anthropic 참여로 제작된 Lean 4 기계검증 버전의 리만 가설·일반화 리만가설 증명 저장소가 공개됐다. **grh(약 300,000행)**과 **grh-compact(약 76,000행)** 두 버전이 있으며, **Lean v4.35.0**과 **Mathlib(commit 56a00585)**가 필요하고 기계검증만 완료됐으며 인간 검토나 논문은 없다."
---

# Much shorter version of GRH Lean verification from Anthropic

> Hacker News · 2026-11-25 · formal_verification

---

Anthropic과 Claude 협업으로 제작되었다고 명시된 Lean 4 형식 증명물이 GitHub에 공개됐다. 저장소는 **리만 가설(Riemann Hypothesis)**과 **Dirichlet L-함수에 대한 일반화 리만 가설(Generalized Riemann Hypothesis, GRH)**의 Lean 4 증명을 포함한다고 되어 있으며, 원저는 Levent Alpöge의 작업을 기반으로 했다고 밝힌다. 저작권·라이선스는 **Apache 2.0, Copyright 2026 Anthropic, PBC**로 표기되어 있다(각 폴더의 LICENSE, NOTICE, ATTRIBUTION.md 확인 가능).

## 배치·구성
근거 문서에 따르면 저장소는 두 가지 판본을 담고 있다: 읽기 쉬운 판본인 **grh/**(약 **300,000행**)과 더 압축된 **grh-compact/**(약 **76,000행**)이 각각 독립적인 Lake 프로젝트로 구성되어 있다. 빌드 요구사항은 **Lean v4.35.0**과 **Mathlib(커밋 56a00585)**이며, 명시된 빌드 명령은 다음과 같다:

lake exe cache get
lake build
lake env
lean scripts/PrintAxioms.lean

빌드 시간 예시는 **12코어·24GB 메모리** 환경에서 1~2시간(만약 Mathlib 캐시가 없으면 약 85분이 더 소요될 수 있음)이다.

## 검증 범위와 한계
저장소 자체 문구에 따르면 이 증명은 **기계 검증(passed machine checks)만 완료**된 상태다. 중요한 점은 "어떤 수학자도 전체를 읽어보지 않았고, 증명과 함께 제출된 논문(paper)은 없다"는 명시다. 또한 이 레포는 "Research artifact. Not maintained and not accepting contributions."로 표시되어 있어 유지·기여 계획이 없음을 밝힌다.

분석: 기계검증이 이루어졌다는 사실은 형식화(formalization)와 자동화 도구의 진전이라는 기술적 의미를 가진다. 그러나 인간의 수학적 검토와 동료심사(peer review)가 부재하므로, 학계에서 통상 요구하는 검증 수준(논문·전문가 리뷰)을 아직 충족했다고 보기는 어렵다.

## 실무적 의미(개발자·형식화 담당자 관점)
- 재현을 위해서는 명시된 **Lean·Mathlib 버전**을 정확히 맞춰야 하므로 환경 고정이 필수다. 빌드 명령과 시간·리소스 추정은 실무적 테스트 계획 수립에 직접 활용할 수 있다. 
- 저장소가 유지되지 않으므로 장기적 의존(예: 다른 형식화 프로젝트의 기반으로 삼는 것)은 추가 검토가 필요하다(분석). 
- 라이선스는 Apache 2.0으로 공개되어 있어 코드·형식화 산출물의 재사용 가능성은 열려 있다.

원문 근거는 저장소의 README와 각 폴더 안내에 한정되어 있으며, 인간 검토 결과나 학술적 승인 여부는 제공된 근거에 포함되지 않는다.

[Hacker News에서 원문 읽기 →](https://github.com/lsernau/grh-lean)

