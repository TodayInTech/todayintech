---
title: "Kimi K3, and what we can still learn from the pelican benchmark"
sidebar_label: "Kimi K3, and what we can still learn from the pelican benchmark"
---

# Kimi K3, and what we can still learn from the pelican benchmark

> Hacker News · 2026-07-17 · 인공지능/모델

---

중국 연구소 Moonshot AI가 내놓은 Kimi K3는 ‘2.8조 매개변수’로 발표되며 회사는 이를 소위 ‘오픈 3T급 모델’로 소개했고 7월 27일까지 오픈 웨이트 공개를 약속했다. 자체·서드파티 측정에서 K3는 인공분석(Artificial Analysis) 보고서 기준 장기 지식 작업에서 Elo 1547을 기록해 이전 K2.6보다 +732 포인트 향상됐고, 전반적으로 Claude Fable 5와 GPT-5.6 Sol에는 뒤지지만 Claude Opus 4.8 max나 GPT-5.5 high를 대체로 앞서는 것으로 보고됐다. 토큰 사용 측면에서는 K2.6 대비 출력 토큰이 21% 감소했고, 작업당 비용($0.94)은 GPT-5.6 Sol($1.04)과 비슷하면서 Opus 4.8($1.80)보다 저렴하지만 오픈 웨이트 경쟁모델보다는 높은 편이다. 가격 책정은 입력 $3/백만 토큰, 출력 $15/백만 토큰으로 Anthropic Sonnet 계열과 비슷해 중국계 연구소 출시 모델 중 가장 비싼 수준으로 보인다. 또한 Arena.ai의 Frontend Code 경쟁에서 선두에 오른 점과 이미지 입력을 지원하는 점도 눈에 띈다.
간단한 '펠리컨(자전거 타는 펠리컨 SVG 생성)' 테스트로 K3를 직접 다뤄본 결과는 모델 평가에서 얻을 수 있는 실무적 통찰을 잘 보여준다. OpenRouter를 통해 실행한 사례에서 입력 95토큰, 출력 16,658토큰(그중 추론 토큰 13,241)으로 해당 요청의 비용이 약 $0.25였고, SVG 렌더링에 대한 대체 텍스트 생성(비전 기능)은 매우 만족스러웠다. 관찰된 기술적 특징으로는 현재 단 하나의 추론 노력 수준('max')만 제공되어 추론 토큰 소모가 크고, 토크나이저 계수 비교로 보아 숨겨진 시스템 프롬프트가 존재할 가능성(약 85토큰)이 있다는 점, 그리고 펠리컨 벤치마크가 최신 모델의 핵심 요소인 도구 호출(agentic tool calling)과 장기 대화 내 도구 운용 능력을 평가하지 못한다는 한계가 지적된다. 따라서 펠리컨은 ‘빠른 실험·연습’과 모델의 기본 출력·비용 특성을 확인하는 용도로 유용하지만, 오늘날 모델 성능의 결정적 지표로 보기는 어렵다는 결론을 제시한다.

[Hacker News에서 원문 읽기 →](https://simonwillison.net/2026/Jul/16/kimi-k3/)

