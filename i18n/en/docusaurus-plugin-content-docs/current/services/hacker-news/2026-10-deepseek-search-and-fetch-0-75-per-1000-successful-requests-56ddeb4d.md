---
title: "DeepSeek search and fetch – $0.75 per 1000 successful requests"
sidebar_label: "DeepSeek search and fetch – $0.75 per 1000 successful requests"
---

# DeepSeek search and fetch – $0.75 per 1000 successful requests

> Hacker News · 2026-10-18 · 검색 API

---

DeepSeek의 문서는 에이전트와 RAG(검색 결과 증강) 애플리케이션이 실시간 웹 콘텐츠에 접근하도록 설계된 Search API와 Fetch API의 동작 방식을 자세히 설명한다. 두 API는 모두 원시 JSON 인터페이스로 제공되며 베어러 토큰 인증과 application/json 헤더를 사용하고, 기본 URL은 https://api.deepseek.com이다. Search는 내부 검색 엔진으로 쿼리에 맞는 웹 페이지를 구조화된 결과로 반환하고, Fetch는 단일 페이지의 본문을 Markdown으로 추출해 돌려준다. Search 요청은 query, count, ori_question, localization, need_content 같은 필드를 지원하며 쿼리에서 site:, -site:, - (제외), "..."(문구 일치), lang:, after:, before: 같은 연산자를 그대로 전달해 결과를 세밀하게 제어할 수 있다. 응답 항목에는 rerank_score(0~3), title, url, snippet, summary, content, site_name, site_icon, date, authority 등이 포함되어 UI나 모델용 후처리에 필요한 메타데이터를 제공한다.
과금과 운영 제약도 명확히 기술되어 있어 통합 설계 시 유의할 점이 분명하다. Search와 Fetch는 성공적인 요청(HTTP 200에 대해 Search는 non-empty results, Fetch는 실제 페이지 콘텐츠 반환) 건당 과금하며 단가는 각각 1,000건에 $0.75이다. 실패 응답, 빈 검색 결과, 타임아웃은 과금 대상이 아니다. 또한 계정 수준에서 각각 초당 5 QPS의 제한이 적용되며 Fetch에는 추가로 도메인별 QPS 제한이 있어 대량 호출 설계 시 스로틀링과 도메인 분산을 고려해야 한다. 오류 코드(400, 401, 402, 403, 404, 408, 413, 429, 500, 504)와 권장 재시도 행동도 명시돼 있어 안정성 설계에 실무적으로 유용하다. 문서에는 DeepSeek Harness, Claude Code, Codex를 통한 서버사이드 툴 호출은 현재 무료지만 2026년 11월 1일 북경 시간부터는 과금이 적용된다는 점도 포함되어 있어 비용 예측과 배포 일정 수립에 참고할 만하다.

[Hacker News에서 원문 읽기 →](https://api-docs.deepseek.com/guides/search/)

