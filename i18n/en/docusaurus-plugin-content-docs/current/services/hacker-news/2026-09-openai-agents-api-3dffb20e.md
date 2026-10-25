---
title: "OpenAI Agents API"
sidebar_label: "OpenAI Agents API"
---

# OpenAI Agents API

> Hacker News · 2026-09-10 · AI 플랫폼

---

OpenAI의 Agents API는 개발자가 OpenAI가 관리하는 Codex 하니스에 애플리케이션을 연결해 에이전트를 생성·운영할 수 있도록 설계된 관리형 인터페이스입니다. OpenAI는 세션 관리, 작업 오케스트레이션, 컨텍스트 압축(요약) 및 복구를 담당하고, 개발자는 도구와 실행 환경을 제공해 에이전트가 코드 실행·파일 편집·MCP 서버 연결·아티팩트 생성 등을 수행하도록 할 수 있습니다. 핵심 개념으로는 에이전트(모델·지침·도구·MCP), 환경(옵션인 샌드박스), 세션(지속적 인스턴스), 이벤트·아이템(입출력)이 제시되며, 문서에는 사고 대응 에이전트·슬랙 봇·데이터 분석가·깃허브 이슈 조사자·문서 검토자 등 실제 응용 예도 포함되어 있습니다.
사용 예시 코드에서는 model로 "gpt-6-astra"를 지정하고, 지침으로 OpenAI 문서 MCP와 웹 검색을 활용해 기술 질문에 답하라며 도구로 programmatic_tool_calling, mcp(transport HTTP, server_url=https://developers.openai.com/mcp), web_search를 등록하고 multi_agent를 활성화해 최대 동시 서브에이전트 4개를 허용하는 구성을 보여줍니다. 세션은 OpenAI가 환경을 프로비저닝한 뒤 입력을 받아 스트리밍 출력이나 웹훅으로 진행 상황을 알리고, 동일 세션에 추가 작업을 보내어 작업을 이어갈 수 있습니다. 관리형 하니스는 작업 분할·서브에이전트 위임·이전 작업 요약·재개 기능을 제공하며, 과금은 선택한 모델의 API 요금과 OpenAI 도구 표준 요금, OpenAI 호스티드 샌드박스의 컨테이너 요금이 적용됩니다. 데이터 관련 제한으로는 현재 데이터 거주가 미국만 지원되고 Zero Data Retention(ZDR)은 지원하지 않으며, 셀프 호스티드 샌드박스를 선택해도 ZDR 대상이 되지 않는 점이 명시되어 있습니다.

[Hacker News에서 원문 읽기 →](https://developers.openai.com/api/docs/guides/agents-api/overview)

