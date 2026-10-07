---
title: "Expanding the Cyber Verification Program"
sidebar_label: "Expanding the Cyber Verification Program"
---

# Expanding the Cyber Verification Program

> Anthropic Blog · 2026-10-06 · 사이버 보안

---

Anthropic이 자사 Cyber Verification Program(CVP)을 통합·확장해 방어자에게 강력한 사이버 역량과 완화된 차단 분류기를 제공한다고 발표했다. 업데이트된 CVP는 Defense Access, Red Team Access, Specialized Access의 세 티어로 구성되며 각 티어는 적격성 요건과 보안 통제가 달라진다. 일반 공개 모델은 보수적 차단을 적용해 악용을 억제하는 반면, CVP는 검증된 보안팀에 대해 Claude Opus 5.5, Claude Sonnet 5.5, Claude Mythos 5.1 등 고성능 모델에 대한 더 적은 차단을 허용한다. Defense Access는 보안운영·침해대응·리버스엔지니어링 등 방어적 작업을 주대상으로 빠른 심사를 목표로 하고, Red Team은 권한 있는 침투테스트를 추가로 허용하되 물리적 피해·대규모 중단을 유발하는 행위에는 실시간 차단을 유지한다. Specialized Access는 항공·전력망·통신·금융 인프라 등 생명·시장에 치명적 영향을 줄 수 있는 시스템 시험을 허용하는 제한된 조직을 대상으로 하며 미국 정부와 협력해 심층 검토를 진행한다.
기술적 유효성 검증도 제시됐다. CyScenarioBench 평가에서 일반 접근은 첫 프롬프트에서 전부 차단됐고, Defense Access에서는 50회 시도 중 46회가 어느 시점에서 차단되었으나 4건은 성공했다. Red Team Access에서는 차단이 발생하지 않아 Claude Opus 5.5가 50개 과제 중 34개를 성공(약 67.6%와 유사)했다는 결과를 보고해, 티어별 분류기 조정으로 방어자에게 고급 역량을 신중히 개방할 수 있음을 시사한다. 또한 Project Glasswing을 통해 2026년 4~7월에 검증된 취약점 129,000건(추가 오픈소스 스캔 5,500건, 그중 33,000건 이상이 고·심각 등급)이 확인되었다는 점을 들어 실무적 효과를 강조한다. 데이터 보존 정책도 중요한 논점으로 남아 있는데, 현재는 참여 조직의 데이터 보관이 요구되며 추후 Enterprise Frontier Safeguards(EFS)로 제로 데이터 보존 환경을 제공할 계획이다. CVP는 Claude Platform, Google Cloud Vertex AI, Microsoft Foundry에서 이용 가능하고 Amazon Bedrock은 EFS 대상 고객에 한해 제공된다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/cyber-verification-program)

