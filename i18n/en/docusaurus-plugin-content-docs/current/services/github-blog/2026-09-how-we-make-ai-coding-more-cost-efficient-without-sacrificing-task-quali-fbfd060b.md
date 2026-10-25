---
title: "How we make AI coding more cost efficient without sacrificing task quality"
sidebar_label: "How we make AI coding more cost efficient without sacrificing task quality"
---

# How we make AI coding more cost efficient without sacrificing task quality

> GitHub Blog · 2026-09-02 · AI &amp; ML

---

GitHub은 AI 기반 코딩 작업에서 토큰 수 자체를 줄이는 것보다 ‘작업 전체’의 효율을 최적화하는 쪽으로 설계 방향을 잡았습니다. 이를 위해 Copilot 팀은 출력에서 반복적 노이즈를 선별적으로 압축하고, 파일 내용을 읽을 때 불필요한 라인 번호 접두사를 제거하며, 프롬프트를 축소하고, 백그라운드로 수행된 작업의 완료 결과를 추가 호출 없이 배치 전달하는 네 가지 변경을 도입했습니다. 중요한 설계 원칙은 '유용한 컨텍스트는 보존하고, 복구를 강요하지 않는 범위에서만 줄이기'였으며, 초기 실험에서 과도한 압축이 모델의 재호출과 작업 지연을 유발한 사례를 통해 도구 호출 단위의 지역 최적화가 전체 비용을 악화시킬 수 있음을 확인했습니다.
이들 변화는 오프라인 에이전트형 벤치마크와 통제된 온라인 실험을 거쳐 정량적으로 검증됐습니다. 예컨대 파일 뷰에서 라인 번호를 제거하자 오프라인에서는 모델 추론 비용이 약 5% 줄었고 온라인에서는 일일 모델 추론 비용이 약 3% 감소했고, 프롬프트 축소는 턴당 약 1,300 토큰을 줄여 세션당 총 토큰을 1.8% 낮추며 활성 시간당 정규화된 비용을 2.9% 절감했습니다. 또한 백그라운드 작업 완료 결과를 배치로 전달해 불필요한 추가 호출을 제거함으로써 AI 크레딧 기준으로 약 2.3%의 토큰 관련 사용량 감소를 기록했습니다. 다만 한 워크플로에서 긍정적이던 변화가 다른 워크플로에서 비용을 늘릴 수 있어, 변경은 광범위한 벤치마킹과 회귀 테스트를 통해 신중히 선별·조정되었다고 보고서는 명시합니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)

