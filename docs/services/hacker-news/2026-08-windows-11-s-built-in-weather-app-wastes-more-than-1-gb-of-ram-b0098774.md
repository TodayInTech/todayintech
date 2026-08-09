---
title: "Windows 11's built-in Weather app wastes more than 1 GB of RAM"
sidebar_label: "Windows 11's built-in Weather app wastes more than 1 GB of RAM"
---

# Windows 11's built-in Weather app wastes more than 1 GB of RAM

> Hacker News · 2026-08-09 · 운영체제/성능

---

Windows 11에 기본 탑재된 Weather 앱이 간단한 예보 표시만으로도 1GB가 넘는 메모리를 소모한다는 테스트 결과가 나왔다. Windows Latest는 앱이 1.2GB 이상을 사용하는 사례를 보고했으며, Wccftech는 보통 시작 시 약 1GB, 유휴 때 500~600MB로 떨어졌다가 확대(줌)나 화면 이동 같은 기본 동작만으로 1.5~1.6GB까지 치솟는다고 관찰했다. 8GB RAM을 장착한 PC에서는 앱 하나가 시스템 메모리의 약 20%를 차지할 수 있어 메모리 압박이 증가하고 페이지 파일 의존도가 높아지며 체감 성능 저하로 이어질 가능성이 있다. 비교로 macOS의 기본 Weather는 유사 조건에서 250MB 이하를 쓰는 것으로 전해져 차이가 크다.
근본 원인으로는 Weather가 완전한 네이티브 앱이 아니라 WebView2 기반의 MSN Weather 웹 앱이라는 점이 지목된다. 작업 관리자에 여러 개의 Chromium 계열 서브프로세스가 나타나는 것이 높은 메모리 사용의 주된 요인으로 분석된다. 앱 내부에 광고(스폰서드 콘텐츠)가 예보 피드에 섞여 노출되는 점도 사용자 비판을 받는 대목이다. 마이크로소프트는 저사양 하드웨어 최적화를 목표로 일부 내장 앱을 개선해왔다고 밝혔고, 향후 더 많은 네이티브 앱을 개발하겠다는 의사도 있지만 MSN 브랜드 앱(Weather 등)을 WinUI로 재구성할지는 불확실하다. 이번 사례는 운영체제 기본 앱의 구현 방식이 시스템 자원 사용과 사용자 경험에 직접적인 영향을 준다는 점을 다시 상기시킨다.

[Hacker News에서 원문 읽기 →](https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html)

