---
title: "GPT-6 Astra Solves a WWI German Radio Cipher"
sidebar_label: "GPT-6 Astra Solves a WWI German Radio Cipher"
---

# GPT-6 Astra Solves a WWI German Radio Cipher

> Hacker News · 2026-09-19 · AI·암호해독

---

한 1차 세계대전 독일 무선 암호문이 대형 언어모델 GPT-6 Astra에 의해 해독되었다는 보고가 공개됐다. 원문은 ADFGVX 방식으로 암호화된 1918년 11월 27일자 전신으로, 기사에는 전통적인 ADFGVX 테이블 예시(키 ‘HOUSE’)와 함께 실제 해독에 사용된 절차가 설명되어 있다. Astra는 암호 키로 ‘TRUPPENVERSCHIEBUNG’을 사용해 열의 알파벳 순서로 재배열하고, 19열 단위로 메시지를 가로로 적은 뒤 열 길이가 다른 칸을 고려해 열별 위치를 계산하는 전형적인 전치(열열기) 작업을 수행해 복호화를 진행했다. 그 결과 제시된 독일어 평문은 “EIN ENGLISCHER KREUZER … SEWASTOPOL … EIN GESCHWADER … FOLGT 26STEN”으로 해석되며, 기사에선 영어 번역(세바스토폴에 도착한 영국 순양함과 연합 함대의 추후 도착)을 함께 제시한다.
흥미로운 점은 Astra가 단순히 표 기반 복호를 끝낸 뒤 관련 역사 기록으로 스스로 교차검증을 했다는 점이다. 모델은 HMS Canterbury의 일지에서 1918년 11월 24일 세바스토폴 도착과 11월 26일 연합 함대의 도착을 확인했다고 보고했다. 다만 논문 인용을 통해 이 암호문이 기존에 알려진 복호 키 목록과 시기상 불일치(‘TRUPPENVERSCHIEBUNG’ 키는 12월 9일부터 사용된 것으로 기록되어 있음)가 존재함을 지적하며, 왜 이 키가 해당 전신에 적용됐는지는 불명이라고 밝힌다. 기술적으로 이번 사례는 고전 암호(ADFGVX) 해독 절차를 모형화하고 역사적 기록과 대조해 가설을 검증한 언어모델의 활용 가능성을 보여주지만, 키 사용 시기 불일치 등 남은 불확실성도 분명히 제시하고 있어 추가 역사·암호학적 검증이 필요함을 시사한다.

[Hacker News에서 원문 읽기 →](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio)

