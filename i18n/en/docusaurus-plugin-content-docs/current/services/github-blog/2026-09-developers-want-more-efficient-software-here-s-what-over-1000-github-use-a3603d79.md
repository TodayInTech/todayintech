---
title: "Developers want more efficient software. Here’s what over 1000 GitHub users told us they need."
sidebar_label: "Developers want more efficient software. Here’s what over 1000 GitHub users told us they need."
---

# Developers want more efficient software. Here’s what over 1000 GitHub users told us they need.

> GitHub Blog · 2026-09-23 · Research

---

GitHub과 Yale 기후커뮤니케이션 프로그램이 수행한 1,039명 대상 설문은 개발자들이 소프트웨어 효율성에 높은 관심을 보이지만 이를 실무로 옮기기 위한 도구와 측정 방법, 실증적 근거가 부족하다는 점을 드러냅니다. 응답자의 대다수가(80%는 에너지 효율 코드 도구에, 78%는 환경발자국 저감 베스트프랙티스에, 74%는 소프트웨어·개발 프로세스 영향 측정에) 관심을 보였고 AI의 환경 영향에 우려(71%)와 지구온난화에 대한 걱정(79%)도 높았습니다. 다만 표본은 마케팅 이메일에 옵트인한 비확률 표본에 기반하므로 전체 개발자 집단과 직접 비교할 때 제한이 있습니다.
실무적 권고는 '보이는 폐기물'을 측정 가능한 지점에서 찾으라는 것입니다. 코드(중복 계산·비효율 알고리즘), 데이터(과다 페칭·비배치 쿼리), 네트워크·I/O(중복 요청·압축 누락), 프론트엔드(불필요한 렌더링·미디어 최적화) 등 네 영역을 점검하고 실행 시간·CPU 사용량·메모리 할당·네트워크 전송량 같은 지표를 적절히 선택해 변경 전후 재현 가능한 벤치마크를 제시해야 효과를 검증할 수 있다고 권고합니다. 예로 O(n²) 탐색을 해시맵으로 교체하는 PR은 대표 워크로드의 전후 측정과 재현 명령, 트레이드오프 설명을 포함해야 합니다. 또한 GitHub Agentic Workflows와 오픈소스 'Daily Efficiency Improver' 워크플로우는 리포지토리 전반의 개선 기회를 자동으로 찾고 테스트·초안 PR을 생성하되 자동 병합은 하지 않으므로 권한·모델 사용·주기·추정 계산 비용을 검토하고 각 권고를 가설로 취급해 수치로 검증한 뒤 유지보수자가 결정하도록 설계되어 있습니다. 이러한 접근은 효율성 작업을 기존 엔지니어링 루프에 통합해 실무에서 지속가능한 개선으로 이어질 수 있다는 실용적 의미를 갖습니다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/news-insights/research/developers-want-more-efficient-software-heres-what-over-1000-github-users-told-us-they-need/)

