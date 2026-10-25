---
title: "Gemini Omni 1.1 Flash lets you build with more control"
sidebar_label: "Gemini Omni 1.1 Flash lets you build with more control"
---

# Gemini Omni 1.1 Flash lets you build with more control

> Google Blog · 2026-08-27 · AI 개발자 도구

---

Gemini Omni 1.1 Flash는 개발자용 창작 제어와 생성형 비디오 기능을 확장해 ‘실무용(production-ready)’ 워크플로를 목표로 한다. 이번 업데이트는 Omni가 제공하던 현실적 추론 능력을 바탕으로, API를 통해 장면 연장(scene extension), 시작·종료 프레임 지정, 비디오 참조의 멀티모달 입력 등 구체적 제어를 가능하게 만든다. 특히 장면 연장은 이전 모델의 마지막 1초 참조에서 확장돼 최대 10초의 이전 맥락을 분석할 수 있고, 10초 단위로 누적 최대 40초까지 영상을 이어 생성할 수 있어 보다 긴 서사와 시각적 일관성 유지에 유리하다. 예시 코드에는 genai.Client의 interactions.create 호출과 model="gemini-omni-1.1-flash", previous_interaction_id 파라미터 사용이 포함돼 개발자 통합 방법을 직접 보여준다.
생산성 측면에서는 360p 초안 생성이 표준 720p 대비 최대 60% 빠르고 비용은 3분의 1 수준으로 제시돼 스토리보드·프로토타이핑 단계의 반복을 빨리 돌릴 수 있다. 반면 고해상도 출력도 지원해 1080p·4K 업스케일을 통해 최종 제작용 결과물을 얻을 수 있으며, 최대 3초짜리 비디오 레퍼런스를 넣어 캐릭터·장면 콘시스턴시를 유지하는 멀티모달 입력이 가능하다. 이들 기능은 생성형 비디오를 기존 편집·미디어 툴의 워크플로에 통합하거나, 프로토타이핑과 고해상도 최종 산출물을 함께 요구하는 애플리케이션에 실질적 이점을 준다. Omni 1.1은 Google AI Studio, Agent Platform API, Google Flow(유료 구독자 대상)를 통해 배포되며 문서·쿡북·프롬프트 가이드도 제공된다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

