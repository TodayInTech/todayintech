---
title: "Prefer strict tables in SQLite"
sidebar_label: "Prefer strict tables in SQLite"
---

# Prefer strict tables in SQLite

> Hacker News · 2026-07-11 · Databases/SQLite

---

SQLite에는 CREATE TABLE 구문 끝에 STRICT를 붙여 엄격한 타입 검사를 적용하는 기능이 있으며, 작성자는 이 기능을 선호한다고 밝힙니다. STRICT 테이블은 INTEGER, REAL, TEXT, BLOB, INT, ANY 등 허용된 타입만 인정하고, INSERT나 UPDATE 시 컬럼 타입과 불일치하는 값(예: 텍스트를 INTEGER 컬럼에 넣는 시도)을 오류로 막습니다. 다만 '123'처럼 손실 없는 변환이 가능한 문자열은 받아들이므로 실사용에서 완화된 유연성도 유지합니다. 또한 잘못된 사용자 정의 타입이나 타입 미지정 컬럼 같은 표준에 맞지 않는 테이블 정의를 거부하고, ANY 타입을 쓰면 엄격 테이블 안에서도 유연성을 확보할 수 있습니다.
단점으로는 기존 비엄격 테이블을 ALTER로 직접 엄격화할 수 없어 새 테이블을 만들고 데이터를 복사·교체하는 마이그레이션이 필요하며, 이 과정에서 잘못된 데이터가 있으면 사전 정리가 요구된다고 설명합니다. STRICT는 SQLite 3.37.0(2021년 11월) 이상에서만 지원되고, 이전 버전은 STRICT 테이블이 들어있는 데이터베이스를 읽지 못할 수 있어 호환성 고려가 필요합니다. 성능상 이론적 오버헤드가 있으나 저자의 간단한 대량 삽입 실험에서는 차이가 관찰되지 않았고, 작성자는 데이터 무결성 차원에서 STRICT를 권하지만 키-값 저장소나 잡다한 속성을 담는 경우처럼 유연한 타입이 유리한 상황도 있음을 인정합니다.

[Hacker News에서 원문 읽기 →](https://evanhahn.com/prefer-strict-tables-in-sqlite/)

