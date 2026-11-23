---
title: "Inside the Codex sandbox"
sidebar_label: "Inside the Codex sandbox"
description: "OpenAI는 Codex가 사용자 호스트에서 명령을 실행할 때 파일시스템과 네트워크 접근을 OS별 샌드박스로 제한하는 Codex sandbox 설계(권한 프로파일, 네트워크 프록시, macOS/Linux/Windows 구현 및 Windows의 MXC 전환)를 공개했다."
---

# Inside the Codex sandbox

> OpenAI Blog · 2026-11-18 · Engineering

---

OpenAI는 Codex가 사용자의 기존 환경에서 명령을 실행하면서도 **파일시스템과 네트워크 접근을 권한 프로파일로 제한하는** Codex sandbox의 설계와 구현 세부를 공개했다. 샌드박스는 VM/컨테이너가 아닌 각 운영체제의 네이티브 제약을 활용해 ‘호스트에서 실행하되 접근을 통제’하는 접근을 택한다.

## 권한 프로파일과 기본 정책
Codex는 :workspace 같은 보수적 기본 프로파일을 제공한다. 예시로 작업공간 내 쓰기는 허용하되 .git, .codex, .codex/config.toml, .git/hooks 같은 민감 경로는 읽기 전용으로 유지한다. 기본적으로 **광범위한 파일 읽기는 OS 권한에 따르며 네트워크는 비활성화**해 직접 업로드를 막는다. 다만 node_modules 같은 외부 패키지를 변조하면 Git 상태에 드러나지 않을 수 있는 위험을 지적한다.

프로파일 병합과 조직 정책도 지원한다. 예를 들어 /etc/codex/requirements.toml에 ":danger-full-access" = false를 설정해 클라우드 요구사항이 시스템 요구사항을 우선하도록 강제할 수 있다.

## 네트워크 제어: 프록시와 DNS 처리
네트워크 제한은 codex-network-proxy 라이브러리(HTTP+SOCKS5)를 통해 구현된다. 샌드박스 환경에서 프로세스에는 HTTP_PROXY, HTTPS_PROXY, ALL_PROXY 등 관련 환경변수가 주입되며, 프록시는 도메인 허용·거부 규칙을 적용한다. 프록시는 허용 여부를 먼저 판정한 뒤 호스트명을 해석하므로 DNS 조회로 인한 정보 유출 가능성을 줄이려는 설계가 반영돼 있다.

## macOS, Linux, Windows별 구현
- macOS: Apple의 Seatbelt(SBPL) 정책을 /usr/bin/sandbox-exec로 적용해 포트·파일 접근을 제한한다.
- Linux: bubblewrap 기반 네임스페이스를 사용하며, 샌드박스 내부에서 루프백 리스너를 만들고 외부 프로세스가 이를 받아 프록시로 중계하는 방식(유닉스 소켓 페어·파일 디스크립터 전달)을 쓴다. 이로써 샌드박스 내부에 별도의 네트워크 네임스페이스를 유지하면서도 외부 프록시에 안전히 연결할 수 있다.
- Windows: 기존 샌드박스에서 Microsoft의 MXC(Microsoft eXecution Container) 기반 샌드박스로 전환 중이다. MXC 전환의 목적은 관리자 권한 필요성, ACL 설정 비용, 호스트에 남는 영구적 설정 상태(ACL·방화벽·사용자·제어 파일) 같은 한계를 해소하기 위함이다. Codex는 MXC JSON 스키마를 통해 파일시스템·네트워크·데스크탑·클립보드 등 권한을 매핑하며, MXC의 기본 방식(deny-by-default)과 deny-glob 전개, 드라이브별 권한 처리(C:\\등) 등 구현상의 세부를 설명한다.

## 실무적 함의(근거 기반)
Codex 샌드박스는 개발자가 호스트 특화 도구(예: macOS의 iOS 빌드 툴체인)를 그대로 쓰면서도 에이전트의 권한을 제어하려는 설계다. 다만 문서 자체도 지적하듯 광범위한 파일 읽기 허용과 wildcard DNS 규칙 등은 여전히 정보 유출 경로가 될 수 있어, 프로파일 설계와 추가적 엔터프라이즈 정책(예: requirements 파일 병합)이 중요하다.

원문은 샌드박스 CLI(codex sandbox) 사용 예시, 권한 병합 규칙, 플랫폼별 기술적 구현 흐름(Seatbelt, bubblewrap+네트워크 네임스페이스, MXC 전환)과 네트워크 프록시의 동작 방식을 상세히 다룬다. 이 글의 기술적 세부는 Codex를 도구에 통합하거나 프로파일을 구성하려는 엔지니어에 실무적 참고가 된다.

[OpenAI Blog에서 원문 읽기 →](https://openai.com/index/inside-the-codex-sandbox)

