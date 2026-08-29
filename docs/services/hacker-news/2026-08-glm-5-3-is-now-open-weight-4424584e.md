---
title: "GLM-5.3 is now open-weight"
sidebar_label: "GLM-5.3 is now open-weight"
---

# GLM-5.3 is now open-weight

> Hacker News · 2026-08-28 · 모델 공개/릴리스

---

GLM-5.3는 내부적으로 GLM-5.2와 동일한 베이스 모델을 사용하되, 포스트트레이닝으로 성능을 끌어올린 점을 전면에 내세웁니다. 특히 코드 작성 능력에서 자사 Z.ai Code Bench 기준으로 GLM-5.2 대비 50% 향상을 보였고, Terminal Bench 3.0·Agents' Last Exam 등 공개 벤치에서도 오픈소스 최상위 성능을 기록했습니다. 포스트트레이닝 규모를 늘리면서 예상보다 빠르게 발전한 '사이버 역량'도 눈에 띄어 CyberGym에서는 높은 취약점 발견 성능을 보였고, 익스플로잇 관련 벤치에서는 상위 단계(익스플로잇 체인)에서 GLM-5.2보다 두 배 이상 큰 폭의 개선이 나타났습니다. 벤치마크 표와 수치가 공개되어 있어 구체적인 비교 지표를 확인할 수 있습니다.
배포·운영 측면에서는 Hugging Face에 게시된 모델을 vLLM, Transformers, SGLang, TokenSpeed 등 다양한 프레임워크로 실행할 수 있도록 문서와 레시피를 제공하며, Ascend NPU용 추론 프레임워크(vLLM-Ascend, xLLM 등)도 지원한다고 명시했습니다. 모델은 reasoning_effort( low/high/max)와 chat 템플릿의 clear_thinking 파라미터 등을 통해 ‘사고 예산’을 조절할 수 있고, 평가에서는 최대 300,000~1,000,000 토큰 수준의 컨텍스트와 수십만 토큰 출력(예: max_new_tokens 128k, 평가 시 max_generation 163,840 등), temperature/top_p 등의 샘플링 설정을 일관되게 적용했습니다. 또한 각 벤치에 맞춘 타임아웃·컨테이너 격리·도메인 화이트리스트 등 평가 재현성과 안전성을 고려한 절차를 상세히 기술해 연구·제품화 단계에서의 재현 가능성과 적용 고려사항을 함께 제공합니다.

[Hacker News에서 원문 읽기 →](https://huggingface.co/zai-org/GLM-5.3)

