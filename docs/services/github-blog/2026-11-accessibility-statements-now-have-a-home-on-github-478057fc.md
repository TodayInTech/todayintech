---
title: "Accessibility statements now have a home on GitHub"
sidebar_label: "Accessibility statements now have a home on GitHub"
description: "GitHub은 저장소 개요에 ACCESSIBILITY.md를 표시하고 루트, .github/, docs/ 경로와 조직 .github/ 상속을 지원하며, 공개 저장소는 Insights > Community Standards에서 접근성 성명을 추가·제안할 수 있고 새 저장소에 접근성 이슈 라벨을 기본 포함한다고 발표했습니다."
---

# Accessibility statements now have a home on GitHub

> GitHub Blog · 2026-11-05 · 오픈소스·접근성

---

GitHub이 저장소 수준에서 **ACCESSIBILITY.md를 공식적으로 인식해 리포지터리 개요에 노출**하도록 변경했다. 이 파일은 저장소 루트, .github/ 또는 docs/ 디렉터리에서 인식되며 조직의 .github/ 리포지토리로부터 성명을 상속할 수도 있다. 공개 저장소의 유지관리는 Insights &gt; Community Standards 경로에서 간결한 스타터 문서를 이용해 접근성 성명을 추가하거나 제안할 수 있다. 또한 새 리포지터리는 접근성 관련 이슈 라벨을 기본으로 포함한다.

## 무엇이 바뀌었나: 가시성·수단·예시
- 파일 위치 인식: ACCESSIBILITY.md는 root, .github/, docs/에서 찾아 리포지터리 개요에 표시된다. 조직 단위 상속도 가능하다. 
- 신고·분류 지원: 접근성 문제를 보고하는 절차를 파일에 문서화하도록 권장하고, 새 저장소에 접근성 이슈 라벨을 기본 추가해 유지관리가 쉬워진다.
- 실무 예시: GitHub CLI의 성명은 표 출력이 화면낭독기에서 어려운 점과 대체 명령을 제안하고, GitHub Annotation Toolkit은 Figma 애노테이션의 한계를 설명하며 구조화된 텍스트 대안을 권고한다. 이들은 성명이 실제 사용·기여자 기대치를 어떻게 구체화하는지 보여준다.

## 실무적 의미와 유의점
성명은 우선 접근성 정보의 '예측 가능한 집'을 제공한다는 점에서 즉시적인 가치가 있다. 프로젝트는 우선순위·기여자 기대치·신고 경로·응답 프로세스·지원 환경·알려진 제약·소유권 등을 명시해 유지관리자가 일관되게 대응할 수 있도록 해야 한다는 GitHub의 권고가 근거다. 또한 WCAG 목표를 명시하는 것은 가능하지만, **성명 자체가 인증된 적합성(conformance)을 증명하지 않으며** 적합성 주장은 평가의 범위·일자·방법·평가자를 밝혀야 한다.

프로젝트 규모와 성격에 따라 형식은 달라져야 한다는 점도 강조된다. 작은 라이브러리와 대형 웹 애플리케이션은 서로 다른 유지보수 역량과 사용자·위험 프로필을 가지므로, GitHub이 제공하는 간단한 스타터를 기반으로 실제로 유지관리할 수 있는 내용부터 작성하고 점진적으로 보완하라는 권고가 적용된다.

이 변경은 접근성 관련 정보 탐색과 이슈 분류·추적을 간소화해 기여자와 사용자 간의 기대를 명확히 하고, 유지관리자가 접근성 문제를 체계적으로 기록·처리할 수 있는 출발점을 만든다. 다만 성명의 내용과 이행 상태는 프로젝트가 직접 업데이트·관리해야 하므로, 자동적 검증이나 보증을 제공하지 않는다는 점은 명확히 구분해야 한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/open-source/maintainers/accessibility-statements-now-have-a-home-on-github/)

