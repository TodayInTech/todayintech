---
title: "We found a division by zero bug in FFmpeg with a vibecoded fuzzer"
sidebar_label: "We found a division by zero bug in FFmpeg with a vibecoded fuzzer"
---

# We found a division by zero bug in FFmpeg with a vibecoded fuzzer

> Hacker News · 2026-08-27 · Security/Vulnerability

---

Sony PS2용 VPK 데마럭서(libavformat/vpk.c)의 vpk_read_packet 함수에서 채널 수(par-&gt;ch_layout.nb_channels)를 확인하지 않고 vpk-&gt;last_block_size와 (par-&gt;block_align - vpk-&gt;last_block_size)를 나누는 코드 때문에 정수 나눗셈 0(SIGFPE) 예외가 발생한다는 보고입니다. 퍼저(https://github.com/daedalus/fuzzer/)로 만든 21바이트 입력이 유일한 demuxer 코드 경로를 밟아 항상 충돌을 일으키며, 원인은 헤더 검사 시에는 nb_channels&gt;0로 처리되었으나 커스텀 AVIO 경로에서는 프로브 시점의 값과 패킷 읽기 시점의 값이 달라져 이후에 nb_channels가 0으로 되돌아오는 시나리오입니다. 제출된 GDB 백트레이스와 크래시 헥스 덤프, 충돌 메타데이터는 문제의 결정론성과 재현성(단일 포맷 매직에 의한 자동 감지)을 뒷받침합니다.
영향도 평가는 신뢰성 높은 서비스 거부(DoS)로 정리되어 있으며 메모리 안전성 문제(범위 벗어난 읽기/쓰기, use-after-free 등)는 동반하지 않는다고 명시됩니다. 제안된 수정안은 vpk_read_packet 초기에 par-&gt;ch_layout.nb_channels == 0을 검사해 AVERROR_INVALIDDATA를 반환하는 가드 추가로, vpk_read_header에 이미 존재하는 검증과 일관되게 동작하고 충돌을 우회합니다. 함께 제시된 21바이트 회귀 테스트 벡터와 기대 반환값(-22, AVERROR_INVALIDDATA)은 패치의 유효성 확인에 유용합니다. 기술적으로는 포맷 자동 감지로 인해 손쉽게 트리거되는 얕은 깊이의 취약점이므로 FFmpeg를 라이브러리로 쓰는 응용에 있어 안정성 차원에서 우선적으로 패치 적용을 권고합니다.

[Hacker News에서 원문 읽기 →](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290)

