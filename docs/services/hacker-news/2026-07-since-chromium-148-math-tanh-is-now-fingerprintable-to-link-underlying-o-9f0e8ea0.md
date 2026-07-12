---
title: "Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS"
sidebar_label: "Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS"
---

# Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS

> Hacker News · 2026-07-12 · 브라우저 보안·프라이버시

---

피드 메타데이터에 따르면 Scrapfly에 올라온 글 제목은 “Since Chromium 148, Math.tanh is now fingerprintable to link underlying OS”로, Chromium 148 이후 JavaScript의 Math.tanh 호출과 관련해 운영체제 식별(fingerprinting) 가능성이 제기되었다고 보입니다. 작성자는 joahnn_s이며 Hacker News에서 131점과 52개의 댓글을 기록해 개발자·보안 커뮤니티에서 활발히 논의되고 있음을 알 수 있습니다. 제공된 정보만 보면 이 변화가 브라우저 업데이트로 인해 새로 생긴 경로임을 주장하는 것으로 읽힙니다.
메타데이터만으로는 구체적 재현 방법, 어떤 환경이나 OS 구성이 차이를 만드는지, 또는 Chromium 측의 대응 계획 등 기술적 세부는 확인되지 않습니다. 다만 브라우저 수치 연산에서 드러나는 미세한 플랫폼 차이가 프라이버시·트래킹 문제로 이어질 수 있다는 점에서 보안·프라이버시 관점의 추가 검증과 완화책 검토가 필요해 보입니다. 원문을 통해 실험 조건과 완화 방안 등을 직접 확인하는 것이 권장됩니다.

[Hacker News에서 원문 읽기 →](https://scrapfly.dev/posts/browser-math-os-fingerprint/)

