---
title: "Building and Shipping Mac and iOS Apps Without Ever Opening Xcode"
sidebar_label: "Building and Shipping Mac and iOS Apps Without Ever Opening Xcode"
---

# Building and Shipping Mac and iOS Apps Without Ever Opening Xcode

> Hacker News · 2026-07-13 · Apple 개발 / 빌드 자동화

---

Xcode를 GUI로 직접 열지 않고도 macOS와 iOS 앱을 빌드·서명·배포하는 전체 흐름을 실무 관점에서 정리한 글입니다. 핵심은 Xcode.app는 설치되어 있어야 하지만 열 필요는 없고, xcodebuild·xcrun notarytool·stapler·devicectl 같은 도구들이 Xcode 내부에 있어 셸에서 완전한 빌드·배포 파이프라인을 수행할 수 있다는 점입니다. 프로젝트 자동화에는 xcodegen으로 project.yml을 관리해 .xcodeproj를 소스에 두지 않는 전략을 쓰고, 배포는 저장소 내 scripts/release.sh 하나로 archive → Developer ID 서명 → notarize → staple → /Applications 설치까지 처리합니다. 또한 CommandLineTools 패키지와 Xcode.app의 차이, xcode-select로 올바른 경로를 지정해야 하는 점도 강조합니다.
실무적 제약과 보안 처리도 구체적으로 다룹니다. 서명은 로그인 키체인에 있는 개인키로 이루어지며 Developer ID Application과 Apple Development 인증서가 용도별로 다르다는 설명, notarization은 앱 특화 비밀번호로 notarytool에 한 번만 자격을 저장해야 하는 절차(앱별 프로필 권장) 등이 포함됩니다. 디바이스 배포는 devicectl과 -allowProvisioningUpdates 옵션으로 헤드리스로 가능하고, 빠른 내부 루프 검증은 CODE_SIGNING_ALLOWED=NO로 수행할 수 있습니다. 저자는 Claude Code 같은 LLM을 이용해 release.sh와 CLAUDE.md를 생성·보완함으로써 반복 가능한 '한 문장으로 배포' 워크플로우를 완성했다고 전하며, 비밀값은 리포지토리에 남기지 않고 키체인이나 비밀번호 관리자에 보관하는 실무적 권장도 함께 제시합니다.

[Hacker News에서 원문 읽기 →](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/)

