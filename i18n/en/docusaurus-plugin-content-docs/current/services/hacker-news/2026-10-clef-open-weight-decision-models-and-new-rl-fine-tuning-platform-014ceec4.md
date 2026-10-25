---
title: "Clef: Open-weight decision models, and new RL fine-tuning platform"
sidebar_label: "Clef: Open-weight decision models, and new RL fine-tuning platform"
---

# Clef: Open-weight decision models, and new RL fine-tuning platform

> Hacker News · 2026-10-01 · 인공지능/머신러닝

---

Cloudflare가 의사결정용 분류기(Decision model) 계열인 Clef와 저지연 버전 Clef-flash를 공개했다. 이 모델들은 Jev API와 호환되며 Hugging Face에 Apache 2.0 라이선스로 가중치를 공개해 로컬 실험도 가능하다. 회사 측 평가는 Clef가 Jev Decision Index에서 선도적 성적을 냈다고 밝혔고, 웹 도메인 분류 사례에서는 Clef가 브라우저 렌더링 포함해 2.2초 만에 분류를 완료한 반면 비교한 범용 LLM(gpt-oss-120b)은 동일 워크플로에서 4.7초가 걸렸다고 제시했다. Clef는 시각 입력을 처리하는 비전 인코더와 64k 컨텍스트 윈도우를 지원해 더 많은 상태를 다룰 수 있고, Workers AI의 엣지 GPU 호스팅을 통해 네트워크 지연을 줄여 ‘핫 패스’에 넣을 수 있다고 설명한다.
기술적으로 Clef는 Qwen 계열(대형: Qwen3.8-27B, 플래시: Qwen3.5-9B)을 백본으로 고정(freeze)한 뒤, 비자동회귀(non-autoregressive) 방식으로 스키마 선택지를 병렬 스코어링해 구조화된 확률 출력만 반환하는 점이 핵심이다. 내부적으로는 두 단계 주의(routing)와 옵션별 증거 추출, 교차 필드 어텐션을 결합하고, 라벨 스무딩 교차엔트로피·브리어 손실(Brier loss) 및 RLCD(Reinforcement Learning for Calibrated Decisions) 같은 보정 기법을 활용해 확률 보정 및 일반화 성능을 개선했다고 밝혔다. 클라우드플레어는 고객 요청을 읽거나 저장·훈련하지 않는다고 약속하면서(단, 파인튜닝 제품 이용 시 예외), 초기에는 FDE(현장 엔지니어) 기반의 핸즈온 파인튜닝을 제공하고 추후 AI Gateway·Containers·Trainer·Workers AI를 결합한 자가 서비스형 RL 파인튜닝 플랫폼을 내놓을 계획이라고 밝혔다. 이러한 설계는 빠르고 결정론적인 분류가 필요한 에이전트형 워크플로우(티켓 라우팅, 신뢰·안전 평가, 봇 판별 등)에 직접 투입해 지연과 맞춤성 간 균형을 맞출 수 있다는 실무적 의미를 가진다.

[Hacker News에서 원문 읽기 →](https://blog.cloudflare.com/clef-decision-models/)

