---
title: "Alpine Linux Security Advisory: OpenSSH-server password authentication bypass"
sidebar_label: "Alpine Linux Security Advisory: OpenSSH-server password authentication bypass"
description: "Alpine Linux는 openssh-server의 비밀번호 인증 우회 취약점을 공지했다. PAM 미사용 또는 UsePAM no 환경에서 PasswordAuthentication yes, '*' 비밀번호 필드(비밀번호 없음) 계정과 $5/$6 해시가 공존하면 원격에서 비밀번호 없이 로그인 가능—즉시 배포판용 고정 패키지로 업그레이드하거나 PasswordAuthentication을 no로 비활성화해야 한다."
---

# Alpine Linux Security Advisory: OpenSSH-server password authentication bypass

> Hacker News · 2026-11-05 · 보안

---

Alpine Linux가 발표한 보안 권고는 openssh-server에서 **비밀번호 인증 우회**가 가능한 치명적 조건을 설명합니다. 공격자는 SSH 포트에 한 번 접속해, 올바른 비밀번호 없이도 로그인할 수 있으며 재시도나 복잡한 절차가 불필요하다고 명시되어 있습니다(작성 시점에 CVE는 할당되지 않음).

## 영향 조건과 범위
- 영향을 받는 구성: Alpine의 openssh-server 패키지( **PAM 없이 빌드된 경우**) 또는 openssh-server-pam을 사용하더라도 **UsePAM no**로 설정한 경우. UsePAM yes인 패키지는 영향을 받지 않습니다.
- 추가 조건: sshd 설정에서 **PasswordAuthentication yes**(기본값)이고, 시스템에 비밀번호 필드가 '*'인 계정(예: 키 전용 사용자, root:* 등)과 적어도 하나의 $5 또는 $6 형식 비밀번호 해시가 공존해야 합니다. 한 사용자만 $5/$6 해시를 갖고 있어도 모든 '*' 계정이 위험해집니다.
- 영향을 확인한 릴리스: Alpine 3.21~3.24와 edge 및 더 오래된(3.16~3.20) 릴리스를 점검해 동일한 문제가 보고되었습니다. Docker/컨테이너처럼 sshd를 실행하지 않는 환경은 영향이 없습니다.

## 취약점 동작 원리(요약)
sshd가 PAM 없이 빌드된 환경에서 암호 비교에 musl의 crypt()를 사용합니다. musl의 crypt()는 입력 키가 256바이트를 초과하면 오류 표시로 문자열 `*`을 반환합니다. 시스템에 비밀번호 필드가 `*`인 계정(비밀번호 없음)과, 길이가 긴(257~1024바이트) 암호 시도가 조합되면 비교 결과가 `*`로 일치해 인증이 통과합니다. OpenSSH 측은 이 문제를 OpenSSH 10.6p2에서 해결했습니다.

## 권장 대응(우선순위)
1) 업데이트(권장)
- 가능한 한 빨리 패키지를 설치하고 **sshd를 재시작**하세요. 패키지 업그레이드만으로는 실행 중인 데몬이 교체되지 않습니다.

```
apk upgrade -U -a
rc-service sshd restart
```
- 고정된 패키지가 포함된 포인트 릴리스(예시): Alpine 3.21.10, 3.22.8, 3.23.8, 3.24.4. 브랜치별 고정 openssh 버전(원문 그대로):
  - edge: 10.6_p2-r0
  - 3.24: 10.3_p1-r2
  - 3.23: 10.2_p1-r1
  - 3.22: 10.0_p1-r11
  - 3.21: 9.9_p2-r1
  - 3.20: 9.7_p1-r6
  - 3.19: 9.6_p1-r3
  - 3.18: 9.3_p2-r4
  - 3.17: 9.1_p1-r7
  - 3.16: 9.0_p1-r6

2) 업데이트 불가 시 임시 완화(즉시 적용)
- SSH 키 로그인으로의 접근을 확인한 뒤, 원격 세션을 유지하면서 비밀번호 인증을 비활성화하세요. Alpine 3.19 이상은 drop-in 디렉터리를 읽습니다.

```
mkdir -p /etc/ssh/sshd_config.d
echo 'PasswordAuthentication no' > /etc/ssh/sshd_config.d/00-no-passwords.conf
sed -i.bak -e '1i PasswordAuthentication no' \
  -e 's/^\(\s*PasswordAuthentication[^y#]*\)yes/\1no/i' \
  /etc/ssh/sshd_config
sshd -t && rc-service sshd restart
sshd -T | grep -i passwordauthentication
```
- 마지막 명령은 `passwordauthentication no`를 출력해야 합니다. 변경을 되돌리려면 생성한 파일을 삭제하고 백업을 복원하세요.

## 클라우드 이미지(증례) 및 침해 여부 확인
- tiny-cloud 공식 이미지(3.18.11~3.24.3)의 `alpine` 계정은 `*` 비밀번호 필드를 가지며 doas가 비밀번호 없이 구성되어 있어, **초기 부팅 시에는 안전하지만** 이후 시스템에 $6 해시가 추가되면(예: 콘솔 비밀번호 설정 또는 user-data로 hashed_passwd 추가) 즉시 악용될 수 있습니다. 3.21.10 등 이후 빌드에는 고정 패치가 포함되어 있습니다.
- 침해 여부 확인: /var/log/messages에서 `Accepted password for`와 함께 비밀번호가 없는 계정(alpine, root 또는 키 전용 사용자)이 인증된 로그가 있는지 확인하십시오. 로그인 의심이 남으면 시스템을 침해된 것으로 간주하세요.

## 참고 및 제한
- OpenSSH의 10.6p2 릴리스 노트에 상세가 있으며, 권고문은 Alpine에서 확인한 영향·패치 버전과 대응 명령을 제공합니다. (작성 시점에 CVE는 할당되지 않았음)

소규모 호스팅 인스턴스부터 클라우드 이미지를 운영 중인 팀까지, 조건에 해당하면 즉시 패치하거나 PasswordAuthentication을 비활성화해야 합니다. 업데이트 후에도 반드시 sshd를 재시작해 수정이 적용되었는지 확인하세요.

[Hacker News에서 원문 읽기 →](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/)

