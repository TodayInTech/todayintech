---
title: "Automating cross-repo documentation with GitHub Agentic Workflows"
sidebar_label: "Automating cross-repo documentation with GitHub Agentic Workflows"
---

# Automating cross-repo documentation with GitHub Agentic Workflows

> GitHub Blog · 2026-07-08 · AI &amp; ML

---

제품 개발은 완료됐지만 문서는 뒤처지는 문제를 해결하려고 Aspire 팀은 GitHub Agentic Workflows를 도입해 코드 레포와 문서 레포 간 자동화를 설계했다. 릴리스 브랜치 매핑(마일스톤→release/*), 사전 처리로 PR 메타데이터 추출, 에이전트가 직접 쓰지 않고 의도(intent) JSON을 내보내면 안전한 출력 핸들러(safe-outputs)가 제한된 권한의 GitHub 앱으로 문서용 PR을 생성하는 흐름을 구축했다. 수치로 보면 396개의 제품 PR 실행 중 82개의 문서 PR이 생성·병합되었고(병합율 100%), 문서 병합의 중앙값 대기 시간은 44.8시간, 24시간 이내 병합 38%, 7일 이내 96%로 기록됐다. 에이전트는 변경사항이 문서화 대상인지 판정해 불필요한 드래프트를 거르며, 초기 과대판정 문제는 프롬프트 개선으로 해결했다.
보안적 제약이 설계의 핵심으로 작동한 점도 중요하다. 각 워크플로우마다 특정 레포에만 설치되는 앱 토큰을 사용하고, base-branch를 main 또는 release/*로 제한하며 AGENTS.md·패키지 매니페스트 같은 보호 파일은 차단하는 frontmatter 정책을 적용했다. 크로스-레포 푸시를 위해 문서 레포를 이중으로 체크아웃하는 패턴과 대형 diff에 대비한 사전 요약(pre-extract)도 실무적 해결책으로 제시된다. 결과적으로 에이전트가 초안 작성과 반복적 레퍼런스 업데이트를 자동화하고, 엔지니어가 SME로서 검토하는 흐름으로 문서 작성 책임을 재배치해 문서팀은 보다 인간 중심의 서사·샘플 작업에 집중할 수 있게 됐다. 기술 독자는 마일스톤 기반 타깃 라우팅, 최소 권한 앱 토큰, safe-outputs 계약 같은 구체적 패턴을 통해 비슷한 크로스-레포 자동화를 설계할 수 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/automating-cross-repo-documentation-with-github-agentic-workflows/)

