---
title: "QuadRF can spot drones and see WiFi through my wall"
sidebar_label: "QuadRF can spot drones and see WiFi through my wall"
---

# QuadRF can spot drones and see WiFi through my wall

> Hacker News · 2026-07-10 · RF/SDR 하드웨어

---

QuadRF는 라즈베리 파이 5와 FPGA를 결합한 소형 위상배열 무선기기로, 피코초 수준 타이밍과 빔포밍을 통해 4.9–6GHz 대역의 RF 환경을 실시간으로 시각화하고 드론을 추적할 수 있다고 보고됩니다. 장비는 부팅 시 자체 Wi‑Fi 핫스팟을 띄우고 브라우저 기반 VNC로 GNU Radio, SDR 소프트웨어, 그리고 AR 기반 RF 시각화기를 실행합니다. 저자는 실제로 스튜디오 주변의 5GHz AP와 주변 네트워크를 색상으로 구분해 확인했고, DJI Mini Pro 4를 비행시키며 QuadRF가 드론 신호를 문제없이 포착하는 것을 확인했습니다. UI는 다소 투박하고 자동이득제어(AGC) 같은 편의 기능이 부족하다는 한계가 있지만, Mobile Expansion Pack을 통해 휴대형 분석이 가능하다고 합니다.
기술적 핵심은 라즈베리 파이 5의 카메라·디스플레이 FFC MIPI 커넥터를 역설계해 I/Q 데이터를 &gt;5Gbps로 스트리밍한 점입니다. 저자는 MIPI가 USB보다 저지연·신뢰성 높은 전송을 제공하고 수백 MSPS의 I/Q를 무손실로 처리할 수 있다고 설명하며, 다수의 QuadRF 모듈을 데이지체인해 각 모듈이 자체 위상 보정을 수행하도록 설계한 점을 주목합니다. 더 큰 프로젝트 맥락에서는 여러 모듈을 묶어 최대 1.15MW EIRP 수준의 대형 지향안테나 실험도 목표로 하고 있으나, 현재의 핸드헬드 QuadRF 자체는 문 거리를 넘어 달과의 통신을 할 정도는 아니라고 명시합니다. 전체적으로 사전생산 제품·크라우드펀딩 특유의 변수(배송 지연, UI 개선 필요 등)를 명백히 밝히며도, Pi 기반의 MIPI I/Q 전송과 소형 위상배열의 실사용 데모는 SDR 생태계와 측정·감시 도구의 접근성 측면에서 기술적 의미가 큽니다.

[Hacker News에서 원문 읽기 →](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/)

