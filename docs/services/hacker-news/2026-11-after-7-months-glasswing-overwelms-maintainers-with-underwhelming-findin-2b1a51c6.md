---
title: "After 7 months, Glasswing overwelms maintainers with underwhelming findings"
sidebar_label: "After 7 months, Glasswing overwelms maintainers with underwhelming findings"
description: "VulnCheck 집계에 따르면 Anthropic의 Project Glasswing은 7개월 동안 **442 CVE**와 **37,966건의 발견**을 기록했으나 공개된 것은 **7,349건(19.4%)**, 수정 보고는 **217건**에 불과해 발견·수정 간 격차가 크고, OSS 스캐너 도입으로 검증 부담이 유지관리자에게 이동해 curl 사례에서는 **55.9%**의 초기 비취약 판정이 나왔습니다."
---

# After 7 months, Glasswing overwelms maintainers with underwhelming findings

> Hacker News · 2026-11-10 · 보안/오픈소스

---

VulnCheck가 7개월간 추적한 Project Glasswing의 성과는 수량적으로는 크지만 실무적 효과에서는 균열이 보입니다. 근거에 따르면 Anthropic 관련으로 기록된 **442 CVE** 가운데 실제로 악용이 확인된 것은 단 **2건(CVE-2026-61500, CVE-2026-26980)**에 불과합니다. 한편 Anthropic이 공개한 자체 장부에는 **37,966건의 발견**이 적혀 있으나, 이 중 **7,349건(19.4%)만 공개**되었고 **217건**만이 '수정됨'으로 표시되어 있습니다(근거: chunk-0001).

## 발견·공개·수정 사이의 불일치
VulnCheck는 같은 기간 중 중복·철회된 항목이 빠르게 쌓이고 있음을 지적합니다. **1,654건(4.4%)이 중복**으로 표시됐고 **419건은 철회**되었으며, 9월 이후 거의 **12,000건이 추가**됐지만 실제로 추가된 수정은 단 **15건**에 그쳤습니다. 또한 Anthropic의 장부에서 주장하는 **True Positive 비율이 90.8%에서 94.2%로 상승**한 것은 중복·철회 건수가 수정 건수보다 훨씬 많다는 사실과 상충해, 집계 방식이나 정의가 어떻게 적용되는지 의문을 남깁니다(근거: chunk-0001).

## OSS 스캐너와 검증 책임의 이동
인간의 전수 검증이 병목이 되자 Anthropic은 프로젝트가 선택적으로 쓰는 **OSS Scanner**를 공개했고, 이 도구는 "사람의 검토 없이 모델이 생성한 보고서"임을 명시합니다. 결과적으로 검증 부담은 유지관리자 쪽으로 이동했습니다. Anthropic이 밝힌 내부 숫자도 스캐너 도입 전후 상황을 보여주는데, 후보 취약점 **29,000건** 중 수동 검토는 약 **6,000건**에 불과했고 약 **5,000건**의 미검증 보고서를 유지관리자 측에 일괄 전달한 이력이 있습니다(근거: chunk-0002).

## 검증 사례 — curl의 응답
curl 유지관리자 Daniel Stenberg가 받은 배치에서 확인된 초기 결과는 실무적 부담을 분명히 드러냅니다. Anthropic이 보낸 45건 중 공개된 34건에서는 **19건이 취약점 아님으로 표시**, **6건이 저위험으로 확인**, **9건은 평가 대기** 상태였습니다. 단순 계산으로는 현재까지 **55.9%의 비취약 판정**과 **17.6%의 확인 비율(모두 저위험)**이 나오며, 이는 Anthropic 장부의 높은 True Positive 주장과 뚜렷한 차이를 보입니다(근거: chunk-0002).

## 실무적 의미
근거에 근거한 사실은 두 가지입니다. 첫째, Glasswing이 대량의 후보를 생성하는 데는 성공했지만 공개·수정·활용(악용 여부)로 이어지는 비율은 낮습니다. 둘째, 검증이 자동화 모델에만 의존되는 환경에서는 **유지관리자가 추가 물리적·시간적 비용을 부담**해야 하며, 중복과 철회가 많은 상황에서는 우선순위 결정이 흐려집니다. VulnCheck는 또한 Anthropic 장부의 'disclosed' 필터가 과대계상되는 버그 가능성을 지적해 데이터 해석 시 주의가 필요하다고 밝혔습니다(근거: chunk-0001).

이 관찰들은 AI가 취약점 발견에 유용한 도구라는 점을 부정하지는 않지만, Glasswing의 현재 운영 방식과 공개 지표는 유지관리자 대상의 실무적 부담과 데이터 투명성 문제를 낳고 있음을 보여줍니다. 독자는 VulnCheck의 집계와 curl 사례를 근거로 프로젝트 규모 대비 수리·우선순위 체계의 불일치를 염두에 두고 Glasswing 보고서를 검토해야 합니다.

[Hacker News에서 원문 읽기 →](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

