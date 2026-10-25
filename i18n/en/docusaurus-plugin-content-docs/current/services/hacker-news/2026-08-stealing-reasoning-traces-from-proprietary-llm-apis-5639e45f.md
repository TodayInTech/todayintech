---
title: "Stealing Reasoning Traces from Proprietary LLM APIs"
sidebar_label: "Stealing Reasoning Traces from Proprietary LLM APIs"
---

# Stealing Reasoning Traces from Proprietary LLM APIs

> Hacker News · 2026-08-11 · AI 보안/LLM

---

연구진은 공개적으로 수집한 에이전트 궤적에서 ‘숨겨진 추론(hidden reasoning)’을 복원하는 공격을 제시하고, 이를 OpenAI·Anthropic·Google 계열의 최전선 모델 전반에서 검증했다. GitHub과 Hugging Face에서 수집한 6,708개의 공개 에이전트 궤적에 남아 있던 서명된(암호화된) 추론 블록에 대해 디코딩 파이프라인을 적용한 결과 315,320개의 추론 블록을 재구성했고, 복원된 추론의 토큰 수는 API가 보고한 숨겨진 thinking-token 수와 밀접하게 일치한다고 보고한다. 또한 120개 Codeforces 문제를 대상으로 한 비교에서는 API가 보고하는 숨겨진 토큰 수와 디코딩된 추론 토큰 수 간의 정량적 대응을 제시했다는 점이 근거로 제시된다.
가장 직접적인 보안 문제는 복원된 추론에 실제 민감 정보가 포함되어 있다는 사실이다. 연구자는 벤치마크를 제외한 실제 사용자 세션에서 704개의 고유 프라이버시 유물(62개 API 키, 33개 비밀번호, 24개 액세스 토큰, 30개 개인 이메일 주소 및 이름·우편주소·내부 URL 등 기술 식별자)을 확인했고, 이 가운데 64개 항목은 가시 세션에는 전혀 나타나지 않고 오직 추론 블록 안에만 존재했다. 기술적 영향으로는(1) 한 모델의 추론 일부를 다른 모델에 프리필(prefill)하면 타깃 모델의 가시적 답변 표현이 시드 모델 쪽으로 이동하는 현상(Kimi‑K3가 Opus 4.8의 처음 1% 토큰으로 영향을 받음), (2) 유해한 내용을 표면적으로는 무해하게 처리하더라도 위험한 지식이 숨겨진 추론 안에 남을 수 있다는 점, (3) API의 요약이 실제로는 ‘답을 먼저 말하고 뒤에서 유도한’ 상황을 깨끗한 유도 과정으로 보이게 만들 수 있다는 관찰 등을 제시한다. 논문은 arXiv에 등록되어 있으며, 복원 기술과 발견된 민감 정보 수치가 함께 제시되어 LLM 기반 서비스의 추론·로그 처리 방식과 개인정보·안전성 정책에 즉각적인 재검토를 요구하는 의미 있는 증거를 제공한다.

[Hacker News에서 원문 읽기 →](https://stolen-thoughts.com/)

