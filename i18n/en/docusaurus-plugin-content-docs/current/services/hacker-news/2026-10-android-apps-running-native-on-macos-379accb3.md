---
title: "Android apps running native on macOS"
sidebar_label: "Android apps running native on macOS"
---

# Android apps running native on macOS

> Hacker News · 2026-10-19 · macOS 오픈소스 호환성

---

Mac.apk은 Apple Silicon 맥에서 안드로이드 앱을 에뮬레이터나 가상머신 없이 직접 실행하도록 설계된 오픈소스 알파 소프트웨어다. macOS 프로세스로 앱을 띄우고 Mac의 GPU로 렌더링하며 CPU에서 네이티브 속도로 동작한다고 소개한다. 앱은 Dock에 표시되고 macOS 창으로서 크기 조절·회전·라이트·다크 모드 연동이 가능하며, 창 상단에 뒤로가기 버튼이 추가되는 등 플랫폼 통합을 목표로 한다. 요구사항은 macOS 26.4(Tahoe) 이상과 Apple Silicon으로, 인텔 맥은 지원되지 않는다. 배포는 디스크 이미지를 통해 이루어지며 실행파일은 애플 서명·노타리제이션을 거쳤다. 설치·앱 관리 절차와 첫 실행 시 준비 때문에 대형 앱은 초기 실행이 최대 1분까지 걸릴 수 있다는 점, 설치파일과 설치된 앱의 디스크 점유(앱 자체 약 280MB, 설치된 앱은 APK 크기의 1.5~3배)도 문서화되어 있다.
기술적으로 Mac.apk는 안드로이드 환경을 macOS 위에 직접 재구현하는 접근을 취한다. 레포지토리에는 Android 프레임워크 재구현, 네이티브 런타임, arm64 로더와 Bionic shim, ARM32 리컴파일러 및 macOS 앱 구현체가 포함되어 있으며 BUILDING.md로 빌드 방법을 안내한다. ANGLE·MoltenVK·Vulkan 로더·Capstone·libpng 등 여러 오픈소스 구성요소와 OpenJDK 기반 JRE를 번들하고, 일부는 LGPL로 제공되어 해당 소스와 패치가 릴리스에 첨부된다. 프로젝트는 GNU AGPL v3.0으로 라이선스되며 상업용 라이선스 옵션을 별도로 제공한다. 중요한 보안 경고로, Mac.apk로 실행한 APK는 macOS 사용자 권한으로 네이티브 코드로 동작하므로 전화기 수준의 샌드박스가 없고 파일 접근·쓰기 권한을 가질 수 있어 신뢰할 수 있는 소스의 APK만 사용해야 한다. 로그 경로와 버그 리포트 절차, 기여·빌드 관련 정보도 명시되어 있어 기술 검토와 포팅·디버깅에 필요한 근거가 충실하다.

[Hacker News에서 원문 읽기 →](https://github.com/kksimp/Mac.apk)

