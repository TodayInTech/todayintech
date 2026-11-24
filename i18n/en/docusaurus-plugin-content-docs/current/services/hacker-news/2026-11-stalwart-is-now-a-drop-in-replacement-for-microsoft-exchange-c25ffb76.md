---
title: "Stalwart is now a drop-in replacement for Microsoft Exchange"
sidebar_label: "Stalwart is now a drop-in replacement for Microsoft Exchange"
description: "Stalwart 1.2.0이 MAPI over HTTP, EWS, Exchange ActiveSync, Autodiscover를 구현해 **Microsoft Exchange의 드롭인 교체**가 가능해졌다. 새 Outlook(클라우드 전용)은 지원하지 않아 마이그레이션 시 주의가 필요하다."
---

# Stalwart is now a drop-in replacement for Microsoft Exchange

> Hacker News · 2026-11-23 · 오픈소스 이메일 인프라

---

**Stalwart 1.2.0 — Exchange의 드롭인 교체**

Stalwart 1.2.0은 **MAPI over HTTP, Exchange Web Services(EWS), Exchange ActiveSync, Autodiscover**를 구현해 Outlook(클래식), Apple Mail, 모바일 기본 앱 등 기존 Exchange 클라이언트가 그대로 연결할 수 있는 오픈소스 대안이 됐다고 발표했다. 이 기능은 커뮤니티 에디션(AGPL)에 포함되어 있다.

## 교체가 가능한 범위와 지원 클라이언트
- 지원 프로토콜은 MAPI over HTTP(EMSMDB·NSPI), EWS(Exchange 2010 SP2~2016 스키마), ActiveSync(14.1·16.1), Autodiscover다. 메일·캘린더·연락처·작업·노트와 인크리멘탈 동기화, 전역 주소록, 오프라인 주소록, 위임·공유·규칙·푸시(ActiveSync Ping) 등 주요 기능을 커버한다.
- 연결 가능한 클라이언트로는 클래식 Outlook(Outlook 2016 이상 포함 Microsoft 365 Apps), Outlook for Mac(EWS), Apple의 Mail/Calendar/Contacts(EWS), iOS·Android 기본 앱(ActiveSync), Thunderbird(e.g. EWS/TbSync), Evolution, eM Client 및 EWS/ActiveSync 기반 라이브러리(exchangelib) 등이 명시되어 있다.

## 중요 제약 — '새 Outlook'과 Microsoft의 클라우드 경로
- 새 Outlook(Windows 기본 설치)은 온프레미스 Exchange를 지원하지 않으며, IMAP 계정 추가 시 사용자 자격증명과 서버 정보를 Microsoft 클라우드로 전송해 Microsoft 인프라가 대신 연결한다는 점이 지적되어 있다. Stalwart 측은 새 Outlook을 자가호스팅 메일과 함께 사용하지 말 것을 권고한다.
- Outlook 모바일 앱도 온프레미스 접근을 위해 Microsoft의 클라우드 서비스에 의존하므로, 모바일에서는 기기 기본 앱(ActiveSync)을 권장한다.

## 아키텍처와 데이터 관리, 마이그레이션
- Exchange 호환성 코드는 약 **200,000행**의 코드가 추가되었으나, 별도 모듈로 분리되어 단일 Cargo feature(free toggle)로 제어된다. 기본 빌드에서는 비활성화 상태이며, 사용하지 않으면 바이너리에 포함되지 않는다.
- Exchange 관련 메타데이터는 JMAP Object Metadata 확장을 통해 아이템에 첨부하는 형태로만 저장하고, Exchange 클라이언트가 연결해 설정할 때에만 기록된다. 메타데이터 삭제로 Exchange 전용 데이터만 제거할 수 있다.
- 마이그레이션 도구 Vandelay는 온프레미스 Exchange를 EWS로, Microsoft 365(Exchange Online)를 Microsoft Graph로 읽어 JMAP으로 Stalwart에 복사한다. 도메인 컷오버는 MX 레코드와 클라이언트 설정 변경으로 이뤄진다.

## 동반 기능과 운영 편의성
- 1.2.0에 같이 포함된 기능들: 서버사이드 메일 규칙(웹UI/JMAP/Outlook에서 관리, Sieve로 컴파일), Message Disposition Notifications(읽음 영수증), 근무 시간 표시와 조직 내부의 가용성 조회, 리소스(회의실·장비) 계정, **네이티브 FoundationDB 비동기 Rust 클라이언트**(libfdb_c 대체).
- FoundationDB 새 클라이언트는 포인트 읽기에서 **4.5~6.9배 높은 처리량**, **5~7배 낮은 중앙값 지연**, 약 **절반의 CPU 사용량**을 보고했다고 밝혔다.
- stalwart-cli 2.0.0은 SSH 환경용 대화형 콘솔을 추가해 관리자가 브라우저 없이도 계정·도메인·트레이스·대시보드를 다룰 수 있도록 했다.

## 실무적 의미
- 조직은 서버를 먼저 대체하고 클라이언트를 점진 교체하는 현실적인 경로를 확보한다. 관리자는 메일박스 마이그레이션(Vandelay), DNS 변경, Autodiscover 구성을 통해 사용자의 작업 흐름을 깨지 않고 전환할 수 있다. 다만 새 Outlook과 모바일 Outlook 경로는 Stalwart의 목적(데이터 주권 보장)에 맞지 않으므로 **사용자 교육과 정책**이 필요하다.
- Exchange 관련 코드는 기본적으로 비활성화·모듈화되어 있어 적용 여부와 장기 유지 비용을 선택할 수 있다.

출처: Stalwart 공식 블로그 릴리스 노트(1.2.0) 및 변경 로그에 따른 기술·마이그레이션 설명.

[Hacker News에서 원문 읽기 →](https://stalw.art/blog/microsoft-exchange-replacement/)

