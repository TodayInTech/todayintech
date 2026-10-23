---
title: "OpenShell – A safe, private runtime for fleets of autonomous AI agents"
sidebar_label: "OpenShell – A safe, private runtime for fleets of autonomous AI agents"
---

# OpenShell – A safe, private runtime for fleets of autonomous AI agents

> Hacker News · 2026-10-22 · AI 인프라/보안

---

OpenShell은 자율 AI 에이전트들이 파일 읽기·패키지 설치·API 호출·자격증명 사용 같은 실제 작업을 수행하도록 허용하면서도 데이터·비밀·네트워크에 대한 무제한 접근을 막는 ‘안전·사적 런타임’을 목표로 한다. 프로젝트는 에이전트별 샌드박스를 운영하고 커널 수준에서 파일 접근, 시스템 콜, 네트워크 연결을 계수해 정책을 강제하는 한편, 정책 변경 시 형식 검증(formal verification)을 통해 새로 허용될 위험한 접근(예: 자격증명을 포함한 새로운 호스트 접근이나 새로운 API 메서드 호출)을 자동으로 플래그하고 사람의 승인 없이 적용되지 않도록 설계했다. 에이전트는 실제 자격증명을 직접 보지 못하며 OpenShell이 승인된 엔드포인트로 향하는 요청에 대해서만 자격증명을 첨부한다.
설치·운영 관점에서도 실무성을 갖췄다. 로컬 게이트웨이 설치·데모 샌드박스 실행 명령이 제공되며, Linux·Apple Silicon macOS·Windows(WSL2 실험적)와 Docker·Podman·호스트 가상화 등을 지원한다. 아키텍처는 게이트웨이·슈퍼바이저·샌드박스의 조합으로 설명되고, 파일시스템·네트워크·프로세스 규칙을 정의하는 정책과 정책 변경 검토용 어드바이저·증명기(prover), 자격증명 제공자(provider), Helm을 통한 게이트웨이 배포(네트워크 정책을 CNI가 적용해야 함), 미들웨어·인터셉터·컴퓨트 드라이버 같은 확장 지점, Python/TypeScript/Go/Rust용 SDK와 에이전트용 스킬 패키지까지 실전 적용에 필요한 구성 요소들을 갖추고 있다. 익명화된 운영 텔레메트리 수집은 기본 활성화지만 비활성화 옵션을 제공하며, 0.1.x에서의 안정적 릴리스 주기·새 격리 프리미티브·확장된 확장 표면과 새 API 등 단계적 개선도 명시되어 있다. 커널 강제와 형식 검증을 결합한 설계는 에이전트 플릿을 안전하게 운영하려는 엔지니어와 보안 담당자에게 실질적인 가치를 제공할 가능성이 크다.

[Hacker News에서 원문 읽기 →](https://github.com/NVIDIA/OpenShell)

