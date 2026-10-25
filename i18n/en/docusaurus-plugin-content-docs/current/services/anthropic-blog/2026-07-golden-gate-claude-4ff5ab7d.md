---
title: "Golden Gate Claude"
sidebar_label: "Golden Gate Claude"
---

# Golden Gate Claude

> Anthropic Blog · 2026-07-08 · AI 해석가능성(interpretability)

---

Anthropic이 발표한 연구는 Claude 3 Sonnet 내부에 수백만 개의 개념(그들은 ‘피처’라 부름)이 존재하며, 특정 뉴런 조합이 특정한 개념에 반응한다는 사실을 제시한다. 그중 하나가 샌프란시스코의 상징인 Golden Gate Bridge였고, 연구진은 이 피처의 활성 강도를 올리거나 내림으로써 모델의 응답 패턴을 의도적으로 바꿀 수 있다는 실험 결과를 공개했다. 활성화를 높이면 질문과 무관하더라도 대답이 다수 Golden Gate Bridge에 초점을 맞추게 되며, 예로 '10달러를 쓰는 방법'을 묻자 다리를 건너 톨비를 내는 것을 권하거나, 사랑이야기를 써달라는 요청에 안개 낀 날 다리를 건너는 차의 이야기로 바꾸는 식의 편향적 출력을 보였다.
이 실험은 단순한 프롬프트 변경이나 추가 학습(파인튜닝)이 아니라 모델 내부 활성화의 특정 요소를 정밀하게 조작하는 '외과적' 접근이라고 연구진이 설명한다. 연구진은 동일한 기법으로 위험한 코드·범죄 행위·기만성과 관련된 안전성 피처들의 강도를 조절할 수 있음을 보였고, 이는 향후 모델 안전성 개선에 기여할 잠재성을 시사한다. Golden Gate Claude라는 이름의 데모는 한시적으로 claude.ai에서(우측의 Golden Gate 로고를 통해) 공개되었으나 24시간 동안만 온라인으로 제공되었고 현재는 더 이상 이용할 수 없다는 점도 원문에 명시되어 있다. 이러한 결과는 대형 언어모델 내부의 설명 가능성(interpretablity) 연구가 단순한 관찰을 넘어 행동 제어와 안전 응용으로 연결될 수 있음을 보여준다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/golden-gate-claude)

