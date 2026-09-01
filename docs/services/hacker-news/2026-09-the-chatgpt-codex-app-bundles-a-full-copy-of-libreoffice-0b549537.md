---
title: "The ChatGPT/Codex app bundles a full copy of LibreOffice"
sidebar_label: "The ChatGPT/Codex app bundles a full copy of LibreOffice"
---

# The ChatGPT/Codex app bundles a full copy of LibreOffice

> Hacker News · 2026-09-01 · software

---

작성자는 로컬 디스크 정리 도구(OmniDiskSweeper)를 살피다 ~/.cache 폴더에서 흥미로운 항목을 발견했다. OpenAI의 데스크톱 앱(최근에는 단순히 ChatGPT로 사명 변경)에 codex-primary-runtime이라는 이름의 폴더가 존재하며 해당 폴더 크기가 약 1.7GB에 달한다는 점을 지적한다. 그 내부에는 전체 Python 설치, 전체 Node.js 설치와 더불어 Poppler, git, 그리고 LibreOffice(2010년 OpenOffice.org에서 갈라져 나온 오픈소스 오피스 스위트)의 네이티브 바이너리까지 포함되어 있다. 또한 ~/.cache/codex-runtimes/.../plugins/documents 경로에는 Codex가 이들 바이너리를 찾아 사용하도록 알려주는 'skills'가 들어 있다고 보고한다.
이 관찰은 데스크톱 앱이 많은 런타임 의존성을 자체적으로 묶어 배포하고 있음을 보여준다. 전체 런타임과 네이티브 도구들을 포함해 설치 용량이 커지는 한편, 내부의 'skills' 구성은 앱이 로컬에 포함된 도구들을 직접 참조해 문서 처리나 네이티브 명령 호출과 같은 기능을 수행하도록 설계되었음을 시사한다. 제공된 근거만 보면 구체적 동작 방식이나 보안·라이선스 영향까지는 확인되지 않으므로, 해당 발견은 주로 패키징 방식과 배포 크기 측면에서 기술 독자들이 주목할 만한 자료로 평가할 수 있다.

[Hacker News에서 원문 읽기 →](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)

