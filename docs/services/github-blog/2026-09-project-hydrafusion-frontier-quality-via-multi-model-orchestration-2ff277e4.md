---
title: "Project HydraFusion: Frontier quality via multi-model orchestration"
sidebar_label: "Project HydraFusion: Frontier quality via multi-model orchestration"
---

# Project HydraFusion: Frontier quality via multi-model orchestration

> GitHub Blog · 2026-09-04 · AI &amp; ML

---

GitHub은 런타임에서 여러 모델과 공급자를 조합해 작업을 설계·실행하는 연구 프리뷰 'Project HydraFusion'을 발표했다. HydraFusion은 요청별로 실행 계획을 세워 여러 모델을 조합해 초안 작성, 독립적 검토·수정, 또는 고성능 모델로의 에스컬레이션을 선택한다. 세 가지 기본 실행 패턴(단일 모델 직접 해결, 캐스케이드—초안 후 품질 게이트로 에스컬레이션, 크리틱—다른 모델의 독립적 검토 후 수정)을 품질·비용·대기시간의 균형을 고려하는 최적화 문제로 다루며, 개발자는 Copilot에서 일반 모델처럼 HydraFusion을 선택하면 내부에서 적절한 워크플로가 자동 선택된다.
HydraFusion은 실제 리포지토리 수준 작업을 감안해 설계 원칙(비용·사용량의 완전 집계, 각 단계의 시간 제한·취소, 검토 단계의 격리 실행, 실패 시 패치 적용 금지, 실행 전 검증)을 마련했다. 고정 정책으로 Claude Opus 5와 GPT-5.6 Sol을 비교한 오프라인 평가에서 TerminalBench 2.1은 Opus 5 대비 검증된 작업 품질이 4.9포인트 높고 추정 비용은 67% 낮았으며, DeepSWE에서는 품질 -1.5포인트·비용 36% 절감, CheckpointBench는 -0.1포인트·65% 절감 결과를 냈다. 다만 이 결과들은 평가용 벤치마크 구성, 모델 풀, 가격 가정 등에 한정된 통제된 실험 수치라는 점을 GitHub도 명확히 밝히고 있으며, 프리뷰 단계에서 실제 개발자 워크로드에서의 지표·지연·신뢰성·안전성 등을 검증해 생산 수준으로 조정할 계획이다. 현재는 첫 턴·단일 프롬프트 코딩 작업에서 시도해보길 권장하며, 이후 다중 턴·반복적 세션으로 확장하려는 의도를 분명히 하고 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/)

