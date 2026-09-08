---
title: "I-have-ADHD: A skill to stop coding agents from burying the answer"
sidebar_label: "I-have-ADHD: A skill to stop coding agents from burying the answer"
---

# I-have-ADHD: A skill to stop coding agents from burying the answer

> Hacker News · 2026-09-08 · Agent UX / Developer Tools

---

이 저장소는 코딩 어시스턴트가 답을 장황하게 숨기는 대신 '액션 우선'으로 응답하도록 만드는 i-have-ADHD라는 스킬을 제안한다. 사용자는 SKILL.md에 정리된 10가지 규칙을 붙여 넣어 에이전트 동작을 바꿀 수 있는데, 규칙에는 '다음 행동을 먼저 제시', '단계에 번호 매기기', '구체적 다음 단계로 마무리', '여담 억제', '매 회차 상태 재진술', '시간 추정은 분 단위로', '목록은 최대 5개로 제한' 등 실무 대화에서 즉시 활용 가능한 지침들이 포함되어 있다. 이 규칙들은 J. Russell Ramsay와 Anthony L. Rostain의 The Adult ADHD Tool Kit을 느슨하게 토대로 삼았으나, 인간을 위한 조직법이 아니라 LLM이 어떻게 반응해야 하는지에 맞춰 조정되었다고 명시한다.
설치·사용 안내도 저장소에 포함되어 있어 CLI 프롬프트에 복사해서 쓰거나, 저장소의 AGENTS.md와 SKILL.md를 참조해 바로 적용할 수 있다. 특히 Claude 플러그인 환경에서의 동작 예시가 제공되어 있으며(업스트림 복사본 제거, 포크한 이름으로 마켓플레이스에 추가·설치, Claude Code 재시작 후 /i-have-adhd 재호출 등), MIT 라이선스로 공개되어 있어 포크와 수정이 자유롭다. 기술적 의미는 간단하지만 명확하다: 응답 형식을 규격화해 개발자 생산성과 가독성을 높이고, 에이전트 설계에서 UX 규칙을 코드로 배포할 수 있음을 보여준다는 점이다.

[Hacker News에서 원문 읽기 →](https://github.com/ayghri/i-have-adhd)

