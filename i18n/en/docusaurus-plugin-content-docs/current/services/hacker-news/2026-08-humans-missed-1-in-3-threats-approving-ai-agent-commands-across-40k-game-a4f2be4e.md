---
title: "Humans missed 1 in 3 threats approving AI agent commands across 40k game runs"
sidebar_label: "Humans missed 1 in 3 threats approving AI agent commands across 40k game runs"
---

# Humans missed 1 in 3 threats approving AI agent commands across 40k game runs

> Hacker News · 2026-08-06 · 보안 · AI 에이전트

---

개발자가 AI 코드 에이전트의 명령을 승인하거나 거부하는 역할을 하는 브라우저 게임의 통계 분석에서 인간-중재는 위협을 3건 중 1건가량 놓친다는 점이 드러납니다. 제공된 데이터는 4만 회 이상의 세션과 40만 건 이상의 승인·거부 결정을 포함하며, 전체 평균 정확도는 66.3%였습니다. 세션의 32.9%는 승인한 위협으로 인해 음수 점수를 기록했고, 플레이어의 35.2%는 모든 위협을 잡았지만 그중 절반 이상은 안전한 명령을 과도하게 차단해 'Human Bottleneck' 상태를 유발했습니다. 게임이라는 점과 위협 비율(약 34%)이라는 한계는 있지만 실험은 인간의 피로와 시간 압박이 보안 판단에 미치는 영향을 명확히 보여줍니다.
세부 결과는 위험 유형별로 차이를 보입니다. 명백한 파괴적 명령(rm -rf 등)은 비교적 잘 차단되었으나 자격증명 탈취나 코드 실행을 수반하는 명령은 놓칠 확률이 더 높았습니다(노출·코드 실행 33.4%, 범위 침범 35.0%). 특히 'npm run analyze'처럼 package.json에 정의된 스크립트 뒤에 악성 페이로드를 숨기면 승인률이 높아져(해당 명령 승인률 64.7%) 히스토리 로그가 있어도 주의 깊게 읽지 않는 경향을 드러냈습니다. 반대로 정상 의도지만 자주 차단된 명령(예: 내부 레지스트리 설정 59% 차단, 빌드 출력 제거 45% 차단)은 노이즈를 키워 권한 피로를 가중시킬 수 있습니다. 저자는 이 결과를 근거로 인간-중재만으로는 불충분하다고 지적하며 샌드박싱, 자격증명 분리 등 권한 모델 설계와 실무적 완화책의 중요성을 제안합니다.

[Hacker News에서 원문 읽기 →](https://scalex.dev/blog/ai-agent-permissions-stats/)

