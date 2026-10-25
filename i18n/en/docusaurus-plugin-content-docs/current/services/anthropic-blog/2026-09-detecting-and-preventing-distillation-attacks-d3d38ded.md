---
title: "Detecting and preventing distillation attacks"
sidebar_label: "Detecting and preventing distillation attacks"
---

# Detecting and preventing distillation attacks

> Anthropic Blog · 2026-09-08 · AI 보안·정책

---

Anthropic은 자사 모델 Claude의 능력을 불법적으로 추출하려는 대규모 'distillation' 캠페인을 공개하며, DeepSeek·Moonshot·MiniMax 등 세 연구소가 약 24,000개의 사기 계정을 통해 1,600만 건 이상의 교환을 생성했다고 밝혔습니다. 정당한 지식증류(distillation) 기법이지만, 경쟁사가 더 강력한 모델의 출력을 학습 데이터로 삼아 시간과 비용을 크게 단축하며 기능을 복제하는 방식으로 악용되었다는 점이 핵심입니다. 이들 캠페인은 동형의 프롬프트를 대량 반복해 추론의 체인오브소트(chain-of-thought)나 도구 사용·코딩 능력 등 Claude의 차별적 역량을 표적화했고, IP와 요청 메타데이터·인프라 지표 등을 통해 높은 신뢰도로 공격 주체를 귀속했다고 보고합니다. 특히 MiniMax의 사례에서는 1,300만 건 이상의 교환을 통해 모델 출시 전에도 추출이 진행되었고, 새 모델 출시 후 공격 트래픽을 빠르게 재조정한 정황을 제시합니다.
Anthropic은 이러한 불법 증류가 안전장치가 제거된 모델을 양산해 군사·정보·감시 용도의 악용 위험을 키우고, 수출통제로 유지하려는 경쟁 우위를 약화시킨다고 경고합니다. 방어 측면에서는 API 트래픽의 행태 분류기와 거동 지문화, 계정 검증 강화, 기술 지표 공유, 제품·모델 차원의 대응책을 병행 중이라고 밝혔습니다. 또한 상호 대응과 정책·클라우드 사업자와의 협력이 필요하다고 강조하며, 관련 사안과 연계된 과거의 무단 시스템 접근 사건 조사 및 Model Hardware Standard 연구 프리뷰 공개 등 추가적 맥락도 제시합니다. 이 보고서는 대규모 자동화된 접근과 프록시·'hydra cluster' 구조를 통해 이뤄지는 증류 공격의 전형을 실증하며, AI 연구·운영·규제의 교차점에서 시급한 공동 대응의 필요성을 시사합니다.

[Anthropic Blog에서 원문 읽기 →](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

