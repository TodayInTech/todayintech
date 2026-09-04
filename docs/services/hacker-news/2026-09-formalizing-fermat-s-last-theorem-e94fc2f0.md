---
title: "Formalizing Fermat's Last Theorem"
sidebar_label: "Formalizing Fermat's Last Theorem"
---

# Formalizing Fermat's Last Theorem

> Hacker News · 2026-09-04 · 수학/형식증명

---

Anthropic는 Claude라는 대형 언어 모델이 11일 동안 거의 자율적으로 작업해 Lean 증명 보조기(Proof assistant)로 페르마의 마지막 정리(FLT)를 처음으로 완전하게 컴퓨터 검증 가능한 형태로 형식화(formalize)했다고 발표했다. 이 과정에서 Claude는 1,300만 줄의 Lean 코드와 최종 증명에 사용된 약 2만9,500개의 중간 정리를 포함해 총 3만300여 정리를 생성했고, 결과물은 Lean에 의해 표준 공리만으로 확인되었으며 Mathlib의 FLT 명세와도 일치한다고 보고되었다. 증명은 Darmon·Diamond·Taylor의 Wiles 정리 해설을 단순화한 전개를 따랐고, 인간의 개입은 Tianyi Peng의 고수준 지시로 제한되었으며 초기 실패 시도들이 최종 코드의 약 7%를 차지했다.
기술적으로 이 성과는 대형 자동화 형식증명이 복잡한 현대 수학 정리에 실질적으로 적용될 수 있음을 보여준다. Prove2Me라는 협업 플랫폼과 다중 에이전트 허브를 결합해 약 60억 출력 토큰을 소모한 내부 모델(Claude Fable 5에 상응)로 작업을 조직했고, 이 증명은 Mathlib보다 5배 이상 큰 단일 최종 산출물로서 현재까지 만든 Lean 증명 중 최대 규모라는 점도 주목된다. Anthropic 측은 이는 새로운 수학적 발견이 아니라 '검증'에 해당한다고 명확히 했고, 자동 형식증명은 심사 부담 경감과 AI 생성 수학 결과의 신뢰성 확보에 기여할 수 있다고 전망한다. 다만 이번 성공은 기존 Mathlib, Prove2Me 같은 인프라와 대규모 토큰·에이전트 협업에 의존한 사례라는 점을 근거로 향후 적용 범위와 실무적 표준화 과정이 남아 있음을 암시한다.

[Hacker News에서 원문 읽기 →](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

