---
title: "Today's PHP security release, and how we're strengthening security"
sidebar_label: "Today's PHP security release, and how we're strengthening security"
---

# Today's PHP security release, and how we're strengthening security

> Hacker News · 2026-10-21 · 보안

---

이번 PHP 보안 릴리스는 PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35에 적용된 취약점 수정으로, 적절한 조건에서 인증되지 않은 공격자가 원격으로 코드 실행을 할 수 있는 두 가지 치명적 결함을 다룹니다. 문제는 거의 모든 요청이 거치는 엔진의 핵심 구성요소인 메모리 관리와 에러 처리에 있었고(CVE-2026-109618 관련), 설계적 트레이드오프 때문에 호환성 파괴나 성능 저하, 서드파티 확장과의 조정 문제 없이 해결하기 어려웠습니다. 2024년 외부 감사를 통해 초기 징후가 포착된 뒤 여러 접근법을 놓고 합의 과정이 지연되었고, 이 과정은 자원과 의사결정 구조의 한계를 드러냈습니다. 이후 PHP 재단은 생태계 보안팀 신설, 외부 감사 및 AI 도구(Anthropic, OpenAI 등) 도입, 빌드·재현 환경 개선 등으로 대응 역량을 키웠습니다.
공개 전 누출과 조기 배포 사건은 조정된 공개 절차에 부담을 줬습니다. 10월 20일 CVE ID 유출과 잘못된 CVSS(유출시 10.0, 실제 9.2) 정보 유통, Calif의 증명 영상 유출, Chainguard의 임베고 파기 사례로 인해 일부 PoC 확산이 가속화되었고, 이에 대응해 배포 일정이 앞당겨졌습니다. 기술적으로 본 취약점은 엔진 설계의 근본적 부분을 건드려 전 영역에 영향을 미치므로 단순한 패치 외에 연속적인 감사, 숙련된 엔지니어 확보와 재단 후원이 필수적입니다. 원문은 패치 배경과 조사 타임라인, 프로세스 개선과 재원 확보의 필요성을 구체적으로 연결해 설명하고 있어 보안 실무자와 인프라 담당자에게 유의미한 참고가 됩니다.

[Hacker News에서 원문 읽기 →](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

