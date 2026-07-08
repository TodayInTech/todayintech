---
title: "The classifiers Anthropic puts in front of Fable are too zealous"
sidebar_label: "The classifiers Anthropic puts in front of Fable are too zealous"
---

# The classifiers Anthropic puts in front of Fable are too zealous

> Hacker News · 2026-07-08 · AI 안전성

---

저자는 Anthropic의 '안전 지향' 모델 Fable이 연구용 컴퓨터과학 작업에서 사실상 쓸모가 없다고 주장한다. 초판(6월 9일)과 행정제한(6월 12일), 이후 접근 복원(7월 1일) 등의 배경을 설명한 뒤, 공개 오픈소스 도구인 RNA-seq 전사체 정량화 소프트웨어 salmon을 C++에서 Rust로 포팅하려다가 Fable이 안전 분류기로 즉시 거부했다고 전한다. 저자는 거부 사유를 묻거나 프롬프트를 재구성해도 설명을 주지 못했고, 결국 Opus 4.8로 작업을 마쳤다고 밝힌다. 일상적·무해한 질문들조차 차단되는 사례가 소셜미디어에서 보고된 점도 함께 짚는다.
더 나아가 저자는 이론적 그래프 문제(네트워크 진화의 최솟값 재구성 문제)를 수학적으로 추상화해 제시했음에도 Fable이 계속 거부했다고 적시한다. 단어·맥락을 지우고 결정문제로 바꾼 뒤에도 차단이 이어졌고, ChatGPT의 도움으로 최대한 비맥락적 진술로 재작성해도 실패했다는 점에서 분류기가 단순한 용어 필터를 넘어 과잉 차단하는 경향을 보인다고 판단한다. 기술적 의미는 명확하다: 안전 장치의 과잉 적용은 바이오인포매틱스·계산생물학·보안·일반 CS 연구자들이 모델을 평가·활용·비교하는 능력을 저해하고, 모델의 실용성·가격 대비 가치 평가를 불가능하게 만든다. 저자는 당장은 Fable을 유용하다고 보기 어렵다고 결론짓는다.

[Hacker News에서 원문 읽기 →](https://combine-lab.github.io/blog/2026/07/07/fable-is-not-a-useful-model.html)

