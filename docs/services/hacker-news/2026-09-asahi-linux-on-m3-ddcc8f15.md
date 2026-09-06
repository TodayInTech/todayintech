---
title: "Asahi Linux on M3"
sidebar_label: "Asahi Linux on M3"
---

# Asahi Linux on M3

> Hacker News · 2026-09-06 · 오픈소스/운영체제

---

Asahi Linux가 설치 프로그램에 M3 시리즈 기기 지원을 병합하며 M3 계열 SoC를 탑재한 Mac을 공식적으로 지원하게 됐다고 발표했다. 공개된 내용에 따르면 M1·M2 계열에서 동작하던 주요 기능들이 M3에서도 거의 그대로 작동하며, 웹캠·내장 마이크·Wi‑Fi·Bluetooth·USB(하드웨어 한계인 USB 3 10 Gb/s까지 포함)와 하드웨어 가속 비디오 디코딩(AV1 포함) 등이 지원된다. 다만 전체 DCP(디스플레이 암호화) 지원과 GPU 쪽은 아직 완전하지 않아 현시점에서는 성능 좋거나 전력 효율적인 3D 가속을 기대하기 어렵다고 명시한다.
현재 이 지원은 신선한 작업이 많아 설치기의 Expert 모드에서만 활성화되며, macOS 터미널에서 제공된 curl 명령에 EXPERT=1을 설정해 설치할 수 있다. 설치 직후에는 dnf upgrade --refresh로 시스템 업그레이드를 권장하고, Fedora Linux 45 베타 공개 전후로 Expert 요구를 제거하는 것을 목표로 하고 있다. 알려진 제약으로는 펌웨어가 제공하는 프레임버퍼 제약 때문에 절전(sleep)이 작동하지 않고, DCP 미지원으로 일부 기기의 HDMI 포트가 비활성화되며 Mac Studio(M3 Ultra)는 아직 지원 대상에 포함되지 않는다. 전반적으로 이번 병합은 M1·M2 수준에 근접한 기능성을 M3로 확장한 의미 있는 진전이지만, 외부 디스플레이 및 전원/절전 동작, GPU 가속 같은 남은 기술적 과제가 실제 사용성과 전력 효율에 영향을 미친다.

[Hacker News에서 원문 읽기 →](https://asahilinux.org/2026/09/m2-episode-1/)

