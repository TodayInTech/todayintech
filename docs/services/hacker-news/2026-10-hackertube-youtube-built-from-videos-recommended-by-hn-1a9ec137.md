---
title: "HackerTube: YouTube built from videos recommended by HN"
sidebar_label: "HackerTube: YouTube built from videos recommended by HN"
description: "Karpathy는 Opus 5.5와 Sonnet 기반 워크플로로 Hacker News 댓글에서 추천된 6,454개(2007–2026, 150주제) 유튜브 영상을 모아 hackertube.org로 배포했으며, 로컬 세션 기반 추천·50% 썸네일·데이터 내보내기 등 기능을 제공한다."
---

# HackerTube: YouTube built from videos recommended by HN

> Hacker News · 2026-10-31 · projects

---

Karpathy는 개인용 AI(“Opus 5.5”)를 활용해 Hacker News 댓글에서 추천된 유튜브 영상들만 모은 YouTube 클론 **HackerTube**(hackertube.org)를 만들었다고 밝혔다. 작업 과정은 HN의 모든 댓글을 받아 스팸·저급 콘텐츠를 제거하는 필터링을 거쳐 '비디오 추천'으로 태깅된 40,000개의 댓글을 선별했고, 그 결과 **2007년부터 2026년까지 HN 사용자들이 추천한 6,454개 유튜브 영상**을 확보했다고 한다. 전체 항목은 약 150개 주제에 걸쳐 분포한다.

## 데이터 수집·선별과 구현
Karpathy에 따르면 Opus가 댓글을 다운로드하고 Sonnet을 포함한 워크플로로 필터링을 수행했다. 그 뒤 유튜브 스타일 UI를 씌우고 도메인을 얻어 VPS에 배포했으며, 서비스는 '보안·하드닝·최적화' 과정을 거쳤다. 전체 제작 시간은 약 **2시간**으로 적시했다.

## 사용자 기능과 실무적 의미
- **로컬 브라우저 세션에 상태를 저장하는 사용자 계정 없는 맞춤 추천(ForYou)**: 서버에 개인 프로파일을 두지 않는 접근이라 사생활·운영 복잡도 측면에서 간소화된다(근거: 원문 문장).  
- **'50% 썸네일' 사용**: 업로더가 올린 썸네일 대신 다른 방식의 축약 이미지를 사용한다고 표기했다(근거: 원문).  
- **데이터 내보내기 기능**: 사이트 데이터를 에이전트에 넘겨 자신의 버전을 만들 수 있게 한다고 밝혀, 재사용·파생 프로젝트가 용이하다(근거: 원문).  
- **키보드 단축키 등 UI 편의 기능**도 제공한다.

이 사례는 개인용 AI와 간단한 자동화 파이프라인으로 커뮤니티 추천 기반의 콘텐츠 큐레이션·배포가 빠르게 가능함을 보여준다. 출처는 Karpathy의 설명이며, 기술적 세부(구체적 필터 기준, 추천 알고리즘의 내부 동작, YouTube API/저작권 처리 등)는 원문에 서술되지 않아 본문 범위에서는 확인되지 않는다.

[Hacker News에서 원문 읽기 →](https://karpathy.bearblog.dev/hacker-tube/)

