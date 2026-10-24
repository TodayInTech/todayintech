---
title: "Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)"
sidebar_label: "Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)"
---

# Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)

> OpenAI Blog · 2026-10-23 · Engineering

---

피드 기준으로는 OpenAI가 'Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)'에서 내부 저장소 계층인 Habitat를 확장해 대규모 트래픽을 처리한 경험을 다루고 있습니다. 제공된 정보만 보면 신뢰할 수 있는 다중 테넌시 구현과 전역 캐싱 전략, 그리고 Azure Cosmos DB의 활용을 통해 ChatGPT의 읽기 성능을 12배 이상 향상시킨 점을 중심 결과로 제시하고 있습니다.
이 변화가 기술적으로 시사하는 바는 명확합니다. 다중 테넌시는 자원 분리와 안정성 측면의 운영 부담을 낮추고, 전역 캐시는 지연 시간과 처리량 개선에 직접적인 영향을 줍니다. Azure Cosmos DB 같은 글로벌 분산형 데이터베이스를 도입했다는 사실은 일관성·복제·운영 복잡도 측면의 절충이 있었음을 암시하지만, 피드 메타데이터만으로는 구체적 아키텍처나 수치 검증 방법, 부하 분산·일관성 설정 등 세부 구현과 트레이드오프를 확인할 수 없습니다.

[OpenAI Blog에서 원문 읽기 →](https://openai.com/index/scaling-storage-one-billion-users-part-two)

