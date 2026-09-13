---
title: "I'm being cyberattacked by Tesla, Inc"
sidebar_label: "I'm being cyberattacked by Tesla, Inc"
---

# I'm being cyberattacked by Tesla, Inc

> Hacker News · 2026-09-13 · Security

---

한 개인 운영 NTP 풀 서버 운영자가 nginx 로그를 조사하던 중, AWS 소속으로 보이는 세 IP(54.165.75.96, 35.168.63.24, 52.44.200.251)에서 pool-ntp.tesla.com을 Host/Referer로 붙인 채 Assetnote 사용자 에이전트를 사용해 지속적인 스캔과 익스플로잇 시도를 받았다고 보고했다. 로그 샘플에는 SSRF 콜백(Assetnote 콜백 도메인), Log4Shell 페이로드, 패스 트래버설, 웹셸 업로드, CMS·관리 엔드포인트 탐 probing 등 다양한 공격 템플릿이 포함되어 있으며, 작성자는 수일간 약 8,000건(누적 50,000건 이상)의 요청을 받았고 다른 NTP 풀 운영자도 유사 트래픽을 관찰했다고 전한다. 모든 시도는 성공하지는 않았지만 콜백 도메인과 템플릿에 제3자 호스트명이 박혀 있어 스캐닝 템플릿의 광범위한 영향이 드러난다.
작성자는 원인으로 테슬라가 pool-ntp.tesla.com을 pool.ntp.org로 CNAME 처리한 점을 지적하며, Assetnote(현재 마케팅명 Searchlight Cyber로 언급됨)의 자산 수집이 tesla.com 하위 도메인을 그대로 수집해 pool.ntp.org의 라운드로빈 대상(자원 봉사 NTP 서버)을 테슬라 자산으로 잘못 인식했을 가능성을 제시한다. 그 결과 외부의 자발적 서버들이 테슬라 내부 자산으로 간주되어 적극적인 탐지·익스플로잇 대상이 된 사례로, CNAME과 외부 서비스가 얽힌 자산 인벤토리의 한계와 자동화 스캐닝의 부작용을 경종으로 삼는다. 작성자는 테슬라에 통보하고 비표준 응답(299)으로 주의를 환기시켰으나 트래픽은 지속되고 있어, 벤더 존 사용, 자산 범위 명확화, 스캐너의 재해석·재검증 절차 강화 등이 필요한 교훈을 제공한다.

[Hacker News에서 원문 읽기 →](https://dreamstation.systems/personal/tesla.html)

