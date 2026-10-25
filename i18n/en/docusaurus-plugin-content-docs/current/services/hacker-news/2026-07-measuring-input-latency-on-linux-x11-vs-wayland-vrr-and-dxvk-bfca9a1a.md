---
title: "Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK"
sidebar_label: "Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK"
---

# Measuring Input Latency on Linux: X11 vs. Wayland, VRR, and DXVK

> Hacker News · 2026-07-14 · 리눅스/입력 지연 측정

---

작성자는 직접 제작한 광센서 기반 측정 장비로 모니터에 붙인 장치의 클릭 신호와 화면 밝기 변화가 발생한 시간을 비교해 엔드투엔드 입력 지연을 측정했다. 테스트 환경은 Diabotical(DirectX11, Proton)을 사용했고, 하드웨어는 Ryzen 7 5800X3D와 RTX 4070 SUPER, QD-OLED 2560×1440/500Hz 같은 고주사율 구성이다. 비교 변수는 X11 vs Wayland, VRR(가변 주사율) 사용 여부, 그리고 dxvk-low-latency(프레임 페이서) 적용이었다. 모든 캡드 테스트는 CPU 바운드 상태를 유지하도록 설계했고, dxvk 설정과 PROTON_ENABLE_WAYLAND 같은 런처 플래그를 명시해 재현성을 높였다. 측정 분포는 대체로 정규형에 가까웠고 이상치가 적었다고 보고한다.
정량적 결과는 흥미롭다. 네이티브 Wayland는 네이티브 X11과 거의 동등했으나 XWayland는 평균 3.13ms까지 지연을 증가시켜 다른 모든 영향보다 큰 악영향을 보였다. X11이 각 시나리오에서 우세하긴 했지만 차이는 0.14~0.22ms로 미미했고, VRR은 모든 조합에서 0.26~0.45ms 빠르고 p95-p5 범위를 줄여 지터를 완화했다. dxvk-low-latency는 캡드 상황에서 약 0.10~0.29ms의 이득을, 언캡드(uncapped) 상황에서는 0.84ms의 개선과 GPU 이용률을 95~97%로 유지해 렌더 큐 빌드를 막는 효과를 보였고, XWayland 환경에서는 최대 2.11ms를 회복했다. 작성자 본인은 결과가 특정 하드웨어·소프트웨어 스택과 ‘베스트 케이스’(안정된 FPS, CPU 바운드)에 기반한다고 명시하며, 절대값은 환경에 따라 달라질 수 있지만 VRR·프레임 페이서·XWayland 회피 같은 상대적 영향은 다른 환경으로도 대체로 이전될 것이라고 판단한다. 다른 측정 사례들도 유사한 결론을 내렸음을 함께 인용해 결과의 신뢰도를 보강한다.

[Hacker News에서 원문 읽기 →](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/)

