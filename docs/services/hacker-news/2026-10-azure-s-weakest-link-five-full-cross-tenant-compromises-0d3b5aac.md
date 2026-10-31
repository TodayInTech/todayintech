---
title: "Azure's Weakest Link – Five Full Cross-Tenant Compromises"
sidebar_label: "Azure's Weakest Link – Five Full Cross-Tenant Compromises"
description: "블로거 swq115는 Azure API Connections의 구조적 결함을 이용해 DynamicInvoke/DynamicList와 host.api.RuntimeUrl 등으로 테넌트 간 완전 침해(키볼트·Azure SQL 포함)가 가능하며, 보고한 다섯 건의 취약점으로 총 20만 달러 보상을 받았다고 밝혔다."
---

# Azure's Weakest Link – Five Full Cross-Tenant Compromises

> Hacker News · 2026-10-30 · 클라우드 보안

---

swq115는 Azure Logic Apps의 구성요소인 **API Connections가 전 세계 다른 연결을 완전히 탈취할 수 있는 설계·구현 취약점**을 여러 방식으로 재현해 보고했다. 글은 취약 체인과 재현 페이로드, Microsoft의 패치 반응 및 한계까지 구체적으로 제시한다.

## ARM의 DynamicInvoke/프록시 경로를 통한 권한 위임

작성자는 ARM의 /extensions/proxy/ (DynamicInvoke) 경로에서 API Management(APIM)로 요청을 전달할 수 있음을 이용했다. ARM이 리소스 관리자로서 광범위 권한을 갖고 APIM에게 백엔드 토큰으로 교환하도록 동작하는 점을 악용해 다른 테넌트의 연결에 대해 피해자의 구성 토큰으로 요청을 수행했다. 예시로 Key Vault 비밀을 읽어오는 POST 요청과 응답을 본문에 제시했다:

POST /subscriptions/8e3ce52f-d45b-4347-8705-65892507465e/.../DynamicInvoke?api-version=2018-07-01-preview
Authorization: Bearer &lt;token&gt;
Content-Type: application/json
&#123;
  "request":&#123; "method":"get", "path":"path/%2e%2e/%2e%2e/%2e%2e/%2e%2e/apim/keyvault/.../secrets/victimsecret/value" &#125;
&#125;

응답은 정상적으로 비밀 값을 반환했고, 글은 이를 경로 순회(path traversal) 취약점으로 설명한다 (chunk-0001).

## DynamicList 등 다른 비문서화 엔드포인트와 차단 회피

저자는 DynamicInvoke 외에 DynamicList 등 **문서화되지 않은 4개 함수**를 발견했고 동일한 원리로 악용 가능하다고 보였다. DynamicList를 통해서는 경로 조작 후 임의 SQL 쿼리를 실행하는 페이로드가 제시되어 Azure SQL에 쓰기까지 가능함을 보여준다. Microsoft는 일부 엔드포인트를 차단하는 방식으로 대응했지만, 글쓴이는 차단만으로는 근본적 완화가 되지 않음을 지적한다 (chunk-0002).

예시 페이로드(요약):

POST /subscriptions/162fc6db-.../DynamicList?api-version=2018-07-01-preview
&#123; "dynamicInvocationDefinition": &#123; ... "seven": &#123; "value": "victimservice.database.windows.net,VictimDatabase" &#125;, "query": &#123; "value": &#123; "query": "Insert INTO MySecrets VALUES ('NewEvilSecrets', 3)" &#125; &#125; &#125; &#125;

## Consumption vs Standard Logic Apps와 host.api.RuntimeUrl 우회

핵심 발견 중 하나는 Consumption(공유 호스트) Logic Apps는 Version 1 API Connection을 생성해 암묵적으로 여러 연결에 접근할 가능성이 있다는 점이다. Standard(전용 호스트)는 각 Logic App에 관리 ID를 부여해 그 차이가 생긴다. 또한 Logic Apps의 코드 뷰에서 허용되는 host.api.RuntimeUrl 입력 파라미터를 통해 런타임 URL을 덮어쓸 수 있었고, 이때 azure-apihub.net로 끝나면 필요한 Authorization 헤더가 포함되어 동작했다. Microsoft가 RuntimeUrl에 대해 엄격한 비교 검사를 도입했으나, 검증이 경로 정규화 이전에 수행되어 우회가 가능했고 이후 패치 과정에서 원래 경로 검증이 풀려 재공격이 가능했던 사례를 제시한다 (chunk-0002, chunk-0003).

## 실무적 의미

- API Connections가 보유한 백엔드 토큰(OAuth 토큰·API 키 등)은 연결된 서비스에서 광범위 권한을 줄 수 있으므로 한 연결의 유효성 오류가 다른 테넌트의 리소스까지 직접 노출하게 된다. 글쓴이는 Key Vault, Azure SQL, Jira, Salesforce 등 다양한 백엔드 사례를 예로 들었다 (chunk-0001).
- Microsoft는 보고 후 엔드포인트 차단·경로 검증 등의 패치를 적용했지만, 글쓴이는 패치 범위와 시점 문제(검증 시점과 경로 정규화 순서 등)가 있어 우회가 가능했다고 밝혔다.
- 작성자는 이 취약성들로 총 다섯 건의 치명적 권한 상승을 보고했고, 총 보상금은 **$200,000**이며 패치가 "합리적 시간 내" 이루어졌다고 전했다 (chunk-0001, chunk-0003).

## 주의사항(근거 범위)

이 브리핑은 swq115의 기술 블로그 글(사례·페이로드·검증 화면 포함)을 바탕으로 정리했으며, Microsoft의 내부 의사결정·추가 완화 조치·현재 방어 상태 등은 본문 근거 외 추가 문서는 포함하지 않았다. 원문은 취약한 페이로드와 오류 메시지, 패치 반응을 직접 제시하므로 보안 담당자는 해당 글의 페이로드와 경로 검증 흐름을 우선 검토할 필요가 있다.


출처: swq115, "Azure's Weakest Link – Five Full Cross-Tenant Compromises" (근거: chunk-0001, chunk-0002, chunk-0003)

[Hacker News에서 원문 읽기 →](https://www.binarysecurity.no/posts/2026/10/one-root-case)

