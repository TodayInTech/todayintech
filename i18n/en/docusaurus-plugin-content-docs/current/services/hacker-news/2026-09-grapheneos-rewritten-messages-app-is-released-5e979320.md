---
title: "GrapheneOS' rewritten Messages app is released"
sidebar_label: "GrapheneOS' rewritten Messages app is released"
---

# GrapheneOS' rewritten Messages app is released

> Hacker News · 2026-09-11 · Android / Privacy &amp; UX

---

GrapheneOS의 메시징 앱이 버전 13에서 완전히 재작성되어 기존 레거시 인터페이스를 Jetpack Compose와 Material 3 기반으로 대체하고 모든 화면을 새로 빌드했습니다. 이번 업데이트는 대형 화면용 2-패인 레이아웃, 적응형 아이콘, 온보딩(권한·기본앱·SMS 프라이버시 안내), 대화 고정·스누즈·미읽음 표시·스와이프 아카이브 등 대화 관리 기능의 대대적 개선을 담고 있습니다. 미디어 픽커·오디오 녹음·사진 뷰어·vCard 뷰어가 재작성되었고, 공유·전달 파이프라인과 위젯도 개편되어 전송 오류 보고와 첨부 처리 신뢰성이 향상됐습니다.또한 읽지 않은 알림 유지, MMS 주제·다운로드 상태 표시, 삭제 중 도착 메시지 손실 방지 등 메시지·알림 처리에서 여러 경합 조건과 크래시를 고쳤습니다.
보안·프라이버시 측면에서도 중요한 변경이 포함됩니다. YouTube 링크 미리보기는 기본 비활성화·옵트인 방식이며, 공유 컨텐츠 검증에서 file: URI와 사설 앱 파일을 차단하고 콘텐츠 URI 권한을 확인합니다. 위젯 리시버 비노출, 불필요한 PendingIntent에 FLAG_IMMUTABLE 적용, EXIF/MMS 파싱에 대한 할당 한계 추가, GIF·vCard 파서 관련 버그 수정 등으로 공격 표면과 메모리·네이티브 처리 취약점을 줄였습니다. 개발 플랫폼 요구사항은 minSdk 36·target/compileSdk 37으로 상향되었고 AGP, Kotlin, Gradle 및 Compose BOM, CameraX 등 의존성 업데이트가 포함되어 CI 기반의 단위·계측 테스트가 PR마다 실행됩니다. 전반적으로 최신 안드로이드 스택으로의 이행과 보안성·접근성·대형 화면 지원 개선을 동시에 노린 릴리스입니다.

[Hacker News에서 원문 읽기 →](https://github.com/GrapheneOS/Messaging/releases/tag/13)

