---
title: "60% Fable cost cut by converting code to images and having the model OCR it"
sidebar_label: "60% Fable cost cut by converting code to images and having the model OCR it"
---

# 60% Fable cost cut by converting code to images and having the model OCR it

> Hacker News · 2026-07-03 · AI/ML 툴·인프라

---

pxpipe는 길고 토큰 집약적인 시스템 프롬프트·툴 문서·과거 대화 기록을 PNG 이미지로 렌더링해 전송함으로써 입력 토큰을 크게 줄이는 로컬 프록시입니다. 이미지의 토큰 비용은 픽셀 크기로 고정되므로 코드·JSON처럼 문자당 토큰 밀도가 높은 컨텐츠는 이미지화할 때 훨씬 적은 토큰으로 표현됩니다. 실제 측정에서 약 25k 텍스트 토큰을 ≈2.7k 이미지 토큰으로 줄인 사례가 보고되며, 전체 청구서 관점에서도 샘플 스냅샷에서 ~59–70% 비용 절감(압축 요청은 ~72–74%)을 기록했습니다. 도구는 요청별로 이득이 있는 블록만 이미징하는 수익성 게이트를 두어, 드문 영문 텍스트나 최근 대화 등은 그대로 둡니다. 절차는 /v1/messages 인터셉트, 원본 바디에 대한 count_tokens 병행 조사, 그리고 결과를 ~/.pxpipe/events.jsonl에 기록해 같은 요청을 카운터팩추얼로 비교하도록 설계되어 있습니다.
기술적 한계와 운영 옵션도 상세히 제시됩니다. 핵심 제약은 비가역성: 이미지화한 내용에서 바이트 정밀도가 필요한 ID·해시·정확한 숫자 등은 오독·침묵적 위조(confabulation)를 일으킬 수 있어 보존이 필요하면 서브에이전트나 keepSharp/emitRecoverable 같은 수단으로 텍스트를 유지하도록 권장합니다. 주 대상 모델은 claude-fable-5이며 GPT 경로는 툴 정의를 JSON으로 유지해 호출 신뢰도를 보존합니다. Opus 계열은 읽기 오류가 더 커 기본 비활성화되어 있고, 렌더·OCR 품질(글리프/폰트)과 PNG 인코딩 지연이 실제 응답 지연에 일부 영향을 줍니다. 벤치마크(SWE-bench, novel-number eval 등)와 측정 방법이 포함돼 있어 기술 독자가 재현하고 비용·정확도 트레이드오프를 평가하기에 충분한 근거를 제공합니다.

[Hacker News에서 원문 읽기 →](https://github.com/teamchong/pxpipe)

