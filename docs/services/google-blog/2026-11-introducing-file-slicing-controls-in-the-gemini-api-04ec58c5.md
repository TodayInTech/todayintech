---
title: "Introducing file slicing controls in the Gemini API"
sidebar_label: "Introducing file slicing controls in the Gemini API"
description: "Google은 Gemini API에 서버사이드 파일 슬라이싱과 Microsoft Office·OpenDocument 네이티브 업로드를 추가해 파일 전체를 전부 전처리하지 않고도 페이지·셀·미디어 구간·레이어 단위로 모델에 전달해 토큰 청구를 줄일 수 있게 했습니다."
---

# Introducing file slicing controls in the Gemini API

> Google Blog · 2026-11-23 · Developer tools

---

Google은 Gemini API에 **서버사이드 파일 슬라이싱** 제어를 도입하고 Microsoft Office 및 OpenDocument 형식의 네이티브 파일 업로드를 지원한다고 발표했습니다. Google은 PDF, Office 문서(문서·슬라이드·스프레드시트), 오디오, 비디오 파일을 Files API에 업로드한 뒤 해당 URI를 재사용해 필요한 페이지만, 셀 범위만, 미디어 구간만 모델에 전달할 수 있다고 밝혔습니다. 이때 Gemini는 검사한 부분에 대해서만 토큰을 청구합니다.

## 서버사이드 슬라이싱과 URI 재사용
Google은 파일을 한 번 업로드하면 Files API의 URI를 여러 턴과 툴 호출에서 재사용할 수 있다고 설명합니다. 에이전트는 함수 응답(function_result) 안에서 직접 어떤 부분을 검사할지 지정할 수 있어 다중 턴 워크플로의 응답 속도와 효율을 높일 수 있습니다. Google은 이 방식을 통해 클라이언트 측에서 LibreOffice, PDF 렌더러, ffmpeg 같은 도구로 파일을 렌더·분할하는 부담을 줄인다고 명시했습니다.

## 지원 형식과 슬라이싱 옵션
Google은 **모든 Gemini 4 모델**에서 네이티브 파일 슬라이싱을 제공한다고 했으며, 업로드 파일에는 기존의 파일 크기·페이지 제한이 계속 적용됩니다. 문서·슬라이드(PDF·Office·OpenDocument)에서는 start_page/end_page, 해상도(low/medium/high), 레이어(page_text 또는 page_image)를 지정할 수 있습니다. 스프레드시트(.xlsx, .xls, .ods)는 sheet_index, visible_cells, 레이어(data, formulas, visuals)를 지원하고, 비디오는 start_offset/end_offset, fps, 해상도, 레이어(transcript, frames, audio)를, 오디오는 구간 자르기(start_offset, end_offset)를 지원합니다. 처리 옵션이 제공되지 않으면 문서는 레이아웃을 보존하는 페이지 이미지가 기본값이고, 스프레드시트는 평가된 값·수식·시트명이 모든 탭에 포함됩니다.

## 실무적 의미
Google의 설명에 따르면 이 기능은 두 가지 실무적 효과를 갖습니다. 첫째, '먼저 저비용으로 스킴(skimming)한 후 중요 부분만 고해상도로 읽는' 작업 흐름을 API 차원에서 지원해 불필요한 토큰 사용을 줄입니다. 둘째, 서버사이드 렌더링과 토큰화로 클라이언트 하니스(harness)의 메모리·디스크 부담을 경감하고 per-user 샌드박스 유지 비용을 낮출 수 있습니다. 원문에는 구체적 과금 구조(예: 토큰 단가 변경)는 없고 "검사한 부분만 청구"된다고만 명시되어 있으므로 과금 영향은 제공된 설명 범위 안에서 해석해야 합니다.

## 예시
원문에 포함된 Python 예시는 문서를 한 번 업로드한 뒤 저해상도 텍스트로 먼저 스킴한 뒤 동일한 URI로 특정 페이지를 고해상도로 재요청하는 흐름을 보여줍니다:

```python
from google import genai
client = genai.Client()
doc = client.files.upload(file="quarterly_report.docx")
# 1. Skim the whole document cheaply as extracted text.
skim = client.interactions.create(
    model="gemini-4-hydrogen",
    input=[
        {
            "type": "document",
            "uri": doc.uri,
            "mime_type": doc.mime_type,
            "processing": {
                "type": "static",
                "page_options": {"content_layers": ["page_text"]},
            },
        },
        { "type": "text", "text": "Which page has the revenue bridge chart?", },
    ],
)
print(skim.output_text)
# 2. Zoom into the target page at high resolution (reusing the same URI).
detail = client.interactions.create(
    model="gemini-4-neon",
    input=[
        {
            "type": "document",
            "uri": doc.uri,
            "mime_type": doc.mime_type,
            "resolution": "high",
            "processing": {
                "type": "static",
                "page_options": { "start_page": 3, "end_page": 3, "content_layers": ["page_image"], },
            },
        },
        { "type": "text", "text": "Read the revenue bridge chart and footnotes on page 3.", },
    ],
)
print(detail.output_text)
```

원문 근거만으로는 파일 크기·페이지 한도 등 기존 제한의 정확한 수치나 과금 세부항목이 제시되지 않았으므로 그 부분은 제공된 정보 범위 내에서만 해석해야 합니다.

[Google Blog에서 원문 읽기 →](https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/)

