---
title: "On caring for user data: NeoVim caused Vim undo files to be deleted"
sidebar_label: "On caring for user data: NeoVim caused Vim undo files to be deleted"
---

# On caring for user data: NeoVim caused Vim undo files to be deleted

> Hacker News · 2026-09-27 · 개발 도구

---

컴퓨터 과학자 David Chisnall의 경험담을 인용한 글은, 수년간 글 작업에 Vim을 써온 사용자에게 ‘persistent undo’가 언제나 보이지 않는 안전망으로 작동해 왔음을 강조한다. 그는 몇 주 전 작업을 되돌려 과거 상태에서 내용을 복원한 사례를 들어 이 기능의 가치를 설명하고, Vim이 수십 년에 걸쳐 이 기능을 안정적으로 유지해 온 점을 신뢰의 근거로 제시한다. 반면 NeoVim을 초기에 사용해 보았을 때 undo가 작동하지 않았고, 원인은 NeoVim이 undo 파일 포맷을 바꾸면서 기존 Vim의 undo 파일을 업그레이드하지 않고 같은 이름의 파일을 감지해 삭제하고 교체해 버린 행위였다고 전한다. 문제 제기 후 프로젝트 쪽에서는 포맷이 불안정하니 사용자가 데이터 보존을 기대하면 안 된다는 답변을 받았고, 이로 인해 저자는 NeoVim에 대해 데이터 보존 의무를 지키지 않는다고 판단하게 되었다고 밝힌다.
글은 여기서 Jef Raskin의 ‘First Law’를 끌어와 맥락을 정리한다: 소프트웨어는 사용자의 작업을 해치거나 방치해 손상시켜서는 안 된다는 원칙이다. 저자는 이 사례가 단순 버그를 넘어 개발자가 온디스크 형식과 마이그레이션, 이름 충돌 처리 같은 사안에서 사용자 데이터를 어떻게 다루는지가 신뢰에 직결된다는 점을 보여준다고 해석한다. 기술적으로는 포맷 안정성·호환성 유지, 안전한 마이그레이션 전략, 사용자 파일을 임의로 삭제하지 않는 정책의 중요성을 환기시키는 사례로 읽힌다. 글쓴이는 사람들이 소프트웨어가 자신의 작업을 잃어버렸을 때 오래 기억한다는 점을 상기시키며, 도구 설계와 유지보수에서 '사용자 데이터에 대한 배려'가 실무적·윤리적 필수임을 강조한다.

[Hacker News에서 원문 읽기 →](https://unsung.aresluna.org/they-had-no-concept-of-a-duty-of-care-to-their-users/)

