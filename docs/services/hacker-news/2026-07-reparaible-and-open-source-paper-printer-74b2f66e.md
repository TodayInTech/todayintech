---
title: "Reparaible and open source paper printer"
sidebar_label: "Reparaible and open source paper printer"
---

# Reparaible and open source paper printer

> Hacker News · 2026-07-05 · Open Hardware

---

Openprinter는 수리성과 개방성을 전면에 내세운 프린터/플로터 프로젝트로, 소모품 비용 절감과 전자폐기물 감소를 목표로 한다. 카트리지를 독립적으로 사용(검정 단독·컬러 단독·병행 사용)할 수 있어 한 색이 비었을 때 전체 인쇄가 막히는 문제를 피하고, HP 63/302/803 계열 카트리지와 호환되며 Inkit(블랙·마젠타·시안·옐로우 100ml 병)으로 리필할 수 있다고 명시되어 있다. 표준 용지와 롤 용지(여러 폭·길이)를 모두 지원하고 통합 커터로 배너·스트립·맞춤 포맷을 출력할 수 있으며, A4·A3 등 표준 규격도 수용한다. 속도 항목은 아직 정의되지 않았다.
하드웨어·소프트웨어 구성도 구체적이다. 메인 보드로 Raspberry Pi Zero W를 쓰고 카트리지 제어용으로 STM32 마이크로컨트롤러를 명시했으며, 오픈소스 프린트 서버(CUPS)를 탑재해 Windows·macOS·Linux·iOS·Android 등 운영체제와 드라이버 없이 네트워크 인쇄를 지원한다. 연결은 USB-C/USB-A, Wi‑Fi 802.11ac(AirPrint 포함), Bluetooth 4.1을 제공하며 600dpi(흑백)·1200dpi(컬러) 해상도와 1.47인치 TFT 등 사양을 공개했다. 모든 플라스틱 부품을 3D 출력 가능하게 하고 표준 부품을 사용해 조립·보수성을 높였으며, 파일과 튜토리얼을 공개할 계획을 밝히되 최종 제품이 준비된 이후에 파일을 배포하겠다고 명시해 버전 혼선을 줄이려는 의도도 드러난다. 프로젝트는 Creative Commons BY-NC-SA 4.0으로 배포되며 디자인·기술 아키텍처 보호를 위한 특허·디자인 등록이 병행된다고 설명한다. 이 조합은 개인·소규모 워크숍 수준에서 유지·수리 가능한 오픈 하드웨어 프린터를 실용화하려는 시도로 기술적·환경적 의미가 있다.

[Hacker News에서 원문 읽기 →](https://www.opentools.studio/)

