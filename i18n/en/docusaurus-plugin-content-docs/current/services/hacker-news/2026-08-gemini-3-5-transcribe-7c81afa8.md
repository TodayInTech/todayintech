---
title: "Gemini-3.5-Transcribe"
sidebar_label: "Gemini-3.5-Transcribe"
---

# Gemini-3.5-Transcribe

> Hacker News · 2026-08-27 · AI/음성인식

---

Gemini 3.5 Transcribe는 구글이 발표한 최신 음성-텍스트 모델로, 잡음, 전문용어, 말의 수정과 같은 현실적 발화 문제를 다듬어 ‘정제된’ 텍스트로 직접 변환하는 것을 목표로 한다. 제품 설명에 따르면 실시간 스트리밍용(gemini-3.5-transcribe-live)과 녹음 파일 처리용(gemini-3.5-transcribe) 두 가지 API를 통해 서브초 지연의 양방향 스트리밍과 발화자 구분·단어 단위 타임스탬프를 제공한다. 모델은 자체 보정(“let’s meet Tuesday—no, Wednesday”)과 억양·충동어 제거, 자동 포맷팅을 지원하고 커스텀 용어 사전을 인식하는 기능도 제공한다.
성능 측정 결과도 함께 제시돼 기술적 의의를 판단하기 쉽다. 인공분석(Artificial Analysis) 기준으로 스트리밍 WER 4.0%, 비실시간 2.6%를 기록했으며, FLEURS 벤치마크에서는 스트리밍 5.50%, 비실시간 5.04%의 다국어 WER를 보인다고 명시돼 있다. 또한 이전 모델(Chirp 3)에 비해 최종 전사까지의 시간이 70% 개선되는 등 지연 및 정확도 측면에서 향상이 강조된다. 85개 이상의 언어 자동 감지, 최대 3명까지의 발화자 구분(3명 초과는 실험적)과 함수 호출을 통한 다른 Gemini 모델 위임 기능 등은 실시간 캡션, 음성 에이전트, 회의 분석 파이프라인 같은 개발적 응용에 직접적으로 활용 가능한 요소다. Rambler(Gboard), Gemini macOS 앱, Antigravity, 그리고 Chrome(추후) 같은 제품 통합 사례와 Agora·LangChain 등 플랫폼 파트너 사례도 제시돼 있어 개발·엔터프라이즈 도입 맥락을 판단하는 데 도움이 된다.

[Hacker News에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)

