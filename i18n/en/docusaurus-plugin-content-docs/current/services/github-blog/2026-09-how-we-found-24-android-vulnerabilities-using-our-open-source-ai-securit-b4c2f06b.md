---
title: "How we found 24 Android vulnerabilities using our open source AI security agent"
sidebar_label: "How we found 24 Android vulnerabilities using our open source AI security agent"
---

# How we found 24 Android vulnerabilities using our open source AI security agent

> GitHub Blog · 2026-09-28 · Security

---

GitHub Security Lab은 보안 연구자가 AI 프롬프트와 워크플로를 자동화·공유하도록 돕는 seclab-taskflow-agent를 공개하고, 이를 이용해 안드로이드 앱에서 24건의 취약점을 찾아 보고했다고 설명합니다. 글 작성자는 모바일 특화 감사를 위해 entry point를 모바일·비모바일로 분리하는 gather_mobile_entry_point_info.yaml과, 각 엔트리포인트별로 흔한 취약 클래스(예: 인텐트 기반 취약점)를 체크하도록 하는 classify_application_local.yaml을 도입해 반복 실행과 엄격·광범위 프롬프트의 조합으로 탐지율을 높였다고 밝힙니다. 에이전트를 직접 돌리는 절차와 요구사항(코드스페이스 실행, GitHub Copilot 라이선스·프리미엄 모델 사용, 토큰 소모 주의)도 안내하고 있습니다.
구체적 사례로는 OsmAnd에서 외부 앱이 exported Activity에 인텐트 엑스트라를 주입해 설정을 몰래 교체하고 지도의 타일 URL을 공격자 서버로 바꿔 사용자가 불러온 타일 좌표와 경로를 유출하는 취약점, 위키백과 앱에서는 deeplink 호스트 파서와 쿠키 검사 로직의 허점을 악용해 공격자 제어 페이지로 사용자를 유도하고 장시간 유효한 세션 쿠키를 탈취해 계정 탈취로 이어지는 연쇄 공격을 제시합니다. 저자는 LLM이 논리적 취약점과 API 동작 이해에는 강하지만 심각도 판단과 실제 영향도 산정에서는 오탐과 저평가를 보였고, 증명(PoC) 생성을 위한 추가 프롬프트나 연구자 검토가 필요하다고 지적합니다. 전반적으로 오픈소스 taskflow를 통해 AI가 실무적 취약점 발견에 기여할 수 있음을 보여주며, 보안 연구자와 오픈소스 유지관리자에게 실험·기여를 권장합니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/)

