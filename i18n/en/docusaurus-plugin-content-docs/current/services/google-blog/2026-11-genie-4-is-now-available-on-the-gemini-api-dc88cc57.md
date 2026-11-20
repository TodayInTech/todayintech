---
title: "Genie 4 is now available on the Gemini API."
sidebar_label: "Genie 4 is now available on the Gemini API."
description: "Genie 4가 Gemini API(Interactions API)와 Google AI Studio에 공개되어 텍스트·참조 이미지로 연속 720p(24fps) 월드를 네이티브 오디오와 함께 생성하고 실시간 키보드·텍스트 제어로 환경을 조작할 수 있게 되었습니다. 모든 출력에는 imperceptible SynthID 워터마크가 포함됩니다."
---

# Genie 4 is now available on the Gemini API.

> Google Blog · 2026-11-19 · Developer tools

---

Google은 Genie 4를 Gemini API(Interactions API)를 통해 개발자에게 제공한다고 발표했다. 텍스트 프롬프트나 참조 이미지를 시작점으로 **연속적인 720p(24fps) 월드**를 네이티브 오디오(앰비언트·효과·대사 포함)와 함께 생성할 수 있으며, 실시간 키보드 입력과 라이브 텍스트 프롬프트로 환경을 탐색하고 날씨·조명·오브젝트·이벤트를 즉시 변경할 수 있다. 

## 상호작용 가능 월드와 상태 일관성
Genie 4는 실시간 제어와 함께 작동하도록 설계되었고, Google은 **Gemini의 추론 능력**이 월드 상태를 일관성 있게 유지한다고 설명한다. 이는 단순한 정적 이미지 생성이 아니라 사용자 입력에 따라 환경 상태가 연속적으로 유지되는 인터랙티브 프로토타입을 구축할 수 있다는 뜻이다. 실무적으로는 인터랙티브 경험 프로토타이핑, 공간 개념 시각화, 로보틱스·AI 에이전트 훈련 같은 케이스에서 즉각적인 환경 조작과 오디오 피드백을 한 환경에서 실험할 수 있게 된다.

## 오디오·워터마킹·실행 경로
모델 출력은 네이티브 오디오를 포함하도록 설계되어 대화나 효과를 동기화할 수 있으며, Google은 모든 출력에 **imperceptible SynthID 워터마크**를 포함한다고 명시해 생성물의 출처 표시에 대한 기술적 조치가 적용됨을 알렸다. 개발자는 Google AI Studio의 인터랙티브 캔버스와 스타터 앱으로 실습해볼 수 있고, Gemini API 문서와 가격 정보를 검토해 시작하라고 안내되어 있다.

## 개발자 관점의 실무 영향
근거에 따른 직접적 변화는 (1) Genie 4를 API와 스튜디오에서 바로 호출해 상호작용형 720p 환경을 생성·제어할 수 있다는 점, (2) 월드 상태 유지와 오디오 동기화가 통합되어 별도 오디오·동기화 레이어를 만들 필요가 줄어든다는 점, (3) 출력에 워터마크가 자동 포함된다는 점이다. 이들 변화는 프로토타이핑 속도를 높이고 단일 워크플로에서 시각·청각 피드백을 검증하는 데 유용하지만, 근거는 가격·요금제 세부사항과 API 사용 제한(예: 호출당 처리 시간, 동시 연결 수 등)을 명시하지 않으므로 실제 운영 도입 전에는 문서와 가격정보를 확인해야 한다.

출시 경로로는 Gemini API(Interactions API)와 Google AI Studio가 명시되어 있으며, Google은 개발자에게 인터랙티브 캔버스와 스타터 앱 사용을 권장하고 있다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/)

