---
title: "Kimi K3.1 Pro and K3.1 Pro Highspeed"
sidebar_label: "Kimi K3.1 Pro and K3.1 Pro Highspeed"
---

# Kimi K3.1 Pro and K3.1 Pro Highspeed

> Hacker News · 2026-10-23 · 오픈소스/언어모델

---

Kimi는 K3를 확장한 포스트트레인형 모델 K3.1 Pro와 2–3× 속도의 K3.1 Pro Highspeed를 공개했다. 두 모델은 1백만 토큰의 장기 컨텍스트를 지원하는 3T급 오픈 웨이트 제품군으로, Kimi 플랫폼(웹·Work·Code·API)에서 이용 가능하며 전체 모델 가중치는 11월 4일 공개 예정이라고 명시했다. 개발팀은 대규모 공동 강화학습(RL)을 위한 스택 전반의 최적화(환경 품질 검사, 롤아웃 스케줄링, 장문 추론·학습 효율 등)를 통해 도메인별 RL 컴퓨트가 안정적으로 성능 향상으로 이어지도록 했다고 설명한다. 이로 인해 코딩, 3D 생성, 금융 워크플로와 에이전트 작업에서 일관된 이득을 얻었다고 주장한다.
구체적 성과로는 Terminal‑Bench 4.0에서 65.7%를 기록해 GPT‑6 Astra(58.2%)를 앞서고 Claude Opus 5.5(66.4%)에 근접했으며, 내부의 Kimi Code Bench 3.0 Long‑horizon에서는 61.2%로 기존 K3(55.95%)보다 개선됐다. BenchCAD(툴 사용) 92.7%, OfficeQA Pro v2 64.4 등 각종 멀티모달·에이전트 벤치에서도 높은 결과를 보고한다. 한 사례로는 인간 보행 시뮬레이터를 설계·디버그해 어깨 근육 모멘트 암 계산의 36개 오류를 바로잡고 연속 보행을 11.2초까지 개선한 점을 들어 장기 계획·도구 사용·실험 분석 역량을 강조한다. 참고로 보고된 결과들은 'reasoning effort=max, temperature=1.0, top-p=0.95' 등의 평가 설정과 Claude‑Code/Kimi‑Code 등 하네스 사용 조건 하에서 측정되었으므로, 다른 설정이나 하드웨어에서는 성능 차이가 있을 수 있다.

[Hacker News에서 원문 읽기 →](https://www.kimi.ai/blog/kimi-k3-1-pro)

