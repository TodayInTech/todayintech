---
title: "I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models"
sidebar_label: "I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models"
---

# I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models

> Hacker News · 2026-06-14 · AI/ML &amp; Video

원문 링크: [I indexed 669 GB of my GoPro videos using my M1 Max computer and local ML models](https://news.ycombinator.com/item?id=48528029)

---

피드 요약에 따르면 작성자는 M1 Max에서 오픈소스 ML 모델을 사용해 로컬로 GoPro 영상들을 인덱싱하고, 관심 장면을 검색해 바로 DaVinci Resolve 타임라인으로 보내는 워크플로를 만들었습니다. 그는 원래 2,207개의 비디오를 보유했고 그중 628개(668.68 GB, 총 재생 시간 15시간 13분 18초)를 인덱싱했다고 보고합니다.
제공된 정보만 보면 구현 상세와 성능 메트릭은 마지막 섹션의 메트릭 표에 정리되어 있다고 합니다. 개인 영상 아카이브를 로컬에서 처리하려는 개발자나 영상 편집자에게 실제 사례로 참고가 될 만합니다.

## 핵심 포인트

- M1 Max에서 로컬 오픈소스 ML 모델로 GoPro 영상 인덱싱 수행.
- 인덱싱 대상: 628개 비디오, 668.68 GB, 재생 시간 15시간 13분 18초.
- 검색한 하이라이트를 DaVinci Resolve 타임라인으로 자동 전송하는 워크플로.

## 읽어볼 만한 이유

로컬 환경에서 대용량 비디오를 처리하고 편집 파이프라인과 연계한 실제 사례입니다. 개인 데이터 보관·프라이버시와 비용 측면에서 클라우드 대체 가능성을 보여줍니다.

## 확인할 점

- 피드 기준으로는 처리 시간이나 사용한 모델 이름 같은 상세 벤치마크가 명시되지 않음 — 원문 메트릭 표 확인 필요.
- 코드·설정·재현 절차의 공개 여부는 제공된 정보만으로 확인 불가.

## 문서 정보

- 수집일: 2026-06-14T23:05:27.946119+00:00
- 후보 ID: `hacker-news:c06b50199a3c18f9`
- 후보 점수: 60.0
- 편집 상태: `published`
- 생성 방식: `llm`

