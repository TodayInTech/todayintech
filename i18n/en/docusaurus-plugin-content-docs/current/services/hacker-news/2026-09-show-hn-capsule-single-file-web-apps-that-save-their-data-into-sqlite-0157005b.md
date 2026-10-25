---
title: "Show HN: Capsule – Single-file web apps that save their data into SQLite"
sidebar_label: "Show HN: Capsule – Single-file web apps that save their data into SQLite"
---

# Show HN: Capsule – Single-file web apps that save their data into SQLite

> Hacker News · 2026-09-15 · 소프트웨어/개발 도구

---

Capsule은 HTML/CSS 기반 UI와 사용자 데이터를 하나의 이동식 .capsule 파일 안에 묶어 배포·실행할 수 있게 하는 도구입니다. 제공된 설명에 따르면 앱의 UI, 스키마, 로컬 SQLite 데이터, 심지어 PDF나 이미지 같은 자산까지 데이터베이스 안에 직접 포함되며, 클라우드 계정이나 별도 서버 없이 파일을 공유하면 즉시 실행 가능한 형태로 전달됩니다. 오프라인 지원과 플랫폼 간 호환성을 강조해 macOS·Windows·Linux에서 별도 설정 없이 실행되며, iOS·Android 네이티브 지원도 곧 추가될 예정이라고 밝혔습니다. 또한 AI 기반의 앱 생성·수정 기능(프롬프트로 앱을 생성하고 실시간 AI 업데이트를 적용)이 통합되어 있어, 간단한 지시로 완전한 단일 파일 데스크탑 애플리케이션을 만들어낼 수 있습니다.
기술적 구현 측면에서는 개발자가 제공한 메타정보에서 Rust와 Tauri 2.0으로 작성되었다는 점, HTML 자산을 SQLite 파일에 임베드하는 구조, 로컬스토리지식 키/값 저장소 혹은 MongoDB 유사 컬렉션 API로 문서를 저장하는 방식 등 구체적 설계 요소가 확인됩니다. 보안·프라이버시도 설계 우선순위로 언급되어 문서가 기본적으로 파일 시스템 직접 접근 권한을 갖지 않으며 네트워크 접근도 권한을 필요로 하는 모델을 채용 중이라 했고, 다중 사용자가 만든 서로 다른 복사본을 병합하기 위해 각 데이터 항목에 UUID와 타임스탬프를 부여하는 전략을 사용한다고 합니다. 파일 포맷 1.0에 대한 사양 공개와 버전 마이그레이션 계획도 예고되어 있어 타 애플리케이션과의 상호운용성 및 데이터 보존 측면에서 실무적 관심을 끌 만합니다.

[Hacker News에서 원문 읽기 →](https://withcapsule.app/)

