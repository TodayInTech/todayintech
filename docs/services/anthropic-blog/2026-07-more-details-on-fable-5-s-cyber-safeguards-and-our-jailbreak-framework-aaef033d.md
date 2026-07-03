---
title: "More details on Fable 5’s cyber safeguards and our jailbreak framework"
sidebar_label: "More details on Fable 5’s cyber safeguards and our jailbreak framework"
---

# More details on Fable 5’s cyber safeguards and our jailbreak framework

> Anthropic Blog · 2026-07-03 · AI 안전·사이버보안

---

Anthropic은 Fable 5의 글로벌 재배포와 함께 사이버 안전 장치에 대한 구체적 설명과 AI 탈출(jailbreak) 심각도 평가 초안을 공개했다. 사이버 분류기는 사이버 역량의 '이중 용도(dual use)' 문제를 고려해 네 가지 사용 범주(금지·고위험 이중용도·저위험 이중용도·무해 사용)로 구분해 동작하도록 설계됐다. 모든 분류기는 단독 장치가 아니라 접근 통제, 모델 안전 교육, 오프라인 모니터링 등 다층 방어의 일부로 운용되며, 이전 모델보다 더 넓은 '안전 마진'을 설정해 잠재적 유해 동작을 포착하려는 보수적 접근을 취하고 있다. 일부 사이버 연관 활동(예: 캡차 풀이, 웹 스크래핑)은 이 분류기 범위에서 제외되며, 시스템 프롬프트 노출 같은 일부 탈출 유형은 사이버 리스크로 간주하지 않음을 명시했다.
또한 회사는 AI 탈출의 위험을 정량화하기 위한 ‘Cyber Jailbreak Severity(CJS)’ 초안을 제시했다. 평가는 공격자가 새로 얻는 역량(능력 향상)과 그 역량의 범용성(유니버설리티), 실전화 난이도(무기화 용이성), 기법 입수 용이성(발견 가능성) 네 축을 합산해 로그 스케일의 0~4 수준으로 등급을 매긴다. 초기 점수는 하한으로 작용하며, 심각한 출력이나 장기간 완화가 불가능한 경우 상향 조정될 수 있다. 부록에는 Log4Shell 사례처럼 초안 규칙에 따른 가상의 채점 예시가 제시되어 있어, 기술적 위험 평가와 표준화 논의의 출발점으로 활용될 수 있다. Anthropic은 이 초안을 업계·정부와 논의하고 보안 연구자용 HackerOne 접수를 통해 실세계 발견을 받아 지속 개선하겠다고 밝혔다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework)

