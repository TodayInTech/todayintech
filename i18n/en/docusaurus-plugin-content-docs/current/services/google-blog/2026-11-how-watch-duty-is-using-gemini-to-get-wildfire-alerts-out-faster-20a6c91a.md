---
title: "How Watch Duty is using Gemini to get wildfire alerts out faster"
sidebar_label: "How Watch Duty is using Gemini to get wildfire alerts out faster"
description: "Google 엔지니어들이 Gemini 기반 도구로 잡음 많은 VHF 무전음을 정리해 단어 오류율을 **38%→22.34%**로 낮추고, 30초 이내에 화재 신호를 포착해 Watch Duty의 야간 Critical Alert 발송을 가능하게 했다."
---

# How Watch Duty is using Gemini to get wildfire alerts out faster

> Google Blog · 2026-11-20 · 공공안전·AI

---

Google 연구진과 엔지니어들이 Watch Duty에 적용한 Gemini 기반 무전음성 도구는 아날로그 VHF 라디오의 심한 정적과 전문 소방 용어를 빠르게 정리해, 자원봉사자가 사건 검증과 경보 발송에만 집중하도록 돕는다. Google.org 펠로십으로 6개월간 상주하면서 **2만 시간가량의 과거 무전 녹음**을 활용해 모델을 다듬었다.

## 잡음 제거와 전문 용어 변환
도구는 무전의 강한 정적을 제거하고 전문 소방·전술 용어를 '검색 가능한 텍스트'로 변환한다는 점이 핵심이다. 이로 인해 손상된 VHF 오디오의 단어 오류율이 **38%에서 22.34%로 감소**했고, 자원봉사자들의 무전 전사 도구 만족도는 **35.3%→92.3%**로 올랐다(원문 근거).

## 운영 성능과 실전 검증
시스템은 하루에 **200시간 이상의 라디오 연설을 전사**하며 약 **400개 활성 피드**를 처리하고, 설계·테스트 단계에서 **1만 개 이상 피드 동시 처리**를 목표로 했다. 실전 적용 사례로는 2026년 7월 워싱턴의 Railroad Fire가 언급되며, 최초 911 디스패치를 정적 속에서 자동 전사해 **30초 이내에 신호를 포착**했고, Watch Duty는 이를 바탕으로 야간에 최초로 Critical Alert(긴급 모드에서 방해 금지 해제 기능)를 발송해 대피 시간을 벌었다.

## 협력 구조와 실무적 의미
이 도구는 Google의 자금·인프라 지원과 연계된 산물이다. 2024년 Google.org는 Watch Duty에 **200만 달러와 30만 달러 상당의 Google Cloud 크레딧**을 지원했으며, Google Search와 Firebase Cloud Messaging 등 Google 생태계의 지원(메시징 한도 60만→100만 증액)도 경보 전달 안정성에 기여했다. 또한 Watch Duty는 AI Collaborative: Wildfires의 일환으로 모델·데이터를 공공기관과 공유하는 방향으로 확장하고 있다.

기술적으로는 '정적 제거 + 전문 용어 표준화 → 빠른 전사'의 파이프라인이 핵심 변화다. 이 변화는 특히 인구 밀집 지역이 아닌 곳에서 처음 감지되는 화재를 놓치지 않게 하는 데 실무적 효과를 냈다. 원문 근거 범위 내에서, 이 사례는 AI 기반 오디오 전사가 응급 통신의 초기 감지 시간을 단축하고 경보 전달 체계를 보완할 수 있음을 보여준다.

[Google Blog에서 원문 읽기 →](https://blog.google/company-news/outreach-and-initiatives/google-org/watch-duty-gemini-tool/)

