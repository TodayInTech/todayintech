---
title: "Java4Shell: RCE in OpenJDK when processing Base64"
sidebar_label: "Java4Shell: RCE in OpenJDK when processing Base64"
description: "OpenJDK의 Base64 디코더에서 메모리 손상으로 인한 원격 코드 실행 취약점 **CVE-2026-114938**이 공개됐다. CVSS 9.2, OpenJDK 17.0.6 이상 및 AVX‑512 VBMI를 지원하는 x86-64 CPU에서 영향이 확인됐다."
---

# Java4Shell: RCE in OpenJDK when processing Base64

> Hacker News · 2026-11-17 · Security

---

Calif 연구진은 OpenJDK의 Base64 디코더에서 메모리 손상으로 원격 코드 실행이 가능한 취약점 **CVE-2026-114938 (CVSS 9.2)**을 공개했다. 이 취약점(Java4Shell)은 OpenJDK의 x86-64용 고성능 Base64 인트린식 구현에서 발생하는 **패딩 처리 오류**로 인해 발생하며, 악성으로 조작된 입력이 힙 메모리를 덮어쓰고 결국 민감 정보 유출(Heartbleed류)이나 RCE로 이어질 수 있다(chunk-0001, chunk-0002).

## 취약점 원리: 인스트린식의 마스크 언더플로우
OpenJDK는 성능을 위해 AVX-512 VBMI 등 CPU 명령을 이용해 여러 바이트를 한 번에 처리한다. 취약한 코드 경로는 tail(패딩 처리)에서 출력 길이를 계산할 때 음수로 언더플로우되는 경우가 있어, 출력 마스크(output_mask)가 0xffff...(-1u64)로 설정된다. 이후 evmovdqub 같은 벡터 저장 명령이 마스크의 모든 비트를 허용으로 보고 **한 번에 64바이트를 쓰게 되어**, 실제로 할당된 버퍼(예: 50바이트)를 62바이트 넘겨 쓰게 된다(chunk-0002).

## 재현·영향과 PoC
연구진은 64개의 'A' 뒤에 '=' 한 문자(또는 오래된 OpenJDK 17에서는 128 A + '=')로 간단히 트리거할 수 있음을 보였고, 자체 PoC에서 **오프셋 50부터 111까지 총 62바이트가 덮어써지는 것**을 확인했다. PoC는 제한된 4096바이트 배열을 사용해 안전하게 트리거만 재현하며, 디코더는 입력을 거부하지만 덮어쓰기 자체는 이미 일어남을 출력한다(chunk-0004).

간단한 PoC(원문에 기재된 전체 예제에서 발췌):

```
Base64.Decoder decoder = Base64.getDecoder();
byte[] valid = "A".repeat(64).getBytes();
byte[] malformed = ("A".repeat(64) + "=").getBytes();
// ... 반복으로 인트린식 사용을 유도한 뒤 malformed로 디코드 시도
```

## 영향 범위와 전제 조건
공개 근거에 따르면 **OpenJDK 17.0.6 이상** 빌드가 영향받으며, Amazon Corretto, Eclipse Temurin, Microsoft Build of OpenJDK, Azul Zulu, BellSoft Liberica, SAP SapMachine, Red Hat OpenJDK, Oracle OpenJDK/Java SE/GraalVM 등 주요 배포판도 동일한 코드 기반이므로 영향 대상에 포함된다. 다만 이 취약점은 **하드웨어 의존적**으로, x86-64에서 AVX-512 VBMI 지원이 필요하며 ARM64 CPU는 영향을 받지 않는다. 연구진은 Intel Xeon(Ice Lake, Sapphire Rapids 등)과 AMD Zen 4 이상 EPYC/Ryzen 등에서 요구 조건을 충족한다고 적시했다(chunk-0004).

## 실운영 영향과 제약
Calif는 기본 설정 상태에서 Keycloak, Atlassian Jira·Confluence, JFrog Artifactory, Jenkins, PingFederate 등에서 사전 인증(pre-auth) RCE를 시연했고, Apache Kafka Broker, Solr, Elasticsearch, Gerrit, Spinnaker 등에서는 포스트 인증 체인도 시연했다고 밝혔다. 또한 클라이언트 측 TLS 연결만 열어도(서비스 미노출) 피해가 발생할 수 있는 클라이언트-사이드 익스플로잇 가능성도 공유되었다(chunk-0001).

중요한 제한으로는 "범용적"인 원클릭 익스플로잇은 없다는 점이다. 각 표적 애플리케이션별로 디코더 접근 경로, 쓰기/읽기 피드백 경로, 힙 레이아웃 등이 달라서 **제품별 맞춤(프로파일) 익스플로잇 체인이 필요**하다. 또한 일부 완화책은 일반적이지 않다: 예를 들어 요청 바디 버퍼링은 Elasticsearch 같은 일부 체인에선 효과가 없다고 연구진이 지적했다(chunk-0004).

## 공개와 대응 상황
Calif는 취약점과 일반적 활용 기법을 공개했으나, 각 제품별 무기화된 익스플로잇 체인은 업데이트가 배포될 때까지 비공개로 유지한다고 밝혔다. 또한 취약점 발견 및 익스플로잇 개발 과정에서 AI(코덱스 등)를 활용해 취약점 탐지·체인 구성 속도를 높였다고 설명한다(chunk-0001, chunk-0002).

근거 문서들은 취약점의 기술적 원인, PoC 재현 결과, 영향 배포판과 하드웨어 요구조건을 상세히 제시하고 있어 운영 중인 Java 런타임(특히 OpenJDK 17.0.6 이상 및 AVX‑512 VBMI 지원 CPU)을 우선적으로 점검해야 할 근거를 제공한다. 상세 패치·권고는 공급사(예: Oracle 등) 공지와 배포판별 보안 업데이트를 확인해 적용해야 한다(chunk-0004).

[Hacker News에서 원문 읽기 →](https://calif.io/java4shell/)

