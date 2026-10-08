---
title: "Secret protection must scale with software"
sidebar_label: "Secret protection must scale with software"
---

# Secret protection must scale with software

> GitHub Blog · 2026-10-07 · Security

---

최근 GitHub의 분석은 소프트웨어 생성 속도가 비밀(시크릿) 노출 방어 역량보다 더 빠르게 증가하고 있음을 보여준다. 작성자는 현재 풀 리퀘스트의 약 3분의 1이 AI 에이전트가 관여하며, 공개 코드에 새로운 비밀이 대략 2초마다 나타나고 지난 3년간 연간 두 배 증가했다고 지적한다. 2024년 Q2에서 2026년 Q2 사이에 스크린된 푸시량은 2.84배 늘었고 자격증명 포함 푸시는 2.59배 늘어났지만 푸시당 노출 비율 자체에는 유의미한 변화가 없었다는 점을 근거로, 개발자들이 더 부주의해진 것이 아니라 개발 속도에 방어체계가 따라가지 못하는 상황이라고 설명한다. 수작업으로 비밀을 폐기하는 평균 소요가 약 40일이며 20%는 90일 이상 걸리는 현실도 지적한다.
대응으로 GitHub는 탐지에서 조치로 연결되는 시스템을 확장하고 있다. 150개 이상의 기술 파트너와의 시그널 공유로 2026년 Q2에 공개 스캐닝은 초당 평균 26건의 자격증명 매치를 보고했으며, 푸시 보호는 최근 적어도 초당 한 번 이상 비밀을 차단한다고 밝혔다. 특히 Microsoft Applied Sciences와 함께 미세조정한 ModernBERT 분류기를 푸시 경로에 도입해 후보 비밀들을 문맥과 함께 2밀리초 미만으로 판단할 수 있게 했고, 기존 LLM 기반 파이프라인보다 정밀하면서 비용 효율적으로 동작해 차단 가능한 비밀 수를 2배 이상으로 늘릴 수 있다고 보고한다. 이 분류기는 사설 프리뷰 단계이며 곧 Enterprise Cloud·GitHub Teams의 Secret Protection과 연동되어 AI 크레딧을 소모하고, Enterprise Server 3.23 공개 프리뷰와 Copilot의 /security-review 명령에도 통합되어 푸시 전후 검사 지점을 넓힌다. 글은 ‘예방은 컴퓨트로 확장되지만 복구는 사람으로 확장된다’는 요지를 통해 플랫폼 차원의 자동화와 낮은 지연·높은 정밀도의 검사 도입이 필수적임을 강조한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/secret-protection-must-scale-with-software/)

