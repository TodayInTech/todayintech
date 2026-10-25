---
title: "Introducing WeatherNext 3, our most advanced and accurate global weather AI model"
sidebar_label: "Introducing WeatherNext 3, our most advanced and accurate global weather AI model"
---

# Introducing WeatherNext 3, our most advanced and accurate global weather AI model

> Google Blog · 2026-09-03 · 기후·날씨 AI

---

Google DeepMind와 Google Research는 실시간 위성 관측과 지상 관측치를 직접 학습해 시간·공간 해상도를 크게 개선한 전지구 기상 AI 모델 WeatherNext 3를 공개했습니다. 이 모델은 1시간 단위의 정지궤도 위성 모자이크를 입력으로 받아 Functional Generative Network(FGN) 메쉬 트랜스포머를 통해 촘촘한 격자장, 사이클론 궤적, 관측소 수준의 희소 좌표를 예측합니다. 핵심 변화로 2m 기온·수분 등 주요 지표를 5km 해상도(일부 표면 변수는 10km, 대기 변수는 25km)로 제공하며, 이전 모델(WeatherNext 2)의 25km·6시간 간격보다 대략 5배 더 선명한 전지구 시각화를 가능하게 했습니다. 실시간 위성 기반 갱신과 관측 중심 학습으로 급변하는 강수·표면온도 등 변수의 편향을 줄였다고 설명합니다.
강수 예측의 경우 IMERG 등 위성 기반 자료와 자체 위성 레이더 재분석을 학습해 중기 예측에서 CRPS 기준 IMERG 대비 최대 60% 개선, MRMS 대비 30%, 초기 단기에서는 강우계(관측) 기준 약 10% 개선을 보고합니다. 또한 풍력·태양광 예측을 위해 터빈 고도에 해당하는 100m 풍속과 고해상 구름·일사량을 제공해 재생에너지 운영·전력계획에 활용할 수 있도록 설계했습니다. WeatherNext 3은 BigQuery·Earth Engine·Google Cloud Storage 등을 통해 통합 데이터로 제공되며, Search·Gemini 앱·Maps·Maps Platform Weather API 등 Google 제품군에 즉시 적용됩니다. 대기 불확실성은 여전하다는 점을 인정하면서도, 실시간 관측 기반 접근으로 국지적·급변 기상 대응력과 전력·농업 등 응용 분야의 실용성이 크게 향상될 가능성을 제시합니다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/)

