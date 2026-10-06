---
title: "ReviewBench: An open benchmark for AI code review"
sidebar_label: "ReviewBench: An open benchmark for AI code review"
---

# ReviewBench: An open benchmark for AI code review

> GitHub Blog · 2026-10-05 · AI·ML / 벤치마크

---

GitHub이 공개한 ReviewBench는 실제 GitHub 풀 리퀘스트 분포를 반영한 오프라인 코드리뷰 벤치마크로, AI 리뷰어들의 강점·약점과 운영상 트레이드오프를 비교·평가하려는 목적을 가진다. 저자들은 1억 39만 개의 PR 분석을 바탕으로 언어·저장소 규모 분포를 유지하되 검토 품질이 중요한 중간·대형 PR 비중을 높여 총 219개 PR(187개 공개 저장소, 19개 언어)을 포함시켰다고 밝힌다. 골든셋 구축은 실제 인간 리뷰, 후속 커밋으로 추론된 이슈, 정적 분석 도구, 다수의 최신 LLM에서 제시한 후보를 모으고 의미론적 중복을 병합한 뒤 Claude Sonnet 5를 이용한 일관된 루브릭으로 검증하는 세 단계로 이뤄져 있어 다원적 근거와 편향 완화를 목표로 한다. 또한 기존의 고정 골든셋에만 의존하지 않는 '증강(augmented)' 지표를 도입해, 골든셋에 없는 유효한 지적도 개별 판정으로 인정할 수 있도록 설계했다.
검증·운영 측면에서 ReviewBench는 데이터셋·판정기·매처의 버전 관리와 공개된 검증 방법론을 통해 재현 가능성을 확보했고, 독립 심사자들이 재라벨링한 결과와 96.6%의 일치율을 보고했다. GitHub 내부에서 Copilot 코드리뷰 실험에 적용한 사례도 제시되는데, 멀티모델 앙상블 도입은 벤치마크에서 정밀도·재현율·코멘트량 상승, 비용 절감 등을 예측했고 실제 온라인 A/B에서도 addressed rate +8.0%, recall +13.6%, comment volume +61%, cost per review -8.0% 등 동일한 방향으로 이동했음을 근거로 든다. 기술적 의의는 개발팀이 프로덕션 실험에 앞서 비교적 신뢰할 수 있는 오프라인 신호로 시스템 변화를 평가하고, 심각도·카테고리·Fβ 조정으로 운영 선호에 맞춘 순위를 매길 수 있다는 점이다. 제출 절차(컨테이너·모델 키 등록, 25-PR 테스트 후 219-PR 전체 평가, 유지 관리자 검토 후 리더보드 게시)도 공개되어 연구자·실무자가 직접 반복 실험하고 개선할 수 있도록 설계되었다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/)

