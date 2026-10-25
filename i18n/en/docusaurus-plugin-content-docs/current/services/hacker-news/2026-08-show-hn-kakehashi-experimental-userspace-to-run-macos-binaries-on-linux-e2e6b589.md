---
title: "Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM"
sidebar_label: "Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM"
---

# Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM

> Hacker News · 2026-08-02 · 시스템·호환성

---

Kakehashi는 macOS ARM64(Darwin) 사용자용 CLI 바이너리를 Linux aarch64에서 직접 실행하도록 설계된 사용자공간 번역 계층입니다. JIT 없이 동작하며 Mach-O 로더와 freestanding libSystem을 포함한 런타임을 통해 BSD 스타일 시스템콜을 변환하고, clang 프로브·7-Zip(7zz)·curl 등 실사용 도구를 실행해 동작을 검증합니다. 호스트 파일시스템을 /Volumes/linux로 브리지하는 'bottle'을 제공하고 Docker/Colima/UTM과 베어메탈 환경에서 동작함이 문서화되어 있으며, kh CLI로 설치·실행(kh run, kh install 등)할 수 있습니다. Apple 프레임워크 일부는 소프트 스텁으로 처리되며 OpenSSL 관련 optional config가 없다는 경고가 나타나지만 호스트 CA 번들을 통해 HTTPS는 동작하는 등 현실적 제약과 처리 방식이 명시되어 있습니다.
기술적 의미는 '명령행 도구를 macOS 대신 저비용 Linux aarch64 러너에서 돌리는 것'에 있습니다. Kakehashi는 명령어를 에뮬레이트하지 않고 게스트 코드를 CPU에서 네이티브로 실행하되 시스템콜 경계에서 TLS 전환·대체 스택·NEON 저장/복원·Rust 디스패치 등 비용이 발생한다고 설명합니다. 성능 예시로 대용량 다중 파일 7zz 압축에서는 네이티브 Linux 22.5초 대비 Darwin 7zz가 kh 상에서 약 118초로 약 5.2배 느렸고, 파일이 적고 압축 중심 작업에서는 격차가 1.1–1.2배로 작게 나타납니다. 하이퍼콜이 기본 활성화되어 있으며(KAKEHASHI_HYPERCALL), GUI·코드사인·Xcode UI 테스트 등은 대상이 아니므로 CI에서 Darwin CLI 작업을 저렴한 Linux arm64로 대체해 비용과 가용성 문제를 완화하려는 실무적 목표가 분명합니다. 프로젝트는 테스트·스모크·벤치 스크립트와 로드맵을 제공하고 Apache-2.0으로 배포됩니다.

[Hacker News에서 원문 읽기 →](https://github.com/wie-project/kakehashi)

