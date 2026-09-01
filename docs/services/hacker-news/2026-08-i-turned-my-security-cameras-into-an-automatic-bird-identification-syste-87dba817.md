---
title: "I turned my security cameras into an automatic bird identification system"
sidebar_label: "I turned my security cameras into an automatic bird identification system"
---

# I turned my security cameras into an automatic bird identification system

> Hacker News · 2026-08-31 · Edge AI / Homelab

---

작성자는 기존 보안 카메라의 마이크를 이용해 BirdNet-Go를 도커 환경에서 24/7로 구동하며 새와 박쥐(및 개구리 등)를 실시간으로 식별하는 시스템을 구축했다. 모든 처리와 모델 추론은 로컬에서 이뤄져 클라우드 의존이나 월간 비용이 없고, 라즈베리파이나 개인 서버에서 여러 모델을 병행해 운영할 수 있다. RTSP 지원 카메라를 가리키기만 하면 되고, 실시간 채널별 오디오 레벨 시각화로 마이크 위치나 노이즈 문제를 진단할 수 있다는 점이 실무적 장점으로 제시된다. 또한 Google Perch v2 추가로 탐지 가능한 종 수가 6,000에서 14,795종으로 확장되었다는 점을 구체적으로 언급한다.
사용성 측면에서는 종 목록 매칭으로 특정 종 출현시 알림을 보내고, 처음 관측된 종을 추적하는 ‘신규 종 추적’ 기능과 BirdWeather로 관찰을 공유할 수 있는 통합 기능을 제공한다. Home Assistant와 MQTT로 연동하거나 디스코드 채널·iOS 전용 앱과 연결해 가정 내외에서 결과를 확인할 수 있으며, 저자는 3대 카메라로 12개월 동안 418,726회 감지·271종 식별(평균 확신도 60.9%, 최다 118,667회 House Finch)을 기록한 실사용 데이터를 제시한다. 유머러스한 검출 사례(방귀 탐지)와 함께, 박쥐는 전용 마이크가 있으면 더 정확히 감지된다는 실무적 팁도 덧붙여 엣지 AI 기반 환경 모니터링의 가능성과 한계를 동시에 보여준다.

[Hacker News에서 원문 읽기 →](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/)

