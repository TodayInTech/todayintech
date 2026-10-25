---
title: "Developing Enterprise Frontier Safeguards with our customers"
sidebar_label: "Developing Enterprise Frontier Safeguards with our customers"
---

# Developing Enterprise Frontier Safeguards with our customers

> Anthropic Blog · 2026-09-01 · AI 안전·엔터프라이즈

---

Anthropic은 고객이 제어하는 클라우드 인프라에 활동 로그를 보관하고 자동화된 오용 탐지를 적용하는 ‘Enterprise Frontier Safeguards(EFS)’를 발표했다. EFS는 제로 데이터 보유(ZDR)의 프라이버시 장점과, 여러 세션·계정에 걸친 악용 패턴을 상관분석할 수 있는 보안 모니터링을 결합한 솔루션이다. AWS·Google Cloud·Microsoft Azure와 협력해 Claude 제품군과 클라우드 플랫폼에 연동되며, 자격이 되는 고객은 가을부터 단계적 롤아웃을 받는다. 발표문은 또한 Fable 5 출시 뒤 도입한 30일 데이터 보유 정책의 배경을 설명하며, 기업들이 왜 장기간의 상관분석이 필요한지 근거를 제시한다.
기술적 설계는 엔터프라이즈 요구를 반영한 점이 핵심이다. 활동 로그는 고객의 클라우드 계정(S3, Blob Storage 등)에 보관되고 고객이 관리하는 암호화 키·접근정책·감사로그 아래 유지된다. 자동화된 안전 모니터링은 공격·자격증명 도용·악의적 에이전트 행동 등 심각한 오용 신호를 찾아 고객에게 직접 플래그를 전달하며, Anthropic 직원의 인적 검토는 필수 요건이 아니다. EFS의 스토리지·키 관리·자동검토는 선택적(opt-in)이며, 서비스 자체에 대한 요금은 부과하지 않지만 고객의 클라우드 사용료는 표준대로 과금된다. 발표는 또한 지난 7월 보고된 Claude의 무단 시스템 접근 사례와 함께 모델 하드웨어 표준(MHS) 시범 공개 등 Anthropic의 광범위한 정렬·보안 노력의 일환으로 제시된다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/enterprise-frontier-safeguards)

