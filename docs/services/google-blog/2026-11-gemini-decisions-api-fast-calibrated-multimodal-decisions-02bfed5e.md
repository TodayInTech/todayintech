---
title: "Gemini Decisions API: Fast, calibrated multimodal decisions"
sidebar_label: "Gemini Decisions API: Fast, calibrated multimodal decisions"
description: "Google은 Gemini Decision 1을 지원하는 Gemini Decisions API를 발표했다. 단일 포워드로 멀티모달 입력(최대 256K 토큰)을 평가하고 150–250ms의 엔드투엔드 지연과 $0.10/1M 입력 토큰 요금, 출력 토큰 무과금 구조를 제시한다."
---

# Gemini Decisions API: Fast, calibrated multimodal decisions

> Google Blog · 2026-11-11 · AI

---

Google이 Gemini Decision 1(모델명: gemini-decision-1)을 기반으로 하는 **Gemini Decisions API**를 공개했다. 이 API는 생성형 응답을 토큰 단위로 생성하는 대신 후보 옵션을 한 번의 모델 포워드로 점수화해 빠르게 닫힌 선택(도구 선택, 정책 체크, 모델 라우팅, 컨텍스트 채점 등)을 반환하는 것이 핵심이다.

## 단일 포워드 멀티모달 판정
Gemini Decisions는 텍스트, 이미지, 오디오, 비디오, PDF를 하나의 공유 입력으로 받아 처리할 수 있으며, 문서에 따르면 단일 멀티모달 입력은 최대 **256K 토큰**까지 허용된다. API는 한 요청에서 최대 **1,000개의 독립 질문**을 평가할 수 있고, 각 요청은 내부에서 한 번의 forward로 후보들을 점수화해 확률과 신뢰도(0~1)를 반환한다.

## 질문 타입과 신뢰도
지원되는 질문 타입은 세 가지다: noul(예/아니오 확률), choice(2~255개 선택지의 정규화 확률과 승자), score(순서형 루브릭의 연속 가중 점수 및 레벨별 확률). 모든 답변에 신뢰도 점수가 포함되어 애매한 사례를 휴먼 리뷰나 폴백으로 라우팅하는 데 쓸 수 있다.

## 지연·비용 구조와 성능
Google은 엔드투엔드 지연을 **150–250ms**, 모델 계산의 중간값 지연을 **50–100ms**로 제시했고, 특정 벤치마크에서는 Gemini 3.5 Flash‑Lite(Interactions API) 대비 **거의 5배 비용 절감** 효과를 보였다고 밝혔다. 문서에서는 입력 토큰 기준 비용을 **$0.10 / 1M 입력 토큰**으로 명시하고 출력 토큰은 **청구하지 않는다**. 한 요청의 공유 입력은 한 번만 청구되며, 질문마다 해당 지침·기준 토큰이 추가로 청구된다고 설명한다.

## 적용 사례와 통합
Google 내부 사례로는 Gemini Notebook의 동적 모델 라우팅, Stitch의 빠른 UI 캔버스, CC의 이모지 선택, Search의 안전성 레이어 등이 제시되어 API의 저지연 제어평면(use as control plane) 역할을 강조한다. 에코시스템 통합도 공개되어 OpenRouter, LangChain, Vercel, LiteLLM 등과 연동이 진행 중이며 Google Cloud로의 지원도 곧 제공될 예정이라고 적혔다.

## 개발자 관점 실무 영향 (해석)
자료에 근거하면, 응답 생성 대신 후보 점수화 방식을 쓰는 이 API는 다수의 짧은 판단을 실시간으로 처리해야 하는 워크플로(의사결정 라우팅, 안전성 체크, 인터랙티브 UI 반응 등)에 즉시 적용 가능하다. 특히 출력 토큰 무과금과 요청당 공유 입력 한 번만 청구되는 요금 구조는 많은 선택지에 대해 빠르게 평가해야 할 경우 비용 우위를 제공할 수 있다. 다만 문서에서 성능·지연 수치는 주로 최대 16K 토큰 컨텍스트 기준으로 제시된 부분도 있어(문서 본문 참조) 대규모 컨텍스트나 특정 멀티모달 조합에서의 실제 지연·비용은 직접 테스트가 필요하다.

## 빠른 시작
Google AI Studio에서 API 키를 발급받아 시도할 수 있으며, 문서에 Python/JavaScript/REST 가이드와 Doorstep Parcels, Speed Sketch, Find the Zoo Keeper 데모가 제공된다고 밝혔다. 아래는 문서에 있는 Python 예시 호출의 핵심 형태다:

```python
from google import genai
client = genai.Client(http_options={"api_version": "v1beta"})
result = client.decisions.create(
  model="gemini-decision-1",
  input=[{"type":"image","uri":"https://.../spill.jpg"},{"type":"text","text":"Breakroom counter check"}],
  questions={...}
)
```

출처: Google 블로그(공식 발표).

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

