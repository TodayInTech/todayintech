---
title: "Your alt text passes automated checks. That doesn’t mean it’s any good."
sidebar_label: "Your alt text passes automated checks. That doesn’t mean it’s any good."
---

# Your alt text passes automated checks. That doesn’t mean it’s any good.

> GitHub Blog · 2026-08-24 · 접근성

---

웹 상단 페이지의 이미지 중 16.2%가 alt 속성이 없고, 추가로 10.8%는 'alt="image"'나 파일명처럼 무의미한 설명을 쓰는 등 품질 문제가 널리 퍼져 있다는 통계에서 출발해, GitHub 접근성팀이 만든 alt 텍스트 플러그인은 이런 현실적 한계에 대응하는 실무적 설계결정을 보여준다. 저자는 우선 문자열만으로 판정 가능한 다섯 가지 결정적 규칙(빈값·파일명·플레이스홀더·매체명 단어·인접 중복)을 기본으로 두고, 과잉 탐지를 피하려는 이유로 엄격한 정확 일치 방식과 Playwright의 역할 기반 로케이터를 사용해 명시적 장식 이미지(alt="")를 제외한다고 설명한다. 인접 이미지 반복을 잡기 위해 문서 순서가 아니라 화면상의 경계상자 간격을 비교하는 레이아웃 기반 판정으로 바꾸었고, 간격 비교에서 사용하는 곱셈기(GAP_MULTIPLIER)는 경험적으로 조정하는 판단값임을 명시한다.
문자열 규칙으로 잡기 어려운 사례는 선택적 모델 검사(opt-in)를 통해 보완한다. 모델 검사 시에는 가장 가까운 제목, 페이지 제목, , 링크/버튼 여부, 주변 600자 등 문맥을 함께 전송하고, 모델에는 결정 절차와 '니트픽 방지' 지침, 구조화된 출력 양식을 적용해 일관성을 높였다. 동시에 이미지 URL·href 쿼리·프래그먼트는 마스킹하고 src/srcset은 '(omitted)'으로 교체하는 등 프라이버시·데이터 흐름을 설계했으며, 모델 호출 비용 때문에 이 규칙은 기본 비활성화·스케줄식 실행을 권장한다. 마지막으로 이 도구의 한계(alt가 아닌 계산된 접근성 이름 미검토, img 태그만 대상, 인증 뒤 이미지 재검출 실패 가능성, 제안은 초안 수준임)를 솔직히 밝히며 자동화는 사람의 판단을 보조하는 '바닥선'일 뿐이라는 실무적 조언으로 마무리한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/engineering/user-experience/your-alt-text-passes-automated-checks-that-doesnt-mean-its-any-good/)

