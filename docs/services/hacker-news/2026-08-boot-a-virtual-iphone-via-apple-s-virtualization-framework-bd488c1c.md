---
title: "Boot a Virtual iPhone via Apple's Virtualization.framework"
sidebar_label: "Boot a Virtual iPhone via Apple's Virtualization.framework"
---

# Boot a Virtual iPhone via Apple's Virtualization.framework

> Hacker News · 2026-08-28 · Virtualization / iOS 연구 도구

---

이 프로젝트는 Apple's Virtualization.framework과 PCC 연구용 VM 인프라를 활용해 Apple Silicon Mac에서 가상 iPhone을 부팅·운영하는 커맨드라인 도구 vphone-cli를 제공합니다. macOS 15(Sequoia) 이상이 호스트 요구사항이며 Xcode와 iOS SDK가 필요하고, 단일 명령(vphone-cli vm create myphone -V jb)으로 다운로드→패치→DFU 복원→커스텀 펌웨어(CFW) 설치→첫 부트까지 전 과정을 자동화합니다. VM 라이브러리와 IPSW, 도구 캐시는 ~/.vphone/ 아래에 유지되며 $VPHONE_ROOT/$VPHONE_LIBRARY_ROOT/$VPHONE_VENV_DIR 등으로 경로를 재정의할 수 있습니다. vphone-cli는 vm list/info/config/clone/export/import 같은 스크립팅 친화적 서브커맨드를 제공하고, 실행 중인 VM을 제어할 수 있는 소켓(/vphone.sock)을 통해 스크린샷·터치·하드웨어 키 조작을 지원해 AI 기반 E2E 테스트 흐름으로도 활용 가능합니다.
보안·권한 측면에서 실무적 고려사항이 상세히 정리돼 있습니다. 실행을 위해서는 SIP/AMFI 완화가 필요하며, 옵션A는 SIP를 완전히 비활성화하고 nvram 부트 인자(amfi_get_out_of_my_way=1)를 설정하는 방식, 옵션B는 SIP를 부분 허용(debug-only)한 뒤 특정 바이너리를 허용하는 amfidont 방식을 제시합니다. 패치 변형은 less→regular→dev→jb→exp 순으로 보안 우회 수준과 패치 수(예: jb 113개, exp 141개)가 증가하며 연구용 안티-VM 회피 패치 등도 포함됩니다. 알려진 문제로는 홈브루 ldid-procursus의 특정 릴리스 버그가 CFW 설치 중 무한 루프를 일으키는 사례와(해결책: --HEAD 빌드로 재설치), 호스트가 이미 VM으로 실행 중이면 가상화가 되지 않는다는 점(중첩 불가), 지역 설정에 따라 일부 시스템 앱 설치가 실패할 수 있다는 점(일부 지역 회피 권장), EXC_GUARD 관련 충돌에 대한 재패치 지침 등이 문서에 구체히 담겨 있습니다. 기술 독자에게는 iOS 부트체인·이미지 패치 파이프라인과 연구 목적의 특권·권한 우회 수위, 그리고 도구의 자동화·테스트 확장 가능성이 핵심 의미로 다가옵니다.

[Hacker News에서 원문 읽기 →](https://github.com/Lakr233/vphone-cli)

