---
title: "Total Annihilation, rebuilt for modern computers"
sidebar_label: "Total Annihilation, rebuilt for modern computers"
---

# Total Annihilation, rebuilt for modern computers

> Hacker News · 2026-10-11 · 게임 엔진·오픈소스

---

Nanolathe는 클래식 실시간전략 게임 Total Annihilation을 대상으로 한 클린룸 재구현 오픈소스 엔진으로, 코드가 MIT 라이선스로 공개되어 연구·수정·확장이 가능하다고 소개합니다. 웹 브라우저(Chrome·Edge·Safari)에서 시험해볼 수 있는 세 개의 데모 미션을 제공하며, 별도 설치된 원본 게임 파일(예: GOG·Steam·CD)을 가져오면 전체 캠페인·스커미시·온라인 플레이까지 지원하는 네이티브 베타로 확장할 수 있습니다. 원본과 동일한 장면을 현대적 GPU 렌더링(라이트·글로우·슈퍼샘플링)으로 재현하거나 클래식 룩으로 전환할 수 있고, 비교 드래그 뷰와 캡처(엔진 커밋 617540c5 기준) 설명을 통해 렌더러 경로와 타일 캐시 처리 방식 같은 구현 세부를 보여줍니다.
기술적으로 주목할 부분은 문서화된 게임 포맷과 엔진 설계, 그리고 원본 32×32 타일을 합성해 실질적 64×64 타일을 생성하거나 트리 스프라이트를 2× 합성하는 등 자산 처리와 렌더러 파이프라인을 명확히 밝힌 점입니다. 멀티플레이는 데스크톱 브라우저와 설치본 간 상호 접속을 지원하며 스커미시·서바이벌 전투를 녹화(replay)하는 기능도 포함되어 있어 재현성·분석에 유리합니다. 아직 베타 단계라 일부 버그와 호환성 변동, 세이브 호환성 정교화가 필요하다고 명시되어 있어 연구·모딩 목적의 접근과 실사용 병행 시 유의할 필요가 있습니다.

[Hacker News에서 원문 읽기 →](https://nanolathe.gg/)

