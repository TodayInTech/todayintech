---
title: "Detecting LLM-Generated Texts with “Classical” Machine Learning"
sidebar_label: "Detecting LLM-Generated Texts with “Classical” Machine Learning"
---

# Detecting LLM-Generated Texts with “Classical” Machine Learning

> Hacker News · 2026-07-16 · Generative AI/검출

---

저자는 최신 LLM 생성 텍스트가 여전히 뚜렷한 통계적 패턴을 보이며, 전통적 머신러닝 기법으로도 효율적으로 구분 가능하다는 결론을 제시한다. 연구는 대규모 인간 작성 샘플(2010–2022에서 추출)과 여러 상용·실험적 LLM으로 생성한 대응 샘플을 사용해 학습 데이터를 구성했고, 문장 단위 TF-IDF 특징과 LinearSVC(및 보조로 Naive Bayes)를 적용해 문장 수준 약 85% 정확도를 기록했다. 이후 7개 모델별 이진 분류기를 만들어 문장별 다수결(≥2표)로 의심 구간을 표시하고, 문서의 AI 비율로 최종 판정을 내리는 방식으로 문서 수준 성능을 크게 향상시켰다. 코드와 데모가 공개되어 있어 재현 가능성도 강조된다.
배포·강건성 측면에서도 흥미로운 관찰을 제시한다. 모델은 ONNX 대신 브라우저용 TF-IDF+SVM 구현으로 500k 피처(압축 시 약 38MB) 정도를 사용해 실시간 검사 데모를 제공하며, 대규모 Lofter 샘플 테스트에서 임계값 설정에 따라 허위 양성률이 매우 낮게 유지되는 결과(예: 70% 임계값에서 사실상 0%)를 보고한다. 번역 왕복·재작성 같은 회피 시도는 탐지가 다소 약화시키지만 완전히 회피하진 못했고, 저자는 보다 정교한 우회(대규모 인간 데이터로 파인튜닝하거나 특징을 교란하는 규칙적 조작)가 필요할 것이라 전망한다. 마지막으로 저자의 개인적 견해로는 현재 생성 텍스트의 반복성·피상성이 탐지 신호로 작동한다는 점을 들어 창작물로서의 한계를 지적한다.

[Hacker News에서 원문 읽기 →](https://blog.lyc8503.net/en/post/llm-classifier/)

