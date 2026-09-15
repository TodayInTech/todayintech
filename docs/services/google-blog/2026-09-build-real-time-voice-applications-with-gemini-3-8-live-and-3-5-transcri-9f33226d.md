---
title: "Build real-time voice applications with Gemini 3.8 Live and 3.5 Transcribe"
sidebar_label: "Build real-time voice applications with Gemini 3.8 Live and 3.5 Transcribe"
---

# Build real-time voice applications with Gemini 3.8 Live and 3.5 Transcribe

> Google Blog · 2026-09-15 · 인공지능·개발자 도구

---

구글은 실시간 음성 중심 애플리케이션을 겨냥한 새로운 모델군을 공개하며 개발자 도구를 확장했다. Gemini 3.8 Live와 3.8 Live Extended Thinking은 대화의 흐름을 유지하면서 배경에서 API·툴 호출을 실행하는 비동기 함수 호출, 실시간 시각 입력을 활용한 컨텍스트 결합, 확인 코드·청구번호 등 알파벳·숫자 조합의 정밀 파싱, 97개 이상 언어의 악센트 일관성 등 실무 중심 기능을 나열한다. 특히 Extended Thinking은 복수 단계의 복잡한 추론을 백그라운드에서 수행하면서 메인 대화에서 진행 상황을 서술하거나 응답을 계속한다는 점을 강조하며, 이전 라이브 모델과 비교해 계단식(cascaded) 아키텍처를 대체할 수 있는 더 직접적인 처리 흐름을 제시한다고 설명한다.
음성→텍스트 전용 모델 Gemini 3.5 Transcribe는 85개 이상 언어를 지원하며 스트리밍 환경에서 평균 WER 4.0%, 비스트리밍에서 2.6%를 기록한 점을 근거로 저지연 고정밀 전사 엔진을 표방한다. 자동 코드스위칭, 최대 1,000개 용어의 사용자 사전 편향(custom_vocabulary), 불필요 어미·채우기 말 제거 등 '스마트 전사' 모드를 통해 가독성 높은 결과를 내며, Interactions API를 통해 최대 1시간 분량 오디오의 타임스탬프·화자 라벨링 전사도 지원한다. 이들 모델은 실시간 캡셔닝, 콜센터 자동화, 오디오 분석 같은 적용 맥락에서 지연과 정확성 사이의 균형을 재정의할 수 있으며, ai.studio/live에서 직접 시험해보고 GitHub 샘플 앱이나 라이브 API 스킬로 통합해 개발에 활용할 수 있다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)

