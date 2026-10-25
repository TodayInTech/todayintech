---
title: "Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents"
sidebar_label: "Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents"
---

# Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents

> Hacker News · 2026-07-23 · AI 도구

---

Screenpipe는 사용자의 화면과 오디오를 로컬에만 기록해 AI 에이전트가 '본 것·말한 것·들은 것'을 검색 가능한 메모리로 활용하도록 설계된 도구다. 창작자는 Louis로, 개인적인 ‘세컨드 브레인’ 경험과 Obsidian 플러그인·Embedbase 개발 이력이 바탕이 되어 있다. 초기에는 프레임별 OCR로 접근했으나 중복 데이터와 자원 소모 문제가 커 이벤트(앱 전환, 클릭, 타이핑 멈춤, 스크롤, 유휴 등)를 감지해 의미 있는 시점의 스크린샷과 운영체제의 접근성 트리를 쌍으로 저장하는 방식으로 전환했다. OCR은 접근성 데이터가 없을 때 보조 수단으로만 사용하며, 오디오는 지속 기록해 화자 식별·전사(Parakeet/Whisper 또는 클라우드)를 지원한다.
데이터는 로컬 SQLite·mp4·때로는 md 파일로 색인되며, 포트 3030의 API를 통해 인증된 에이전트가 접근할 수 있다(기본적으로 MCP와 스킬 지원). 활용 예로 채팅 맥락 보강, 특정 시간대 작업 회수·미완료 항목 추출, 에이전트용 개인 위키 자동 구성, 방문 기반 CRM 업데이트 같은 자동화가 제시된다. 개인정보 보호를 위해 자체 PII 마스킹 모델을 로컬(Apple MLX, Windows DirectML)로 제공하고 저사양 기기를 위해 클라우드 기밀 추론 옵션도 마련했다. 대부분 코드베이스는 Rust·MLX·Onnx 기반이며 소스-가용성으로 배포되나 상업적 사용에 대해선 별도의 상업 라이선스를 적용해 지속 가능성을 확보하려는 선택을 명시한다. 이러한 설계는 데스크톱 활동을 문맥으로 삼아 에이전트를 보다 실용적으로 만드는 시도라는 점에서 기술적·운영적 함의를 갖는다.

[Hacker News에서 원문 읽기 →](https://news.ycombinator.com/item?id=49024620)

