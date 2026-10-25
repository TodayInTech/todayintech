---
title: "Testing and mitigating elections-related risks"
sidebar_label: "Testing and mitigating elections-related risks"
---

# Testing and mitigating elections-related risks

> Anthropic Blog · 2026-10-19 · AI 안전·거버넌스

---

Anthropic은 2024년 선거 주기 대응을 위해 전문가의 심층 수동 테스트(Policy Vulnerability Testing, PVT)와 대규모 자동화 평가를 결합한 검증·완화 프로세스를 소개한다. PVT는 외부 주제 전문가와 함께 실제·적대적 시나리오를 만들어 모델 출력의 정확성·편향·정책 위반 가능성을 정성적으로 파악하고, 그 결과를 바탕으로 우선 보완 항목을 도출한다. 수작업 중심인 PVT의 심도는 중요한 인사이트를 제공하지만 확장성이 낮다는 한계가 있어, PVT에서 드러난 행태를 바탕으로 수백~수천 건의 문항을 생성하는 자동화 평가를 병행해 폭넓은 커버리지를 확보한다고 설명한다. 자동화 평가 샘플 검토에서 64문항 중 89%가 관련성이 있는 것으로 확인되는 등 정확성 검증 절차도 병행하고 있다.
이들 테스트는 실제 완화책 설계와 효과 측정에 직접 연결된다. 예컨대 시스템 프롬프트에 지식 컷오프(2023년 8월)를 명시한 개입은 관련 지표에서 47.2% 개선을 보였고, 권위 있는 출처로의 참고 유도를 보상하는 파인튜닝은 출처 제시 빈도를 10.4% 끌어올렸다. 이 밖에도 약 10개의 구체적 완화 조치를 도입하고, 사용자 탐지 시 미국은 TurboVote, EU는 유럽의회 안내로 리다이렉트하는 UX 개입을 병행했다. Anthropic은 단일 대책에만 의존하지 않는 ‘스위스 치즈 모델’을 채택해 다층 방어를 구축한다고 밝히며, 테스트를 반복해 개입의 유의미한 효과를 재검증하는 순환적 검증 체계를 강조한다. 전반적으로 원문은 방법론과 계량적 결과를 함께 제시해 모델 거버넌스와 선거 관련 리스크 경감에 실무적으로 참고할 만한 자료를 제공한다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/testing-and-mitigating-elections-related-risks)

