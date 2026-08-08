---
title: "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones"
sidebar_label: "DeepMind's WeatherNext model achieves breakthrough forecasting cyclones"
---

# DeepMind's WeatherNext model achieves breakthrough forecasting cyclones

> Hacker News · 2026-08-08 · AI for Weather

---

DeepMind가 발표한 WeatherNext는 사이클론 예측에서 계산 효율성과 불확실성 포착을 동시에 끌어올린 점이 핵심 성과다. 모델은 Functional Generative Networks(FGNs)를 써서 다양한 예측을 빠르게 생성하는 앙상블을 만들며, 단일 TPU에서 15일짜리 예측을 1분 미만에 산출할 수 있다. 지난해 50개 규모였던 동시 예측을 올해 1,000개로 확장해 허리케인 멜리사(2025)처럼 급격한 강도 변화 같은 희소하지만 치명적인 시나리오의 확률 분포를 더 잘 포착했다고 보고한다. 전통적으로 강도 예측에는 매우 높은 공간 해상도가 중요하다고 여겨졌으나, WeatherNext Cyclones는 28×28km 해상도(전통 모델보다 약 100배 거친 수준)만으로도 성능을 내며, 소형 버전인 WeatherNext 2-mini는 111×111km 해상도에서 잘 작동하는 점이 과학적 관심을 불러일으킨다. 이로부터 단순 해상도 향상 외에 모델 구조나 앙상블 처리 방식 등이 예측력에 기여했을 가능성이 제기되며, 정확한 메커니즘은 추가 연구가 필요하다고 명시한다.
기술적·운영상 의미도 분명하다. 연구 논문과 함께 코드와 모델 가중치를 오픈소스로 공개해 학계·기상기관·비영리단체가 모델을 재현·확장할 수 있게 했고, WeatherNext Cyclones·WeatherNext 2·2-mini 세트와 공개 Colab 노트북을 통해 접근성을 높였다. 결과 시각화는 Google Earth AI의 Weather Lab에서 통합 제공되며, DeepMind는 더 많은 예측 리드타임—사이클론 예측에서 하루 이상 향상되었다고 표현하며—을 획득했다고 평가한다. 다만 공식 경보는 지역 기상청을 따르라는 점을 명확히 하며, 모델의 낮은 공간 해상도 원인 규명과 실무 적용 과정에서의 검증·협업이 다음 과제로 남아 있다.

[Hacker News에서 원문 읽기 →](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/)

