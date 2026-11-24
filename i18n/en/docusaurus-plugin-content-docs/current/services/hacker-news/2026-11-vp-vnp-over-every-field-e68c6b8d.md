---
title: "VP ≠ VNP over Every Field"
sidebar_label: "VP ≠ VNP over Every Field"
description: "Anthropic 내부 연구 Claude 모델이 발견했다고 밝힌 증명은 **'VP ≠ VNP over every field'**을 주장하며 해밀토니안 순회 다항식과 영이 아닌 특징에서의 퍼머넌트에 대해 **m^(c (log m)^(1/3))** 보다 큰 게이트 하한을 제시한다. 논문과 Lean 4 형식화가 공개됐으나 인간 수학자의 검증은 이루어지지 않았습니다."
---

# VP ≠ VNP over Every Field

> Hacker News · 2026-11-23 · 이론 컴퓨터 과학

---

**AI가 생성한 형식증명·논문이 'VP ≠ VNP over every field'을 주장**

Anthropic 저장소에 올라온 연구 산출물은 **'VP ≠ VNP over every field'**라는 명제를 주장한다. 핵심 수식적 내용으로는 해밀토니안 순회 다항식과 특징(characteristic) 2가 아닌 경우의 퍼머넌트(permanent)에 대해, 모든 충분히 큰 m에 대해 회로가 **m^(c (log m)^(1/3))** 보다 많은 게이트를 필요로 한다는 하한을 제시한다. 근거 텍스트는 이 하한이 근사(approximating) 회로에도 동일하게 적용된다고 명시하며, 이로써 VP가 VNP의 진부분임과 VNP가 VP의 폐포(closure)에 포함되지 않음을 주장한다. 문서에는 동시에 "이 결과는 P vs NP 문제를 해결하지는 않는다"는 명시도 있다.

## 형식화와 검증 상태
저장소는 논문(paper.pdf)과 Lean 4 형식화(Statement.lean 등)를 포함하고 있으며, 텍스트는 이 결과가 내부 연구 Claude 모델에 의해 발견되었다고 적시한다. 다만 중요한 검증 관련 설명도 병기되어 있다: Lean이 증명들을 검사하지만 "이 파일이 주장하는 바를 기계가 곧바로 확인해주지는 않는다"고 되어 있고, 논문 부록 Q(Appendix Q)는 논문 명제들과 Lean 상응 명제들(Table 3) 사이의 차이를 목록화한다고 밝혔다. 빌드·검증 지침도 포함되어 있는데, 제공된 명령들(lake, lean 등)을 실행하면 Challenge.lean에서만 'sorry' 경고가 출력되고, 마지막 명령은 propext, Classical.choice, Quot.sound 이외의 공리가 이름으로 나오지 않아야 한다고 적혀 있다. 저장소의 CI는 comparator-check.sh를 돌려 Challenge.lean과 명제들을 비교하고, 두 번째 독립 커널(nanoda)로 재검증을 수행한다고 설명한다.

## 무엇이 바뀌고 왜 중요한가
만약 주장이 정확하고 형식화가 명시된 차이를 모두 해소하면, 이는 대수적 회로 복잡도(algebraic circuit complexity)에서 오랫동안 열린 핵심 분리 문제에 대한 중대한 전진이다. 다만 지금 공개된 근거는 모두 AI 모델이 작성·정리한 산출물이며 "어떤 인간 수학자도 증명을 검토하지 않았다"는 점이 근거 문서에 명확히 적혀 있다. 따라서 현재 상태는 "AI가 생성한 형식화된 증명 초안(및 자동 검증 절차 포함)이 공개됨"이라는 사실의 보도이지, 수학 공동체가 검증·수용한 확정적 증명 발표로 받아들여지지는 않는다.

## 실무적·학계적 영향
근거 문서만 보면 연구자들은 공개된 Lean 형식화와 부록의 대응표(Table 3)를 중심으로 사람이 읽어 검증해야 한다. 저장소 자체는 "연구 산출물(Research artifact). 관리되지 않음. 기여 불가"로 표기되어 있어 공개된 형식화·스크립트로부터 독립적인 재현·검증 작업이 필요하다. 또한 문서는 이 결과가 P vs NP 문제를 해결하지는 않는다고 분명히 밝히므로, 해당 주장은 대수적 복잡도 분리의 맥락에서 해석되어야 한다.

근거는 저장소의 README·설명 텍스트(제공된 chunk-0001)로 제한되며, 추가 인간 검증이나 동료심사, 커뮤니티의 독립적 형식검증 결과가 나오기 전까지는 주장을 잠정적으로 평가하는 관점이 필요합니다.

[Hacker News에서 원문 읽기 →](https://github.com/anthropics/formal-math/tree/main/vp-vnp)

