---
title: "Turn off Apple Intelligence on macOS 27 and get its disk space back"
sidebar_label: "Turn off Apple Intelligence on macOS 27 and get its disk space back"
---

# Turn off Apple Intelligence on macOS 27 and get its disk space back

> Hacker News · 2026-10-04 · macOS 프라이버시/유틸리티

---

RemoveMacAI는 macOS 27에서 Apple Intelligence 기능을 끄고 관련 온디스크 모델을 삭제한 뒤 재다운로드를 차단하는 오픈소스 도구다. 원문은 설치 방법(한 줄 curl 스크립트, Homebrew 탭)과 함께 배포된 릴리스의 SHA-256 검증, GitHub Actions로 태그 기반 빌드를 하고 빌드 증명(attestation)을 제공하는 점을 명시한다. 사용자는 툴이 현재 상태를 보여준 뒤 System Settings에서 승인해야 하는 구성 프로파일을 설치하도록 안내받고, 이 프로파일이 Apple의 제한 키들을 적용하거나 설정을 강제해 모델 다운로드를 로컬의 닫힌 포트로 리다이렉트함으로써 macOS가 해당 모델을 다시 내려받지 못하게 만든다. 모델 삭제는 Apple의 asset service를 통해 이루어지며 System Integrity Protection은 유지되고 /System 하위 파일을 직접 수정하지 않는다. 툴 자체는 네트워크 요청을 발생시키지 않고 사용자 데이터도 수집하지 않는다고 밝힌다.
구체적으로 끄는 기능에는 Siri(“Hey Siri” 포함), 글쓰기 도구, Genmoji·이미지 생성, Mail·Messages·Safari·Notes의 요약 등 여러 기능이 포함되며, 기초 모델과 이미지 생성·Genmoji·Spatial Photos·Photos Clean Up·Xcode 예측완성 모델 등이 제거된다. 되돌리기는 동일한 설치 스크립트에 revert 인자를 주거나 removemacai revert 명령으로 가능하며, Homebrew로 설치한 경우에는 brew uninstall로 제거할 수 있다. 주의점도 문서에 명시되어 있는데(예: 음성 받아쓰기는 별도 설정으로 영향 없음, macOS 업데이트로 제거되지 않음, 저장 공간 화면은 macOS가 파일을 실제로 지우는 시점까지 항목을 계속 표시함, Spotlight 관련 프로세스가 Siri라는 이름으로 남는 현상 등), Foundation Models 프레임워크나 단축어의 Use Model 액션을 쓰는 앱은 기능 손실을 겪는다. 원문은 또한 이 도구가 4evy의 pared를 기반으로 빌드되었음을 밝히며 호환성은 macOS 27에서 테스트되었고 이전 버전은 지원하지 않는다고 적고 있다. 이러한 점들은 사용자가 모델 삭제와 재다운로드 차단을 구성 프로파일과 자산 서비스 조합으로 실무적으로 관리할 수 있음을 보여주며, 저장 공간과 온디바이스 모델 관리를 직접 통제하려는 기술 사용자에게 실용적 의미가 있다.

[Hacker News에서 원문 읽기 →](https://github.com/omlahore/RemoveMacAI)

