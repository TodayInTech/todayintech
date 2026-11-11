---
title: "Blender 5.3 released with Gaussian Splat support"
sidebar_label: "Blender 5.3 released with Gaussian Splat support"
description: "Blender 5.3이 공개됐다. Cycles 뷰포트에 NVIDIA DLSS 디노이즈가 추가되고(드라이버 620 이상 필요), 프로젝트 단위 설정·합성기 효과 스택·Video Sequencer의 리플 편집·Blade 2.0 등 작업 흐름 개선이 핵심이다."
---

# Blender 5.3 released with Gaussian Splat support

> Hacker News · 2026-11-10 · 3D/그래픽스 소프트웨어

---

**릴리스와 맥락 — 2026년 11월 10일**
Blender 팀은 2026년 11월 10일 Blender 5.3을 공개했다. 이번 버전은 뷰포트 반응성·합성 워크플로·타임라인 편집 등 여러 실무 영역에서 눈에 띄는 개선을 담고 있다.

## Cycles: 뷰포트용 NVIDIA DLSS 디노이즈
Cycles 뷰포트에서 **NVIDIA DLSS 디노이즈**를 지원해 조명 확인과 룩 개발을 더 빠르고 반응성 있게 할 수 있다. 애니메이션 재생 중 프레임 간 깜빡임도 실질적으로 줄어든다고 명시되어 있다. DLSS 디노이즈는 Render properties &gt; Sampling &gt; Denoise 패널에서 찾을 수 있고, **NVIDIA 드라이버 620 이상**이 필요하다.

## 합성기: 효과 스택과 성능 향상
합성기(Compositor)는 이제 장면에 효과를 모디파이어처럼 쌓을 수 있어 Bloom, Chromatic Aberration, Film Grain, Vignette 등 빌트인 효과나 외부 에셋을 하나의 체인으로 적용·관리할 수 있다. 내부적으로 각 효과는 노드 그룹으로 구현되며 언제든 Compositor 에디터에서 세부 조정이 가능하다. 또한 GPU에서 재생 속도가 **최대 2배** 빨라졌고, Apple GPU에서는 Anisotropic Kuwahara가 **최대 10배**, NVIDIA GPU에서 **2배**, CPU에서 **25–30%** 성능 개선이 보고된다.

## 프로젝트 단위 설정과 에셋 관리
Blender는 이제 **프로젝트** 개념을 도입해 관련 파일·설정·에셋 라이브러리를 한 묶음으로 관리할 수 있다. 프로젝트별 변수(예: 캐릭터명, 파일 경로), 프로젝트 전용 에셋 라이브러리와 색상 관리 설정, 커스텀 스플래시 화면 등을 지원한다. 애드온 등 확장 기능의 프로젝트 단위 적용은 향후 버전에서 추가될 예정이라고 명시되어 있다.

## EEVEE·I/O·Grease Pencil 주요 변화
EEVEE는 구면·큐브맵·여러 파노라마 및 다양한 fisheye 프로젝션을 지원하는 파노라마 카메라 렌더링을 추가했다. 다만 현재 뷰포트에서의 일부 제약(깊이 흐림, 레이트레이싱, 볼류메트릭 시간 재투영 미지원)이 있다. I/O 측면에서는 컬렉션에 임포터를 연결해 재임포트 설정을 보존하는 Collection Importer가 추가되었고, 5.3에서는 **USD importer만 지원**된다고 명시되어 있다.

Grease Pencil에는 Draw Mode 전용 선택 도구(Tweak, Lasso, Box, Circle), 새로운 Carver 도구(정교한 Boolean 절단), 여러 영역을 한 번에 채우는 Fill 개선 및 그라디언트 입력이 도입됐다.

## Video Sequencer: 리플 편집과 Blade 2.0
Video Sequencer에 **리플(Ripple) 편집 프레임워크**가 도입되어 편집 중 간격을 자동으로 메우도록 할 수 있다. 편집 모드(Ripple, Shuffle, Overwrite)는 스트립 이동 시 각각 R, S, V로 전환된다. 새 연산자와 단축키로는 Ripple Trim(Shift+Q/Shift+W), Ripple Delete(Shift+X)이 있고, Blade 도구는 시각화가 강화되어 C 키를 누르고 있으면 임시로 블레이드를 활성화할 수 있다. 하드웨어 디코딩, 씬 스트립 썸네일, OpenTimelineIO 초기 지원 등도 포함된다.

## UI·검색·문서화 편의성
아웃라이너의 사용자 정의 정렬, 사이드바 검색(Ctrl/Cmd+F) 지원, 노드 에디터의 Comment 노드 및 label_markdown·label_multiline 위젯으로 기본 Markdown 렌더링을 지원하는 등 인터페이스 탐색성과 문서화 편의성이 개선됐다.

## 실무적 의미(출처 기준 해석)
이번 릴리스는 뷰포트에서의 실시간 확인(특히 DLSS 기반 디노이즈)과 편집·합성 파이프라인의 사용자 경험을 동시에 끌어올리는 데 초점이 맞춰져 있다. 프로젝트 단위 설정과 에셋 확장(Extensions) 지원은 팀 단위 작업의 설정 공유를 단순화할 가능성이 크다. 단, 일부 기능(EEVEE 파노라마의 뷰포트 제약, Collection Importer의 USD 한정 지원, 애드온의 프로젝트 적용 미지원 등)은 문서화된 제약으로 남아 있어 도입 시 확인이 필요하다.

Blender 5.3의 상세 기능 목록과 기여자 정보는 릴리스 노트에서 확인할 수 있다. (Blender 팀, 2026-11-10)

[Hacker News에서 원문 읽기 →](https://www.blender.org/download/releases/5-3/)

