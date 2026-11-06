---
title: "Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3"
sidebar_label: "Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3"
description: "Rivet은 S3에 데이터를 두고 메모리·실행을 경량 액터로 처리하는 오픈소스 액터 플랫폼입니다. 문서상 **액터당 72KB**, **p99 콜드스타트 4.99ms**, SQLite를 S3에 저장해 내구성을 확보하는 아키텍처를 표준 런타임(Node/Bun)으로 제공합니다."
---

# Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3

> Hacker News · 2026-11-05 · 인프라/플랫폼

---

Rivet은 에이전트·액터 워크로드를 목표로 한 오픈소스 분산 액터 플랫폼으로, 문서와 벤치마크를 통해 **액터 밀도와 콜드스타트 성능**을 핵심 차별점으로 내세웁니다. Rivet은 액터를 장수 프로세스(virtual actor)로 운영하고 상태는 메모리와 각 액터별 SQLite로 유지하되, 모든 영속 데이터는 S3(또는 S3 호환 스토리지)에 둡니다.

## 핵심 성능·구성

- **72 KB per Actor**: 액터는 별도 샌드박스 대신 노드 프로세스들 위에서 경량 인스턴스로 실행되므로 한 서버에서 수십만 개를 운용할 수 있다고 설명합니다(chunk-0001).
- **4.99 ms p99 콜드스타트**: 이미지 풀이나 VM 부팅이 없어서 지연이 매우 낮다고 명시되어 있습니다(chunk-0001, chunk-0002).
- **SQLite on S3**: 액터별 내구성 있는 SQLite DB를 S3에 백업해 재시작·이동 시 상태를 보존하며, 문서에는 p99 쓰기 1.07ms·읽기 1.36ms 등 수치와 “디스크 대비 약 10.4× 비용 우위” 주장이 포함되어 있습니다(chunk-0001, chunk-0002).

아키텍처 측면에서 Rivet은 Node.js·Bun·Rust 런타임 위에서 동작하며 컨트롤플레인은 Rust로 제공됩니다. 클러스터는 S3 버킷 하나만 외부 의존으로 삼아 노드가 제어 정보를 찾는 구조를 취하고, Docker·Kubernetes·VM·베어메탈 등 다양한 배포 옵션을 지원합니다(chunk-0002).

## 런타임·신뢰 경계와 샌드박스 전략

문서에는 "head와 hands 분리" 관점이 명확히 제시됩니다: 에이전트의 상태·메모리는 액터에 두고, 에이전트가 실제로 작성한(또는 실행할) 신뢰할 수 없는 코드는 필요할 때만 샌드박스(agentOS 등)를 통해 실행하도록 설계되어 있습니다. 따라서 샌드박스는 모든 에이전트에 항상 할당되는 것이 아니라, 요구되는 경우에만 사용합니다(chunk-0001).

## Durable Objects(Cloudflare)와의 비교

Rivet 문서는 Cloudflare Durable Objects와 비교해 몇 가지 제약을 해결했다고 명시합니다. 예컨대 메모리 캡(128MB) 제한이 없고, SQLite 크기 제한 대신 S3를 통한 ‘무제한’ 스토리지, 액터 임의 추방(eviction) 문제가 없고 표준 런타임(Node/Bun)을 구동한다고 주장합니다(chunk-0002). 이 점들은 자체 호스팅이나 BYOC(Bring Your Own Cloud) 환경을 중시하는 팀에 특히 관련성이 큽니다.

## 개발자 경험·운영 기능

문서에는 WebSocket을 통한 실시간 연결, 액터 간 호출, 스케줄링(Cron), OpenTelemetry 통합, 타입 안전한 클라이언트·React 훅, 다양한 SDK(Rust, 실험적 Python/Swift 등)를 제공한다고 적혀 있습니다. 또한 로컬 개발부터 Rivet Cloud(매니지드)·BYOC까지 동일한 컨트롤플레인을 운영할 수 있다고 설명합니다(chunk-0002, chunk-0003).

## 실무적 시사점(해석)

- 고밀도 액터 모델은 에이전트 중심 워크로드에서 샌드박스 기반 접근보다 비용·대기시간 측면에서 유리할 수 있습니다. 문서의 수치(72 KB, 4.99 ms)는 이러한 주장의 근거가 되지만, 실제 성능·비용은 앱 특성, S3 지연·요청 패턴, 샌드박스 사용 비율에 따라 달라집니다.
- 자체 호스팅·BYOC를 통해 규제·데이터 주권 요건을 맞출 수 있는 점은 엔터프라이즈 적용에서 이점이 될 수 있습니다. 다만 문서 기반 비교·벤치마크는 Rivet이 제공한 자료를 기반으로 하므로, 도입 전에는 동일 워크로드로 재현·검증하는 것이 필요합니다(chunk-0002).

## 간단한 사용 예시

다음은 문서에 실린 액터 생성·메시지 스트리밍 예시의 핵심 부분입니다(chunk-0001):

```ts
import { actor, setup } from "rivetkit";
export const agent = actor({
  db: db({ onMigrate: async (db) => { await db.execute("CREATE TABLE IF NOT EXISTS messages (role TEXT, content TEXT)"); } }),
  createVars: () => ({ online: new Map() }),
  actions: { sendMessage: async (c, text) => { await c.db.execute("INSERT INTO messages VALUES (?, ?)", "user", text); /* ... */ } }
});
```

문서는 더 많은 예제와 벤치마크 스크립트, 재현 방법을 rivet.dev/docs/benchmarking에 올려뒀다고 밝힙니다.

근거: Rivet의 기술 문서와 벤치마크(문서 내 수치와 기능 설명)를 바탕으로 작성했습니다(chunk-0001, chunk-0002, chunk-0003).

[Hacker News에서 원문 읽기 →](https://github.com/rivet-dev/rivet)

