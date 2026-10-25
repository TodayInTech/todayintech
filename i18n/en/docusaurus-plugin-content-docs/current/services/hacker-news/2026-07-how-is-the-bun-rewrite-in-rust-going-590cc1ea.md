---
title: "How is the Bun Rewrite in Rust going?"
sidebar_label: "How is the Bun Rewrite in Rust going?"
---

# How is the Bun Rewrite in Rust going?

> Hacker News · 2026-07-27 · 인공지능·오픈소스

---

Bun의 Rust 리라이트를 둘러싼 주장과 실제 진행 상황을 깔끔하게 추적한 글이다. 작성자는 Jarred Sumner의 "Rewriting Bun in Rust" 발표와 그에 따른 Anthropic API 호출 비용(총 165,000달러, 5월 3일–14일 사이)을 출발점으로 삼아 깃 저장소와 PR·빌드 로그를 확인했다. 분석 결과로는 리라이트가 메인에 병합된 지 여섯 주가 지났지만 릴리스 태그는 없고(최근 태그: 2026-05-12), robobun(Claude)에서 만든 오픈 PR 수가 7월 9일의 1277건에서 7월 27일 2475건으로 급증했다는 점, 빌드파이프라인이 지속적으로 돌고 있어 CI 비용·인력 투입이 추가로 발생했을 가능성이 높다는 점이 드러난다. 작성자는 하루 1만5천 달러라는 초기 수치가 CI·내부 인력 등 비용을 반영하지 않아 과소평가됐을 수 있고, 현재 진행 중인 작업을 감안하면 총비용이 훨씬 커질 수 있다고 경계한다.
기술적 의미는 두 가지다. 하나는 "AI가 오픈소스 유지보수를 대체해 빠르게 코드베이스를 전환했다"는 단순한 서사는 근거가 부족하다는 것이다: Anthropic 직원의 직접 개입, Claude 사용량 급증, 완료 후에도 이어지는 대규모 PR·CI 활동은 단기간의 API 호출 비용만으로 전체 작업을 설명할 수 없음을 시사한다. 다른 하나는 자본·평가 관점으로, AI 성능을 근거로 한 높은 기업 가치 주장에 대해 더 신중한 검증이 필요하다는 점이다. 저자는 자신도 ML·AI 작업 경험이 있지만 현재의 과도한 과대포장(hype)을 경계하며, 단순한 비용·성공 사례보다는 지속적 유지·검증 관점에서 결과를 봐야 한다고 결론지었다.

[Hacker News에서 원문 읽기 →](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html)

