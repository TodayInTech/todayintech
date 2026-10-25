---
title: "Tailcat – Like netcat, but over Tailscale’s data plane"
sidebar_label: "Tailcat – Like netcat, but over Tailscale’s data plane"
---

# Tailcat – Like netcat, but over Tailscale’s data plane

> Hacker News · 2026-08-26 · 네트워킹·오픈소스

---

Tailcat은 Tailscale의 오픈소스 구성 요소를 모아 'netcat처럼 동작하지만 Tailscale의 데이터 평면 위에서' 작동하도록 만든 도구입니다. 제어 평면을 사용하지 않고 magicsock(포인트간 WireGuard 암호화 터널, STUN·UDP 홀펀칭)과 DERP 릴레이를 통해 초기 부트스트랩과 페일오버를 처리하며, 서버가 짧은 연결 토큰(conn blob)을 출력하고 클라이언트가 그 토큰으로 연결을 맺는 토큰 기반 워크플로를 채택합니다. 유저스페이스 WireGuard 및 gVisor 네트스택을 사용해 루트 권한 없이 포트 포워딩, 무인 SSH(no-auth 옵션), SOCKS5 프록시, 파일 전송 등을 수행할 수 있고, 브라우저용 WebAssembly 데모로 CLI와 상호운용이 가능합니다. 기본적으로 공개 rate-limited DERP 릴레이를 쓰되, 자신만의 DERP 서버·DERP 맵을 호스팅해 토큰에 릴레이 정보를 내장할 수 있어 제약(공개 릴레이의 속도·요금 제한)을 피할 수 있습니다.
내부 동작은 클라이언트가 토큰에서 서버의 WireGuard 공개키와 DERP 정보를 파싱해 임시 키쌍을 만들고 동일한 DERP로 접속한 뒤 "Meow/Meowed" 식의 발견 핸드셰이크를 통해 피어 목록에 추가되고 표준 WireGuard 핸드셰이크로 터널을 형성하는 순서입니다. 병렬로 STUN으로 학습한 UDP 엔드포인트를 교환해 UDP 홀펀칭을 시도하며 성공 시 DERP에서 직접 P2P 경로로 업그레이드됩니다. 오픈소스화되어 있고(2026년 공개 근거 포함) 편리하지만 API·CLI·와이어 포맷 안정성 보장은 없고 공개 DERP는 SLA 없이 베스트에포트로 제공된다는 제한이 명시되어 있어, 실무에서는 자체 DERP 호스팅이나 운영 정책을 고려해 활용하는 편이 안전합니다.

[Hacker News에서 원문 읽기 →](https://github.com/tailscale/tailcat)

