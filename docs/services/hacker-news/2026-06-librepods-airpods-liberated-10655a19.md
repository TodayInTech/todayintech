---
title: "Librepods: AirPods liberated"
sidebar_label: "Librepods: AirPods liberated"
---

# Librepods: AirPods liberated

> Hacker News · 2026-06-28 · 오픈소스/무선오디오

---

LibrePods는 AirPods가 Apple 기기들 사이에서 주고받는 독점 프로토콜을 리버스엔지니어링해 비애플 플랫폼에서 Apple 전용 기능을 사용할 수 있게 하는 오픈소스 프로젝트입니다. 프로젝트는 리스닝 모드 전환, 이어 착용 감지, 배터리 상태 표시, 기기 이름 변경, 대화 인식, 자동 연결 등 Linux와 Android에서 이미 작동하는 기능들을 정리해 두었고(기능 표 참조), 일부 접근은 VendorID를 Apple로 바꾸는 스푸핑(예: /etc/bluetooth/main.conf에 DeviceID = bluetooth:004C:0000:0000 추가)이나 안드로이드에서 Xposed 기반 모듈이 필요하다고 명시합니다. 프로젝트 측은 librepods.org 같은 사이트가 공식 사이트를 사칭하는 사례를 경고하고 있으며, Apple 상표와 SF Pro 폰트 사용 문제 등 라이선스·상표 관련 고지도 포함하고 있습니다.
기술적으로 이 작업은 AACP/ATT 계층 구현과 블루투스 장치 식별 조작, 루트 권한이 필요한 OS 영향 지점들을 건드리는 수준의 리버스엔지니어링을 요구합니다. 일부 고급 기능(Find My 통합, 헤드 트래킹 기반 HRTF, 고품질 양방향 오디오)은 추가 RE와 루트 권한을 필요로 하며 공간화(stereo spatializing)는 범위 밖으로 명시되어 있습니다. 개발 과정에서는 Wireshark dissector 같은 RE 도구와 커뮤니티 기여가 중요했으며, 소스 일부는 AI로 생성 또는 Kotlin→Rust 변환된 코드(aacp.rs, att.rs, media_controller.rs)를 포함합니다. GPL 라이선스로 배포되며, 접근 방식(특히 VendorID 스푸핑과 루트 필요성)은 사용자 환경과 보안·안정성 영향을 고려해 '사용자 책임' 하에 사용하라는 안내가 함께 제시되어 있습니다.

[Hacker News에서 원문 읽기 →](https://github.com/librepods-org/librepods)

