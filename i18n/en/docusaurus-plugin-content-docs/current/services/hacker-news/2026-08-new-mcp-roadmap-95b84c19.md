---
title: "New MCP Roadmap"
sidebar_label: "New MCP Roadmap"
---

# New MCP Roadmap

> Hacker News · 2026-08-22 · 프로토콜/오픈스탠다드

---

Model Context Protocol(MCP)가 다음 명세 릴리스와 이후 작업을 정리한 업데이트 로드맵을 공개했다. 로드맵은 핵심 유지관리자와 커뮤니티 작업 그룹이 함께 수립한 다섯 가지 우선 영역으로 구성되며, 이전 로드맵에서 예고된 서버-발신 이벤트, 결과 타입 개선, 에이전트 신원 등의 과제가 이제 우선순위로 승격되었다고 밝힌다. 기술적으로 눈에 띄는 변화로는 에이전트형 워크로드를 지원하는 메시징 원시(primitives)의 강화가 있다. 장기 루프, 스트리밍 결과, 중간 조정 필요성에 대응하기 위해 Tasks, subscriptions/listen, 진행 알림과 같은 확장(예: SEP-2663)과 서버-발신 이벤트(웹훅·채널) 통합, 그리고 Agents·Transports·Triggers &amp; Events 그룹 간의 조합 검토가 예정되어 있다는 점이 강조된다.
전송 계층 측면에서는 2026-07-28 릴리스로 원격 MCP 서버를 일반 HTTP 워크로드와 동일하게 다루게 되어 호스팅·운영이 쉬워졌다고 설명한다. 여기에 더해 로컬 배포 모드(예: stdio 상의 Streamable HTTP)까지 확장해 단일 전송으로 통일하는 방향을 제시한다. 보안과 인증 부분은 대화형 브라우저 승인 중심에서 벗어나 클라우드에서 동작하는 에이전트 신원을 표준 방식으로 인식·위임할 필요를 짚으며, DPoP 채택, Workload Identity Federation, ID-JAG 기반의 Enterprise-Managed Authorization, 표준 토큰 교환 및 IETF OAuth·WIMSE 등 표준화 기구와의 협업을 통해 이를 추진하겠다고 밝혔다. 또한 도구 호출 결과의 형태가 중복되는 문제를 하나의 명확한 계약으로 표준화하고, 수백 개 도구를 가진 서버가 초기 연결 시 전체 표면을 노출하지 않도록 점진적 디스커버리 전략을 추진하겠다고 적시한다. SDK의 사용성·명세 준수·문서화 개선에 투자하고, 우선 영역에 속하는 SEP는 심사가 가속화된다는 점을 안내하며 기여 방법(워킹 그룹 참여, SEP 제안·코멘트, SEP-2133을 통한 실험적 확장 등)도 함께 제시한다.

[Hacker News에서 원문 읽기 →](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)

