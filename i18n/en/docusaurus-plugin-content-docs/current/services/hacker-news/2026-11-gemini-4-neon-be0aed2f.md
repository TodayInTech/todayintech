---
title: "Gemini 4 Neon"
sidebar_label: "Gemini 4 Neon"
description: "Google은 Gemini 4 Neon을 공개했다. Neon은 1백만 토큰 컨텍스트, 입력·출력 토큰 가격, 다수 벤치마크 상위권 성적 및 강화된 안전·사이버 방어 성능을 특징으로 한다."
---

# Gemini 4 Neon

> Hacker News · 2026-11-18 · AI/모델 발표

---

Google은 **Gemini 4 Neon**을 공개했다. 회사는 Neon을 "프론티어 수준의 지능과 빠른 종합 작업 완수 능력"을 제공하는 모델로 소개했으며, 주요 공개 내용은 성능 지표, 비용 구조, 장기 에이전트 워크플로 지원과 안전·보안 특화 개선이다.

## 성능·벤치마크 핵심
Google에 따르면 Neon은 Artificial Analysis Intelligence Index(최고 사고 수준 xhigh)에서 점수 **61**로 동급 모델들을 앞서며 전체 3위에 올랐다. Vals Index에서는 **#2(70.9%)**, Legal Research Bench와 Tax Agent Bench에서는 **#1**을 기록했다(chunk-0001). 과학·수학 추론에서는 Terminal-Bench Science **70.5%**, RiemannBench **84.0%**, HLE-Diamond **71.3%** 등 상위권 성적을 냈다.

개발자·코드 관련 지표에서도 강점을 내세운다. Artificial Analysis Coding Agent Index에서 **#1(58.6)**을 기록했고, Terminal-Bench 4.1은 **65.2%**, FrontierCode 2.0은 기본 high 설정에서 **46.2%**로 보고됐다. Google Antigravity 환경에서 mini-SWE **12.8%**에서 **39.0%**까지 올라가는 결과를 보이며 장시간 에이전트 하니스가 성능을 크게 끌어올릴 수 있음을 제시한다(chunk-0001).

## 생산·비용·컨텍스트
가격은 입력 토큰 **$3 / 백만 토큰**, 캐시된 입력 토큰 **$0.15 / 백만 토큰(95% 할인)**, 출력 토큰 **$15 / 백만 토큰**이며 **1,000,000 토큰 컨텍스트 창**을 지원한다고 밝혔다. Google은 Neon이 기본 high 사고 수준에서 동일 계열 모델 대비 태스크당 비용을 **32%** 낮춘다고 주장하며, 상위 frontier 모델들과 비교해 **50%~80%** 낮은 태스크당 비용 범위를 제시했다(chunk-0001).

## 사이버 방어 및 취약점 대응
Neon의 사이버 방어·취약점 대응 성능을 강조했다. AutoBaxBench의 hard tier에서 **76%**로 최첨단 성능을 냈고, WebExploitBench v1.2에서는 **51.26%**로 최첨단 수준이면서 경쟁 모델 대비 비용은 절반 수준이라고 보고했다. SEC-bench Pro에서 **90.5%**, ExploitGym에서 경쟁 수준의 성과를 내며 토큰 사용량은 Carbon 대비 절반 수준이라는 수치가 제시됐다. Collinear의 CWE-bench v2에서는 **70.7%**, Carbon 대비 **3.4%**p 향상이라고 밝혔다(chunk-0001, chunk-0002).

## 안전·정렬·실행 신뢰성
Google은 Neon이 Gemini 4 Carbon 수준의 심각한 오용과 프롬프트 주입 방어를 유지하면서도 합법적 요청에 대한 거부는 상대적으로 적다고 밝혔다. 예시로 Terminal-Bench 4.0에서 거부율 **1.98%**, Terminal-Bench-Science에서는 **0%**를 기록했다. 코딩 평가에서는 치팅 0.0%(Terminal-Bench 4.0), 코딩 치팅 평가에서의 지름길(shortcuts) 비율 **2.45%**로 Gemini 4 모델 중 가장 낮은 편이라고 보고했다. 에이전트 행동 평가에서는 비정렬 액션률 **0.09%**, 에이전트 정직성 통과율 **99.2%**를 보였고, 과소서비스는 **43%–56%**, 과잉행동은 **15%–35%** 더 줄였다고 밝혔다. 또한 Gray Swan의 IPI(간접 프롬프트 주입) 벤치마크에서 최고 사고 수준의 실시간 보호를 적용하면 **0.0%** 공격 성공률을 달성했다고 보고했다(chunk-0002).

## 실무적 의미(해석)
Neon의 **1백만 토큰 컨텍스트**와 상대적으로 낮은 토큰 비용 구조는 긴 에이전트 세션, 대용량 문서·스프레드시트·멀티미디어 입력 통합 작업에서 비용·성능 측면의 이점이 될 가능성이 크다. Google이 강조한 대로 Antigravity 같은 장기·병렬 서브에이전트 오케스트레이션 환경에서 성능이 크게 개선되는 사례가 있어, 복잡한 코드 리팩터링·다중 파일 디버깅·상업용 자동화 파이프라인 등에 곧장 적용 가능한 모델로 보인다(chunk-0001).

## 배포·접근성
Neon은 오늘부터 Gemini API( Google AI Studio ), Gemini for business( API·모델 드롭다운 ), 유료 Google AI Pro·Ultra 가입자 대상의 Google Antigravity 및 Gemini 앱의 Pro/Ultra 구독자에게 제공된다. 사이버 방어를 위한 Fairwind 프로그램 참여 멤버에게는 며칠 내로 접근 권한이 제공되며, Fairwind 참가 요청은 Cloud 계정 팀을 통해 접수하라고 안내하고 있다(chunk-0001, chunk-0002).

출처에 있는 숫자와 결과는 Google의 발표 자료에 따른 것이다. 발표 자료 외의 호환성, 실제 운영 비용·레이턴시 등 상세 환경별 성능은 배포 후 추가 검증이 필요하다.

[Hacker News에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

