---
title: "Claude reveals ECDSA curve origins"
sidebar_label: "Claude reveals ECDSA curve origins"
---

# Claude reveals ECDSA curve origins

> Hacker News · 2026-10-16 · 보안/암호학

---

Anthropic의 내부 연구 모델 클로드(Claude)가 NIST가 제시한 ECDSA 표준 곡선들의 'seed' 기원 문제를 계산적으로 해결했다고 보고했다. 조사 결과 P-192, P-224, P-256, P-384, P-521 등 다수의 시드값은 해시나 암호적 절차로 생성된 것이 아니라 당시 C 라이브러리의 lrand48 선형 합동 생성기(LCRNG)의 출력에서 나온 20바이트 후보들을 Unix 타임스탬프로 초기화한 결과였다. 클로드는 시드들을 비트 단위로 슬라이딩하며 1990년대형 PRNG 출력 패턴을 찾아내고, 상위 비트가 모두 0인 패턴에서 lrand48의 특징을 식별해 내부 48비트 상태를 복원했다. 잘려 나온 출력에서 상태를 회복하는 문제는 LLL 격자 환원 등으로 해결했고, prime-curve들의 초기화 시점은 1997년 5월~1998년 4월 범위의 타임스탬프와 대응했다는 것이 보고서의 핵심이다. 또한 일부 곡선의 기준점(G)은 FreeLIP(Arjen Lenstra의 LIP 패키지) 기반 난수 생성기에서 유래한 것으로 밝혀졌고, prime192v1 등에서 사용된 시드 값들도 재현되었다.
이 결과는 암호학적 결함이나 백도어의 발견을 의미하지 않으며, 오히려 곡선 파라미터가 의도적 약화를 위해 조작되었을 가능성을 줄여준다. 다만 B-163 하나의 바이너리 시드는 설명되지 않았고, P-224·P-256·P-384·P-521의 일부 기준점 생성 방식은 여전히 미해명으로 남아 있다. 출판본은 후보 생성 과정에서 일부 유효한 곡선이 건너뛰어진 사실과, 시간값을 탐색해 특정 곡선을 찾을 가능성은 이론적으로 존재한다고 언급하되, 건너뛴 후보 수가 적어 약화된 곡선 선택 가능성은 낮다고 평가한다. 이 작업의 보상금은 Internet Security Research Group에 기부될 예정이며, 연구에는 여러 명의 Anthropic 연구자들이 참여했다.

[Hacker News에서 원문 읽기 →](https://www.anthropic.com/research/ecdsa-curve-origins)

