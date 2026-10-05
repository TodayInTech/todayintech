---
title: "Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s"
sidebar_label: "Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s"
---

# Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s

> Hacker News · 2026-10-04 · AI / 오픈소스

---

Strata는 Qwen3.8-Flash-Next(125B) 같은 대형 언어모델을 개인용 GPU로 실행할 수 있게 해주는 오픈소스 런타임이다. 문서와 측정 결과에 따르면 RTX 50·30·20 계열이나 AMD의 RX 7000/9000 계열 등 VRAM 12GB 이상 카드와 32GB 이상의 시스템 RAM을 갖춘 윈도우/리눅스 PC에서 모델을 돌릴 수 있으며, 모든 처리와 응답이 로컬에서 이뤄진다고 명시한다. 저자들이 제시한 벤치마크는 두 대의 일반 게이밍 PC(예: RTX 5070, RX 9070 XT)에서 수행되었고, 예시로 Q2_0는 최대 94 토큰/s, IQ3_S는 약 53 토큰/s로 답변을 생성했으며 긴 프롬프트 읽기는 초당 수천 토큰 수준을 보였다. 설치는 약 70GB 규모의 모델 다운로드와 함께 진행되며, 첫 기동 시 35–55GB를 RAM에 로드해 1~3분가량 시스템이 느려질 수 있다고 안내한다.
기술적 의미는 세 가지다. 첫째, Strata는 GPU VRAM만으로 모델을 온전히 보관하지 않고 RAM·SSD·CPU를 조합해 믹스드 리소스 방식으로 대형모델을 '맞춰 넣는' 아키텍처를 사용해, 개인 하드웨어로도 서버급 모델을 활용할 수 있게 한다. 둘째, 모델 크기별 권장 RAM(32/48/64/96GB 등)과 압축·튜닝(예: Swift 1.5, Unsloth ~4-bit) 옵션을 제공해 성능·정확도·응답속도 간의 실용적 트레이드오프를 사용자가 선택하게 한다. 셋째, OpenAI/Anthropic 호환 API 엔드포인트를 제공해 기존 코드보조기나 앱과 손쉽게 통합할 수 있다는 점에서 로컬 프라이버시와 개발자 워크플로우에 즉시 활용 가능한 대안으로 주목된다. 다만 문서가 여러 하드웨어·설치 환경에서의 실험적 결과와 트러블슈팅 절차를 포함하므로, 실제 배포 전 자신의 VRAM·RAM·SSD 여유를 확인하고 권장 모델 크기를 따르는 것이 필요하다.

[Hacker News에서 원문 읽기 →](https://github.com/Niko1221/Strata)

