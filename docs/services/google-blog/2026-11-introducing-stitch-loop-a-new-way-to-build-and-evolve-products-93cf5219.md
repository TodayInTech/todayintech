---
title: "Introducing Stitch Loop: A new way to build and evolve products"
sidebar_label: "Introducing Stitch Loop: A new way to build and evolve products"
description: "Google Labs는 코드·실시간 지표와 연동해 목표 달성까지 24/7로 작업하는 장기 실행 제품 에이전트 'Stitch Loop'를 공개했다. 보안·지연·접근성 루프와 Gemini 4 Carbon·CodeMender 통합을 제공하며 대기자 명단을 열었다."
---

# Introducing Stitch Loop: A new way to build and evolve products

> Google Blog · 2026-11-18 · AI/DevTools

---

Google Labs는 2026-11-18 블로그를 통해 **Stitch Loop**를 공개했다. Stitch Loop는 코드베이스와 라이브 메트릭스(로그, 사용자 행동, 피드백 등)를 연결해 측정 가능한 목표를 향해 장기적으로 계속 작업하는 제품 에이전트다. 기존 코딩 에이전트가 PR 머지 시점에서 역할을 멈추는 한계를 넘는 것이 목표다.

## 제안→해결→구현→반영: 루프 기반 작동

Stitch Loop는 제품 컨텍스트를 GitHub, 180개 이상의 통합, 커스텀 MCP 서버 또는 로컬 CLI 업로드로 연결한 뒤 **세 가지 기본 루프**를 제공하고 필요시 사용자 지정 루프를 추가할 수 있다. 각 루프는 1) 제안(Suggestions) — 증거에 기반한 개선 기회 제시, 2) 해결책(Solutions) — 선택 가능한 설계·스코핑과 트레이드오프 제시, 3) 구현(Build) — 격리된 클라우드 샌드박스에서 코드 작성 후 GitHub PR 생성(관련 스크린샷·비디오 포함 가능), 4) 반영(Reflect) — 라이브 데이터 모니터링과 학습으로 구성된다. PR은 사용자가 검토하기 전까지 병합되지 않는다.

## 보안 루프: Gemini 4 Carbon + CodeMender

Stitch Loop에는 사이버보안, 지연(latency), 접근성(accessibility)을 위한 내장 루프가 포함되어 있다. 보안 루프는 **Gemini 4 Carbon**의 사이버보안 역량과 Google DeepMind의 에이전트 **CodeMender**를 결합해 코드베이스를 스캔하고 취약점을 증거와 함께 표시한다. 발견된 이슈에 대해 PR 형태로 제안된 수정안을 열어 사용자가 검토하도록 한다.

## 통합과 실무적 의미

기존 코딩 에이전트(예: Google Antigravity)를 서비스 계층으로 연결하거나 Slack 같은 팀 협업 툴에 통합해 사용 가능하다. 에이전트들은 Stitch CLI와 MCP를 통해 지속적 제품 컨텍스트를 가져와 혼합 모델 구성이나 완전 자동화 개선 작업을 수행할 수 있다. Slack에서는 @stitch로 일일 인사이트 요약을 받고 새 루프를 생성할 수 있다. 핵심 실무적 변화는 문제 발견에서 패치 제안, 배포 전 검토까지의 주기 일부를 Stitch Loop가 계속 돌려 팀의 관찰·반복 부담을 경감할 수 있다는 점이다(단, 병합 권한은 항상 사용자에게 있다).

## 이용 방법

Stitch Loop 대기자 명단은 전 세계 사용자 대상으로 오늘 열렸으며, **Google AI Ultra** 자격이 있는 사용자가 우선 접근권을 가진다. 대기자 등록 페이지는 stitch.google.com/loop/waitlist로 안내됐다.

위 내용은 Google Labs의 블로그 공지에 근거하며 제품의 실제 동작 범위와 통합 방식은 블로그에 공개된 설명에 한해 정리했다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/)

