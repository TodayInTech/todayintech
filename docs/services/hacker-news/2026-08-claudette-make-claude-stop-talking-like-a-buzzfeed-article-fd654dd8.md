---
title: "Claudette: Make Claude stop talking like a BuzzFeed article"
sidebar_label: "Claudette: Make Claude stop talking like a BuzzFeed article"
---

# Claudette: Make Claude stop talking like a BuzzFeed article

> Hacker News · 2026-08-21 · 생성형 AI 도구

---

Claude가 지나치게 '테드톡식'이나 클릭베이트 문체로 기술 답변을 꾸미는 문제를 해결하려는 개발자용 스킬입니다. 작성자는 Claude의 응답을 그대로 다른 모델(구글의 Gemini)에 전달해 '평범한 영어'로 재번역하는 방식을 택했고, 이 파이프라인을 /debuzz라는 Claude Code 스킬로 구현했습니다. 도구는 Claude가 스스로 문체를 고쳐버리는 것을 경계해 Gemini의 출력을 그대로 출력하도록 설계되어 있으며, 예시로는 수사적인 "로드-베어링 가정" 식의 장황한 설명이 실제로는 세 가지 버그와 구체적 수리 방안으로 단순화되는 전후 비교가 제시됩니다.
설치와 사용법도 실무적입니다. 요구사항으로 Claude Code와 npm을 통한 @google/gemini-cli 설치, GEMINI_API_KEY 설정 또는 gemini로 인증 실행이 필요하고, 깃 클론 후 nobuzz/debuzz를 ~/.claude/skills에 복사해 사용합니다. 기본 모드 colleague는 엔지니어 대상의 완전한 기술적 내용(파일 경로·코드 블록 보존)을, manager는 기술 비전문가용 요약, director는 30초 수준의 임원용 3~5문장 요약을 출력합니다. 또한 Gemini 오류(보통 인증 문제)가 발생하면 실제 오류를 보여주고 Claude의 자체 재번역은 명확하게 표기된 대체 수단으로만 제공해, 모델 체이닝으로 스타일을 교정하는 실용적 패턴과 위험을 동시에 드러냅니다.

[Hacker News에서 원문 읽기 →](https://github.com/adnanakil/nobuzz/blob/main/README.md)

