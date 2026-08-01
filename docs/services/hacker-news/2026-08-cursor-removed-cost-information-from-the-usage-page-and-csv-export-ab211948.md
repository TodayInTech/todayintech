---
title: "Cursor removed cost information from the usage page and CSV export"
sidebar_label: "Cursor removed cost information from the usage page and CSV export"
---

# Cursor removed cost information from the usage page and CSV export

> Hacker News · 2026-08-01 · 청구·사용량 리포팅 변경

---

Cursor가 7월 말 자사 Usage 페이지와 CSV 수출물에서 달러(cost) 표시를 제거하고 토큰 기반 표기로 전환한 변경이 의도적이라는 공지가 올라왔습니다. 회사는 엔터프라이즈 플랜과 셀프서비스 플랜의 과금 구조 차이(풀링된 사용량 대 포함된 사용량)를 이유로 들며, 셀프서비스(개인·Teams 포함)는 기본적으로 토큰 수로 표시하고 실제 과금되는 온디맨드 사용분에 한해서만 비용 열에 달러를 보여주는 설계라고 설명했습니다. 다만 이 변경은 레코드를 읽을 때 적용되어 기존의 과거 사용 기록 속 달러 필드들도 0으로 바뀌었고, 일부 API 엔드포인트에서 chargedCents나 usageBasedCosts와 같은 과거 per-request 비용 필드가 모두 초기화되어 외부 보고 시스템과의 호환성에 문제가 생겼습니다.
이후 사용자들은 모델별·요청별 비용 비교와 일일 예산 추적을 할 수 없게 된 점을 강하게 문제 삼고 있습니다. 많은 사용자가 일간 그래프와 per-request 비용을 통해 모델별 성능 대비 비용을 평가해왔고, 그 데이터가 사라지면서 기존에 구축한 리포팅 파이프라인이 무력화됐다고 주장합니다. Cursor 측은 Teams 관리자용 Admin API로는 여전히 집계된 지출 데이터와 비용 필드를 제공한다고 밝혔지만, 셀프서비스 플랜에서는 모델별 달러 분해가 지원되지 않는다고 명시했습니다. 기술적으로는 기록 읽기 시점에 값이 변조되는 방식이 외부 모니터링·회계 자동화에 치명적일 수 있으므로, 제품팀의 명확한 안내나 토글식 표시 복원, 혹은 대체 API 제공이 필요해 보입니다.

[Hacker News에서 원문 읽기 →](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153)

