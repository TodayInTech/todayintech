---
title: "We’re launching Humanity’s First Exam and a Kaggle hackathon to test LLM reliability."
sidebar_label: "We’re launching Humanity’s First Exam and a Kaggle hackathon to test LLM reliability."
description: "Google은 LLM의 일관된 답변 능력을 평가하는 벤치마크 'Humanity’s First Exam(HFE)'을 카글에 공개했다. 데이터셋은 **544개** 텍스트·이미지 프롬프트(20개 역량)로 구성되며, 커뮤니티용 3주 카글 대회는 **12월 15일**까지 열린다."
---

# We’re launching Humanity’s First Exam and a Kaggle hackathon to test LLM reliability.

> Google Blog · 2026-11-24 · AI 벤치마크

---

Google은 'Humanity’s First Exam(HFE)'이라는 새로운 공개 벤치마크와 이를 활용한 카글 해커톤을 발표했다. HFE는 **모델이 한 번이라도 문제를 풀 수 있는가**가 아니라 **항상, 약간의 변형에도 일관되게 해결할 수 있는가**에 초점을 맞춘 점이 핵심 변화이다. Google은 HFE 데이터셋이 **544개의 초등 수준 텍스트·이미지 프롬프트**로 구성되어 있고, 이 프롬프트들이 **20개의 기본 역량(foundational capabilities)**을 가린다고 밝혔다.

## HFE가 측정하려는 '일관성'과 방식
HFE는 단일 정답 도달 능력 대신 모델의 재현성(reliability)을 테스트한다. Google은 지난 6개월 동안 '프론티어' 모델들이 HFE에서 유의미한 진전을 보였다고 밝혔으며, 이는 복잡한 수학·코딩·과학 능력과는 다른 실생활 질문에서의 실패 모드를 드러내기 위한 의도로 보인다. 벤치마크는 텍스트와 이미지 프롬프트를 섞어 일상적이면서도 변형 가능한 문제를 제시하며, 예시로 공개된 항목은 “List the color of the third letter of each word in the neon sign in order, separated by a semicolon.”(정답: green; yellow; white; blue; blue)처럼 직관적이지만 모델이 오답을 내기 쉬운 유형을 포함한다.

## 커뮤니티 참여와 실무적 의미
Google은 HFE의 생태계 유지를 위해 커뮤니티 참여를 권장하며, **3주간의 카글 대회(through December 15)**를 통해 사람들이 현실에서 모델이 아직 틀리는 '일상 질문'을 제출하도록 요청한다. 벤치마크와 라이브 리더보드, 기술 보고서가 함께 제공되므로 연구자와 엔지니어는 특정 역량에서의 일관성 결함을 추적하고 모델 개선 우선순위를 정하는 데 이 자료를 활용할 수 있다. 다만 게시된 근거에서는 어떤 모델들이 어떤 점수대를 기록하는지, 벤치마크의 정확한 채점 기준이나 시작일 등 세부 절차는 명시되어 있지 않다.

HFE는 실무적으로는 모델 검증 방식에 변화를 촉발할 수 있다. 특히 반복적·변형된 입력에 대한 신뢰성을 요구하는 제품(고객 지원, 정보 요약, 자동화된 이미지 분석 등)은 HFE 결과를 품질 평가 지표에 포함하는 것을 고려할 만하다. 한편 Google이 공개한 라이브 리더보드와 기술 보고서를 통해 구체적 실패 유형과 개선 방향을 확인할 수 있으므로, 모델 개선과 출시에 앞서 HFE에서의 성능을 점검하는 작업이 실무적으로 유용할 것이다.

출처: Google 블로그 발표(We’re launching Humanity’s First Exam and a Kaggle hackathon to test LLM reliability.)

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)

