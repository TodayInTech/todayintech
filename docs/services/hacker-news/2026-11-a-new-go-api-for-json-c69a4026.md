---
title: "A new Go API for JSON"
sidebar_label: "A new Go API for JSON"
description: "Go 1.27에서 **encoding/json/v2**와 **encoding/json/jsontext**가 안정화되었습니다. 새 API는 RFC 8259 준수를 강화하고 스트리밍 토큰 기반 처리와 옵션 기반 마이그레이션을 지원합니다."
---

# A new Go API for JSON

> Hacker News · 2026-11-04 · Go

---

Go 팀은 **encoding/json/v2**와 구문 수준 패키지 **encoding/json/jsontext**를 **Go 1.27**에서 안정화했다고 발표했다(Go 블로그). 이번 변화는 기존 encoding/json(v1)이 가진 여러 동작상의 문제를 바로잡고, 스트리밍 중심의 처리와 세밀한 옵션 제어를 도입하는 데 초점을 맞춘다.

## 엄격한 구문 검사와 안전성

새 구현은 **RFC 8259** 기준을 더 충실히 따르도록 설계됐다. 특히 v1이 허용하던 잘못된 UTF-8과 중복 객체 멤버 이름 처리 등은 기본적으로 엄격하게 에러를 반환하도록 바뀌었다. 블로그는 중복 이름이 CVE-2017-12635처럼 보안 문제로 악용된 사례를 언급하며, 기본 동작은 안전을 우선하도록 설정됐다고 밝혔다. 또한 nil 슬라이스·맵을 null로 직렬화하는 v1의 기본은 호환성 문제를 유발해 많은 사용자가 빈 배열/객체로 직렬화되길 선호했다고 적시한다.

## jsontext: 토큰·값 기반 스트리밍

jsontext 패키지는 구문 수준(JSON-text)에서 동작하며 리플렉션에 의존하지 않는다. 주요 타입과 함수 예시는 다음과 같다:

package jsontext

type Encoder struct &#123; ... &#125;

func NewEncoder(io.Writer, ...Options) *Encoder

func (*Encoder) WriteValue(Value) error

func (*Encoder) WriteToken(Token) error

type Decoder struct &#123; ... &#125;

func NewDecoder(io.Reader, ...Options) *Decoder

func (*Decoder) ReadValue() (Value, error)

func (*Decoder) ReadToken() (Token, error)

Value는 v1의 RawMessage와 동일하며, Token은 할당 없이 임의의 JSON 토큰을 표현하도록 설계됐다. 이 구조는 MarshalJSON/UnmarshalJSON의 성능 한계를 해결하기 위해 **MarshalJSONTo/UnmarshalJSONFrom** 같은 스트리밍 지향 인터페이스를 허용한다.

## encoding/json/v2 API와 타입별 커스터마이징

v2의 고수준 API는 v1과 유사한 함수형 인터페이스를 유지하면서 옵션 인자를 추가했다:

package json

func Marshal(in any, opts ...Options) (out \[\]byte, err error)
func MarshalWrite(out io.Writer, in any, opts ...Options) error
func MarshalEncode(out *jsontext.Encoder, in any, opts ...Options) error
func Unmarshal(in \[\]byte, out any, opts ...Options) error
func UnmarshalRead(in io.Reader, out any, opts ...Options) error
func UnmarshalDecode(in *jsontext.Decoder, out any, opts ...Options) error

타입별 커스터마이징을 위해 v2는 기존 Marshaler/Unmarshaler와 함께 **MarshalJSONTo/UnmarshalJSONFrom**(jsontext.Encoder/Decoder를 받는 인터페이스)를 추가해 스트리밍 처리와 옵션 전파를 가능하게 했다.

## 단계적 마이그레이션 경로

블로그는 v1 동작과 v2 동작을 옵션으로 맞출 수 있어 점진적 마이그레이션이 가능하다고 설명하며 예시를 제시한다:

json.Marshal(..., json.DefaultOptionsV2(), jsontext.AllowDuplicateName(true))

또는

json.Marshal(..., jsonv1.DefaultOptionsV1(), jsontext.AllowDuplicateName(false))

공식 문서는 v1과 v2의 차이와 마이그레이션 가이드를 상세히 제공한다고 밝힌다.

## 의미와 실무적 영향(해석)

공식 문서에 근거하면 **주요 실무 변화는 기본 파싱의 엄격성 강화와 스트리밍·옵션 기반 유연성**이다. 보안 민감 애플리케이션은 중복 키·잘못된 UTF-8에 대해 더 안전한 기본 동작의 이점을 얻고, 라이브러리 제작자는 jsontext의 토큰 API와 MarshalJSONTo/UnmarshalJSONFrom를 이용해 더 효율적인 스트리밍 직렬화/역직렬화를 구현할 수 있다. 반면 기존 v1에 의존한 동작을 전제로 한 코드베이스는 제공된 옵션을 통해 필요한 이전 동작을 유지하면서 단계적으로 이행할 수 있다.

출처: Go 블로그(‘A new Go API for JSON’), encoding/json/v2 문서 및 마이그레이션 가이드(본문 근거).

[Hacker News에서 원문 읽기 →](https://go.dev/blog/jsonv2)

