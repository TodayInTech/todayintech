---
title: "The entire city of San Francisco as a video game"
sidebar_label: "The entire city of San Francisco as a video game"
---

# The entire city of San Francisco as a video game

> Hacker News · 2026-08-24 · interactive web/3D mapping

---

제공된 화면 텍스트에서는 ‘CLICK TO TELEPORT’, ‘NEIGHBORHOOD READY100%’, ‘The streets around you are ready’ 등 플레이어 이동과 타일 스트리밍 상태를 직접 가리키는 UI 문구들이 눈에 띕니다. WASD·마우스 룩·Space 점프·Shift 달리기 같은 조작 안내와 ‘CENTER · WAITING FOR TILE STATE’, ‘TILE STREAM IDLE’, ‘DETAIL MODE’ 같은 문구는 도시 전체를 조각(타일) 단위로 스트리밍하고 레벨오브디테일(LOD) 혹은 상세 모드를 전환하며 렌더링하는 구조를 암시합니다. 또한 ‘FILL = CURRENT OWNER’나 자원 수치(WOOD 0STONE 0METAL 0) 표기는 단순한 3D 지도가 아니라 소유권 오버레이와 게임적 요소를 결합한 인터페이스일 가능성을 시사합니다.\n\n이러한 요소들은 대규모 도시 환경을 브라우저(또는 클라이언트)에서 실시간 탐험 가능하게 만드는 기술적 난제를 드러냅니다. 타일 상태를 기다리는 흐름과 스트리밍 표시, 카메라·글라이더·차량 관련 입력은 네트워크 지연, LOD 전환, 메모리 관리, 렌더링 파이프라인 최적화 등 엔지니어링 고려사항과 직결됩니다. 다만 제공된 근거는 화면 텍스트와 조작 안내에 국한되어 있어 사용된 데이터 소스, 서버 아키텍처, 렌더링 엔진 등 내부 구현은 확인할 수 없습니다. Hacker News에서의 높은 관심(hn points 261, comments 89)은 기술적 호기심과 적용 가능성 탐색을 반영하지만, 구체적 기술 검증을 위해선 추가 정보가 필요합니다.

[Hacker News에서 원문 읽기 →](https://sf.thijs.gg/)

