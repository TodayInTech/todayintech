---
title: "Jamesob's guide to running SOTA LLMs locally"
sidebar_label: "Jamesob's guide to running SOTA LLMs locally"
---

# Jamesob's guide to running SOTA LLMs locally

> Hacker News · 2026-07-03 · 인프라/하드웨어

---

Jamesob의 README는 가정·소규모 랩 환경에서 '로컬 SOTA LLM'을 돌리는 현실적 설계도를 제시한다. 저자는 예산에 따른 선택지를 분명히 보여주며, 약 2천 달러로 Qwen과 좋은 STT(whisper-large-v3)를 운영할 수 있고, VRAM 중심의 접근으로 약 4만~4만6천 달러 규모의 구성(4×RTX PRO 6000, 총 384GB VRAM)까지 제안한다. 핵심 설계 결정은 '비싼 PCIe5/DDR5 대신 대용량 VRAM을 확보하고 PCIe4 스위치(c-payne 제품군)를 써서 GPU 간 P2P를 스위치 내부에서 처리'하는 점이다. 이로 인해 실측 P2P 성능은 단방향 27.5 GB/s, 양방향 50.4 GB/s, 지연 0.37–0.45 µs 수준으로 보고되며, 모델 제공을 위한 Docker 기반 러너와 로컬 ZFS 저장소, opencode를 통한 내부 서비스 구성 방법도 담겨 있다.
실무적 튜닝 항목들이 상세해 기술자 대상 의미가 크다. BIOS에서 PCIe 링크 폭을 x16으로 강제하고 Gen4로 고정, ASPM 비활성화, Re-Size BAR 활성화 등과 함께 커널 파라미터(iommu=off, amd_iommu=off, nomodeset) 및 nvidia_uvm 설정이 NCCL P2P 안정성에 중요함을 강조한다. 또한 ACS 비활성화를 위한 setpci 스크립트 및 systemd 서비스, nvidia-smi로 GPU 전력 제한(예: 350W) 적용 절차, PCI 케이블 규격 문제와 맞춤형 섀시 제작 같은 실무적 경고도 포함되어 있어, 로컬 인퍼런스 설계에서 VRAM·PCIe 토폴로지·전력 제약 간 트레이드오프를 이해하고 재현하는 데 유용한 실전 가이드를 제공한다.

[Hacker News에서 원문 읽기 →](https://github.com/jamesob/local-llm)

