---
title: "Claim your Google Cloud Credits in Google AI Studio"
sidebar_label: "Claim your Google Cloud Credits in Google AI Studio"
description: "Google AI Studio에서 워크스페이스 안에서 바로 Google Cloud 무료 API 크레딧을 신청·연동하고 결제 계정까지 설정할 수 있다. Pro/Ultra 가입자는 월별 크레딧(12개월 유효·자동 이월)을 Gemini API 등 유료 모델에 적용할 수 있으며 Gemini API는 $5 선결제가 필요하다."
---

# Claim your Google Cloud Credits in Google AI Studio

> Google Blog · 2026-11-13 · Developer tools

---

Google은 AI Studio에서 바로 Google Cloud 무료 API 크레딧을 **신청하고 결제 계정까지 연동할 수 있는 흐름**을 오늘부터 제공한다고 밝혔다. 이전에는 크레딧 신청·청구·결제 설정을 위해 여러 사이트를 오가야 했지만, 이제는 AI Studio 내부에서 개발자 프로필 생성, 청구 계정 연결, 잔액 확인까지 한 번에 처리할 수 있다.

## AI Studio 내부에서의 크레딧 신청·청구 흐름

- 로그인 후 왼쪽 내비게이션에서 **미청구 크레딧과 현재 잔액 알림**을 확인할 수 있다. 인-제품 다이얼로그로 Google Developer Program 프로필을 만들고 크레딧을 즉시 수령할 수 있다.
- 같은 흐름에서 Cloud 결제 계정을 설정하고, 향후 월별 지급분을 자동 적용(auto-apply)하도록 구성할 수 있다. 남은 잔액과 사용량은 aistudio.google.com/billing에서 실시간으로 추적할 수 있다.

## 월별 크레딧 동작 방식과 제한

- **Google AI Pro 및 Ultra 구독자에게 매월 반복 제공되는 Google Cloud 크레딧**이 해당된다. 월별 지급분은 AI 플랜 등급에 따라 달라진다.
- 각 월별 크레딧은 **발급일로부터 12개월 유효**하며, **월별 지급분은 누적(자동 이월)**된다. 이미 몇 달간 구독을 유지해온 사용자라면 미수령 크레딧이 쌓여 있을 가능성이 있다.
- 크레딧은 AI Studio에서 구독 할당량을 소진했을 때 **유료 모델 사용·오버리지 발생 시** 우선 사용될 수 있다. 플랜을 업그레이드하면 월별 지급분도 자동으로 늘어난다.

## Gemini API와 선결제 요건, 사용자 범위

- **Gemini API를 Cloud 결제와 함께 사용하려면 $5 최소 선결제(prepayment)와 잔액이 요구**되어야 프로모션 크레딧을 차감할 수 있다. 이 조건은 Gemini API 이용 시 크레딧이 자동으로 소진되기 위한 전제다.
- 크레딧 사용은 **주요(Primary) 구독자에 한해 가능**하며 가족 구성원 간 공유는 불가능하다.

## 실무적 의미

이 변화는 AI Studio에서 아이디어를 시험하고 애플리케이션을 빠르게 프로토타입하는 개발자 경험을 단순화한다. 특히 Gemini 등 유료 모델로 생성형 미디어나 복잡한 태스크를 처리할 때, 더 이상 여러 콘솔을 전환해 결제·크레딧을 설정할 필요가 없어 작업 중단이 줄어든다. 다만 Gemini API를 실제로 프로모션 크레딧으로 소진하려면 **$5 선결제 요건**을 충족해야 하므로 초기 API 호출을 준비할 때 이 점을 고려해야 한다.

정보 출처: Google 블로그의 "Claim your Google Cloud Credits in Google AI Studio" (게시일 표기).

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/google-cloud-credits-gdp-ai-studio/)

