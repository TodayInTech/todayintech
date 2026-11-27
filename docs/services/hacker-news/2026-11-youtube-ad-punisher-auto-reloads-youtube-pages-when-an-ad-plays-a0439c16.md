---
title: "YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays"
sidebar_label: "YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays"
description: "YouTube Ad Punisher는 광고가 감지되면 **1~3회 자동 새로고침**으로 광고 슬롯을 비우고 &t=Xs 방식으로 재생 위치를 복원해 광고를 우회한다. 광고 발생 기록을 로컬에 저장해 JSON/CSV로 내보낼 수 있다."
---

# YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays

> Hacker News · 2026-11-26 · 브라우저 확장/유튜브 광고 우회

---

**YouTube Ad Punisher**는 광고가 재생되면 페이지를 자동으로 새로고침해 광고를 제거하고 재생 위치를 보존하는 크롬·사파리 보조 도구다. GitHub 설명에 따르면 핵심 아이디어는 단순하다: 유튜브는 페이지 로드 시 광고를 다시 평가하므로 몇 차례 reload로 광고 슬롯이 비워지는 경우가 많고, 확장은 이를 자동화한다.

## 재생 타임스탬프 보존과 자동 리로드
확장은 광고를 감지하면(video DOM의 .ad-showing 클래스, 스킵 버튼, 오버레이를 500ms 폴링 + MutationObserver로 감시) 현재 재생 위치(video.currentTime)를 sessionStorage에 저장한 뒤 location.replace()로 페이지를 **1~3회** 새로고치고 URL에 **&amp;t=Xs** 파라미터를 붙여 유튜브의 자동 탐색(auto-seek)을 유도한다. 재생이 정상으로 돌아오면 이어서 재생된다. 무한 리로드 방지를 위해 **3초 쿨다운** 가드가 있고, **3회 실패 시 보조 탭으로 4초 전환 후 복귀(자동 에스케이프)**하거나 실패 루틴으로 yout-ube.com(광고 없는 미러)로 리다이렉트하며 URL에 **&amp;loop=0**을 포함해 무한 반복 문제를 방지한다.

## 로그·권한·내보내기
모든 광고 이벤트는 광고주, 광고 길이, skip 텍스트, 비디오 제목·타임스탬프 등 항목으로 로컬에 기록된다. 팝업에서 통계·상위 광고주·전체 기록을 확인할 수 있고 JSON·CSV로 내보내기 가능하다. 확장이 요청하는 권한은 설명대로 **storage**와 **tabs**뿐이며 원격 전송은 없다고 명시되어 있다.

## 호환성·설치·제약
크롬에서는 개발자 모드로 압축 해제한 확장을 로드하면 자동으로 작동한다고 문서가 안내한다(설치: git clone https://github.com/antonpictures/youtube-punisher.git → chrome://extensions → Load unpacked 등). 사파리는 사전 서명된 확장이 유튜브에 자동 주입되는 것을 차단해 제공된 AppleScript 기반 watcher(yt-ad-watch.sh)를 별도로 실행해야 하며, 문서상으로는 크롬이 더 신뢰할 수 있고 사파리는 수동 테스트가 필요하다고 적혀 있다. 일부 광고(예: 라이브 스트림의 중간 광고)는 위치 보존이 불가능해 단순 새로고침만 수행된다고 명시되어 있다.

## 작동 방식의 사회적·운영적 의미
작성자는 "Every reload is a vote: I will not watch your ad."라고 표현하며, 문서에서는 수백만 사용자가 이 도구를 동시에 사용할 경우 페이지 로드 수는 늘고 광고 노출은 줄어들어 광고 수익 모델에 영향을 줄 수 있다고 해석해 놓았다. 근거 텍스트는 이를 DDoS로 규정하지 않으며(증폭 없음, 봇넷 없음) '수동적 항의'로 설명한다.

## 실무적 시사점
제공된 근거만 보면 이 확장은 네트워크 필터링이나 요청 차단이 아닌 클라이언트 측 새로고침을 이용한 우회 방식이다. 기술적으로는 구현이 단순하며 manifest.json·content.js·popup.js·background.js 등 manifest v3 구조로 구성되어 있고 MIT 라이선스가 적용되어 있어 코드 검토·수정이 가능하다. 그러나 대규모 사용 시 유튜브 측의 대응(탐지·차단 정책 변경 등)이나 서버 로드 변화는 근거 문서에서 예측·보장하지 않는다.

참고: 본 브리핑의 사실·문구는 제공된 GitHub 설명(README) 내용을 직접 인용·정리한 것이며, 외부 검증 결과나 유튜브 정책 반응 등은 본 근거에 포함되지 않았다.

[Hacker News에서 원문 읽기 →](https://github.com/antonpictures/youtube-punisher)

