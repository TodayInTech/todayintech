---
title: "Apple’s grey list: Words and phrases your iPhone won’t help you spell"
sidebar_label: "Apple’s grey list: Words and phrases your iPhone won’t help you spell"
description: "독립 연구자 데릭 카프먼이 iOS 운영체제 내에 하드코딩된 **10만개 이상 분량의 '그레이리스트'**를 찾아내 스와이프·예측완성에서 약물, 성적 표현과 일부 정치적 문구(예: \"Trayvon Martin\", \"Kashmir dispute\") 등이 자동완성되지 않는다고 보고했다. 애플은 부적절한 제안을 피하도록 설계했다고 밝혔다."
---

# Apple’s grey list: Words and phrases your iPhone won’t help you spell

> Hacker News · 2026-11-07 · 모바일 OS · 콘텐츠 필터링

---

애플의 키보드 예측완성이 특정 단어·구문을 자동완성하지 않도록 제한하는 내부 목록이 존재한다는 발견이 나왔다. 독립 연구자 데릭 카프먼은 iOS 내부에 인코딩된 표에서 **100,000개가 넘는 단어·구문(‘그레이리스트’)**을 확인했고, 이 때문에 스와이프 입력이나 예측완성으로 일부 표현을 입력할 수 없거나 오탐이 발생한다고 밝혔다.

## 발견된 항목과 즉각적 영향
카프먼이 공개한 예시에는 "Dictator Trump", "NSA spies" 같은 표현뿐 아니라 "Australia is a very bad place", "question your sexuality", "on MDMA" 같은 문장 단위 항목도 포함된다. 정치·사회적으로 민감한 표현도 포함돼 있어 "Trayvon Martin", "Kashmir dispute", "Muslim extremist", "male chauvinist pig" 등이 자동완성에서 제외된다. 언어별 사례로는 히브리어에서 "the occupied territories", 아랍어에서 "the Hamas movement"가 포함됐다. 그 결과 스와이프 입력 시 문장이 다른 단어로 잘못 완성되기도 한다(예: "United Ireland" → "United Iceland", "Tibetan independence" → "Tibetan independences").

## 기술적 배경: 하드코딩 표와 최근의 변환기 기반 교정
기사는 이 목록이 운영체제에 하드코딩된 표 형태로 포함돼 있다고 설명한다. 전통적으로 자동완성은 n-그램 등 통계 기반으로 작동해왔고, 애플은 지난해 **변환기(transformer)-기반** 교정 시스템을 도입한 바 있다. 이번 그레이리스트는 이 새로운 시스템과 병행해 작동하면서 특정 항목의 제안을 의도적으로 억제하는 역할을 하는 것으로 보인다.

## 애플의 설명과 사용자 영향
애플은 키보드를 '부적절하거나 공격적인 예측 제안을 제공하지 않도록 설계'했다고 밝혔다. 다만 사용자가 특정 단어나 구문을 직접 타이핑하거나 예측 제안을 무시하고 덮어쓸 수는 있다고 애플은 덧붙였다. 기사에는 또 과거 음성 받아쓰기에서 특정 발화가 다른 단어(예: "racist"를 말했을 때 "Trump"가 나타난 사례)로 잘못 표출된 짧은 결함이 있었고, 애플이 이를 신속히 수정했다고 전한다.

## 의미와 실무적 관점
근거에 따르면 이 변화는 키보드의 '보호적 필터링'이 운영체제 수준에서 광범위하게 적용되는 사례를 보여준다. 기술적으로는 하드코딩된 차단표가 예측 모델의 출력을 제한하는 역할을 하며, 사용자는 스와이프 입력 정확도 저하나 의도치 않은 대체어를 경험할 수 있다. 정치적·언어적 민감어가 포함된 점은 콘텐츠 검열·표현 차단 관점에서 논의를 촉발할 수 있다는 것이 기사 내용의 해석이다(해석은 카프먼의 표현인 "light-touch form of censorship"를 인용한 분석에 근거함).

제공된 정보만 보면 이 목록의 전체 항목, 적용 기준, 지역별 차별 적용 여부 등은 공개되지 않았다. 사용자 관점에서는 원하는 표현을 직접 입력하거나 예측 제안을 무시하여 의도를 달성할 수 있다는 애플의 지적이 실무적 대안으로 제시된다.

[Hacker News에서 원문 읽기 →](https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you)

