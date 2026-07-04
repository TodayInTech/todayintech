---
title: "Potential session/cache leakage between workspace instances or consumer accounts"
sidebar_label: "Potential session/cache leakage between workspace instances or consumer accounts"
---

# Potential session/cache leakage between workspace instances or consumer accounts

> Hacker News · 2026-07-04 · Security / Privacy

---

한 사용자가 엔터프라이즈 ZDR 워크스페이스에 인증된 상태에서 에이전트가 갑자기 다른 사용자의 것으로 보이는 'Minecraft temple' 관련 프롬프트와 회고를 내놓았다는 GitHub 이슈를 올렸습니다. 환경 정보(darwin, 터미널: Apple_Terminal, 버전 2.1.199)와 피드백 ID가 함께 제공되어 사건이 실제 세션에서 발생했음을 보여주지만, 보고서 본문에서는 사용자의 로컬 설정(.claude 디렉토리) 때문에 대화 컨텍스트가 섞였을 가능성도 언급합니다. 작성자는 이 사례가 같은 워크스페이스 내 캐시 문제인지, 아니면 소비자(plan) 계정에서 유출된 데이터가 엔터프라이즈 쪽으로 흘러들어온 것인지 명확하지 않다고 지적합니다.
이 사건이 사실이라면 워크스페이스 격리와 캐시/세션 관리의 결함으로 인해 민감한 채팅 세션이 다른 계정이나 인스턴스에 노출될 위험이 제기됩니다. 다만 현재 근거는 단일 보고서와 사용자의 로컬 작업 방식에 관한 설명에 기반하므로 광범위한 결함으로 단정하기엔 근거가 부족합니다. 기술적으로는 세션 토큰, 캐시 경계, 에이전트의 작업 디렉토리·대화 압축(compaction) 로직 등을 우선 점검해 교차 오염 가능성을 배제해야 하며, 엔터프라이즈 고객의 관점에서는 로그·격리 정책과 재현성 검증이 필요하다는 점이 핵심적입니다.

[Hacker News에서 원문 읽기 →](https://github.com/anthropics/claude-code/issues/74066)

