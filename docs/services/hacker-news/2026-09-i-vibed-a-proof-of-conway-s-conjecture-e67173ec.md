---
title: "I vibed a proof of Conway's conjecture"
sidebar_label: "I vibed a proof of Conway's conjecture"
---

# I vibed a proof of Conway's conjecture

> Hacker News · 2026-09-18 · Mathematics · AI-assisted formal proof

---

한달간의 개인적 노력과 대량의 토큰 소비 끝에 작성자는 Lean으로 정형화한 ‘Conway의 정제(refinement) 추측’ 증명을 얻었다고 보고한다. 추측은 ‘omnific 정수들에 대해 ab = cd이면 a,b,c,d를 각각 쪼개어 공통의 재조합을 만들 수 있다’는 내용으로, 서롤 수(surreal numbers)와 그 정수 부분인 omnific 정수의 구조적 성질을 다룬다. 저자는 증명이 Palomar 레지스트리의 기계적 검사를 통과했고 Lean과 분야에 익숙한 일부에게서 진술이 타당해 보인다는 평가를 받았지만, 독립적 수학자 검증은 아직 이루어지지 않았고 Lean 커널 버그 의존 여부를 점검해야 한다고 명확히 밝힌다.
기술적 서술에서는 AI와 정형검증의 결합 과정이 중심이다. Claude에게 연구 주제를 고르게 한 뒤 초기 Claude 출력이 과장된 금속어와 발명된 용어로 일관성이 떨어지자 저자는 ChatGPT(‘Sol’)로 전환했고, 회의적·검증적 세션을 반복하며 유효한 아이디어를 골라 포킹(forking) 전략으로 통합했다. 이후 로컬 Codex를 내려받아 여러 역할의 에이전트(PM, Math, Red)를 운용해 증명 개발과 반박 검토를 병행했다는 점이 강조된다. 전체적으로 이 사례는 대형 언어 모델의 환각과 과장된 서술을 기계적 정형검증 도구로 보완해 실질적 결과를 도출한 예로, AI-인간 협업, 워크플로우 설계, 형식화(formalization)의 실제 한계와 가능성을 보여준다.

[Hacker News에서 원문 읽기 →](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/)

