---
title: "Show HN: Yogurt – Free, private, open-source alternative to Granola"
sidebar_label: "Show HN: Yogurt – Free, private, open-source alternative to Granola"
description: "Yogurt는 MIT 라이선스의 무료 데스크톱 앱으로, whisper.cpp·llama.cpp 등 온디바이스 OSS 모델을 이용해 회의 녹취·요약·질의응답을 제공하며, 데이터가 컴퓨터를 떠나지 않는 로컬 우선 설계를 표방합니다. HN에서 176점·80댓글의 관심을 받았습니다."
---

# Show HN: Yogurt – Free, private, open-source alternative to Granola

> Hacker News · 2026-11-11 · 오픈소스·프라이버시

---

Yogurt는 MIT 라이선스 기반의 무료 데스크톱 애플리케이션으로, **온디바이스 AI 모델로 회의를 녹취하고 요약하며 대화형으로 검색·질의응답이 가능**하다고 피드 설명에 나옵니다. Granola와 유사하게 통화에 직접 참여하지 않고 백그라운드에서 동작하지만, 제공된 정보에 따르면 Yogurt는 오픈소스이고 회의 기록·전사·요약이 사용자의 컴퓨터를 벗어나지 않는다고 강조합니다.

피드에는 크로스플랫폼을 위해 Electron을 사용하고, 전사에는 whisper.cpp·시스템별로는 Apple의 SpeechAnalyzer를 지원한다고 명시되어 있습니다. 회의 요약·질의응답은 로컬 오픈 가중치 LLM을 llama.cpp로 내려받아 동작시키는 방식이며, 필요하면 로컬 MCP 서버를 통해 Anthropic·OpenAI 등 외부 모델로 공유할 수 있다고 합니다. 또한 캘린더 통합, 에코 감지·감소, 폴더/로컬 수준 검색, 자동 녹음 종료 같은 기능들을 신경썼다고 설명합니다.

데모 영상 링크가 포함되어 있고(HN 포스트 기준), Hacker News에서 176점, 80개의 댓글로 반응이 있었습니다. 피드 메타데이터 기준으로는 이들 기술·설계 선택과 주요 기능들이 확인되지만, 배포판 세부 버전·라이선스 예외·보안 구현 세부사항 등은 제공된 요약에 포함되어 있지 않습니다.

[Hacker News에서 원문 읽기 →](https://github.com/FrigadeHQ/yogurt)

