---
title: "Outlook.com Is Quietly Rejecting Email from Domains Without DMARC"
sidebar_label: "Outlook.com Is Quietly Rejecting Email from Domains Without DMARC"
description: "MailRoute는 2026-11-05부터 Outlook.com 계열이 DMARC 레코드가 없는 도메인의 일부 메일을 묵인 없이 거부하기 시작했다고 보고한다. 해결책은 DNS에 _dmarc TXT 레코드(v=DMARC1; p=none)를 추가하는 것뿐이다."
---

# Outlook.com Is Quietly Rejecting Email from Domains Without DMARC

> Hacker News · 2026-11-08 · 이메일 인증/DMARC

---

Outlook.com(및 Hotmail, Live, MSN)이 2026-11-05부터 DMARC 레코드가 없는 도메인에서 보내는 일부 메일을 거부하기 시작했다고 MailRoute가 보고했다. 문제는 대량 발송자 전용으로 알려진 기존 규칙과 달리 **소규모 발신자도 영향**을 받고, Microsoft는 2026-11-06 기준 별도 공지를 올리지 않았다는 점이다.

## 어떤 메시지가 돌아오는가

반송 메시지는 다음과 같은 형태다:

550 5.7.1 Message rejected: Message lacks SPF/DKIM/DMARC Auth Records (AS9031519)

기존의 550 5.7.515(Access denied) 규칙과 달리 이번 거부는 실패 항목을 상세히 표시하지 않으며, 동일 도메인에서 일부만 반송되고 일부는 정상 전달되는 등 일관성이 없다. MailRoute는 자체 로그에서 11월 5일 처음 관측했고 같은 날 다른 관리자들의 보고가 이어졌다고 전한다.

## 당장 할 수 있는 조치

가장 빠른 해결책은 DNS에 DMARC TXT 레코드를 추가하는 것이다. 예시:

dig +short TXT _dmarc.example.com

(출력에 "v=DMARC1"로 시작하는 줄이 없으면 레코드가 없는 상태임)

레코드(안전한 시작점):

Name: _dmarc

Value: v=DMARC1; p=none

p=none은 DMARC를 선언하되 실패 시 수신자에게 조치를 요구하지 않는 설정으로, **Outlook.com이 현재 요구하는 최소 조건**이다. 단, DMARC는 From 주소 도메인에서 SPF 또는 DKIM 중 하나가 성공적으로 정렬(alignment)돼야 통과한다. SPF/DKIM 둘 다 정렬되지 않으면 DMARC 레코드만으로는 해결되지 않는다.

## MailRoute 사용자의 상황

MailRoute를 통해 발송하는 메일은 MailRoute의 출발 서버를 SPF로 허용(include:spf.mailroute.net)하고, 도메인 서명용 DKIM 키(mr01, mr02, mr03)를 사용해 서명하므로, 해당 경우에는 DMARC 레코드만 추가하면 Outlook.com에서 인증 통과가 가능하다고 MailRoute는 설명한다.

## 향후 방향성

MailRoute는 이번 사례를 주요 메일 사업자들이 먼저 대량 발송자 대상으로 공지한 규칙을 차츰 전체 기준으로 확장하는 패턴의 일부라고 분석한다. 따라서 **v=DMARC1; p=none**을 최소 바닥선으로 간주하고 DNS에 먼저 적용해 두는 것이 실무적으로 권장되는 대응이다.

출처: MailRoute 블로그(관측 날짜 및 메시지 예시는 해당 게시글 근거).

[Hacker News에서 원문 읽기 →](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc)

