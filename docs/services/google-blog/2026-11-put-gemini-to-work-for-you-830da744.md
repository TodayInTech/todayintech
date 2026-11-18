---
title: "Put Gemini to work for you"
sidebar_label: "Put Gemini to work for you"
description: "Google은 Gemini 4 Hydrogen 기반 'Tasks'를 미국·일본·한국 등에서 수백만 사용자에게 무료로 배포하고, 결제용 Agent Payments Protocol(AP2), Google Wallet의 iOS 확장, 계정 전용 하드웨어 격리 실행환경 등 결제·연동·보안 통합을 발표했습니다."
---

# Put Gemini to work for you

> Google Blog · 2026-11-17 · AI 제품

---

Google이 2026-11-17자 블로그에서 개인비서 기능 'Tasks'의 대규모 배포와 연동·보안 개선을 발표했다. **Gemini 4 Hydrogen 모델을 기반으로 한 이 업데이트는 미국·일본·한국·캐나다·호주·인도에서 수백만 사용자에게 무료로 롤아웃**되며, 일부 고급 기능은 우선 미국에서 제공된다(블로그).

## Gemini Tasks의 범위와 작동 방식
Google은 Gmail, 캘린더, 사진, 결제카드 등 Google 생태계에 이미 저장된 민감 데이터를 활용해 사용자의 일상 작업을 대신 수행한다고 밝혔다. 블로그 사례로는 서비스 예약 전화 걸기, 공과금 분석을 통한 문제점 진단, 쇼핑 비교 및 결제까지 자동 처리하는 흐름이 소개됐다. 사용자가 권한을 부여하면 Gemini가 개인정보를 참조해 작업을 수행하고, 기업과 대화할 때는 **사전에 AI임을 고지**하도록 설계됐다(chunk-0001).

## 결제·상거래 통합: AP2, UCP 예고와 Google Wallet iOS
구매 기능은 **Agent Payments Protocol(AP2)**을 사용하며, American Express(추후 제공), Mastercard, Visa와 함께 디지털 토큰을 통해 결제 보안을 유지한다고 Google은 밝혔다. 사용자는 사전 지출 한도 설정이 가능하고, 영수증과 배송 추적 정보는 **Google Wallet으로 수집**된다. 또한 Google은 Universal Commerce Protocol(UCP) 통합을 예고해 체크아웃 흐름 개선을 약속했고, Google Wallet은 **iOS로 확장**되어 오늘부터 사용 가능하다고 표기됐다(chunk-0001).

## 작업 실행과 데이터 보호 메커니즘
중요한 기술적 변화로 Google은 각 사용자 작업을 **계정 전용 하드웨어 격리 가상머신(Agent Compute Engine)**에서 실행한다고 설명했다. 이 환경은 샌드박스화되어 정기적으로 레드팀 검증을 받으며, 프롬프트 주입 필터와 Google Safe Browsing 등 다층 방어를 결합해 웹 탐색과 링크 열기 범위를 제한한다고 명시됐다. 또한 작업 중에는 사용자가 언제든 개입할 수 있고, 결제 등 민감 단계에서 확인을 요구하도록 설계되어 있다(chunk-0001, chunk-0002).

## 연동·개발자 측면과 이용 방법
Gemini는 현재 60개 이상의 인기 앱과 연결되며 개발자는 Connected Apps Platform에 신청할 수 있다. RCS를 통한 문자 연동, gemini@google.com으로 이메일 전달해 일정 생성 등 구체적 이용 경로가 블로그에 포함되어 있다. Google은 실무적 오류에 대비해 피드백(썸즈다운) 수단과 AI 취약점 발견시 참여 가능한 AI VRP(버그 바운티)를 안내했다(chunk-0001, chunk-0002).

이상은 Google 블로그에 공개된 내용만을 바탕으로 정리한 사실이다. 기술 관리자와 개발자는 계정 권한, 결제 토큰 허용 범위, 외부 사이트와의 상호작용 방식(사이트의 허용 여부)에 따라 운용 위험과 UX가 달라질 수 있음을 고려해 권한 설정과 통합 범위를 검토해야 한다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/)

