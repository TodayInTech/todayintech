---
title: "Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting"
sidebar_label: "Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting"
---

# Jack Dorsey launches Buzz to combine team chat, AI agents and Git hosting

> Hacker News · 2026-07-21 · 개발자 도구·협업 플랫폼

---

Jack Dorsey와 Block이 공개한 Buzz는 직원, AI 에이전트, 대화와 소스 리포지토리를 하나의 신원 시스템 아래에 넣으려는 오픈소스 워크스페이스입니다. 제품은 Nostr 기반의 자체 호스팅 가능한 릴레이를 중심으로 설계되어 모든 메시지·반응·워크플로 단계·코드 이벤트를 암호학적으로 서명된 이벤트로 저장하고, 사람과 에이전트 모두에 대해 키 페어·채널 멤버십·감사 추적을 부여합니다. 에이전트는 단순 봇이 아니라 토론 검색, 리포지토리 열람, 패치 제출, 코드 리뷰, 워크플로 실행, 공유 캔버스 편집, 채널 생성 같은 작업을 사용자 권한으로 수행하도록 설계돼 있으며, Goose·Codex·Claude Code 같은 모델을 따로 연결하는 하네스와 에이전트 지향 CLI를 제공합니다. 또한 Git Smart HTTP를 쓰는 내장 소프트웨어 포지는 기능 브랜치를 채널로 전환하고 패치·CI 결과·리뷰·병합 결정을 동일한 기록에 보존해 토론·코드·워크플로 이력을 하나의 검색 인덱스로 합칠 수 있도록 목표합니다. 패키지 빌드는 macOS·Windows·Linux용으로 제공되며, 저장소는 Apache 2.0 라이선스입니다.
Buzz의 분산성은 설계상 배포와 소유권에서 옵니다. 현재 릴레이는 피어투피어 이벤트 교환이나 복제·가십 계층을 제공하지 않으며, 워크스페이스의 모든 읽기·쓰기는 단일 릴레이를 통해 인증·검증·저장·배포됩니다. 이는 자사 호스팅을 통해 인프라·데이터 위치를 통제할 수 있는 한편 가용성·백업·보안·업데이트 책임이 운영자에게 전가된다는 뜻이기도 합니다. 제품은 아직 미완성으로 모바일 클라이언트와 푸시 알림, 일부 워크플로 승인 실행 경로가 개발 중이며, 데스크톱 버전 0.4.21(7월21일 배포)은 에이전트 제어·인증·온보딩 관련 수정·추가를 포함합니다. Block 문서에선 내부용 빌드를 예시로 삼았지만 채택·가격·외부 고객 수치는 공개되지 않아, 외부 엔지니어들이 한 릴레이에 많은 개발 활동을 맡길지 여부가 첫 번째 실전 시험이 될 전망입니다.

[Hacker News에서 원문 읽기 →](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)

