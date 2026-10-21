---
title: "Strengthening our defenses against distillation attacks"
sidebar_label: "Strengthening our defenses against distillation attacks"
---

# Strengthening our defenses against distillation attacks

> Anthropic Blog · 2026-10-17 · AI 보안

---

Anthropic은 불법적 디스틸레이션(distillation) 공격을 통해 대형 모델의 추론(transcript)과 능력이 대규모로 탈취되는 문제를 집중적으로 다뤘다. 기업들이 프론트어 모델의 추론을 수집해 보다 적은 비용으로 유사한 성능의 모델을 재생산하는 사례가 빈번하며, Zhipu의 GLM-5.3 사례와 Moonshot Kimi가 Claude로 요청을 전달한 정황은 이런 행위가 사이버·감시 역량으로 통합될 수 있음을 보여준다. Anthropic은 이러한 공격이 안전장치 없이 배포된 모델을 양산할 위험과 국가안보 측면의 실질적 위협을 제기한다고 설명한다.
대응으로 회사는 세 가지 축의 기술적 방어를 도입했고, 초기 증거에 따르면 디스틸러가 수집한 데이터량을 약 90~99%까지 줄였으며 추론 토큰 추출량은 도입 전보다 10~100배 낮아졌다고 보고한다. 핵심 수단은(1) 보존된 사고(preserved thinking)로 새 API 계정이 이전 컨텍스트를 편집하지 못하게 한 조치와 모델 간·계정 간 추론 이동 차단, (2) 내부·외부 레드팀을 거친 이단계 분류기(two-stage classifier)를 통한 추출 시도 탐지(오탐률 &lt;0.1%), (3) 반복 시도의 사용 제한·계정 차단과 차단된 요청에 대한 과금 재개 등이다. Anthropic은 이러한 조치가 정당 사용자에 대한 일부 영향(통합 업데이트 필요, 소수의 오탐, 차단 요청 과금)을 낳는 한편, 공격자와의 ‘고양이와 쥐’ 게임이 지속될 가능성이 크다고 평가한다. 기술적 관점에서 이번 공개는 모델 제공자와 플랫폼이 연대해 추출 방지를 설계·운영해야 한다는 실무적 교훈을 제시한다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/distillation-defenses)

