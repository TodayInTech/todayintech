---
title: "Building safeguards for Claude"
sidebar_label: "Building safeguards for Claude"
---

# Building safeguards for Claude

> Anthropic Blog · 2026-07-06 · AI 안전·거버넌스

---

Anthropic은 Claude를 '도움이 되면서도 안전한' 시스템으로 운영하기 위해 정책 수립에서 모델 훈련·평가·실시간 집행·지속 모니터링까지 전 주기에 걸친 다층적 안전장치를 구축하고 있다고 밝힙니다. Safeguards 팀은 정책·집행·제품·데이터·위협정보·엔지니어링 전문가를 모아 Unified Harm Framework 같은 구조화된 틀로 물리적·심리적·경제적·사회적·자율성 차원의 위험을 검토하고, 외부 도메인 전문가와의 Policy Vulnerability Testing으로 모형 출력의 취약점을 스트레스 테스트해 정책과 학습·탐지 체계에 반영합니다. 구체적 사례로 2024년 미국 선거 대응에서 권위 있는 투표 정보로 유도하는 배너를 추가한 일과, 자살 및 정신건강 대응을 위해 ThroughLine과 협력해 미묘한 응답 차이를 훈련에 반영한 사례를 제시합니다.
사전 평가에서는 안전성·위험·편향 테스트를 통해 모형의 정책 준수와 능력상승(ability uplift)에 따른 위협 모델을 점검하며 결과는 각 모델 계열의 시스템 카드로 공개합니다. 배포 후에는 'classifiers'라 불리는 특수 소집중 모델들과 사람의 검토를 결합해 실시간으로 위험을 탐지·유도(steering)하거나 필요한 경우 응답 중단, 계정 경고·정지 등 집행을 합니다. 기술적 난제로는 수조 토큰을 처리하면서도 정상 콘텐츠에 대한 과도한 집행을 피하는 것이 있으며, 이를 보완하기 위해 해시 기반 CSAM 비교, 계정 수준의 계층 요약(hierarchical summarization), 외부 위협 인텔과의 교차검증 같은 방법을 활용합니다. Anthropic은 대외 협력·버그바운티·채용을 통해 이러한 보호 작업을 지속할 계획임을 밝히며, 조직 단독으로는 해결하기 어려운 문제라는 점을 강조합니다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/building-safeguards-for-claude)

