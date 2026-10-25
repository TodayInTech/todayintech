---
title: "Disrupting supply chain attacks on npm and GitHub Actions"
sidebar_label: "Disrupting supply chain attacks on npm and GitHub Actions"
---

# Disrupting supply chain attacks on npm and GitHub Actions

> GitHub Blog · 2026-07-28 · 공급망 보안

---

최근 한 해 동안 패키지 레지스트리와 CI/CD를 노린 공급망 공격은 유지보수자 계정 탈취와 워크플로 트리거 취약점을 결합해 빠르게 악성코드를 확산시키는 패턴을 보였습니다. GitHub 보안팀은 이러한 공격 사슬을 끊기 위해 npm과 GitHub Actions에 걸쳐 여러 방어책을 도입했고, 이번 글은 그 성과와 기술적 의도를 정리합니다. 초기 침해 방지 측면에서는 고위험 npm 계정에 대해 이메일 변경이나 2FA 복구 코드 사용 시 72시간 읽기 전용 지연을 둔 것과, actions/checkout의 기본 동작을 변경해 포크에서 온 미검증 코드를 기본적으로 체크아웃하지 않도록 한 조치가 눈에 띕니다. 더불어 누가 어떤 트리거를 실행할지 엔터프라이즈·조직·레포 수준에서 정책으로 제어하는 기능과, 신뢰도가 낮은 트리거에 대해 Actions 캐시를 읽기 전용으로 제한해 캐시 오염을 통한 권한 상승 경로를 차단했습니다.
자격 증명 유출과 확산을 막기 위한 변화도 병행됩니다. CircleCI를 신뢰할 수 있는 게시 공급자로 추가해 장기 자격증명 사용을 줄이는 신뢰 게시(trusted publishing) 지원을 넓혔고, npm은 staged publishing을 도입해 추가 승인과 2FA 없이는 패키지 배포가 완료되지 않도록 했습니다. 추가로 npm v12에서는 설치 시 실행되는 스크립트를 기본 비활성화하고 git·원격 URL을 통한 의존성 설치를 차단하는 등 배포 시점의 악성 실행 벡터를 줄였습니다. Dependabot은 새 릴리스가 3일간 노출된 뒤에만 버전 업데이트 PR을 여는 쿨다운을 기본으로 도입해 탐지 시간을 확보합니다. 운영 측면에서는 Actions 워크플로의 아웃바운드 트래픽을 로깅하는 네트워크 방화벽 기술 미리보기와, 엔터프라이즈 단위의 자격증명 즉시 철회 기능·OAuth/App 토큰 철회 API 확장으로 사고 대응 속도를 끌어올렸습니다. 이 일련의 변화들은 단일 솔루션으로는 차단할 수 없는 복합적 공급망 공격 사슬의 여러 고리를 동시에 약화시키려는 실무적 접근이며, 더 많은 개선이 계속될 예정임을 밝혔습니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)

