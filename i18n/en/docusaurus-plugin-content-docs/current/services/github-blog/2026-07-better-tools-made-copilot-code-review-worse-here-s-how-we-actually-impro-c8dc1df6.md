---
title: "Better tools made Copilot code review worse. Here’s how we actually improved it."
sidebar_label: "Better tools made Copilot code review worse. Here’s how we actually improved it."
---

# Better tools made Copilot code review worse. Here’s how we actually improved it.

> GitHub Blog · 2026-07-10 · Developer Tools / AI Agents

---

Copilot code review는 자체 코드 탐색 도구에서 GitHub Copilot CLI의 공유된 Unix풍 도구(grep, glob, view)로 전환했을 때 오히려 리뷰 비용이 늘고 유용한 코멘트가 줄어드는 회귀를 발견했습니다. 표면적으로는 더 좋은 도구를 썼으니 성능 개선을 기대했지만, 내부 벤치마크와 호출·출력 추적(trace)은 에이전트가 풀리퀘스트(diff)를 좁혀 조사해야 할 상황에서 저장소를 광범위하게 ‘브라우징’하는 루프에 빠졌음을 보여주었습니다. 이전 전용 도구는 모델이 적은 도구 호출으로도 유의미한 주변 컨텍스트를 함께 반환해 효율을 유지했으나, 공유 도구의 기본 지침은 탐색형 워크플로우를 암시해 검토 작업과 맞지 않았습니다. 그 결과 불필요한 파일 내용이 에이전트의 컨텍스트에 누적되어 토큰 비용과 집중도가 떨어졌습니다.
해결책은 도구 자체가 아니라 도구를 쓰는 지시문을 ‘리뷰형’으로 재설계한 것입니다. 핵심 규칙은 diff에서 출발해 특정 질문을 세우고, 경로 불확실성에는 glob·grep으로 후보를 좁힌 뒤 view로 필요한 파일·라인 범위만 읽는 것, 저비용 검색을 배치하고 집중된 읽기를 묶어 수행하는 것입니다. 이렇게 지시문을 튜닝하고 벤치마크로 워크플로우를 반복적으로 점검한 결과, 프로덕션에서 평균 리뷰 비용이 약 20% 낮아졌고 품질 신호에는 문제가 없었습니다. 동일한 도구를 다른 제품(Copilot CLI)에 그대로 적용했을 때는 같은 이득이 나타나지 않았다는 점도 주목할 만합니다. 요지는 에이전트 설계에서 도구 표면은 단순 구현물이 아니라 에이전트의 주의(attention), 탐색 방식, 컨텍스트 비용을 결정하는 제품 경험의 일부라는 점이며, 도구 설명과 시스템 지침을 마치 API 문서처럼 정확하게 설계해야 한다는 실무적 교훈입니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/)

