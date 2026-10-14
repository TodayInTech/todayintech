---
title: "I posted to HN, and then my website was flooded with AI bot traffic"
sidebar_label: "I posted to HN, and then my website was flooded with AI bot traffic"
---

# I posted to HN, and then my website was flooded with AI bot traffic

> Hacker News · 2026-10-13 · 웹 인프라·보안

---

한 개발자가 자신의 커스터마이저블 뉴스 리더(스프링클즈)를 Hacker News에 올린 뒤 겪은 실전 운영 사례를 공유한다. 초기 조회 증가로 예상되는 트래픽 급증을 넘어서며 사이트는 '아주 느리게' 반응했고, 분석 결과 다수의 요청이 SPA 특성상 자바스크립트를 실행하지도 않은 상태에서 들어온 비정상적 호출이었다. NGINX 집계에서 트래픽의 거의 절반이 특정 서비스 사용자로부터 초당 다수의 요청을 받는 형태였고, 해당 서비스는 변경 감지를 위해 사이트를 분당 수십회 쿼리하는 것으로 설명되어 있었다. 그 외 Claude bot, OpenAI bot, Google 등으로 자칭하는 크롤러와 워드프레스 취약점 경로를 노린 스캐너 요청도 포착됐다.
운영자는 문제 식별을 위해 엔드포인트별 로깅을 추가하고, 문제적 에이전트를 차단했으며 robots.txt로 대다수 AI 스캐너를 제지하되 검색엔진에는 접근을 허용하는 정책을 적용했다. 취약점 탐색을 확인하기 위해 Claude에게 취약 경로를 모의 요청하게 하는 등 특이한 검증도 시도했고, 합리적인 레이트 리미트와 함께 인프라 구조 개선을 진행해 실사용 QPS를 견딜 수 있도록 성능을 끌어올렸다고 적었다. 이 사례는 HN 같은 노출이 자동화된 크롤링·요약 서비스의 집중 쿼리로 이어질 수 있음을 보여주며, SPA 특성상 비정상 트래픽 판별, 엔드포인트 수준 로깅, 식별된 사용자 에이전트 차단·robots.txt·레이트리밋 도입, 그리고 근본적인 성능 개선이 실무적 대응이라는 점을 시사한다.

[Hacker News에서 원문 읽기 →](https://www.sammystraus.com/#i-posted-to-hn-and-then-my-website-was-flooded-with-ai-bot-traffic)

