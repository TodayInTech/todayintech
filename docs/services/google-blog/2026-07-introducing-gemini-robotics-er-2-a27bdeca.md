---
title: "Introducing Gemini Robotics ER 2"
sidebar_label: "Introducing Gemini Robotics ER 2"
---

# Introducing Gemini Robotics ER 2

> Google Blog · 2026-07-30 · 로보틱스·물리 에이전트

---

구글이 발표한 Gemini Robotics ER 2는 로봇의 ‘고수준 두뇌’ 역할을 목표로 하는 최신 임베디드(reasoning) 모델로, 실제 물리 세계 속에서 인간과 상호작용하면서 동시에 사고하고 행동을 조율하도록 설계됐다. ER 2는 비전-언어-액션(VLA) 하위 제어기를 도구로 선언해 멀티모달(비디오·오디오·텍스트) 스트리밍을 직접 받아들이고, Google Search 같은 외부 도구 호출을 네이티브로 지원한다. 실시간성 확보를 위해 Gemini Live API의 양방향 스트리밍 엔드포인트와 통합해 지연에 민감한 작업에서 “멈추고 생각하는” 정지 현상을 줄였으며, Boston Dynamics의 Spot을 이용한 내비게이션·조작 오케스트레이션 데모와 코드 예제를 공개해 실무 적용 사례를 제시한다.
기술적 진전은 주로 시간적 이해와 안전성에서 드러난다. ER 2는 연속 비디오를 통한 진행도 분류에서 57.4% 정확도를 기록해 작업 진행 상황을 프레임 단위로 추적하고 실패 시 재시도를 가능하게 한다. 결정적 이벤트를 찾는 모멘트 파인딩 성능은 91.3% 정확도와 평균 절대거리 0.96초를 달성해 서브초 지연으로 물리적 전환 시점을 정확하게 판단한다는 점을 강조한다(더 큰 모델들과 유사한 정밀도를 더 적은 연산 비용과 4배 빠른 실행 속도로 제공). 또한 다중 로봇 협업 기능을 통해 서로 다른 플랫폼(예: Apptronik Apollo 2와 Franka F3 Duo)이 의미적 이해를 공유하며 작업을 분담할 수 있고, 안전 관련 벤치마크(안전 지침 준수·인접 인간 감지)에서 ER 1.6과 경쟁 모델을 능가하는 결과를 보고했다. 이러한 변화는 물리적 에이전트를 실시간으로 감독·조율하고, 더 복잡한 멀티스텝 작업을 안전하게 자동화하는 데 실용적 진전을 뜻한다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/)

