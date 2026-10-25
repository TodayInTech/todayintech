---
title: "Should you read the code, is RAG dead, and did Skills kill MCP?"
sidebar_label: "Should you read the code, is RAG dead, and did Skills kill MCP?"
---

# Should you read the code, is RAG dead, and did Skills kill MCP?

> GitHub Blog · 2026-09-18 · AI &amp; ML

---

최근 GitHub 팟캐스트에서 다룬 여러 AI 관련 '핫테이크'는 자극적 문장으로 소비되기 쉽지만, 실무적으로는 맥락과 위험 판단이 핵심이라는 점을 강조합니다. AI가 생성한 코드를 ‘무조건 안 읽어도 된다’는 주장은 틀렸고, 책임은 인간에게 남아있다는 것이 핵심입니다. 다만 모든 생성 코드에 동일한 수준의 검토를 요구하는 것은 비효율이며, 실무에서는 '결과를 설명하고 맡을 수 있을 때까지' 검토 범위와 깊이를 조정해야 합니다. 채용 관점에서도 단순한 AI 사용 여부보다 언제·어떻게 AI를 쓰는지, 생성물의 품질·보안·유지보수 관점에서 어떻게 검토하는지 설명할 수 있는 판단력이 더 중요한 신호가 됩니다.
스킬(Skills)과 MCP(Model Context Protocol)은 경쟁 관계가 아니라 보완 관계로 설명됩니다. MCP는 도구와 데이터에 표준화된 접근을 제공하고, 스킬은 그 접근을 어떻게 사용해야 할지 문서화된 맥락과 절차를 담아 사람과 시스템 모두에게 도움이 됩니다. RAG가 죽었다는 주장은 과장으로, 좋은 검색·검색 보강은 모델이 유의미한 정보에서 출발하게 해 토큰 낭비와 불완전한 응답을 줄입니다. 또한 모델 파인튜닝을 요구하는 코드는 종종 가독성·구조적 문제가 있어 새로운 사람(또는 에이전트)이 이해하기 어렵다는 신호가 될 수 있다는 점을 들어, AI는 유지보수성과 명확성을 시험하는 또 다른 수단이 된다고 짚습니다. 마지막으로 팟캐스트는 논쟁을 반복하기보다 실험과 증거 축적을 권장하며, Pollinations AI나 Avian Visitors 같은 프로젝트를 예로 들어 실제로 테스트하고 문서화하는 것이 더 유익하다고 결론짓습니다. 요약하면, 도구를 배제하거나 맹목적으로 의존하기보다 검토의 우선순위 설정, 표준화된 인터페이스(MCP), 맥락을 담는 스킬, 그리고 검색 보강(RAG)의 조합으로 실무에 적용하라는 실질적 지침을 제공합니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/should-you-read-the-code-is-rag-dead-and-did-skills-kill-mcp/)

