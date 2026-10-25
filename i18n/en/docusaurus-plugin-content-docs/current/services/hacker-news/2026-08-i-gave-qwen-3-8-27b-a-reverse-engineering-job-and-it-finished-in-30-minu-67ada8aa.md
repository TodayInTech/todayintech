---
title: "I gave Qwen 3.8 27B a reverse-engineering job and it finished in 30 minutes"
sidebar_label: "I gave Qwen 3.8 27B a reverse-engineering job and it finished in 30 minutes"
---

# I gave Qwen 3.8 27B a reverse-engineering job and it finished in 30 minutes

> Hacker News · 2026-08-23 · AI 보안

---

Qwen 3.8 27B가 로컬에서 상용 애플리케이션의 라이선스 검증을 역공학해 실제로 작동하는 우회 스크립트를 만들어낸 사례가 보고됐다. 작성자는 Lenovo ThinkStation PGX(GB10 Grace Blackwell, 128GB 통합 메모리 등)에서 모델을 구동하며 기본적으로 초당 15~30토큰, NVFP4 등 최적화 설정으로 코드·추론 시 약 50토큰/초를 기록했다고 밝힌다. 테스트는 작성자가 정당히 보유한 라이선스가 있는 실제 상용 바이너리를 대상으로 진행됐고, 모델은 실행 없이 정적 분석으로 수천 줄의 arm64 코드를 해독해 보안 함수와 호출 지점을 매핑한 뒤, 바이너리에 은닉된 공개키를 복원해 서명 검증을 통과시키는 데 성공했다. 전체 작업은 약 30분 걸렸고, 모델은 초기에 만든 거의 정답 수준의 첫 키에서 발견된 무결성 해시 불일치를 스스로 찾아내어 재시도해 바이트 단위로 일치시키는 등 자체 오류 수정을 수행했다.
이 사례가 갖는 기술적 의미는 명확하다. 한 기계에서 소비자급 하드웨어로 구동 가능한 27B급 로컬 모델이 복잡한 역공학·암호 복원 과업을 완수했다는 점은 클라우드 의존 없이도 고급 분석 능력이 로컬에 상주할 수 있음을 보여준다. 장점으로는 기밀 코드나 악성코드 분석을 외부 전송 없이 수행할 수 있다는 점이 있으나, 반대로 같은 능력이 악의적 사용자의 손에 들어가면 로컬에서 제어 가능한 공격 벡터가 된다는 점이 보안 위협 모델의 변화를 의미한다. 다만 결과는 단일 대상·단일 실행에 기반하며, 작성자 자신도 이 사례를 일반화하지는 않으므로 모델 능력의 폭과 한계는 더 많은 샘플이 필요하다는 한계가 분명하다.

[Hacker News에서 원문 읽기 →](https://www.xda-developers.com/qwen-3-8-27b-reverse-engineering-job-frontier-model/)

