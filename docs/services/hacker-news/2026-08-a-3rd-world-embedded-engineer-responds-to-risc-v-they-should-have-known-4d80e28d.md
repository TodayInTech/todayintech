---
title: "A 3rd World Embedded Engineer Responds to \"RISC-V They Should Have Known Better\""
sidebar_label: "A 3rd World Embedded Engineer Responds to \"RISC-V They Should Have Known Better\""
---

# A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"

> Hacker News · 2026-08-16 · Opinion / 임베디드·아키텍처

---

트리니다드토바고에서 활동하는 임베디드 엔지니어인 저자는 Dmitry Grinberg의 RISC-V 비판에 대해 현장 경험으로 반박한다. 그는 개인적 이유로 ARM에서 RISC-V로 전환했고, Grinberg가 제기한 인코딩·확장 문제나 Zicsr 같은 세부적 불편을 인정하면서도 논점이 본질적으론 지역성과 접근성 문제를 간과한다고 지적한다. 저자가 제시하는 실물 근거는 저가 RV32EC 계열인 CH32V003(16레지스터, 곱셈·나눗셈 없음, 2KB SRAM, 16KB 플래시, 약 10센트)와 고성능 듀얼코어 CH32H417(400MHz/144MHz, 수백KB 메모리, USB3.2·이더넷·카메라 인터페이스 등), Baochip(오픈 코어에 MMU를 추가해 Xous·seL4·리눅스까지 구동) 등으로, 동일한 기본 ISA가 초저가 실험용 칩부터 MMU·프로세스 분리를 갖춘 고급 칩까지 수직적 이동을 가능하게 했다는 점을 강조한다. 또한 저자는 배송비와 수입 제약이 개발자 선택에 미치는 현실적 영향을 상세히 설명해, 한 나라에서 50개의 CH32V003과 디버거를 합리적 비용으로 확보할 수 있었던 경험을 들며 ARM 생태계의 라이선스·제품 경계가 사실상 진입 장벽으로 작동한다고 주장한다.
기술적 함의로 저자는 RISC-V의 확장 메커니즘이 표준 분열(fragmentation)을 낳는 한편으로는 바로 그 확장성이 초저가·고성능 모두를 포괄하는 스케일러빌리티를 제공한다고 정리한다. ARM은 제품 프로파일과 라이선스에 따라 마치 벽 같은 경계가 존재해 MMU나 고급 주변기능을 얻으려면 다른 코어 계열을 구매해야 하지만, RISC-V는 특권 명세의 체크박스를 켜고 끄는 식으로 동일한 ISA 위에서 점진적 기능 추가가 가능하다. 저자는 이 관점이 단순한 이론적 우열을 넘어 교육과 현지 개발자 접근성, 혁신의 분산화에 실질적 영향을 준다고 보며, 비용·개방성 관점에서 RISC-V의 확산은 설계 우아성 이상의 사회적 가치를 지닌다고 결론지었다.

[Hacker News에서 원문 읽기 →](https://rvembedded.com/blog_post/12/)

