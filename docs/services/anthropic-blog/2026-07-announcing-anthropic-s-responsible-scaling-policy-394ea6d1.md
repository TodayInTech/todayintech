---
title: "Announcing Anthropic's Responsible Scaling Policy"
sidebar_label: "Announcing Anthropic's Responsible Scaling Policy"
---

# Announcing Anthropic's Responsible Scaling Policy

> Anthropic Blog · 2026-07-03 · AI 안전/정책

---

Anthropic은 'Responsible Scaling Policy(RSP)'를 발표하고, 개발되는 AI 시스템의 재앙적(catastrophic) 위험을 관리하기 위한 기술·조직적 프로토콜을 제시했다. 핵심은 AI Safety Levels(ASL)라는 등급 체계로, 생물안전(BSL) 표준을 느슨하게 본떠 모델의 재앙적 위험 잠재력에 맞춘 안전·보안·운영 기준을 요구한다. 예컨대 ASL-1은 의미 있는 재앙적 위험이 없는 시스템을, ASL-2는 생물무기 제조 같은 위험 지시가 일시적이거나 신뢰성이 부족해 실용적이지 않은 초기 위험 신호를 보이는 현행 LLM 수준으로 규정하며(Anthropic은 Claude 등 현행 모델을 ASL-2로 봄), ASL-3는 비(非)AI 기준보다 재앙적 오용 위험을 크게 높이거나 저수준 자율성을 보이는 경우로 엄격한 조치와 더 강한 보안·검증을 요구한다. ASL-4 이상은 아직 정의되지 않았지만 자율성·오용 가능성의 질적 상승을 수반할 것으로 예고한다.
RSP는 또한 실무적 운용 원칙을 제시한다. 등급 체계는 안전 절차를 충족하지 못할 경우 훈련을 일시 중단할 수 있는 메커니즘을 포함하되, 동시에 안전 기술을 해결하면 더 강력한 모델 확장을 허용하는 인센티브를 만들어 '경쟁의 상향화(race to the top)'를 유도하려는 설계다. Anthropic은 이 정책이 현재 Claude의 사용이나 제품 가용성을 변경하지 않는다고 밝히며, 이사회 승인 및 Long Term Benefit Trust와의 협의를 거친 절차적 안전장치와 ARC Evals의 평가 협력을 근거로 정책을 마련했다고 밝혔다. 또한 ASL-3 준수를 위해 세계 수준의 레드팀에 의한 적대적 테스트에서 의미 있는 재앙적 오용 위험이 드러나면 배포를 하지 않겠다는 약속과, ASL-4에서 요구될 수 있는 기구적 해석(interpretability) 기반 증명 등 아직 해결되지 않은 연구 문제들이 정책 설계에 반영되어 있다는 점에서 기술적·정책적 함의를 지닌다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)

