---
title: "Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher"
sidebar_label: "Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher"
---

# Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher

> Hacker News · 2026-09-13 · AI·암호학

---

클로드 기반 모델 Fable 5.1이 1653년 Sir Thomas Urquhart의 미해독 암호문 'Cyphral Distich'를 스스로 풀어낸 사례가 보고되었습니다. 원문에 실린 두 줄(x32 숫자씩 총 64개)을 입력으로 받은 모델은 44분, 약 176k 토큰의 추론 끝에 핵심 실마리를 찾아냈습니다. 모델의 두 가지 주요 깨달음은(1) 암호가 저자 본문의 32개 'Proquiritation' 바로 뒤에 배치되어 있다는 점과(2) 본문과 시에서 반복되는 'wish/ desire' 같은 표현이 단서라는 점이었습니다. 이를 바탕으로 각 숫자 i를 해당하는 Proquiritation의 i번째 단어의 첫 글자로 해석하는 규칙을 적용해 'O GOD UPHOLD KING CHARLS THE SECOND...' 형태의 영문 기원문을 얻었습니다. 이 해법은 각 줄이 32자이며 운운(韻)을 맞춘다는 점에서 자체 검증력을 갖습니다.
같은 원리로 Urquhart의 더 큰 암호 'Cyphral Octastich'(285개 숫자)도 페이지 단위 색인(각 숫자 k → 책의 k번째 페이지의 단어 인덱스 → 첫 글자)을 적용해 대부분 복원했습니다. 보고서는 231/275 위치가 정확히 첫 발생(first-occurrence)과 일치하며, 남은 44자리 중 다수는 전사·하이픈·문자표기 등 실무적 사유로 ±1 오프셋이나 일부 불확실성이 있다고 밝힙니다. 저자는 해독 검증용 파이썬 스크립트와 자료 목록을 제시하고 물리적 판본 확인이 필요한 부분을 명시했습니다. 중요한 시사점은 이 해법이 고급 수학적 암호분석이 아니라 '텍스트-내부 키'를 찾는 관찰력과 지속적 탐색에서 나온다는 점입니다. 작성자는 적절한 유도(elicitation)와 탐색 제약을 통해 모델이 역사적 암호·아카이브 난제를 해결할 잠재력을 보였다고 평가하며, 일부 문자는 여전히 확인이 필요함을 분명히 하고 있습니다.

[Hacker News에서 원문 읽기 →](https://www.vals.ai/blogs/fable-solves-cyphral-distich)

