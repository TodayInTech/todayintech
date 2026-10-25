---
title: "Claude Code uses Bun written in Rust now"
sidebar_label: "Claude Code uses Bun written in Rust now"
---

# Claude Code uses Bun written in Rust now

> Hacker News · 2026-07-19 · 개발자 도구/런타임

---

Jarred Sumner의 주장대로 Claude Code v2.1.181(6월 17일 릴리스) 이후 버전이 Bun의 Rust 포트를 사용한다는 점을 로컬 검사로 확인한 기록입니다. 작성자는 자신의 Claude 바이너리에서 strings 명령으로 'Bun v1.4.0 (macOS arm64)' 문자열을 찾아냈고, GitHub의 최신 태그(v1.3.14)보다 높은 버전 번호를 보아 Claude가 아직 공개 태그에 포함되지 않은 Bun 프리뷰(혹은 canary)를 임베드했을 가능성을 제시합니다. 또한 바이너리에서 'src/...\.rs' 형태의 파일 경로 563개를 추출해 시작 파일들(src/runtime/bake/dev_server/mod.rs 등)이 보이는 점을 근거로 Bun의 Rust 구현이 실제로 패키지에 포함되어 배포되고 있음을 보여줍니다.
추가로 bun canary 설치 명령과 Ajan Raj의 트릭(BUN_OPTIONS로 프리로드한 스크립트에서 Bun.version 출력)을 통해 실행 시점에 보이는 버전이 1.4.0으로 확인되었고, package.json의 5월 17일 커밋으로 버전이 업데이트된 사실도 인용됩니다. 기술적 의미는 명확합니다: Bun의 Rust 전환이 단지 개발 브랜치 수준을 넘어 서드파티 애플리케이션(이 경우 Claude Code)에 임베드되어 실제 사용자 환경에서 동작하고 있다는 점이며, 보고된 성능 변화는 스타트업 시간 10% 개선(리포트된 주장)을 포함하지만 저자가 관찰한 것처럼 대부분 사용자는 큰 차이를 체감하지 못했다는 점도 함께 나옵니다. 제공된 근거는 임베드된 버전과 소스 파일의 존재를 직접 보여주지만, 배포 범위나 모든 플랫폼에서의 성능 효과 등은 원문에서 인용된 관찰 범위 안에서만 해석해야 합니다.

[Hacker News에서 원문 읽기 →](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)

