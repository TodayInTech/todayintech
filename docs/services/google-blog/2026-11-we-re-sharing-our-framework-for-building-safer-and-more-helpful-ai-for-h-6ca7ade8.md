---
title: "We're sharing our framework for building safer and more helpful AI for health."
sidebar_label: "We're sharing our framework for building safer and more helpful AI for health."
description: "Google은 의료용 AI 평가를 위한 백서와 프레임워크를 공개했다. **정확성·안전성·유용성** 세 영역을 기준으로 폐쇄형 벤치마크, 자동평가기(autoraters), 전문가 인력 리뷰를 결합해 일반·고위험 시나리오를 평가한다고 밝혔다."
---

# We're sharing our framework for building safer and more helpful AI for health.

> Google Blog · 2026-11-04 · Health

---

Google이 의료용 AI를 평가하기 위한 **엔드투엔드 평가 프레임워크**와 백서를 공개했다. 백서에는 모델을 세 가지 평가 영역 — **정확성(accuracy)**, **안전성(safety)**, **유용성(usefulness)** — 으로 나눠 검증하는 접근법을 제시하며, 폐쇄형(정답이 명확한) 질문 기반 벤치마크, 자동평가기(autoraters), 그리고 전문가의 인간 리뷰를 결합해 일반적인 상황과 **고위험(health high-risk)** 시나리오를 모두 점검한다고 Google은 밝혔다. 이 작업은 Google이 자체 모델을 평가·운영하는 데 실제로 사용하고 있는 프레임워크라고 명시되어 있다.

## 평가 범주와 사용된 방식
Google은 세 영역을 명시적으로 구분해 평가 대상을 체계화했다는 점을 핵심으로 내세웠다. 백서에 따르면 평가 방식은 정량화 가능한 폐쇄형 벤치마크로 기본적 정확도를 측정하고, 자동화된 평가 도구로 보다 넓은 경우를 빠르게 스크리닝하며, 전문가 리뷰로 맥락과 잠재적 위험(예: 잘못된 의료 조언이 초래할 수 있는 해악)을 검토하는 방식으로 설계되어 있다. 원문은 이 조합을 통해 일반적 응답 품질과 고위험 응답의 안전성을 모두 점검할 수 있다고 설명한다.

## 실무적 의미
Google이 이 프레임워크를 공개한 목적은 투명성 제고와 의료 생태계(개발자·연구자·임상의)를 지원하는 데 있다고 회사는 밝혔다. 확인된 사실만 놓고 보면, 이 프레임워크는 의료 AI의 여러 활용 사례를 비교적 구조화된 방식으로 평가할 수 있는 공통 틀을 제공한다. 기술팀과 연구자는 백서에 제시된 세 영역과 평가 구성요소를 참조해 자체 검증 절차를 설계하거나 비교 기준으로 활용할 수 있다. 다만 제공된 근거는 프레임워크의 구체적 메트릭, 데이터셋, 통계적 문턱값, 또는 공개된 도구·코드의 유무 등 세부 사항은 포함하고 있지 않다.

Google은 백서를 통해 이 접근법을 공유함으로써 업계 전반의 평가 관행 논의에 기여하려는 의도를 밝히고 있다. 보다 구체적인 도입·검증 절차나 재현 가능한 방법론을 확인하려면 백서 전문을 직접 검토해야 한다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/health/evaluating-health-ai-at-scale/)

