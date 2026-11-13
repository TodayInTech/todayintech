---
title: "Gemini 4 Hydrogen"
sidebar_label: "Gemini 4 Hydrogen"
description: "Google이 빠른 실행과 100만 토큰 컨텍스트에 최적화된 Gemini 4 Hydrogen을 발표했다. Orchestrator로 Carbon/Argon과 다중모델 협업을 자동화하고, 토큰당 요금($1.50 입력·$7.50 출력)과 다양한 성능·안전 지표를 공개하며 전면 배포를 시작했다."
---

# Gemini 4 Hydrogen

> Hacker News · 2026-11-12 · AI 모델

---

Google은 새로운 대형언어모델 Gemini 4 Hydrogen을 공개하며, **빠른 실행(rapid execution)**과 대규모 컨텍스트(1,000,000 토큰)에서의 실무용 효율성에 초점을 맞췄다고 밝혔다. Hydrogen은 깊은 장기 추론을 목표로 한 Gemini 4 Carbon·Argon과는 역할을 달리해 일상적 코딩·테스트·검증 같은 실행 중심 작업에서 더 나은 속도와 토큰 효율을 제공하도록 설계됐다.

## 포지셔닝과 가격
Hydrogen은 1백만 토큰 컨텍스트 윈도우를 기본으로 제공하며 가격은 **입력 100만 토큰당 $1.50, 출력 100만 토큰당 $7.50**로 고정되어 있다. Google은 Hydrogen을 단독 실행 엔진으로 쓰거나 Carbon·Argon과 짝을 이뤄 다중모델 워크플로에서 고효율 실행자(worker)로 활용할 것을 제안한다.

## Orchestrator: 모델간 동적 전환과 절감 효과
Google은 Google Antigravity의 Orchestrator를 통해 동일 세션에서 Carbon과 Hydrogen을 동적으로 전환하도록 해 다중모델 협업을 자동화한다고 설명했다. 공개된 벤치마크(터미널-벤치 4.0)에 따르면 Orchestrator는 Carbon 수준에 근접한 작업 성공률을 유지하면서 평균 쿼터 사용량을 **24% 절감**하고 작업 완료 시간을 **19% 단축**했다. 이 수치는 실무에서 모델 비용과 응답시간을 동시에 개선할 수 있음을 시사한다.

## 성능·효율·안전성 지표(원문 수치)
- AAII(Artificial Analysis Intelligence Index): Hydrogen은 기본 고사고(High) 설정에서 **51**(Argon 50)이며, 최고 xhigh 설정에서 **54**까지 도달한다고 보고했다.
- 이전 세대(3.8 Flash) 대비 실무 성능: 고(High) 기본 설정에서 작업 완료 속도가 **2.5배 빠르며**, Terminal-Bench 4.1 점수는 **57% 대 18.2%**로 크게 향상되었다. 제작된(허위) 주장(fabricated claims)은 **5배 이상** 줄었다.
- 대규모 리포지토리 작업: 파일 읽기 및 검색 호출을 병렬로 배치해 복잡한 코드·데이터 워크플로에서 **2x–2.8x 빠른 실행**과 토큰 사용 **12%–23% 절감**을 관찰했다고 밝혔다.
- 에이전트·전문 벤치: Agent Arena에서 **#5**, HLE-Diamond **58.8%**, Vals Tax Agent Bench **52.3% (1위)**, Vals Legal Research Bench **55.8% (공동 1위)**, MKA **53.4%**, Agents’ Last Exam v1.1 **71.6%** 등 다양한 벤치에서 상위권 성능을 보고했다.

안전성 측면에서는 에이전트 작업의 과도한 권한 침범(overreach)을 최대 **81%**, 불충분 서비스(under-service)를 최대 **79%**까지 감소시키고, 도구 사용·코딩 평가에서의 비정렬(misaligned) 행동과 작업 단축(shortcutting)을 **12배** 줄였다고 밝혔다. 내부 에이전트 정직성 평가에서 **96.7% 정직성**, 논리(사고 체인) 가독성 99.9% 보존(20만 건 이상의 감사된 턴에서 기만적 추론 편집 0건) 등의 수치도 제시되었다. 또한 Gray Swan IPI 벤치마크에서 간접 프롬프트 주입 공격에 대해 **2.3배** 이상 저항력이 증가했고, HealthBench Pro에서 오탐 거부율은 **0.4% 미만**으로 보고되었다.

## 실무적 의미
제시된 수치와 기능을 종합하면 Hydrogen은 대규모 코드베이스의 반복적 수정·디버깅, 병렬 에이전트 기반 테스트·검증, 멀티모달 문서·보고서 합성 같은 '속도와 안정성'이 중요한 개발·엔터프라이즈 작업에 직접적 이점을 제공한다. Orchestrator를 이용하면 고사고 모델(예: Carbon)을 조정자(coordinator)로, Hydrogen을 작업자(worker)/검증자(verifier)로 배치해 비용과 응답시간을 낮추면서도 높은 성공률을 노릴 수 있다. Google의 수치들은 특히 토큰당 비용 구조와 병렬 처리로 인한 비용 절감 가능성을 구체적으로 보여준다.

## 배포 범위
Google은 Hydrogen을 "오늘부터" 전 세계적으로 배포한다고 밝혔으며, 개발자는 Gemini API·AI Studio·Android Studio에서, 유료 Google AI Pro/Ultra 가입자는 Google Antigravity에서 시험해볼 수 있다. 엔터프라이즈는 Gemini for Business(모델 드롭다운·API), Google Antigravity, 그리고 적격 사업자 대상 Google Sheets 통합을 통해 도입할 수 있고, 일반 사용자는 Gemini 앱 모델 드롭다운과 Google Search의 향상된 응답을 통해 이용 가능하다.

출처: Google 블로그 'Introducing Gemini 4 Hydrogen' (원문 수치 및 배포 정보에 근거)

[Hacker News에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

