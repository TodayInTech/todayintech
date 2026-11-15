---
title: "PyPI's redesigned project pages with clearer security signals are now live"
sidebar_label: "PyPI's redesigned project pages with clearer security signals are now live"
description: "PyPI가 프로젝트 상세 페이지를 재설계하고 **보안 탭**을 추가하여 릴리스·파일별 증명(attestation) 상태(예: Full Provenance/No Provenance)와 다양한 프로비넌스 경고를 표시합니다. 릴리스 파일 탭은 업로드 지연(14일 이상) 경고를 보여주며, 이 프로젝트는 OpenSSF 자금으로 Kabu Creative가 구현했습니다."
---

# PyPI's redesigned project pages with clearer security signals are now live

> Hacker News · 2026-11-14 · 오픈소스 보안 / 패키지 관리

---

PyPI가 사용자 인터페이스를 재설계하고 새로운 **보안 탭**을 도입해 릴리스의 출처 검증 상태와 파일별 증명(attestation)을 한눈에 확인할 수 있게 했다. 이 작업은 커뮤니티 사용자 연구를 바탕으로 진행되었으며 현재 라이브 상태다.

## 새로운 보안 탭과 프로비넌스 상태
보안 탭은 각 릴리스 파일의 증명 유무를 확인해 릴리스의 프로비넌스 상태를 계산한다. 일반적인 상태는 **Full Provenance**(릴리스 파일의 100%가 attestations를 보유)와 **No Provenance**(해당 릴리스에 attestations가 전혀 없음)로 나뉜다. 지원되는 attestations 유형으로는 PyPI Publish attestations(파일이 PyPI Trusted Publisher로 게시되었음을 확인)와 SLSA Build Provenance(정확한 소스 커밋·빌드 플랫폼·빌드 지침과 연결)가 명시되어 있다. UI에서 attestations 메타데이터를 직접 확인하거나 투명성 로그 링크로 더 자세한 정보를 볼 수 있다.

## 프로비넌스 경고의 종류와 실무적 의미
프로비넌스 경고는 파일이 프로젝트의 기존 이력과 충돌하거나 일부 파일에만 attestations가 있는 경우처럼 의심스러운 상황을 강조한다. 경고에는 예컨대 동일 릴리스 내 파일 간 출처 불일치, 이전 릴리스와 다른 리포지토리/워크플로에서 생성된 파일, 이전에 attestations가 있던 프로젝트가 이제 attestations 없이 업로드하는 경우 등이 포함된다. PyPI는 경고를 눈에 띄게 노출하며, 문서에서는 경고가 반드시 악의를 의미하지는 않지만 설치 전 확인이 권장된다고 명시한다. 실무적으로는 경고를 보면 릴리스 노트·이슈 트래커를 확인하거나, 패키지 유지관리자와 소통해 출처와 빌드 파이프라인 변경을 확인하는 절차가 필요하다. 유지관리자라면 Trusted Publishing으로 전환해 다음 릴리스에 attestations를 생성하는 것을 고려하라는 권고가 포함되어 있다.

## 릴리스 파일 탭, 늦은 파일 경고와 정책 변화
릴리스 파일 탭은 긴 파일 목록에서 검색·필터링을 돕고 각 파일의 프로비넌스 상태를 테이블 형태로 보여준다. **'늦은 파일' 경고는 최초 릴리스 시점으로부터 14일 이후 업로드된 파일에 대해 표시되며**, 이 경고는 2026년 7월 이전의 릴리스에만 나타난다. 이유는 2026년 7월에 도입된 정책으로 14일 이후 새 파일을 거부하는 규정이 생겼기 때문이다(문서에 명시). 또한 릴리스 히스토리에는 파일 수, 프로비넌스 상태, 릴리스 상태(격리(quarantined), yank, archived, pre-release)가 더 자세히 드러난다.

## 프로젝트 상세 페이지 변화와 메타데이터 표현
프로비넌스 경고는 페이지 상단의 상태 배너로 표시되어 격리 같은 우선 경고와 함께 노출된다. 메타데이터는 유용성 기준으로 재정렬되며 "PyPI data" 또는 "Data verified by PyPI"로 라벨링되어 이전의 검증 상태 중심 배열을 대체한다.

## 배경·출처
이 작업은 OpenSSF의 자금 지원을 받아 Kabu Creative가 구현했으며, PyPI 팀과 OpenSSF Securing Software Repositories 워킹그룹 구성원들이 참여했다. PyPI는 이번 디자인 패턴과 경고 체계를 OpenSSF Attestations Style Guide의 사례 연구로도 공개했다.

위 변경은 패키지 출처를 UI 수준에서 더 명확히 확인할 수 있게 해 설치 전 위험 판단 흐름을 바꾼다. PyPI가 제시한 권고(메타데이터·릴리스 노트 확인, Trusted Publishing 도입 등)는 문서화되어 있어 실무 적용이 가능한 수준이다.

[Hacker News에서 원문 읽기 →](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/)

