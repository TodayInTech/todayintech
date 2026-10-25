---
title: "Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived"
sidebar_label: "Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived"
---

# Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived

> Hacker News · 2026-09-22 · legacy-dev

---

FoxDev Studio(또는 FoxScript)는 2007년에 중단된 Visual FoxPro(VFP)를 재현하겠다는 목표로 설계된 개발 환경이자 런타임입니다. 기존 프로젝트, 폼, 테이블과 같은 파일을 변환하거나 마이그레이션 없이 그대로 열고 실행하도록 하며, 폼·클래스·메뉴·리포트 편집기, 프로젝트 관리자, 명령 창과 디버거가 익숙한 위치에 통합되어 있다고 설명합니다. 핵심 철학은 동작 일치성에 두어, 작은 차이로 깨지는 오래된 애플리케이션 문제를 피하려고 Visual FoxPro 자체의 응답을 묻고 그에 맞추는 방식으로 동작을 결정한다고 밝혔습니다. 또한 편집기에서의 문법 검사와 런타임이 동일한 컴파일러·바이트코드(interpreter)를 공유하도록 만들어, 코드에서 편집기 경고와 실행 시 오류가 따로 노는 상황을 줄였습니다.
기술적 변화는 재구현된 런타임과 현대적 플랫폼 지원에 집중됩니다. 전체 제품은 64비트로 설계되어 파일 오프셋을 64비트로 처리하고, 테이블을 메모리로 통째로 읽지 않아 수백 기가바이트 단위의 .dbf도 다룰 수 있지만 이렇게 키워진 테이블은 VFP(32비트)에서 다시 열지 못하는 '일방향 문'임을 명확히 합니다. 컴파일러와 바이트코드 인터프리터는 Rust로 작성되어 WebAssembly로 컴파일되며, 실행 중인 프로그램은 섬유(fiber) 모델로 설계되어 MESSAGEBOX(), READ EVENTS 등 기존 FoxPro 이벤트 순서를 유지하면서도 UI 차단을 피한다고 설명합니다. UI는 객체 트리에서 직접 그려지며 React를 사용해 변화가 필요한 부분만 갱신하는 방식으로 성능을 끌어올렸고, 기존 32비트 .fll(라이브러리)는 별도의 32비트 보조 프로세스를 띄워 동기 호출로 연결하는 브리지를 제공해 기존 애드인과의 호환을 확보합니다. 마지막으로 HTTP 서버와 람다 같은 FoxScript 확장 기능을 통해 동일한 런타임에서 웹 요청을 처리할 수 있으며, 매 빌드에서 야간 빌드가 GitHub에 사전 배포된다고 명시되어 있어 개발 진행 상황을 직접 확인할 수 있습니다.

[Hacker News에서 원문 읽기 →](https://foxscript.org/)

