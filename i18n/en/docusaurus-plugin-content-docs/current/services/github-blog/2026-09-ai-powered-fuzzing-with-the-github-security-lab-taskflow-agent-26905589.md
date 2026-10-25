---
title: "AI-powered fuzzing with the GitHub Security Lab Taskflow Agent"
sidebar_label: "AI-powered fuzzing with the GitHub Security Lab Taskflow Agent"
---

# AI-powered fuzzing with the GitHub Security Lab Taskflow Agent

> GitHub Blog · 2026-09-24 · Application security

---

GitHub Security Lab에서 만든 Fuzzing Taskflow는 LLM 기반 Taskflow Agent 프레임워크 위에 구현된 C/C++용 자율 퍼징 파이프라인으로, 저장소 슬러그만 지정하면 적절한 진입점 식별, 빌드 시스템 분석, 해네스(harness) 작성, AFL++ 실행, 커버리지 판독, 해네스 개선, 크래시 트리아지와 취약점 보고서 작성까지 사람이 상시 감시하지 않아도 일련의 작업을 순차적으로 수행하도록 설계되어 있다. 파이프라인은 세 계층(쉘 드라이버, 단계별 taskflow YAML 프롬프트, 실행용 MCP 도구)로 구성되며, 결정은 에이전트가 내리고 실제 실행은 도구가 담당하는 '판단과 실행의 분리'를 핵심 설계 원칙으로 삼는다. 각 해네스는 AFL용(.afl)과 커버리지 재생용(.cov)으로 두 번 빌드되며 상태는 SQLite 데이터베이스에 보관되어 단계 간 데이터 전달을 파일 기반으로 처리한다.
핵심 자동화는 커버리지 피드백 루프에 있다. 에이전트는 지정 시간 예산으로 AFL을 반복 실행하고 .cov 바이너리로 큐를 재생해 미도달 분기를 확인한 뒤, 시드 추가·해네스 편집·딕셔너리 보강 또는 건너뛰기 중 행동을 선택한다. 시간 예산은 반복마다 두 배로 늘리고(최대 약 32분/타깃), 두 반복 연속으로 절대 라인 커버리지가 기본 설정 1% 미만으로 개선되면 정체로 판단해 중단한다. 구조 인지(mutator) 전략으로는 포맷별 딕셔너리·커스텀 변이자, 소스레벨 토큰 추출, 커버리지 기반 동적 딕셔너리 보강, 코퍼스 스플라이스 등이 포함되며 코퍼스는 실행 간 지속되어 재발견 비용을 줄인다. 크래시 트리아지는 afl-tmin·ASan 재생·스택톱 해시 중복 제거 후 에이전트가 호출 경로를 따라 근본 원인·노출 가능성·제안 패치를 마크다운으로 생성한다(판정은 'vulnerability', 'harness_bug' 등으로 구분되며 제안 패치는 검토 필요 표시). 실시간 대시보드(포트 8765)를 통해 진행 상태와 커버리지 추세, 크래시 히트맵 등을 모니터링할 수 있고, 기본 모델은 Claude Sonnet 5로 테스팅됐다. 주의점으로는 에이전트가 호스트에서 직접 빌드·퍼징 명령을 실행하므로 코드를 실행할 때는 코드스페이스나 일회성 VM 같은 격리 환경에서만 돌려야 한다는 점이 명확히 제시되어 있다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/)

