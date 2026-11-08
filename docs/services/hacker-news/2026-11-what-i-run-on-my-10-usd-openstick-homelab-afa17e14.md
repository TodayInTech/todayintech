---
title: "What I run on my $10 USD OpenStick homelab"
sidebar_label: "What I run on my $10 USD OpenStick homelab"
description: "작성자는 배송 포함 10달러짜리 OpenStick(512MB RAM, 4 A53 코어, 4GB eMMC)에서 Debian·Podman 기반으로 AdGuard, Zeroclaw, Cloudflare Tunnel, Beszel, Fusion RSS 등 여러 경량 서비스를 운용하며 각 서비스의 메모리 사용량(예: Zeroclaw ~3MB, Fusion 22MB, Beszel 20MB)을 제시했다."
---

# What I run on my $10 USD OpenStick homelab

> Hacker News · 2026-11-07 · 홈랩·셀프호스팅

---

**$10짜리 OpenStick으로 가능한 실무적 홈랩**

작성자는 배송 포함 10달러에 구한 OpenStick에서 Debian(및 systemd, Podman) 기반으로 여러 경량 서버 서비스를 운영한 경험을 공유한다. 장비 사양은 **512 MB RAM(약 450 MB 사용 가능), 4× ARM Cortex‑A53(1 GHz), 4 GB eMMC, 150 Mbit/s Wi‑Fi, 4G 모뎀·GPS, 수동 냉각(무소음)**이다(작성자 설명).

## 경량 서비스와 메모리 예산

저사양 장치에 맞춘 서비스와 실제 메모리 수치가 핵심 근거다. 글에 따르면 주요 항목의 메모리 사용량은 다음과 같다: Fusion RSS 22 MB, Beszel(서버+에이전트) 약 20 MB(10+10), Shiori 10–20 MB, Gatus 10 MB, Diun 9 MB, Cloudflared 약 8–20 MB, AdGuard Home 계열 40 MB(작성자 포크 기준), Zeroclaw는 유휴 시 **~3 MB RSS**로 매우 가볍게 동작한다. 이러한 수치는 512 MB 환경에서 여러 서비스를 병행 구동할 수 있음을 직접적으로 보여준다.

## Zeroclaw: 경량 AI 에이전트 허브

Zeroclaw은 30개 채널(예: Telegram, 이메일, WhatsApp)을 지원하고 주요 LLM 제공자와 연동 가능한 에이전트 허브로 소개된다. 작성자는 기존 OpenClaw보다 메모리·업데이트 측면에서 안정적이었다고 평가하며, OpenStick에는 모니터링용 루트 셸 권한 수준으로 접근 권한을 부여해 “로그나 디스크 여유” 등 질의에 응답하도록 구성했다고 밝힌다. 글은 Zeroclaw의 낮은 유휴 메모리 소비(약 3 MB)를 근거로 저사양 장치에서도 실용적임을 주장한다.

## 네트워크·보안 노출과 모니터링 선택

외부 노출에는 Cloudflare Tunnel을 사용해 포트를 열지 않고 서비스를 인터넷에 노출한다고 설명한다. 단점으로는 작성자 관점에서 'NSA가 볼 수 있다'는 의견을 함께 제시한다. 모니터링 툴로는 시스템/컨테이너 통계에 Beszel을, 서비스 가용성엔 Gatus를 조합해 경량 모니터링 아키텍처를 만들었다. Dozzle는 Podman 로그 관리에 유리하지만 Beszel과 기능이 겹쳐 한쪽을 제거할 수 있다고 적었다.

## 실무적 시사점(해석)

제공된 수치와 설명을 기준으로 해석하면, **저가·저사양 ARM 기기에서도 적절히 경량화한 구성(로그·모니터링·DNS 차단·경량 AI 에이전트·RSS 아카이빙 등)이 실무적으로 가능**하다. 핵심 제약은 약 450 MB의 실사용 메모리라는 점으로, 서비스 추가·블록리스트 확대·아카이빙 시 일시적 스파이크가 발생할 수 있음을 고려해야 한다(글에서 Shiori와 같은 아카이빙 동작 시 스파이크가 발생한다고 명시).

근거는 작성자의 실제 운용 사례와 각 서비스의 메모리 사용량·행동 설명(chunk-0001, chunk-0002)이며, 구성 세부 설정·보안 정책 등은 원문에 제시된 범위를 넘지 않아 추가 검증이 필요하다.

[Hacker News에서 원문 읽기 →](https://blog.bosscher.ch/posts/openstick/)

