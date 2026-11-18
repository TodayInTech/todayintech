---
title: "Maintainers don’t need more AI bug reports. They need fixes."
sidebar_label: "Maintainers don’t need more AI bug reports. They need fixes."
description: "GitHub·Microsoft의 Codename MDASH 파일럿은 MAI Cyber 모델로 6개 오픈소스 프로젝트를 스캔해 연구자 검토 후 **99건의 사적 보고서**를 전달했고, **11월15일 기준 55건이 수정**되었으며 14건은 릴리스에 포함되었습니다."
---

# Maintainers don’t need more AI bug reports. They need fixes.

> GitHub Blog · 2026-11-17 · 오픈소스 보안

---

GitHub과 Microsoft는 AI 보안 스캔이 ‘보고의 홍수’로 유지관리자를 더 힘들게 할 수 있다는 문제에 대응해, 스캔 결과를 검증하고 곧바로 적용 가능한 수정안을 함께 전달하는 파일럿을 진행했다. 이 프로젝트의 코드명은 **Codename MDASH**이며, 시범 대상은 AutoGPT, Caddy, Express, FastMCP, ImageMagick, Netty 등 6개 널리 쓰이는 오픈소스 프로젝트였다.

## 어떻게 진행되었나
프로세스는 네 단계로 설계됐다. 먼저 Microsoft의 **MAI Cyber** 모델이 프로젝트를 스캔(Find)했다. 그 뒤 GitHub Security Lab의 AI triage 에이전트(맞춤 Copilot 스킬)가 중복 제거·유효성 확인·고임팩트 선별(Filter)을 수행했다. 이후 결과는 GitHub의 **Private Vulnerability Reporting(PVR)** 채널로 개인적으로 전달했고, 최종적으로 유지관리자가 수정(Fix)을 결정·병합했다. 수천 건의 원시 발견에서 출발해, AI 트리아지와 Microsoft FORGE Lab의 연구자 7명이 수동 검토한 뒤 **99건의 사적 보고서**가 유지관리자에게 전달됐다.

## 핵심 결과와 의미
- **11월 15일 기준 55건이 수정**되었고 그중 **14건은 릴리스에 포함**됐다. 이런 수치는 AI가 문제를 찾는 속도는 빠르지만, 실제로 서비스에 반영되는 ‘수정’은 유지관리자의 작업이 관건임을 보여준다.
- 일부 사례는 빠른 대응을 보여준다: Caddy 유지관리자는 받은 22건을 일주일 이내에 전부 수정했고, ImageMagick 팀은 특정 리포트를 받아 **15분 만에** 패치를 제출했다고 보고했다. AutoGPT 쪽은 리포트 수신 후 며칠 내에 패치를 작성해 일주일 내 프로덕션에 반영했다.
- 파일럿 운영에는 사람의 검토가 필수적이었다. 연구자 7명이 프로젝트당 약 이틀씩 수동으로 확인했다는 점에서, 현재 방식은 높은 품질을 내지만 곧바로 대규모로 확장되지는 않는다.

## 실무적 시사점
GitHub·Microsoft는 유지관리자의 부담을 줄이려면 ‘발신자(스캐너)가 먼저 검증하고 수정안까지 제공해야 한다’는 표준을 제안한다. 구체적 권고는 다음과 같다: 보고 전 각 발견을 프로젝트의 기존 지식·위협 모델·보안 정책에照합해 확인하고, 공개하지 말고 사적으로 보고하며, 가능한 경우 제안된 수정안을 포함하라. 유지관리자에게는 GitHub의 PVR 활성화와 gh-secure 설정을, 제품 개발자는 Dependabot 경보 활성화를 권장한다.

## 다음 단계와 연계 프로그램
GitHub은 이 교훈을 PVR과 보안 권고 체계에 반영하고, Microsoft는 **MAI Cyber 2**를 발표했다(파일럿은 이전 MAI Cyber 모델에서 실행). 또한 GitHub Secure Open Source Fund의 지원으로 동문 프로젝트에 대해 검증된 AI 보안 스캔과 Copilot Max 제공을 약속했다. Fund 관련 수치로는 지금까지 **216개 프로젝트**, **300명 이상의 유지관리자**, **4,000건 이상의 취약점 수정**, 월 200억회 이상 다운로드되는 소프트웨어라는 맥락이 제시되어 있다.

사실 관계(누가, 언제, 어떤 숫자 등)는 원문에 근거해 기술했다. 이 실험은 ‘AI가 단순히 발견을 나열하는 것에서 벗어나 유지관리자가 바로 적용할 수 있는 수정까지 제공할 때 실질적 보안 개선이 일어난다’는 점을 구체적 사례와 수치로 보여준다.

[GitHub Blog에서 원문 읽기 →](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/)

