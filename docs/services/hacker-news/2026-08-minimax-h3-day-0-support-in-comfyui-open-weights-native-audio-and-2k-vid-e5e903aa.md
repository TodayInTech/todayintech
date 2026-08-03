---
title: "MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video"
sidebar_label: "MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video"
---

# MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video

> Hacker News · 2026-08-03 · AI/Generative Video

---

MiniMax H3가 오픈 웨이트로 공개되며 ComfyUI에서 출시 당일(day‑0) 네이티브 지원을 받았습니다. H3는 텍스트, 이미지, 비디오, 오디오를 통합해 최대 2K·최대 15초 클립의 비디오를 생성하고, 오디오를 후처리가 아닌 모델 출력의 일부로 실시간 스테레오로 생성하는 옴니모달 비디오 모델입니다. 프롬프트 기반 텍스트→비디오, 이미지→비디오, 시작·종료 프레임 제어, 레퍼런스(이미지·비디오·오디오)를 통한 모션·성향 전이 등 여러 작업을 하나의 모델로 처리할 수 있다는 점을 강조합니다. 글에 포함된 예시는 코믹북 스타일의 연출, 제품 광고와 하이패션 편집 영화 등 다양한 스타일과 오디오·모션 동기화를 보여주며 H3의 멀티모달 컨텍스트 이해 능력을 구체적으로 드러냅니다.
ComfyUI 측의 최적화 작업이 로컬 실행 가능성을 만든 핵심입니다. 문서는 전체 매개변수에서 약 40%를 차지하는 모듈레이션(모델의 modulation) 웨이트를 무손실로 룩업테이블로 대체해 메모리 풋프린트를 크게 줄였고, 정확하고 효율적인 int8 convrot 양자화와 커스텀 커널을 도입해 피크 VRAM 사용량을 낮췄다고 설명합니다. 결과적으로 전체 메모리 사용량을 약 66% 줄여(123.6GB → 42.5GB) RTX 3060 같은 소비자 GPU에서 2K 비디오 모델을 로컬로 실행할 수 있게 되었다고 밝힙니다. 시작하려면 ComfyUI를 0.30.0으로 업데이트하거나 Comfy Cloud를 이용하고, 제공된 워크플로우와 Hugging Face의 Comfy-Org/MiniMax-H3 모델 파일을 지정된 디렉토리에 내려받아 연결된 프레임·레퍼런스를 넣고 실행하면 됩니다. 이러한 최적화와 '오픈 웨이트' 공개는 멀티모달 생성 비디오 도구의 접근성과 실무 적용 가능성을 실질적으로 확장한다는 점에서 기술적 의미가 큽니다.

[Hacker News에서 원문 읽기 →](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)

