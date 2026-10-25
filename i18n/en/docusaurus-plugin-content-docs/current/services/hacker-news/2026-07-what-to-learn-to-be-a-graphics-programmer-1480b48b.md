---
title: "What to learn to be a graphics programmer"
sidebar_label: "What to learn to be a graphics programmer"
---

# What to learn to be a graphics programmer

> Hacker News · 2026-07-01 · graphics programming

---

저자는 그래픽스 프로그래머로 '고용 가능'해지려면 현대 렌더링을 CPU 쪽과 GPU 쪽 두 영역으로 나눠 학습하라고 권한다. CPU 측면에서는 DirectX12, Vulkan, Metal 같은 명시적 API와 에셋 로딩·엔진 프로그래밍 능력을, GPU 측면에서는 조명·셰이딩 수학과 그림자·AO·포스트프로세싱 등 실시간 기법, 그리고 무엇이 GPU에서 빠르고 느린지를 이해하는 역량을 강조한다. 학습 실습으로는 '첫 삼각형'부터 시작해 메쉬를 띄우고, 영화급 렌더링의 기반인 경로추적(path tracer)을 직접 구현해보라고 권하며 이를 위해 Ray Tracing in One Weekend 같은 입문서와 PBR 이론(learnopengl, Filament 문서, PBRT 책)을 차례로 참고하라고 제시한다. 또한 실무 증빙으로는 DX12/Vulkan 기반의 C++ 엔진 유사 프로젝트와 별도의 경로추적기 소스코드를 깃허브에 올려 포트폴리오로 제시하길 권한다.
수학적 기반은 선형대수(행렬, 내적·외적), 삼각법, 약간의 미적분 정도면 필수적이며, 자료구조·알고리즘의 기본도 필요하다고 적시한다. 언어 측면에서는 게임 개발에서는 C++가 표준이며 Rust는 일부 채택례가 있으나 대세는 아니고, WebGPU는 기능적으로 발전했지만 채용 수요는 아직 적다고 평가한다. 셰이더 언어로는 HLSL이 널리 쓰이고 GLSL도 사용되며 멀티플랫폼 환경에서는 트랜스파일되는 경우가 많다. 끝으로 현재 LLM(대형언어모델)에 대해서는 과대광고에 대한 회의적 시각을 보이면서도, 수학·논문·버그 검토 등 제한적 보조 도구로 활용 가치는 있다고 언급하며 페이지를 지속 갱신하겠다고 밝힌다.

[Hacker News에서 원문 읽기 →](https://blog.demofox.org/2026/07/01/what-to-learn-to-be-a-graphics-programmer/)

