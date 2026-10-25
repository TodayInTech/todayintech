---
title: "Show HN: Pulpie – Models for Cleaning the Web"
sidebar_label: "Show HN: Pulpie – Models for Cleaning the Web"
---

# Show HN: Pulpie – Models for Cleaning the Web

> Hacker News · 2026-07-06 · 데이터 전처리/추출

---

Pulpie는 HTML에서 본문을 뽑아내는 Pareto-optimal 모델 계열로, SOTA 수준의 추출 품질을 유지하면서 비용을 크게 줄이는 것을 목표로 한다. 대표 모델인 pulpie-orange-small은 WebMainBench에서 ROUGE-5 F1 0.862를 기록해 선행 추출기 Dripper(0.864)와 거의 동등한 성능을 보이면서도 파라미터 수는 210M로 Dripper(600M)의 약 1/3이다. 설계 측면에서 차별점은 디코더가 토큰을 하나씩 생성하는 방식 대신 엔코더가 블록 단위로 한 번의 포워드 패스로 각 블록을 content/boilerplate로 라벨링한다는 점이다. 이 접근은 메모리 대역폭이 병목인 디코더와 달리 계산 중심(compute-bound)이어서 저비용 GPU에서 처리량이 크게 향상된다. 실제로 L4에서 pulpie-orange-small의 처리량은 13.7 페이지/초로 Dripper의 0.68 페이지/초보다 20배 빠르며, 10억 페이지 처리 비용은 Pulpie가 약 $7,900, Dripper가 약 $159,000로 제시된다. 파이프라인은 HTML 단순화, 블록 청크화(최대 8,192 토큰), 포워드 분류, 결과 반환(HTML 또는 Markdown) 네 단계로 구성되어 긴 페이지도 청크 단위로 처리해 실패를 줄인다.
학습 데이터와 증류 과정도 상세히 공개되어 있다. Common Crawl에서 샘플링한 16,670개 페이지를 전처리해 라벨을 만들고(최종 15,880개), Dripper로 교차검증해 블록 일치도가 일정 기준(70%) 이상인 14,959개를 훈련에 사용했다. 2.1B 파라미터의 EuroBERT 기반 교사 모델은 0.873 ROUGE-5 F1을 기록했고, 이를 KL 손실(가중치 0.7)과 하드라벨 교차엔트로피(가중치 0.3), 온도 2.0으로 증류해 610M·210M 학생 모델을 얻었다. 벤치마크별 성능, 빈 추출 건수, 난이도별 F1 변화, A100·L4에서의 처리량과 비용 비교(예: A100 기준 pulpie-small 25.7 p/s, Dripper 3.6 p/s; 1B 페이지 비용 약 $29,000 vs $210,000) 등 구체적 수치가 있어 전처리·프리트레이닝 코퍼스 구축이나 런타임 컨텍스트 정제 비용을 고민하는 엔지니어에게 실무적 의미가 크다. 모든 모델과 도구는 Hugging Face에 공개되어 있어 재현과 도입이 가능하다.

[Hacker News에서 원문 읽기 →](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/)

