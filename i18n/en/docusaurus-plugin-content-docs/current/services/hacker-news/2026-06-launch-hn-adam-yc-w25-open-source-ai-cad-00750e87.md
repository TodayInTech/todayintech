---
title: "Launch HN: Adam (YC W25) – Open-Source AI CAD"
sidebar_label: "Launch HN: Adam (YC W25) – Open-Source AI CAD"
---

# Launch HN: Adam (YC W25) – Open-Source AI CAD

> Hacker News · 2026-06-17 · AI CAD

원문 링크: [Launch HN: Adam (YC W25) – Open-Source AI CAD](https://github.com/Adam-CAD/CADAM)

---

피드 기준으로는 Adam(YC W25)이 만든 CADAM이라는 오픈소스 Text→CAD 플랫폼을 공개했습니다. 자연어와 이미지 참조로 파라메트릭 3D 모델을 생성하고, OpenSCAD 코드와 자동 추출된 파라미터를 슬라이더로 노출해 즉시 치수를 조정할 수 있다고 합니다.
제공된 정보만 보면 구현은 React 프런트엔드와 Supabase 백엔드로 구성되어 있고, OpenSCAD를 WebAssembly로 컴파일해 브라우저에서 렌더링합니다. 모델은 Vercel AI SDK를 통해 Anthropic·Google·OpenAI 등 여러 백엔드를 지원하며, 간단한 파라미터 변경은 정규식 기반으로 LLM 호출 없이 처리된다고 합니다.

## 핵심 포인트

- 자연어/이미지 입력으로 파라메트릭 3D 모델을 생성하고 OpenSCAD 코드로 출력함.
- 브라우저 내 WebAssembly OpenSCAD + React Three Fiber로 실시간 렌더링을 지원함.
- Vercel AI SDK 기반으로 모델-중립적이며, 간단한 파라미터 수정은 LLM 호출 없이 처리됨.

## 읽어볼 만한 이유

오픈소스 텍스트→코드→CAD 워크플로를 제시해 CAD 자동화와 브라우저 기반 설계 툴 발전에 영향을 줄 수 있습니다.

## 확인할 점

- 피드 기준으로는 코드 품질·라이선스·스케일링 관련 상세 정보는 확인되지 않습니다.
- 모델 평가(예: Gemini 3.1 Pro 우위)와 성능 비교는 원문·리포지토리에서 직접 검증이 필요합니다.

## 문서 정보

- 수집일: 2026-06-17T23:20:48.105084+00:00
- 후보 ID: `hacker-news:00750e87d1af6fa5`
- 후보 점수: 72.8
- 편집 상태: `published`
- 생성 방식: `llm`

