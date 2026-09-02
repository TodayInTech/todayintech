---
title: "Decoding the new AI lingo: Loops, harnesses, squads, hill climbing… oh my!"
sidebar_label: "Decoding the new AI lingo: Loops, harnesses, squads, hill climbing… oh my!"
---

# Decoding the new AI lingo: Loops, harnesses, squads, hill climbing… oh my!

> GitHub Blog · 2026-09-02 · AI &amp; ML

---

최근 GitHub Podcast 에피소드에서 소개된 신조어들을 모아 설명한 글은, 단어 자체보다 그 아래 실무적 패턴을 이해하는 것이 중요하다고 강조한다. 반복 가능한 워크플로우를 설계하는 '루프 엔지니어링'은 일회성 프롬프트를 넘어서 에이전트가 일정에 맞춰 이슈를 가져오고 검증·에스컬레이션하는 식의 자동화된 순환을 만드는 관행이다. 그 변형으로 반복해서 작업을 계속하게 하는 'Ralph 루프'는 큰 작업을 계획-실행-검증의 사이클로 쪼개는 데 유용하지만, 토큰·컨텍스트·컴퓨트 비용이 커질 수 있어 루프 설계 시 스킬, 관찰성, 검증, 라우팅, 체크포인트 같은 원시 연산을 도입해 구조화하는 것이 권장된다.
여러 에이전트가 분업하는 방식도 핵심이다. '스쿼드'는 역할이 다른 에이전트들의 집단으로 계획·심사·구현·테스트·리뷰를 분담하고, '플릿'은 병렬 처리를 뜻해 전문화와 병렬화로 효율을 높일 수 있다. 모델 바깥의 도구·권한·메모리·오케스트레이션을 포함하는 '하니스'는 모델을 실제 워크플로우에 안전하게 연결하는 시스템을 말하며, GitHub Copilot이 예시로 제시된다. 성능 개선을 위한 '힐 클라이밍'은 평가(evals)를 통해 에이전트 출력을 측정하고 하니스를 조정하는 반복적 개선을 뜻한다. 마지막으로, 폐쇄형 모델·오픈 웨이트·오픈 소스 모델의 차이를 설명하며 투명성·커스터마이즈·감사 가능성 측면에서 개방성의 중요성을 짚는다. 글은 용어들이 계속 진화한다고 경고하면서도, 핵심은 반복성·검증·인간 개입 수준·모델 신뢰성·개선 방법 같은 실천적 질문에 답하는 것이라고 마무리한다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/)

