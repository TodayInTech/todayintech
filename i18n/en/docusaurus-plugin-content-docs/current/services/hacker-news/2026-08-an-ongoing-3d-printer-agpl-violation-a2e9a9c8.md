---
title: "An ongoing 3D-printer AGPL violation"
sidebar_label: "An ongoing 3D-printer AGPL violation"
---

# An ongoing 3D-printer AGPL violation

> Hacker News · 2026-08-26 · 오픈소스/라이선스

---

2026년 FOSSY에서 소프트웨어자유보호단체(SFC) 인사들이 발표한 내용은, 3D프린터 시장을 장악한 Bambu Lab이 AGPLv3와 일부 GPL 조항을 우회·위반하고 있다는 주장과 그에 대응하는 커뮤니티 활동을 중심으로 전개됩니다. Bambu Lab은 PrusaSlicer의 변형인 Bambu Studio를 제품에 탑재하면서 초기에는 소스 코드나 제공 약속을 내놓지 않았고, 이후 공개한 소스 역시 대응하는 '완전한 대응 소스'가 아니었다고 지적됩니다. 핵심 기술적 쟁점은 동적 로드되는 .so 라이브러리와 dlopen() 호출로 확인되는 구조, 그리고 클라이언트가 서버 쪽에 접근하기 위해 특정 User-Agent 문자열(‘키’)을 전송해 서버측의 비공개 기능을 사용하는 방식입니다. SFC 측은 이 구조가 AGPLv3가 방지하려던 바로 그 유형—애플리케이션 일부를 웹 서버에 두고 이를 독점화하는 행위—이라고 평가합니다.
커뮤니티 차원의 대응도 활발합니다. 폴란드 개발자 Paweł Jarczak가 User-Agent 및 네트워크 코드를 역분석하자 Bambu Lab이 DMCA 고지를 냈고, GitHub가 이를 이행한 사례가 보고됩니다. SFC는 OrcaSlicer 등의 코드 미러링과 baltobu 프로젝트를 통해 우회 수단을 마련하고 있으며, 모금으로 25만 달러 목표를 훨씬 초과해 상근 소송 담당 변호사 채용이 가능해졌습니다. 기술적·법적 대응 경로는 다양해서, 리버스엔지니어링과 커뮤니티 주도의 대체 구현이 소송보다 빠를 수 있다는 판단, 그리고 GPL 계열 위반을 계약적 소송(예: SFC의 Vizio 사례와 유사한 접근)으로 해결하는 가능성 등이 논의되었습니다. 또한 일부 모델의 펌웨어(300MB 이미지)에서 Buildroot 기반 구성요소에 대한 소스 미제공 문제도 지적되어 GPLv2 위반 가능성이 제기되었습니다. 이 사건은 단순한 라이선스 분쟁을 넘어, 오픈소스 라이선스가 실제로 권리를 보장하려면 커뮤니티의 적극적 집행과 다양한 전략이 병행돼야 함을 보여줍니다.

[Hacker News에서 원문 읽기 →](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/)

