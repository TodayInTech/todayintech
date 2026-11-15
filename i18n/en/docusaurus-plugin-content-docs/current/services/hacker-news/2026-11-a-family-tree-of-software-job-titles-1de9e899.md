---
title: "A family tree of software job titles"
sidebar_label: "A family tree of software job titles"
description: "Ian Miell이 1940년대부터 현재까지 소프트웨어 직함 104개를 시간·계보별로 정리한 가족나무를 공개했습니다. 직함의 분화·재결합, ‘프롬프트 엔지니어’의 흡수, SRE·DevOps·플랫폼 엔지니어의 연결 같은 패턴을 시각적·데이터 파일로 제시합니다."
---

# A family tree of software job titles

> Hacker News · 2026-11-14 · 소프트웨어 직무·문화

---

**104개 직함을 시간 축에 배치한 ‘소프트웨어 직함 가족나무’가 공개됐다.** Ian Miell이 Mr Claude의 도움을 받아 만든 이 작업은 1940년대부터 2020년대까지 직함의 기원·계보·영향 관계를 한 장으로 보여준다. 사이트는 ianmiell.github.io/sw-job-title-family-tree이며 각 직함 설명은 JSON으로도 제공된다.

## 그래프 구조와 파일 형태

그래프는 위에서 아래로 시간이 흐르고, 다섯 년 단위 행으로 구분된다. 직함은 일곱 색 칸(Development, Analysis/Architecture/Leadership, Operations/Infrastructure, Networks/Security, Data/AI, Quality/Test, Support)으로 분류된다. 실선 화살표는 계승(자식 관계), 점선 화살표는 영향·커리어 이동을 뜻한다. 소스는 하나의 Graphviz(.dot) 파일과 설명 JSON이며, SVG로 렌더링하는 예시는 다음과 같다:

.dot

$ dot -Tsvg job_title_family_tree.dot -o job_title_family_tree.svg

직함 추가는 .dot의 노드 한 줄, 연도 행, 부모 화살표를 세 군데 고치는 것으로 설명된다.

## 눈에 띄는 관찰들(원문 정리)

- **코딩의 지위 변화:** 1947년 '계획과 코딩' 분업에서 코딩은 하위·사무적 업무로 여겨졌으나 시간이 지나면서 창의적 핵심으로 자리잡았다.
- **분열과 재결합의 반복:** 예로 웹마스터는 1993년경 등장했다가 2000년대 중반 소멸, 이후 프론트엔드·백엔드 분화 후 2008년경 '풀스택'으로 재결합했다.
- **일시적 직함의 흡수:** 2023년 주목받은 ‘프롬프트 엔지니어’는 모델 성능 향상과 함께 빠르게 AI 엔지니어 등에 흡수되는 양상을 보였다.
- **명칭의 재활용:** 'Systems Engineer'처럼 같은 명칭이 다른 시기·맥락에서 다른 역할을 가리키는 사례가 반복된다.
- **신직함의 과거 유사성:** 2025년 인기 직함인 'forward deployed engineer'는 1960년대 IBM의 시스템 엔지니어와 유사한 고객 현장 밀착형 역할로 비교된다.
- **DevOps·SRE·플랫폼의 상호관계:** Ben Treynor Sloss의 정의로 SRE가 '운영팀을 설계하는 소프트웨어 엔지니어'로 설명되며, DevOps가 문화에서 직함으로 변질된 뒤 플랫폼 엔지니어가 두 계통을 부모로 삼아 연결된다.

## 실무적 의미

이 자료는 직함의 계보를 한눈에 보여줘 직무 정의·채용 공고의 역사적 맥락을 제공한다. 특히 채용 공고나 팀 구조를 설계할 때 'DevOps', 'SRE', '플랫폼 엔지니어' 등 레이블의 중복·중첩 문제를 설명하는 근거로 활용될 수 있다. 또한 '프롬프트 엔지니어' 사례처럼 신직함이 기술 발전에 따라 기존 직무로 흡수되는 경향을 확인하면, 조직의 역할 설계·역량 전환 전략을 논의할 때 참고가 된다.

## 한계와 유의점

날짜는 **직함이 널리 쓰이기 시작한 시점에 대한 필자 추정치(c.)**이며 최초 사용 기록의 연도나 엄밀한 출처를 일일이 인용한 것은 아니다. 저자는 누락·계보 해석 오류 가능성을 열어두고 PR로 수정 제안받겠다고 밝히고 있다.

[Hacker News에서 원문 읽기 →](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/)

