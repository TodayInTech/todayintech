---
title: "Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable"
sidebar_label: "Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable"
---

# Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable

> Hacker News · 2026-07-04 · 오픈소스 게임 포팅

---

이 프로젝트는 2003년 RTS 'Command and Conquer: Generals — Zero Hour' 엔진을 에뮬레이션 없이 ARM64 네이티브로 빌드해 Apple Silicon 맥과 아이폰·아이패드에서 실행하도록 포팅한 작업을 담고 있다. DirectX 8 렌더링 경로를 DXVK → Vulkan → MoltenVK → Metal로 전달하는 기술적 접근을 사용하며, 캠페인·스커미시·Generals Challenge를 포함하고 터치에 맞춘 입력(탭 선택, 드래그 박스, 롱프레스 취소선택, 두 손가락 스크롤, 핀치 줌)을 지원한다. 작업은 EA의 GPL v3 소스 릴리스와 fbraz3/GeneralsX의 macOS/Linux 포트를 기반으로 하며, 이 포크는 iOS/iPadOS 포팅과 엔진 수정들을 추가했다.
빌드·배포 파이프라인과 종속성도 상세히 문서화되어 있다. vcpkg, LunarG Vulkan SDK(홈브류 cask 아님), MoltenVK 프레임워크(체크섬 고정), DXVK iOS 패치, Xcode·Apple 개발자 팀 설정, xcodegen 등 도구체인이 필요하고, 스크립트로 클론·빌드·패키징·앱 설치와 Steam에서 사용자 자산을 가져오는 절차가 제공된다(게임 자산은 포함되지 않음; 소유한 복사본 필요). 실행상 제약도 공개되어 있어 iPad에서 3GB 이상 상주 메모리시 iOS가 세션을 종료하거나 백그라운드 전환 시 드문 레이스 상태로 크래시가 발생할 수 있음을 밝히며 로그 위치도 안내한다. 더불어 포팅 과정의 세부 고장원인·수정 기록을 담은 포팅 플레이북과 패턴, 릴리스 체크리스트가 포함돼 있어 동일한 방식으로 고전 윈도우 게임을 Apple 플랫폼으로 옮기려는 기술자들에게 유용한 참고자료가 된다. 아울러 이 포트가 인간-AI 협업(Claude Code/Fable 모델과 Ammaar Reshi의 지휘)으로 개발되었다고 명시되어 있어 개발 과정의 현대적 측면도 드러난다.

[Hacker News에서 원문 읽기 →](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main)

