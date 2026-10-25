---
title: "Gemini 3.8 Flash and 3.8 Flash Cyber"
sidebar_label: "Gemini 3.8 Flash and 3.8 Flash Cyber"
---

# Gemini 3.8 Flash and 3.8 Flash Cyber

> Hacker News · 2026-09-02 · 인공지능/모델

---

Google은 Gemini 3.8 Flash와 그 사이버 특화판인 3.8 Flash Cyber를 공개하며, 이전 3.7 Flash와 동일한 저비용·고속 운영을 유지하면서 추론과 코딩 성능을 끌어올렸다고 밝혔다. 3.8 Flash는 장기 소프트웨어 엔지니어링(DeepSWE v1.1)과 복합적 다단계 추론(HLE-Verified 54.9%)에서 큰 성과를 보였고, Vals Finance Agent V2와 Harvey’s Legal Agent 같은 전문 벤치마크에서도 개선을 보였다. 비용 민감한 워크로드를 위해선 낮은 노력 수준을 선택하거나 3.7 Flash를 계속 사용할 수 있다고 명시해 성능·비용 선택지를 제공한다. 가격 정책도 공개되어 입력 토큰당 $0.75, 출력 토큰당 $3.75의 도입가를 유지한다.
3.8 Flash Cyber는 취약점 탐지와 자동 패치에서 전방위적 성능 향상을 목표로 하며, CyberGym과 내부 다언어 벤치마크에서 70% 초과 성공률 등 우수한 결과를 보고했다. 패치 능력은 CWE-Bench에서 pass@1 47.2%로 선도 모델과 유사한 효율을 보이면서도 비용은 낮다고 설명한다. 실제 적용 사례로 Chrome 보안팀이 상용 대체 모델보다 2.6배 더 많은 올바른 패치를 얻었고, Wiz와 Google Cloud 팀이 각각 비용 대비 향상된 리콜과 몇 시간 내 핵심 취약점 발견 사례를 제시했다. 보안·악용 방지 측면에서는 CBRN·사이버 공격 관련 완화책을 적용했고, Cyber 판은 보다 완화된 규칙을 필요로 해 신뢰받는 수비자에게 Fairwind 프로그램을 통해 접근을 허용한다고 밝혔다. 또한 모델은 복잡한 문제에서 추가 추론 단계와 도구 반복 호출을 통해 성능을 끌어올리는 설계적 선택을 택해, 토큰 사용량과 계산 비용 사이의 트레이드오프를 명확히 제시한다. 개발자는 Antigravity·Gemini API·AI Studio 등으로 접근 가능하고, 엔터프라이즈·소비자용 배포 경로도 별도로 안내되어 있다.

[Hacker News에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

