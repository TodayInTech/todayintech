---
title: "Safari introduces Adaptive Dark Mode in 27.3"
sidebar_label: "Safari introduces Adaptive Dark Mode in 27.3"
description: "Safari 27.3 베타에 **Adaptive Dark Mode**가 도입되어 시스템 다크 모드일 때 밝은 웹사이트를 엔진 수준에서 어둡게 변환한다. color-scheme 표시 사이트는 변경되지 않고, 캔버스는 변환하지 않으며 브라우저가 변환 적용을 사이트에 노출하지 않아 프라이버시를 보호한다."
---

# Safari introduces Adaptive Dark Mode in 27.3

> Hacker News · 2026-11-03 · 웹/브라우저

---

Apple은 **Safari 27.3 베타**에 Adaptive Dark Mode를 도입했다고 밝혔다. 사용자가 시스템 외관을 다크로 설정하면 Safari가 밝은 디자인의 웹사이트를 자동으로 어둡게 변환해 일관된 다크 경험을 제공한다. 2019년 Safari 12.1이 웹 다크 모드를 최초 지원한 이후의 확장으로, Apple은 전체 페이지 로드 중 약 **40%가 다크 모드 사용자**에서 오지만 실제로 다크 지원이 있는 페이지는 **10% 수준**이라는 상황을 이 기능의 도입 배경으로 제시했다.

## 변환의 핵심 메커니즘
Adaptive Dark Mode의 핵심은 색상 변환이다. WebKit 내부에서 동작하는 색상 행렬을 사용해 색조(hue)는 보존하면서 명도(luminosity)를 반전해 배경은 어둡게, 텍스트는 밝게 만든다. 텍스트 색상 변환은 **WCAG 4.5:1 대비 비율** 목표를 지향하며, CSS의 밝은 그라데이션도 어두운 쪽으로 변환된다. 아이콘·로고·이미지 처리도 구분한다: 대부분 이미지는 변경하지 않지만, SVG는 검사 후 필요한 색을 변형하고 비트맵 로고는 픽셀 히스토그램을 분석해 단순한 흑백 로고를 반전한다.

특정 그래픽 효과는 문제를 일으킬 수 있어 제한적으로 비활성화한다. 예로 **mix-blend-mode**와 마스크 효과는 변환된 요소에서 원치 않는 결과를 만들 수 있어 경우에 따라 끈다. 한편 **&lt;canvas&gt;** 요소의 내용은 변환 대상에서 제외되어 원본 상태로 렌더링된다.

## 개발자가 취할 설정과 권장사항
사이트가 이미 HTML 메타 태그나 CSS로 다크 모드를 지원한다고 신호를 보내면 Adaptive Dark Mode는 아무 변경도 하지 않는다. 예시로 다음을 권장한다:

&lt;meta name="color-scheme" content="light dark"&gt;

또는 CSS:

color-scheme: light dark

완전한 제어를 원하면 색상 시스템과 다크 스타일을 직접 구현하라고 권장하면서, modern CSS 함수인 **color-mix()**, **contrast-color()**, 그리고 CSS 변수 기반 디자인 시스템을 사용하라고 제안한다. 만약 특정 요소를 변환하지 않길 원한다면 다음과 같은 방식으로 "light only"를 선언할 수 있다(단, ‘only’ 키워드는 Safari 27.3 beta 1에서 미지원).

&lt;meta name="color-scheme" content="light only"&gt;

또는

color-scheme: light only

실무적으로는 로고를 SVG로 대체하고 타일 배경 대신 CSS 색상을 쓰는 등 작은 수정으로 Adaptive Dark Mode 호환성을 높일 수 있다.

## 개인정보·탐지 방지
Safari는 Adaptive Dark Mode 적용 여부를 웹사이트가 감지하지 못하도록 설계했다. JavaScript가 CSS 색상을 조회할 때는 **변환된 값이 아니라 원래 작성된 색**을 반환하며, 캔버스에 그려진 이미지는 원본 형태로 남는다. Apple은 이 조치가 추적(핑거프린팅) 위험을 줄이는 방법이라고 설명한다.

## 사용·피드백 경로
사용자는 시스템 외관을 다크로 설정한 뒤 밝은 배경의 웹사이트를 방문하면 Safari가 미리보기를 제공하고 ‘Try’를 눌러 활성화할 수 있다. 웹사이트 측 문의는 web-evangelist@apple.com으로, 문제를 발견한 사용자는 Feedback Assistant로 리포트하길 권장한다.

위 내용은 Apple의 블로그 글을 근거로 정리한 것으로, 기능 동작 원리(색상 행렬, WCAG 대비 목표, 이미지·SVG·캔버스 처리), 개발자 권장 태그와 개인정보 보호 조치가 근거 문서에 상세히 설명되어 있다. 필요한 추가 변화(예: 'only' 키워드 지원 여부의 향후 변경)는 베타 과정에서 달라질 수 있다.

[Hacker News에서 원문 읽기 →](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/)

