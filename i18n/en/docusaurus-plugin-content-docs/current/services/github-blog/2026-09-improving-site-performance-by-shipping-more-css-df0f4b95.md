---
title: "Improving site performance by shipping more CSS"
sidebar_label: "Improving site performance by shipping more CSS"
---

# Improving site performance by shipping more CSS

> GitHub Blog · 2026-09-25 · Architecture &amp; optimization

---

GitHub의 Primer 디자인 시스템 팀은 페이지당 컴포넌트 수 증가로 인해 CSS-in-JS에서 발생한 클라이언트 초기화 비용, 서버 사이드 렌더링(SSR) 성능 저하, 스타일 업데이트 복잡성 문제를 해결하기 위해 CSS Modules로 전면 전환했다. CSS Modules는 네이티브 CSS 기능을 유지하면서 클래스명을 로컬로 취급하고 런타임 동작을 제거해 스타일을 HTML과 함께 전송하도록 했고, 마이그레이션은 구성요소별로 CSS 파일 추가, 기능 플래그, 시각 회귀 테스트를 활용한 점진적 롤아웃 방식으로 진행됐다. Primer 전환을 완료한 2024년 12월 기준으로 SSR 시간은 55% 단축되고 컴포넌트 초기화는 25% 개선되는 등 명확한 성능 이득이 확인됐다.
전체 도메인으로 확장하는 과정에서는 sx prop(인라인 스타일 객체)의 광범위한 사용이 난제로 남았고, 이를 유지하면서도 성능을 확보하기 위해 @primer/styled-react라는 래퍼 패키지를 도입해 호환성을 유지했다. 2025년 4월 시작된 sx 마이그레이션은 VS Code 플러그인과 내부 코데모드로 상당 부분 자동화되어 8명 로테이션으로 6개월 간 6,419개 prop을 옮기며 페이지별 SSR 1~22% 개선을 관측했고, 2026년 4월에는 Copilot 코딩 에이전트를 활용해 남은 895개를 3주만에 제거했다. 또한 스타일링 의존성(테마 유틸리티)까지 단계적으로 분리·교체해 styled-components와 styled-system, sx를 완전히 제거했고, 결과적으로 2026년 6월부로 GitHub는 100% CSS Modules 기반으로 운영되며 대규모 UI 시스템에서 점진적 마이그레이션, 자동화 도구와 기능 플래그를 결합한 실무적 방안을 보여준다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)

