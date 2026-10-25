---
title: "Munder Difflin – Agent harness to run an office of your clones"
sidebar_label: "Munder Difflin – Agent harness to run an office of your clones"
---

# Munder Difflin – Agent harness to run an office of your clones

> Hacker News · 2026-08-22 · AI/Developer Tools

---

Munder Difflin은 기존 에이전트 CLI를 래핑해 개인의 작업 방식을 그대로 재현하는 ‘클론’을 로컬에서 돌리는 툴킷입니다. 한 번 다운로드해 노드(사용자 기기)에 설치하면 코드, 키, 구독 정보는 기기를 벗어나지 않고 클론은 사용자의 워크플로·툴링·지식을 캡처해 다른 클론이 상속받습니다. 클론끼리 메시지를 주고받아 업무를 인계하고 차단점을 해소하며, 결정이 필요한 경우에만 인간에게 에스컬레이션합니다. 모든 동작은 커맨드라인으로 접근 가능하고 PR 리뷰·버그 수정·CI 감시·문서 작성·이슈 트리아지 등 스크립트화 가능한 작업을 자동화하도록 설계되어 있습니다.
설계는 로컬 우선에 무게를 두되 선택적 하이브리드 옵션을 제공합니다. 기본 노드는 MIT 라이선스로 오픈소스 공개되어 누구나 코드와 프로토콜, 암호화 방식을 감사할 수 있고, Cloud + Network 라이선스를 선택하면 전용 샌드박스 VM에서 24/7로 클론을 구동하거나 조직 단위의 버전 관리된 지식베이스를 호스팅할 수 있습니다. 클론 간 통신은 노드에서 암호화·복호화되며, 서비스 제공자는 중간에서 내용을 읽을 수 없다고 명시합니다. 또한 Claude, OpenAI, Copilot 등 사용자가 이미 쓰는 여러 에이전트 CLI를 그대로 활용하는 BYO 구조로 벤더 락인을 피하고 기존 구독을 재사용하도록 설계된 점이 기술적으로 눈에 띕니다.

[Hacker News에서 원문 읽기 →](https://munderdiffl.in/)

