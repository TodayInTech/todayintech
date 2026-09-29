---
title: "Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms"
sidebar_label: "Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms"
---

# Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

> Hacker News · 2026-09-28 · Machine Learning / Tools

---

Jeff는 Jev와 같은 요청 형식을 따르되 소형(0.8B·2B)으로 설계된 ‘결정(decision)’ 모델 모음이다. 입력으로 상황과 옵션을 평문으로 주면 텍스트 생성 없이 단일 순전파로 각 옵션의 확률을 반환해 빠르고 보정된 판단을 내리는 것이 목표다. 저자 측 벤치마크와 실측에서는 RTX PRO 6000에서 약 22 ms, Apple M4 Max에서 약 28 ms 수준의 응답 속도를 보고했으며(CPU는 훨씬 느림), 선택(choice)/noul(yes/no)/score 타입을 한 번의 요청으로 함께 계산할 수 있다. 공개된 표는 Jeff-0.8B가 몇몇 분류·그라운딩 벤치마크에서 대형 모델에 근접하거나 앞서는 반면, 복합적 추론이 필요한 BBH·JudgeBench·JevBench 같은 태스크에서는 큰 모델보다 성능이 낮음을 보여준다.
기술적으로 의미 있는 부분은 '로컬 학습·로컬 서빙'을 목표로 삼았다는 점이다. 0.8B 모델은 단일 RTX PRO 6000에서 약 2시간 내에 학습되며, 합성 학습 데이터는 오픈 모델로 생성하고 각종 누수 필터·학습 레시피(AutoJev 기반)를 공개했다. 제안된 활용법은 대기열 라우팅·의도 분류·모더레이션·음성 네비게이션 등 속도와 보정된 확률이 중요한 시스템에 소형 결합기로 쓰는 것이다. 한편 작은 모델 계열은 다단계 추론·계획 능력이 제한적이라는 점을 명확히 하고 있으며, 제안자는 제로샷 정확도가 부족하면 도메인 예시로 짧게 파인튜닝하면 큰 성능 향상을 얻을 수 있다고 보고한다(예: 음성 네비게이션에서 31.7%-&gt;95.8%). 코드와 가중치는 공개 라이선스(MIT·Apache 2.0)로 배포되어 실무 적용과 재현성이 용이하다.

[Hacker News에서 원문 읽기 →](https://github.com/firelex/jeff)

