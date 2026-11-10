---
title: "Muse Ember: Our smallest, most efficient model"
sidebar_label: "Muse Ember: Our smallest, most efficient model"
description: "Meta가 에이전트와 반복적 코딩 작업에 최적화된 소형 모델 **Muse Ember(muse-ember-1.0)**을 공개했습니다. 1M 토큰 컨텍스트·512K 출력, 입력 $0.10/M·출력 $0.50/M 등 가격과 내부 벤치마크(예: AutomationBench-AA 37.8, Agents' Last Exam 61.6)를 통해 비용 대비 효율을 강조합니다."
---

# Muse Ember: Our smallest, most efficient model

> Hacker News · 2026-11-09 · AI 모델 출시

---

Meta가 새 소형 모델 **Muse Ember (muse-ember-1.0)**을 공개했다. 이 모델은 반복적인 에이전트 작업과 세부 코딩 서브태스크를 겨냥해 **대량 호출에 대한 비용 효율성**과 멀티모달 처리 능력을 중심으로 설계됐다. Meta는 Muse Ember가 Claude Haiku 5.5나 GPT-6 Luna보다 동일 또는 낮은 비용에서 더 높은 지능 대비 성능을 낸다고 밝히며, 내부 벤치마크와 가격을 함께 제시했다.

## 핵심 특징: 컨텍스트·출력 한계와 가격

- 모델 식별자: **muse-ember-1.0** (Meta Model API, Muse Code에서 제공)
- 컨텍스트 윈도우: **1,000,000 토큰**
- 최대 출력: **512,000 토큰**
- 가격(공식): **입력 $0.10 / 1M 토큰**, **캐시된 입력 $0.004 / 1M 토큰**, **출력 $0.50 / 1M 토큰**
- Meta는 인공분석(Artificial Analysis) 기준으로 Muse Ember의 작업당 비용을 약 **$0.14** 수준으로 제시했다.

위 수치들은 모델을 큰 문서나 전체 코드베이스를 한 번에 넣어 처리하거나, 에이전트가 수백 번 호출하는 짧은 단계들을 반복 처리하는 워크플로에 적합하다는 점을 직접적으로 뒷받침한다.

## 평가 결과(선택적 벤치마크 수치)

Meta가 공개한 내부/공개 벤치마크 중 일부 결과(최대 추론 모드 기준)는 다음과 같다. 수치는 원문 표에 제시된 모델별 '점수'다.

- AutomationBench-AA: **Muse Ember 37.8%** vs GPT-6 Luna 20.2% vs Claude Haiku 13.9%
- Agents' Last Exam: **Muse Ember 61.6%** vs GPT-6 Luna 57.1% vs Claude Haiku 57.0% (리눅스 하위셋 기준)
- Personal Superintelligence Index: **Muse Ember 46.8%** vs GPT-6 Luna 37.0% vs Claude Haiku 36.1%
- Terminal-Bench 4.0(코딩): **Muse Ember 40.9%** vs Claude Haiku 39.2% vs GPT-6 Luna 16.4%
- Coding Agent Index-AA: **Muse Ember 46** vs Claude Haiku 37 vs GPT-6 Luna 31
- FrontierCode 2.0-AA(가장 어려운 문제): Claude Haiku 34.9 &gt; Muse Ember 27.2 &gt; GPT-6 Luna 25.2 (Meta는 가장 난제에는 Muse Wonder와 조합 권장)
- 멀티모달/시각·문서 과제: GDP.pdf-AA는 Muse Ember 22.8(동률로 GPT-6 Luna), PerceptionBench는 Muse Ember 80.6 등

문서에는 또한 '같은 지능 수준에서 Haiku의 최고 점수를 약 1/3 비용으로 맞추고, 모든 Luna 설정을 능가한다'는 요약형 주장과, 인공분석 인텔리전스 대 비용 그래프의 요약치들이 포함되어 있다.

## 왜 주목해야 하는가: 설계 목표와 실무적 영향

Muse Ember의 설계는 '에이전트가 반복해서 호출하는 작은 단계들'과 '긴 문서·코드베이스를 한 번에 처리하는 단일 호출'을 모두 겨냥한다. 실제 의미는 다음과 같다:

- 반복 호출 비용 감소: 에이전트 기반 자동화가 수천~수만 건의 짧은 도구 호출을 필요로 할 때, 단위 작업 비용이 낮으면 전체 운영비용에서 실질적 절감이 가능하다(문서의 주장).
- 대용량 문서·코드 처리: **1M 토큰 컨텍스트**와 **512K 출력**은 대형 코드베이스나 문서 묶음을 한 번에 넣어 분석·수정·요약하는 워크플로에 직접적으로 유리하다.
- 멀티모달 단일 모델: 텍스트·이미지·오디오·비디오를 네이티브로 처리하므로 별도 모델 체인 없이 스크린샷·녹음·스캔 문서 등을 에이전트가 다룰 수 있다.

실무적으로는 에이전트 중심 자동화(계약 검토, 연속적 코드 수정·테스트, 도구 연동 작업)에서 Muse Ember를 비용 효율적인 옵션으로 시험해볼 근거가 제시돼 있다. 다만 Meta는 FrontierCode 같은 '가장 어려운 문제'에 대해서는 Muse Wonder와 조합하라고 권장해 모델별 역할 분담을 명확히 하고 있다.

## 안전성과 배포

Meta는 Muse Ember를 **Meta Superintelligence Scaling Framework** 하에서 화학·생물학·사이버보안·통제 상실 위험을 평가했으며, '평가된 범주들에서 고위험 임계값을 넘지 않았다'고 보고했다. 또한 사용자 대행 행동(의도 준수, 민감 정보 처리, 외부 지시 유입 방지, 고영향 행동 전 휴먼 인풋 요구 등)에 대한 평가를 실시했다고 명시되어 있다. 이는 모델이 소형이라도 동일한 핵심 안전 훈련·테스트를 거쳤다는 근거로 제시된다.

가용성 측면에서 Muse Ember는 Meta Model API와 Muse Code에서 제공되며, Google Cloud와 Oracle Cloud에서도 이용 가능하다고 밝혔다.

---

사실과 해석을 구분하면, 문서에 제시된 숫자와 가격·용량은 확인 가능한 근거다. '비용 대비 우수함'이라는 주장은 Meta의 내부 벤치마크(Artificial Analysis)와 비용 추정에 근거한 비교 요약으로 제시되어 있어 외부 독립 평가나 실제 운영 환경에서의 비용/성능은 다를 수 있다. 본 보도는 Meta가 공개한 자료와 표에 기초해 변경 사항과 실무적 의미를 정리했다.

[Hacker News에서 원문 읽기 →](https://research.meta.ai/blog/muse-ember)

