---
title: "Putting Linux on my RTX Spark laptop because I don't have a Microsoft account"
sidebar_label: "Putting Linux on my RTX Spark laptop because I don't have a Microsoft account"
---

# Putting Linux on my RTX Spark laptop because I don't have a Microsoft account

> Hacker News · 2026-10-19 · 리눅스/하드웨어

---

ASUS ProArt P16 H7607BA‑SE033W(128GB RAM, 6,144 CUDA 코어, 2TB SSD)에서 저자가 Arch Linux ARM을 이용해 Windows 전용으로 발표된 하드웨어 지원을 리눅스로 옮긴 경험을 정리했습니다. NVIDIA의 우분투용 커널 작업을 출발점으로 삼아 ACPI 오버라이드 할당과 프레임버퍼 매핑을 고치고, hid-asus와 오디오용 머신 드라이버 패치를 적용해 콘솔·키보드·스피커 지원을 확보했습니다. 빌드 스크립트와 패치, ACPI 테이블 덤프 및 스피커 펌웨어 추출 절차를 공개했고, 입력 파일들은 해시 고정·개인 서명 패키지로 배포해 재현 가능성을 높였습니다. 설치 과정에서는 커널·NVIDIA·전원관리·펌웨어 패키지를 IgnorePkg로 묶어 하드웨어 패치를 고정하고, 일반 패키지는 Arch Linux ARM에서 계속 업데이트되도록 구성했습니다(커널 7.0.0-1022-nvidia, 드라이버 615.78.08 언급).
성능 측정은 CPU·스토리지·메모리·추론 실사용을 포괄합니다. ARM 네이티브 7-Zip 벤치에서 단일 스레드는 Windows와 거의 동일했으나 20스레드 압축·압축해제에서는 각각 약 +5%·+2.7%로 리눅스가 근소하게 앞섰습니다. 메모리 측면에서 리눅스는 OS와 CUDA에 동일하게 116.0 GiB를 보고했는데, Windows는 전용·공유·CPU 전용 영역으로 분리해 관리하고 재부팅으로 예약을 바꿔야 하는 제약이 있습니다. 실제 LLM 실사용 테스트에서는 Qwen3.8-Flash-Next-FP4-Local 체크포인트를 vLLM(B12X CUDA), 혼합 양자화·FP8 KV 캐시로 로드했을 때 모델 로딩에 약 68.2 GiB, KV 캐시에 21.1 GiB를 사용해 거의 90 GiB가 모델 관련 메모리로 할당되는 것을 관찰했습니다. 모델 컴파일 및 로딩은 첫 요청 전 약 16분이 소요되었고, 후속 응답에서는 코드리뷰(첫 토큰 0.316s, 완료 4.008s), 대규모 로그(첫 토큰 4.532s, 완료 5.768s), 추출작업(0.256s / 2.035s) 등 실사용 수준의 응답시간과 안정성(10분간 150회 반복, 응답 시간 저하 &lt;1.6%)을 보였습니다. 이러한 결과는 고용량 메모리 풀과 CUDA 접근성이 로컬 LLM 실험·튜닝에 실질적 이점을 준다는 점에서 기술적 의미가 큽니다.

[Hacker News에서 원문 읽기 →](https://josie.lol/blog/linux-rtx-spark)

