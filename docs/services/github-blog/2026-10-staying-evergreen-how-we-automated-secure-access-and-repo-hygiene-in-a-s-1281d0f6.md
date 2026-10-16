---
title: "Staying Evergreen: How we automated secure access and repo hygiene in a shared org"
sidebar_label: "Staying Evergreen: How we automated secure access and repo hygiene in a shared org"
---

# Staying Evergreen: How we automated secure access and repo hygiene in a shared org

> GitHub Blog · 2026-10-15 · Platform security

---

외부 협업자가 섞인 대규모 조직에서 접근 권한 검토와 저장소 정리 작업은 수작업으로는 유지하기 어렵다는 문제의식에서 출발해, GitHub의 기본 기능만으로 이를 자동화한 사례가 제시됩니다. Evergreen은 분기별 접근권 검토와 휴면 저장소 식별·보관이라는 두 워크플로를 제공하며, '보안 우선(fail secure)'과 '무삭제(never destroy)'라는 원칙을 따릅니다. 구현은 소형 Go 웹훅 서버와 컨트롤러 리포지토리를 중심으로 돌아가고, 일정 트리거는 GitHub Actions의 repository_dispatch 이벤트로 분기별(1일: 휴면검토, 8일: 접근검토, 16일: 휴면정리, 23일: 접근정리)로 작동합니다. 모든 변경은 리포지토리의 이슈와 컨트롤러 리포지토리 내 JSON 상태 파일(state/repos/.json)에 커밋되어 감사 추적이 git 히스토리로 가능하게 설계했습니다.
상호작용은 각 저장소의 체크리스트 이슈를 통해 이루어지며, 체크박스 선택과 이슈 폐쇄만으로 유지·제거를 결정합니다. 권한 없는 사용자가 이슈를 닫으면 앱이 자동으로 재오픈해 결정을 제한하는 등 의사결정 권한을 보호합니다. 소유자 알림은 evergreen_repo_owner 속성이나 최근 이슈·커밋 작성자에 기반한 폴백 체인을 통해 자동으로 해결하고, 부분 실패가 발생하면 '닫지 않고 재시도'하는 fail‑closed 동작으로 일관성을 유지합니다. 롤아웃에서는 DRY_RUN 모드, 사전 공지, Splunk 기반 로그 관찰을 통해 위험을 줄였고, 대규모 조직에서의 콘텐츠 생성 레이트 리밋(초당/시간 단위 제한)을 피하기 위해 배치 처리와 간격 삽입으로 속도를 제어했습니다. 이 사례는 별도 데이터베이스나 맞춤형 UI 없이도 기존 GitHub 프리미티브로 감사 가능하고 되돌리기 쉬운 운영 자동화를 만드는 현실적인 패턴을 보여주며, 작은 반복 작업부터 적용해 확장하라는 실무적 권고로 마무리합니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/platform-security/staying-evergreen-how-we-automated-secure-access-and-repo-hygiene-in-a-shared-org/)

