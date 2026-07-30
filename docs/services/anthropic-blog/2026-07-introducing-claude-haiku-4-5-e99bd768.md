---
title: "Introducing Claude Haiku 4.5"
sidebar_label: "Introducing Claude Haiku 4.5"
---

# Introducing Claude Haiku 4.5

> Anthropic Blog · 2026-07-22 · AI 모델 출시

---

Anthropic이 새 소형 모델 Claude Haiku 4.5를 공개하면서 ‘전방(frontier)급 성능을 더 빠르고 저렴하게’ 제공한다는 주장을 내놨다. 회사는 다섯 달 전의 전성기 모델인 Sonnet 4 수준의 코딩 성능을 유지하면서도 비용은 3분의 1, 처리 속도는 2배 이상 향상됐다고 밝힌다. 일부 컴퓨터 관련 작업에서는 Sonnet 4보다 우수한 결과를 보였고, 실시간 대화형 에이전트·고객 응대·페어 프로그래밍처럼 지연이 중요한 애플리케이션에서 유용하다고 제시한다. Sonnet 4.5는 여전히 최전선 모델로 남아 있지만, 복잡한 문제를 Sonnet 4.5가 분해하고 여러 대의 Haiku 4.5가 병렬로 서브태스크를 수행하는 식의 혼용(use-case)도 가능하다고 설명한다. 가격은 입력·출력 토큰 기준 각각 백만당 $1/$5로 공지됐다.
벤치마크와 안전성 검증 결과도 함께 공개됐다. Augment의 에이전틱 코딩 평가에서 Haiku 4.5는 Sonnet 4.5 성능의 90%를 달성했고, 슬라이드 텍스트 생성 같은 지시문 수행에서는 65% 정확도로 프리미엄 모델(44%)을 앞섰다고 보고한다. 내부 안전·정렬 평가에서는 Haiku 4.5가 이전 세대인 Haiku 3.5보다 정렬성이 크게 개선됐고, Sonnet 4.5 및 Opus 4.1보다 오히려 낮은 비율의 비정렬 행위를 보였다고 주장하며, 이 모델에 대해 비교적 완화된 ASL-2 등급을 적용했다. 방법론 설명에는 도구 사용 스캐폴드, 128K 사고 예산 등 구체적 실험 설정과 프롬프트 추가문구가 명시돼 있어 성능 수치가 특정 평가 조건 하에서 산출되었음을 확인할 수 있다. Haiku 4.5는 Claude API, Amazon Bedrock, Google Vertex AI 등에서 Haiku 3.5 및 Sonnet 4의 비용 효율적 대체제로 바로 사용 가능하다고 안내한다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/claude-haiku-4-5)

