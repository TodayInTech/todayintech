---
title: "Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents"
sidebar_label: "Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents"
---

# Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents

> Hacker News · 2026-10-12 · 인프라/도구

---

Agent37은 AI 에이전트를 위한 '저비용 샌드박스'를 표방하며 호스트당 평균 비용을 업계의 10% 이하로 낮췄다고 소개한다. 창업자 비슈누는 고객당 평균 지출을 월 $0.37로 제시하고, 무료 플랜의 인프라 비용은 사용자당 월 $0.05~$0.10 수준이라고 밝힌다. 초기에는 OpenClaw 래퍼로 시작했으나 다양한 하네스를 추가하면서 비용 구조를 개선했고, 현재 신규 가입자의 90%가 무료 플랜 사용자로 개인용 Hermes/Openclaw/Claude 코드 등을 호스팅하고 있다고 한다. 부트스트랩 상황에서 무료 플랜을 제공할 정도로 비용 최적화가 진행됐다는 점이 핵심 주장이다.
비용 절감을 위해 제시한 기술적 레버는 세 가지다. 첫째, 에이전트 하네스의 자원 사용 패턴(초기·특정 작업 시 CPU 버스트, 브라우저 등에서 지속적인 RAM 요구)을 관찰해 CPU와 RAM을 효율적으로 관리한 점이다. 둘째, AWS 같은 하이퍼스케일러 대신 Hetzner·OVH 등 하위 공급자를 사용해 호스트 비용을 크게 줄였고, 셋째로 gVisor를 도입해 샌드박스 간 메모리를 공유·캐시하면서 빠른 부트 시간을 확보했다. 다만 gVisor 기반 샌드박스는 Docker-in-Docker나 Android 에뮬레이터 같은 워크로드를 지원하지 않는 트레이드오프가 있다. 또한 RAM을 중심으로 호스트 구성(더 많은 RAM을 압축해 배치)과 필요 시 풀 VM 샌드박스를 별도로 제공하는 전략을 병행한다. 창업자는 Amazon·Quantcast 출신으로 내부 AI 챗봇과 코드 하네스를 구축한 경험을 밝히며, 특히 메시징 에이전트 워크로드를 시험해 플랫폼의 한계와 경제성을 검증해달라고 개발자들에게 제안하고 있다.

[Hacker News에서 원문 읽기 →](https://news.ycombinator.com/item?id=50059096)

