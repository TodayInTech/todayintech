---
title: "Shutting down our public encrypted DNS"
sidebar_label: "Shutting down our public encrypted DNS"
---

# Shutting down our public encrypted DNS

> Hacker News · 2026-09-04 · Privacy / Networking

---

Mullvad는 2022년부터 운영해 온 공개 암호화 DNS(DoH) 서버를 중단하고 앞으로 Quad9을 지원한다고 밝혔다. Mullvad VPN 내부에서는 트래픽이 이미 암호화되고 내부 DNS가 쿼리를 처리하므로 공개 DoH는 불필요하지만, VPN 외부에서는 두 가지 역할을 해왔다고 설명한다: Mullvad Browser의 기본 DoH로서 ISP가 방문 도메인을 볼 수 없게 하는 기능과, 누구나 무료로 이용 가능한 공개 서비스로서의 역할이다. Mullvad는 전문성이 높은 공개 DNS 운영을 Quad9 재단이 선도하고 있다고 판단해 자원 중복을 피하고 재정적 지원으로 기여하기로 했다.
실무적으로는 사용자가 직접 Mullvad의 DoH를 수동으로 설정한 경우 2026년 11월 2일 이전에 Quad9로 전환해야 하며, Mullvad Browser 사용자는 기본 DoH 설정이나 포함된 애드블로커 설정을 유지한 경우 자동으로 Quad9로 마이그레이션된다. 사용자가 DoH를 커스터마이즈한 경우 Mullvad가 이를 변경하지 않으므로 수동 복구가 필요하고, Mullvad가 제공한 iOS·macOS 프로필은 중단되어 Quad9용 프로필로 대체해야 한다. 이번 결정은 공개 DNS 제공을 전문 사업자에게 일임해 운영·보안·프라이버시 측면에서 효율을 높이려는 방향으로 읽히며, VPN 외부에서 DoH를 사용하는 사용자와 모바일/데스크톱 프로필을 배포해온 관리자는 구성 변경과 만료 시점에 주의를 기울여야 한다.

[Hacker News에서 원문 읽기 →](https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead)

