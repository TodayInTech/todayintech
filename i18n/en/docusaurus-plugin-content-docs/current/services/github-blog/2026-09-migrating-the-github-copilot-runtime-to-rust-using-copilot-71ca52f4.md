---
title: "Migrating the GitHub Copilot runtime to Rust, using Copilot"
sidebar_label: "Migrating the GitHub Copilot runtime to Rust, using Copilot"
---

# Migrating the GitHub Copilot runtime to Rust, using Copilot

> GitHub Blog · 2026-09-17 · AI &amp; ML

---

GitHub Copilot의 에이전트 런타임을 TypeScript/Node.js(V8) 스택에서 100% 프로덕션 Rust로 재작성한 작업을 내부 경험과 수치로 설명한 글이다. Copilot CLI·앱·SDK를 뒷받침하던 기존 런타임은 TUI와 런타임이 깊게 결합되어 있었고, SDK 소비자는 각자 Node/V8 런타임을 띄워야 해 시작 지연, 메모리 오버헤드(약 100MB 단위), 프로세스 경계 통신, 단일 스레드화 등 성능·신뢰성 제약이 있었다. 이런 제약을 해결하기 위해 임베드 가능하고 낮은 종속성·저오버헤드·C ABI를 통한 상호운용성 등을 이유로 Rust를 선택했고, Rust로 이식하면서 성능이 수 단위 개선되고 공급망·보안 측면의 장점도 기대되었다. 다만 명시적 수명과 공유 상태 관리처럼 Rust 고유의 복잡성도 수반되었다.
포팅은 ‘인플레이스’ 방식의 원자적 교체(각 컴포넌트를 하나씩 TypeScript에서 Rust로 바꾸고 얇은 숏을 통해 즉시 호출)를 택했고, 에이전트가 대부분 코드를 작성해 128개의 메인 머지 PR로 수개월 내에 점진적 배포가 이뤄졌다. 초기 추정 13만 라인이었던 코드베이스는 포팅 과정에서 약 43만 라인의 프로덕션 TypeScript를 거쳤고, 최종적으로 83만2378라인의 프로덕션 Rust(및 광범위한 Rust 단위 테스트)와 17만4675라인의 E2E TypeScript 테스트를 달성했다. 메인 브랜치를 중단하지 않고 약 열넷 주 반에 걸쳐 평균 1.3회/일 릴리스(총 135회)를 하며 점진 검증을 병행한 점이 특징이며, 이 접근은 소비자 영향 최소화와 빠른 회귀 수정이라는 실무적 이점을 가져왔다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)

