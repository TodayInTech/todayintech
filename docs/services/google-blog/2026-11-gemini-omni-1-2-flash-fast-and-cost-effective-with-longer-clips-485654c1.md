---
title: "Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips"
sidebar_label: "Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips"
description: "Google이 Gemini Omni 1.2 Flash를 일반 공개했다. 네이티브 15초 영상 생성(3~15초 1초 단위), 멀티턴 대화식 편집, 참조 고정성 개선과 720p 초당 $0.07(Omni 1.1 대비 30% 인하)를 제공한다."
---

# Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips

> Google Blog · 2026-11-05 · AI / Video generation

---

**Gemini Omni 1.2 Flash 출시 — 더 길고 싸게, 편집은 대화하듯**

Google은 Gemini Omni 1.2 Flash를 일반 출시하며 비디오 생성 워크플로의 주요 변화를 발표했다. 제품은 **네이티브 15초** 영상 생성(기존 10초에서 확대)을 지원하고, 길이는 **3~15초를 1초 단위**로 지정할 수 있다. 또한 멀티턴(대화형) 편집을 통해 한 번 생성한 클립을 재생산하지 않고 이어서 세부를 교정하거나 배경·조명·비율을 바꿀 수 있다(Google 발표).

## 비용과 작업 흐름

가격은 Omni 1.1 대비 **30% 인하되어 720p 기준 $0.07/초**로 책정됐다. Google은 비용 최소화를 위한 권장 워크플로(초안은 360p/720p로 빠르게 생성하고, 필요한 부분만 후속 편집으로 수정한 뒤 우수 결과를 1080p·4K로 업스케일)도 명시했다. 이 접근은 대량 제작을 염두에 둔 비용-품질 트레이드오프를 실무적으로 낮춰준다.

## 참조 고정성과 연속성 개선

Omni 1.2 Flash는 캐릭터, 제품, 스타일 이미지와 최대 3초 길이의 모션 클립, 오디오 단서 등을 조합해 생성 중 참조 정보를 끝까지 유지한다. 문서에 제시된 사례들(모델 사진과 전후방 제품 촬영을 결합한 15초 가상 착용 시퀀스, 포스터를 층별로 조립해 최종 프레임까지 재현하는 예)은 장면 간 드리프트와 모핑이 줄어들어 동일한 인물·의상·타이포·재질을 일관되게 유지한다고 설명한다.

연속 카메라 이동이나 FPV 플라이트 같은 복잡한 동작에서도 점프 컷이 현저히 줄고 스케일이 안정적이라고 밝히며, 음성 측면에서는 더욱 자연스러운 대사, 명확한 립싱크, 다중 화자 조건화가 개선되었다.

## 실무 적용과 접근 경로

Gemini Omni 1.2 Flash는 Gemini API와 Gemini for business를 통해 일반 제공되며, Google Cloud의 인프라와 보안으로 지원된다. Provisioned Throughput 옵션이 제공되고 출력물에는 **감지하기 어려운 SynthID 워터마크**가 포함된다. 개발자는 Google AI Studio, 대화형 스타터 앱, 개발자 문서와 가격표를 통해 시범 및 통합을 시작할 수 있고, 비즈니스 고객은 Google Cloud 콘솔에서 접근할 수 있다. Google 앱 측면에서는 Flow에서 다중 편집을 직접 지시하고, Google Vids에서는 Google 계정·Workspace 구독으로 추가 비용 없이 15초 클립을 생성할 수 있으며, Gemini 앱은 Google AI Ultra 구독자 대상으로 순차 롤아웃된다.

## 해석 — 무엇이 실무적으로 달라지나

제공 근거에 따르면 핵심 변화는 '더 긴 단일 클립을 보다 낮은 비용으로 생성하고, 생성 후 대화형 편집으로 변형을 누적할 수 있는 워크플로'다. 이는 광고·제품 소개·카탈로그·가상 착용 등 반복적인 변형(배경·의상·렌더 각도 등)이 필요한 대규모 비디오 파이프라인에서 재생성 비용과 시간을 줄이는 방향으로 즉시 활용 가능하다. 다만 문서는 빠른 스포츠 액션, 급격한 스크립트 변경, 복잡한 물리 시뮬레이션 개선이 향후 개발 과제라고 명시한다.

근거: Google 블로그(Anish Nangia), Gemini Omni 1.2 Flash 출시 공지(문서에 명시된 기능·가격·가용성·기술적 사례 포함).

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)

