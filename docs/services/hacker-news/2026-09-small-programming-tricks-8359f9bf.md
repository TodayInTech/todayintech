---
title: "Small programming tricks"
sidebar_label: "Small programming tricks"
---

# Small programming tricks

> Hacker News · 2026-09-16 · 개발자 생산성

---

일상적인 엔지니어링 생산성은 종종 작은 지식의 조각들에서 나온다고 저자는 말한다. 몇 줄의 명령어와 설정으로 해결되는 문제들을 모아 소개하며, 이들 대부분은 별도의 큰 사전지식 없이도 즉시 활용할 수 있다는 점을 강조한다. 예컨대 디렉터리에서 간단한 서버를 띄우는 python3 -m http.server, 터미널 히스토리 검색을 fuzzy하게 바꿔주는 fzf나 atuin, 디렉터리별 히스토리, 그리고 git의 pickaxe(git log -S / -G)나 git checkout - 같은 빠른 복구 명령을 통해 디버깅과 탐색 비용을 크게 줄일 수 있다고 제시한다. 또한 SELECT만으로 함수를 시험해보는 방법, Postgres/MySQL의 explain analyze 사용, 정규식의 단어 경계 \b, 로그 스케일로 메트릭을 버킷화하는 방법 등 다양한 언어·도구별 팁을 구체적으로 나열한다.
저자는 현대 자바스크립트의 Array.flatMap·Object.entries·Promise.withResolvers나 Node.js에서 https.Agent를 사용해 연결을 유지함으로써 지연(latency)을 개선하는 등 성능·가독성 측면의 실질적 이득도 함께 설명한다. 파일 검색을 위해 globs(**/*.md)와 bash의 shopt -s globstar, ripgrep(rg)을 권장하고 zsh의 자동완성 활성화 스니펫도 예로 든다. 회사 내에서는 특정 문제를 해결할 데이터 소스, 담당자, 재시작 명령 등 작은 규칙들이 고레버리지로 작동하므로, 저자가 제안한 것처럼 시니어 엔지니어가 팀에 매일 한 가지 팁을 공유하는 관행은 지식 전파에 실용적일 수 있다. 제공된 예시는 범용적 유틸리티부터 환경·팀에 특화된 노하우까지 아우르며, 적은 학습 비용으로 작업 흐름을 개선할 수 있다는 점에서 기술 독자에게 직접적인 가치가 있다.

[Hacker News에서 원문 읽기 →](https://will-keleher.com/posts/small-programming-tricks-matter/)

