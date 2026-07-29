---
title: "Introducing Claude Opus 4.7"
sidebar_label: "Introducing Claude Opus 4.7"
---

# Introducing Claude Opus 4.7

> Anthropic Blog · 2026-07-23 · AI/모델 출시

---

Anthropic이 일반 공개한 Claude Opus 4.7은 Opus 4.6 대비 복잡한 소프트웨어 공학·장기 추론·에이전트 워크플로에서 의미 있는 성능 향상을 목표로 한 모델 업그레이드입니다. 내부 평가와 고객 테스트에서 93개 코딩 과제 기준 Opus 4.6 대비 해결률이 13% 포인트 상승했고 CursorBench에서는 58%에서 70%로 올랐습니다. 연구-에이전트 벤치마크에서 6개 모듈 중 최고 동률(0.715)을 기록했으며 General Finance 모듈은 0.813(기존 0.767)으로 개선을 보였습니다. 또한 모델이 자체 오류를 잡고 검증하는 능력, 긴 실행 시간의 일관성, 도구 호출과 계획 정확도의 이중 향상 등 실무적 자동화·CI/CD·장기 조사 작업에서의 강점이 여러 파트너 평가에서 반복적으로 보고되었습니다. 멀티모달 측면에서는 이미지 처리 최대 긴 변 2,576픽셀(약 3.75MP) 지원과 시각 정밀도 개선이 특별히 강조되며, XBOW의 시각적 민감도 벤치마크에서 54.5%에서 98.5%로 큰 폭 개선 사례가 제시됩니다.
안전·배치 측면에서는 Mythos Preview보다 사이버 역량을 낮추는 실험을 수행했고, 위험한 사이버 사용을 자동으로 탐지·차단하는 보호책을 적용해 공개 배포를 먼저 진행한다고 밝혔습니다. 합법적 보안 연구자를 위한 Cyber Verification Program도 신설되었습니다. 배포는 Claude 제품군과 API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry로 확장되며 요금은 Opus 4.6과 동일하게 입력 토큰 100만당 $5, 출력 토큰 100만당 $25입니다. 운영상 유의할 변경으로는 토크나이저가 바뀌어 입력 토큰 사용량이 콘텐츠에 따라 약 1.0–1.35× 증가할 수 있고, 상향된 노력(effort) 단계에서 모델이 더 많은 생각을 하며 출력 토큰이 늘어날 수 있다는 점을 안내합니다. 개발자용 기능으로는 xhigh(새로운 노력 단계), 태스크 예산 베타, Claude Code의 /ultrareview 및 자동 권한 모드 등 생산성·비용 제어 수단도 함께 출시되어 마이그레이션 가이드를 참고해 실제 트래픽에서 영향도를 측정할 것을 권고하고 있습니다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/claude-opus-4-7)

