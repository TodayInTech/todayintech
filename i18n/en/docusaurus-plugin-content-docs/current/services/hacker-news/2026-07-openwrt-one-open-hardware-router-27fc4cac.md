---
title: "OpenWrt One – Open Hardware Router"
sidebar_label: "OpenWrt One – Open Hardware Router"
---

# OpenWrt One – Open Hardware Router

> Hacker News · 2026-07-06 · 네트워킹 하드웨어

---

OpenWrt One은 MediaTek Filogic 820 SoC를 중심으로 설계된 오픈 하드웨어 라우터로, Wi‑Fi 6 듀얼밴드(3×3/2×2), 2.5Gbps WAN 포트(IEEE 802.3af/at 기반 PoE 지원), 1Gbps LAN 포트, 1GB DDR4, 256MiB NAND와 16MiB 복구용 NOR, M.2 슬롯, 전면 USB‑C 직렬 콘솔 등 실무에 유용한 하드웨어를 갖추고 있습니다. 문서에는 최근(2025-10) 제조 배치에서 M.2 슬롯의 2230 위치에 고정용 포스트가 분리된 채 출하되어 제품에 고정 수단이 포함되지 않는 점을 명시해 하드웨어 호환성·조립 측면의 주의가 필요함을 알리고 있습니다. 제품의 설계 자료와 상세한 HowTo 문서는 프로젝트 사이트에서 제공됩니다.
설치와 유지보수 측면에서 문서는 출고 시 최신 OpenWrt 릴리스를 플래시해 LuCI GUI가 기본 탑재된 상태로 제공되며(단, SNAPSHOT 브랜치로 업그레이드하면 LuCI가 자동 설치되지 않음) 초기 부팅 시 NAND/NOR 스위치를 NAND로 설정하고 192.168.1.1로 접속하라고 안내합니다. 펌웨어 업그레이드는 FAT32로 포맷한 USB에 특정 파일명(openwrt‑mediatek‑filogic‑openwrt_one‑squashfs‑sysupgrade.itb)을 준비해 리셋 버튼 조작으로 수행하며, 일부 USB 드라이브 호환성 문제와 u‑boot의 usb_pgood_delay 환경변수 조정 필요성도 사례로 제시됩니다. 부팅 불능 시 NOR 복구(USB로 preloader 및 factory 이미지 플래시) 또는 UART 부트(mtk_uartboot를 통한 BL2/BL31 업로드 후 TFTP로 NOR 재플래시) 절차가 상세히 기록되어 있어, 시리얼 콘솔(전면 USB‑C, 115200bps, 8N1) 접근과 호스트 측 네트워크 설정(예: 192.168.11.23/192.168.11.0 환경), 그리고 Linux에서의 dialout/uucp 그룹 권한 부여 같은 실무적 준비 사항까지 실용적으로 다룹니다. 전반적으로 이 문서는 OpenWrt One의 하드웨어 특성, 정상 설치 흐름과 다양한 복구 옵션을 기술적으로 연결해 제시하므로 라우터 커스터마이징·펌웨어 유지보수 담당자에게 유익합니다.

[Hacker News에서 원문 읽기 →](https://openwrt.org/toh/openwrt/one)

