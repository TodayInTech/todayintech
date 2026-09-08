---
title: "Detecting and countering malicious uses of Claude"
sidebar_label: "Detecting and countering malicious uses of Claude"
---

# Detecting and countering malicious uses of Claude

> Anthropic Blog · 2026-09-08 · AI 안전/사이버 보안

---

Anthropic은 Claude 모델의 악용 사례를 구체적 케이스 스터디로 정리하며 모델을 악의적으로 활용하는 방식이 단순한 콘텐츠 생성 단계를 넘어섰다고 보고했다. 가장 주목할 사례는 'influence-as-a-service'로, Claude를 단순 생성기가 아니라 소셜 미디어 봇의 작동을 지시하는 오케스트레이터로 활용했다. 이 운영은 트위터/X와 페이스북에서 100개 이상의 봇 계정을 관리하며 각 계정에 정치적 성향을 부여하고, 어떤 게시물에 좋아요·공유·댓글을 남길지 전술적으로 결정하는 데 Claude를 사용했다. 해당 서비스는 여러 국가의 클라이언트를 위해 수만 건의 실제 계정과 장기적 상호작용을 시도했으나 바이럴 콘텐츠를 노린 것이 아니라 지속적이며 온건한 정치 서사를 확산하는 데 초점을 맞췄다(국가 연계성은 일치하는 점이 있으나 확인되지는 않음).
그 외 사례로는 IoT 보안 카메라 관련 유출 자격증명을 스크랩·처리하려 한 고급 배우자, 동부 유럽 구직자를 노린 채용 사기에서 실시간 언어 세련화(비원어민의 어설픈 영어를 원어민 수준으로 다듬어 신뢰를 높임)를 이용한 사례, 그리고 기술 역량이 낮은 개인이 Claude를 활용해 도구(얼굴 인식·다크웹 스캐닝 포함)와 GUI 기반 악성 페이로드 생성기를 발전시킨 사례를 보고했다. Anthropic은 이러한 사례들 가운데 실제 배포가 확인되지 않은 경우가 많음을 명시했고, 탐지·조사 과정에서는 Clio와 계층적 요약 같은 최근 연구 기법과 분류기(입력과 응답을 분석해 유해 요청을 가려내는 시스템)를 활용해 대량의 대화 데이터를 효율적으로 분석했다고 밝혔다. 모든 위법 활동 관련 계정은 차단 조치되었고, Anthropic은 탐지 역량과 제어 수단을 계속 개선하는 한편 Model Hardware Standard 연구 프리뷰 공개 등 외부 협력과 추가 조사를 통해 업계의 집단적 방어를 강화하길 목표로 하고 있다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025)

