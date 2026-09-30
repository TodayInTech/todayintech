---
title: "Jeeves. Reasoning improves Jev-like decision models"
sidebar_label: "Jeeves. Reasoning improves Jev-like decision models"
---

# Jeeves. Reasoning improves Jev-like decision models

> Hacker News · 2026-09-29 · AI/ML

---

PostHog의 Jeeves는 Jev 스타일의 결정(classification) 모델에 '생각하기' 단계(추론 체인)를 더해 성능을 끌어올린 오픈소스 구현이다. Qwen3.5-9B를 기반으로 LoRA와 포인터 헤드를 얹고 SFT와 CISPO(강화)로 학습한 뒤, 블록-4 확산(drafter) 샘플러로 추론 체인을 생성해 결정을 내린다. 저자 측 결과에서는 학습에 쓰이지 않은 테스트에서 Jeeves가 Kev-9B와 Jev를 제치며(테스트 0.889 vs 0.822/0.857), JevBench 공개 항목들에서는 전체 0.935 vs Jev 0.866, 하드 티어에서도 0.865로 우위를 보였다. API는 Jev 호환 형식을 따르며 yes/no(noul), 선택(choice), 평점(score) 질문을 한 요청에서 병렬로 처리할 수 있고, SDK도 Jev의 타입세이프 클라이언트를 대체할 수 있도록 제공된다.
구현·운영 측면에서 현실적인 트레이드오프도 제시한다. '생각하지 않을 때' 응답은 약 0.3초, 전체 체인으로는 H100에서 중앙값 3.3초(지연의 꼬리는 p90 17초)로 느려질 수 있어 max_think·nothink_threshold로 체인 길이를 제어할 수 있다. 학습 파이프라인은 SFT(부분 미세조정)·CISPO 스케줄과 온전한 데이터 준비 스크립트, drafter 학습·추론 코드를 포함하며 CUDA(Hopper FP8) 기반의 배치/추론 최적화도 담겨 있다. 다만 체인 언어의 일관성을 보장하는 보상은 포함되지 않아 생각 텍스트의 해석 가능성은 낮고, 온도 보정과 CISPO 중단 스텝 등 보정 선택이 성능·교정(calibration)에 큰 영향을 미친다는 점이 명시되어 있어 실제 적용 시 지연·해석성·교정 사이의 균형을 따져야 한다.

[Hacker News에서 원문 읽기 →](https://github.com/PostHog/jeeves)

