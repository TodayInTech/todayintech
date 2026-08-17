---
title: "Launch HN: Speko (YC S26) – OpenRouter for Voice AI"
sidebar_label: "Launch HN: Speko (YC S26) – OpenRouter for Voice AI"
---

# Launch HN: Speko (YC S26) – OpenRouter for Voice AI

> Hacker News · 2026-08-17 · Voice AI

---

Speko는 STT(음성인식), LLM, TTS로 구성되는 음성 에이전트 스택에서 최적의 모델 조합을 찾아주는 라우터형 플랫폼을 표방한다. 창업자가 현장 경험으로 반복해온 '신모델 도입 시 네이티브 평가자 모집→벤치마크→교체' 과정을 API로 자동화한다는 점을 핵심 가치로 제시한다. 사용자는 정확도·지연·비용·균형 등 최적화 기준과 언어·지역을 요청으로 보내면, Speko가 측정된 후보 모델을 필터링해 점수화하고 승자를 반환하며 공급자·모델명과 점수를 헤더로 돌려주는 흐름을 구현한다는 설명이 있다. 또한 게이트웨이가 서명된 세션 플랜을 선미리(fetch)해 새 세션에서 제어 플레인 왕복 없이 바로 제공자에 연결하도록 설계했다는 설명도 제공된다.
근거 자료에는 모델별 벤치마크 표와 비용·WER(단어오류율) 수치가 포함돼 기술적 신뢰성을 보강한다. Universal-3.5 Pro, GPT-4o Transcribe, GPT-4o-mini Transcribe, Realtime STT-1, Velma 등 다수 모델이 비교 목록에 올라 있으며, 비용($/분)과 WER 예시가 함께 제시된다. Speko는 OpenAI API 호환 인터페이스를 제공해 기존 프레임워크와의 통합을 쉽게 하고 있으며(예: LiveKit 에이전트용 코드·model:'auto' 설정 예시), 연결 실패 시 세션 설정 단계에서만 후보로 폴백(failover)하는 동작을 설명해 실전 운영의 레이턴시·신뢰성 고려도 드러난다. 기술 독자에게는 다중 공급자·다중 모델 환경에서 자동화된 벤치마크·라우팅이 비용·정확도·운영 복잡성 트레이드오프를 줄이는 실무적 의미가 있는 제안으로 보인다.

[Hacker News에서 원문 읽기 →](https://speko.ai/)

