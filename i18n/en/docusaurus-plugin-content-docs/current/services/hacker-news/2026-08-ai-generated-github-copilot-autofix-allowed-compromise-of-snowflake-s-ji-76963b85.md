---
title: "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira"
sidebar_label: "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira"
---

# AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira

> Hacker News · 2026-08-17 · 정보보안

---

Wiz의 자율 보안 연구 도구인 Red Agent가 GitHub Actions 워크플로우의 스크립트 주입 취약점을 찾아 Snowflake 내부 Jira에 접근권을 검증한 사건이다. 취약점은 snowflakedb/snowflake-connector-net 저장소의 jira_issue.yml에서 이슈 제목을 셸 명령에 직접 보간하면서 발생했고, 위험한 변화는 6월 18일 PR #1218 병합으로 생겼다. 최종 커밋에는 ‘Copilot Autofix powered by AI’가 공동저자로 표기되어 있으며, 이후 업데이트에서 코파일럿이 병합된 PR과 코드 변경을 확인하고 문제가 없다고 판단했다고 명시되나 코드 변경이 AI에 의해 생성되었는지는 불명확하다고 밝혔다. Red Agent는 자동으로 취약점을 스캔·공격·검증했고, 최초 시도에서 문법 오류가 발생하자 자체적으로 페이로드를 조정해 몇 초 내에 Azure IP로부터 base64 인코딩된 Jira 토큰을 받아냈다. 이 토큰은 여러 엔지니어링·보안·버그 바운티 프로젝트에 대한 읽기 권한을 부여했다.
사후 조치로 Snowflake는 신고 당일(6월 23일) 워크플로우를 패치(원래의 env: 변수+jq --arg 파싱 패턴 복구)하고 토큰을 회수·교체했으며, 포렌식 분석에서 노출 기간(약 5일) 동안 외부 접근은 Wiz 테스트 IP에 한정된 것으로 확인했다. 이 사건은 AI 기반 코드 생성·수정과 AI 보안 검토가 기존의 안전 패턴을 무심코 제거할 위험, 그리고 자동화된 리서처가 짧은 시간 내에 취약점을 찾아 악용할 수 있다는 점을 동시에 드러낸다. 기술적 시사점은 AI 생성 PR에 대해서도 정적 분석과 역사적 맥락을 반영한 가드레일을 적용하고, 짧은 탐지 창을 전제로 한 신속한 패치·단기 자격증명 사용 정책을 강화해야 한다는 것이다.

[Hacker News에서 원문 읽기 →](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

