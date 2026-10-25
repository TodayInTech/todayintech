---
title: "GitHub’s model for secret detection: Finding more secrets with less noise"
sidebar_label: "GitHub’s model for secret detection: Finding more secrets with less noise"
---

# GitHub’s model for secret detection: Finding more secrets with less noise

> GitHub Blog · 2026-10-13 · AI &amp; ML / Security

---

GitHub은 제너럴한 패턴 매칭만으로는 구별하기 어려운 ‘일반형(generic) 시크릿’ 문제를 해결하기 위해 컨텍스트 인식 분류기를 도입했다. 기존 LLM 기반 파이프라인을 대체하는 방식이 아니라, 고회수성(regex) 후보 생성 단계와 문맥을 읽는 소형 ModernBERT 분류기를 결합한 두 단계 파이프라인을 적용했다. 후보 생성은 빠르고 결정론적으로 넓은 범위를 포착하고, 분류기는 파일 경로·변수명·주변 코드·텍스트 등을 함께 입력받아 실제 자격증명과 문서의 플레이스홀더·테스트 픽스처·체크섬 같은 하드 네거티브를 구분한다. 모델은 ONNX로 8비트 양자화해 효율적으로 서빙되며, 지연과 비용 측면에서 LLM 호출보다 유리한 형태로 설계됐다.
학습은 GitHub 실사용 예제, 고회수성 후보에서 파생한 약한 레이블, 그리고 문서·테스트·공개키·체크섬 등 난해 사례를 겨냥한 합성 데이터로 구성했다. 오프라인 평가에서 정밀도 13%, 재현율 19% 향상, 프로덕션 A/B 실험에서는 리포지토리 소유자 가중 수용도가 11.5% 상승한 것으로 보고됐고, 포스트-푸시 스캔 실행 시간은 중앙값 기준으로 86% 단축되었으며 LLM 기반 파이프라인 대비 비용은 98% 이상 절감되었다고 명시돼 있다. 기술적 함의는 명확하다: 좁고 측정 가능한 결정 경계에서는 소형의 특화된 인코더 분류기가 대형 생성형 모델보다 실무적 효용과 비용-지연 효율이 높다는 점이며, 이 접근은 푸시 보호까지 실시간 피드백을 확대해 개발자 신뢰도를 높이는 데 기여한다. 향후에는 생산 피드백 루프를 통한 지속적 개선과 탐색적 아키텍처 연구로 탐지·추출을 단일 단계로 통합하는 방안을 모색한다고 밝혔다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/githubs-model-for-secret-detection-finding-more-secrets-with-less-noise/)

