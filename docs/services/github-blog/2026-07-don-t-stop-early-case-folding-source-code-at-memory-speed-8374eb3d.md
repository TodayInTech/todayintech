---
title: "Don’t stop early: Case-folding source code at memory speed"
sidebar_label: "Don’t stop early: Case-folding source code at memory speed"
---

# Don’t stop early: Case-folding source code at memory speed

> GitHub Blog · 2026-07-31 · Architecture &amp; optimization

---

GitHub의 코드 검색 엔진 Blackbird는 인덱싱 대상이 되는 모든 바이트에 대해 대소문자 구별을 제거하는 'case folding'을 수행한다. 원문은 ASCII가 지배적인 소스코드 환경에서 오히려 '일찍 멈추는' 최적화(비-ASCII를 만나면 즉시 분기해 유니코드 경로로 넘기는 방식)를 제거하는 것이 훨씬 빠르다는 역발상에서 출발한다. 핵심은 루프 몸체에서 분기를 완전히 없애고, 바이트마다 상위 비트 유무를 누적해 한 번만 검사하며(A|=b), b.wrapping_sub(b'A') &lt; 26 같은 산술식으로 대문자 판정을 마스크로 만들어 비분기식으로 바로 쓴다는 점이다. 이 ASCII 경로만으로도 단일 코어에서 메모리 대역폭 수준(&gt;45 GiB/s) 성능을 달성하며, 구현은 Rust crate인 casefold로 공개되었다.
비 ASCII 처리도 성능을 포기하지 않기 위해 별도 버퍼를 한 번만 할당하고(out = 1.5× 입력 크기 + 여유), 변경이 드문 유니코드 접두부를 비트맵으로 빠르게 배제한 뒤, 페이지 기반 인덱스·누적 팝카운트·압축된 런(run) 표와 '바이트 공간' 델타 연산으로 코드 포인트를 디코딩하지 않고 변환한다. 그 결과 전체 테이블 크기는 1776바이트에 불과하고, 길이 변화(예: 2바이트→3바이트)도 바이트 단위 산술로 처리한다. 비교 측정에서는 ASCII에서 &gt;45 GiB/s, 혼합·비접힘 워크로드에서도 수 GiB/s대 또는 수백~수천 MiB/s 성능을 보여 기존 해시맵 기반 방법이나 범용 디코딩·재인코딩 방식보다 실무적으로 유리하다. 대규모 소스 코드 색인처럼 매 바이트에 이 작업을 반복 적용해야 하는 환경에서 분기 제거와 디코드-프리 바이트 연산은 실질적 성능 이득을 만든다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/architecture-optimization/dont-stop-early-case-folding-source-code-at-memory-speed/)

