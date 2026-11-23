---
title: "Strengthening NATO and allied cyber defenses with AI"
sidebar_label: "Strengthening NATO and allied cyber defenses with AI"
description: "OpenAI는 Daybreak를 NATO(NCIA), ENISA, CERT-폴ska, 우크라이나 등 신뢰할 수 있는 방어자들에게 제공해 취약점 탐지·검증·수정에 적용했고, NATO는 월 최대 **3000억 토큰**을 사용했습니다. ENISA·CERT 검증 결과와 실제 패치 배포 실적이 공개되었습니다."
---

# Strengthening NATO and allied cyber defenses with AI

> OpenAI Blog · 2026-11-17 · 국제 사이버안보

---

OpenAI가 국방·공공 인프라 방어를 위해 자사 'Daybreak' 모델을 NATO와 유럽 주요 사이버 기관에 제공하고 실제 취약점 탐지·검증·수정 사례를 만들었다는 점이 이번 발표의 핵심이다. 발표에는 **NATO의 NCIA가 NATO 핵심 기관에 고급 사이버모델 접근을 제공**했고, 이 과정에서 NATO는 최대 **월 3000억(raw input/output) 토큰**을 사용했다는 구체적 수치가 포함되어 있다.

## 훈련·운영 적용: Crossed Swords 2026와 인간 감독
OpenAI는 CCDCOE가 주관한 2026년 Crossed Swords 훈련에서 Daybreak를 기술 환경에 배치해 참가자들이 AI 에이전트와 함께 에이전트를 구축·배포·평가하는 새로운 훈련 스트림을 운영했다고 밝혔다. 훈련은 AI를 보조자로 두되 **인간 감독 유지**에 중점을 둔 방식으로 설계되었다.

## EU·CERT 사례: 탐지 정확도와 패치 사례
ENISA는 Daybreak 등 최첨단 모델을 활용해 EU 기관에서 사용되는 소프트웨어의 **4건 취약점**을 식별했고, 해당 취약점들에 대한 **수정이 공개**되었다. ENISA와 CERT-EU의 공동 보고서는 27개 소프트웨어 프로젝트를 검토했고, 모델이 제시한 88건의 잠재 이슈 가운데 **95%가 실제 문제로 확인**되었다고 기록한다. 이는 AI 도구가 정책·인간 검증과 결합될 때 유의미한 탐지 보완 역할을 할 수 있음을 시사한다.

CERT Polska의 사례에서는 OpenAI 모델을 활용해 **MikroTik RouterOS의 6개 취약점**을 식별하고 벤더와 협력해 공개 조치(패치)를 조정했다. CERT Polska는 벤더의 패치가 관찰된 공격을 차단한다고 확인했다.

## 우크라이나 민간 인프라에서의 적용
우크라이나 디지털전환부는 Daybreak를 사용해 민간 인프라의 사이버 방어를 강화하고 취약점 식별·수정 속도를 높이는 데 활용하고 있다. 발표문은 이 도구가 지속적 공격 환경에서 필수 서비스를 보호하는 데 도움을 주도록 설계되었다고 설명한다.

## 실무적 의미와 한계
사실 근거: OpenAI는 여러 국가 기관과의 협업과 구체적 성과(토큰 사용량, 식별·확인된 취약점 건수, 패치 배포)를 제시하고 있다. 실무적 관점에서 해석하면, **Daybreak 같은 전방 모델은 취약점 탐색 및 가설 생성에서 시간과 노력을 절감**시킬 수 있으며, 모델 결과를 연구자가 실제 시스템에서 재현·검증하는 워크플로우가 필수적이라는 점이 반복해서 확인된다(ENISA의 95% 확인률, CERT Polska의 현장 검증). 또한 훈련·연습 환경에 AI 에이전트를 통합하는 것은 실전 운용 능력과 인간 감독 체계에 대한 검증을 촉진한다.

출처 기반 사실과 해석을 구분하면, 토큰 사용량·취약점 건수·패치 배포 등은 OpenAI가 제시한 사실이며, 이들 사례가 의미하는 바(분석 가속화·인간 검증의 필요성 등)는 기사에서 합리적 해석으로 제시했다. 추가 기술적 세부(예: 모델 구성, 내부 보안 통제, 접근·승인 절차)는 원문에 자세히 나오지 않아 본문에 포함하지 않았다.

[OpenAI Blog에서 원문 읽기 →](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)

