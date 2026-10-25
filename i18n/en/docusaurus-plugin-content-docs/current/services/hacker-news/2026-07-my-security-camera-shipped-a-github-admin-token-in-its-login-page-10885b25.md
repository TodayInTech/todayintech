---
title: "My security camera shipped a GitHub admin token in its login page"
sidebar_label: "My security camera shipped a GitHub admin token in its login page"
---

# My security camera shipped a GitHub admin token in its login page

> Hacker News · 2026-07-24 · Security

---

연구자는 한화비전(Hanwha Vision) 보안 카메라 펌웨어를 분석하던 중, 제조사 빌드 아티팩트에 내포된 암호화된 fwimage와 이를 해독하는 fwupgrader 바이너리를 통해 루트 파일시스템을 복원했다(chunk-0001). fwupgrader는 AES 키와 IV를 바이너리 내부의 고정 테이블과 XOR 방식으로 재조립해 openssl CLI로 복호화하는데, 키와 IV가 모델 라인 전반에 걸쳐 동일하게 하드코딩돼 있었다. 루트fs를 분석하면서 trufflehog로 검색한 결과 동일한 GitHub 토큰이 약 30개 파일에 중복 포함되어 있었고, 해당 토큰은 조직 내 수백 개 레포지토리에 대한 관리자 권한을 가지고 있었다고 보고되었다(chunk-0001). 작성자는 빌드 시 Vite가 process.env의 전체 내용을 정적 변수로 주입해 CI 환경 전체가 번들에 쓰여진 점을 유출 경로로 지적했다.
연구자는 약 500개의 펌웨어를 수집해 분석한 결과 약 62%에서 같은 방식으로 추출이 가능했으며, 토큰은 3개 펌웨어에서 동일하게 발견되었다(chunk-0002). 환경변수에는 GITHUB_NPM_TOKEN 등 민감 정보와 함께 일부 미국 국방부(DoD)로 할당된 IP 주소가 나타나 참여 회사 간 CI 공유나 환경 구성 문제를 시사했다. 발견 즉시 제조사에 보고했고 한화는 12시간 내 토큰을 폐기해 대응했음도 문서화됐다. 이 사례는 임베디드 장비의 펌웨어와 빌드 파이프라인에서의 비밀 관리 실패가 얼마나 광범위한 영향(빌드 아티팩트·관리자 토큰 노출)을 줄 수 있는지를 보여주며, process.env 취급, 토큰 최소권한·회전 정책, 빌드 시 비밀 주입 방식 재검토 같은 실무적 개선이 필요함을 시사한다. 다만 토큰이 실제로 UI를 통해 전송되었는지 여부는 저자도 확실치 않다고 밝히고 있어 일부 전송 경로에 대한 판단은 가정의 영역임을 명시한다.

[Hacker News에서 원문 읽기 →](https://hhh.hn/hanwha-github-token/)

