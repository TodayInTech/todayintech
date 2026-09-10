---
title: "Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra"
sidebar_label: "Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra"
---

# Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra

> Hacker News · 2026-09-10 · AI 모델/제품 출시

---

Cognition은 코드 작업에 특화된 최신 모델 SWE-2를 공개했다. 공개 자료에 따르면 SWE-2는 FrontierCode 1.1 Main에서 50.0%를 기록해 Fable 5.1과 근접한 성능을 보이면서도 비용은 약 64% 절감되었다고 보고한다. 이 모델은 Kimi K33(약 2.8조 파라미터)을 기반으로 사후학습(post-training)되었고, 여러 노력 수준(reasoning-effort levels)을 단일 RL 진행에서 동시에 학습하는 새로운 RL 알고리즘을 적용해 전체 비용–성능 파레토 전선을 전진시켰다고 설명한다. 벤치마크 표에선 SWE-1.7과 Grok 4.6을 점수와 비용 측면에서 앞서며, GPT-5.6 Sol·Fable 5/5.1와 유사한 성능을 훨씬 저렴한 가격에 제공하고, GPT-6 Astra에는 근접한 성능을 더 낮은 비용으로 제시한다고 한다. 또한 Devin Desktop·CLI를 시작으로 웹과 Fusion 배포도 내세웠다.
기술적 개선점으로는 하나의 RL 실행 안에서 노력 수준별 선형 비용 페널티를 적용해 파레토 전선의 형태를 보존하면서 실제 사용자 비용을 학습에 반영한 점이 강조된다. 길이 가중 보상 기준(length-weighted reward baseline), DSpark 기반의 speculative decoding과 SpecForge로 개선된 초안(draft) 모델 학습을 도입해 롤아웃 수용 길이를 늘리고 TPM/TPS를 낮췄다. 추론 쪽에서는 NVFP4·FP8 커널과 양자화 인식 학습으로 메모리 사용을 줄이고 추론·훈련의 KL 발산을 낮췄다고 보고한다. 데이터 측면에선 RL 환경 수를 세 배로 늘리고 지시 따르기(instruction-following) 오버레이를 추가했으며, 이전 체크포인트를 활용한 반복적 검증기(hardening)로 보상 조작(reward hacking)을 방지하려 한 점이 눈에 띈다. 내부 테스트에서는 SWE-2가 더 적은 턴(예: FrontierCode에서 중간 설정 기준으로 58% 적은 턴)과 낮은 평균 비용(약 81% 절감), 그리고 첫 실제 편집까지의 중앙값이 18단계로 SWE-1.7의 48단계보다 빠른 점을 개선점으로 보고한다. 신뢰성 평가에서는 선전·검열 테스트에서 전체 통과율 98.0%(영문 99.8%, 간체 95.2%, 번체 99.1%)를 기록했고, 문맥별 취약성 평가에서는 특정 고객 프레이밍이 취약성에 통계적으로 유의미한 변화를 주지 않았다고 한다. 제공된 근거 범위에 한정해 요약했으며, 추가 세부나 외부 검증 결과는 원문을 통해 확인할 필요가 있다.

[Hacker News에서 원문 읽기 →](https://cognition.com/blog/swe-2)

