---
title: "Hister: A private search engine for the pages you visit and the files you keep"
sidebar_label: "Hister: A private search engine for the pages you visit and the files you keep"
---

# Hister: A private search engine for the pages you visit and the files you keep

> Hacker News · 2026-09-17 · Open Source / Privacy Tools

---

Hister는 사용자가 방문한 웹페이지와 저장한 파일의 전체 내용을 색인해 로컬에서 검색할 수 있게 해주는 개인용 검색 엔진입니다. 데스크톱 바이너리나 Homebrew/Docker/Nix를 통해 배포되며, 기본적으로 로컬 서버로 실행해 브라우저(웹 UI), 터미널(TUI), 커맨드라인, 또는 MCP를 통해 검색합니다. 설치·개발 지침과 함께 브라우저 확장으로 방문 페이지를 자동 인덱싱하고, 기존 브라우저 히스토리나 로컬 디렉터리, 파일을 가져와 색인할 수 있다는 점이 강조되어 있습니다. 색인은 전체 텍스트 기반이며 필드 필터, 구문 검색, 와일드카드, 논리 부정, 별칭, 우선순위 같은 강력한 쿼리 옵션을 제공합니다.
기술적으로 Hister의 의미는 '개인이 통제하는' 색인과 검색 파이프라인을 제공한다는 데 있습니다. 기본 설정은 텔레메트리를 보내지 않고 서버에 문서와 색인을 저장하므로 제3자 검색 서비스에 의존하지 않습니다. 다만 선택적 의미 검색은 사용자가 구성하는 임베딩 엔드포인트로 문서 텍스트를 전송할 수 있으므로 원격 통합을 활성화하기 전 개인정보 정책과 설정을 검토하라는 점을 명확히 하고 있습니다. 멀티유저 서버 구성을 지원해 공유 인프라에서도 사용자별 문서 분리를 할 수 있으며, 요구사항(Go 1.26, npm, CGO 의존 빌드 도구)과 AGPLv3 라이선스, 기여·보안 보고 채널도 문서에 포함되어 있어 개발·운영 관점에서 실무적으로 검토할 가치가 있습니다.

[Hacker News에서 원문 읽기 →](https://github.com/asciimoo/hister)

