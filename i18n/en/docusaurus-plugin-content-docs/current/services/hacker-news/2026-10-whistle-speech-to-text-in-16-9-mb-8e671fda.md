---
title: "Whistle: Speech to Text in 16.9 MB"
sidebar_label: "Whistle: Speech to Text in 16.9 MB"
---

# Whistle: Speech to Text in 16.9 MB

> Hacker News · 2026-10-08 · 음성인식/머신러닝

---

Whistle은 16.9MB 단일 파일로 제공되는 온디바이스 음성인식 모델로, CPU에서 의존성 없이 실행되며 Needle 엔진과 같은 컨테이너·양자화 방식을 공유한다. 16kHz 모노 입력을 처리해 최대 30초까지 한 번에 전사하고(영어·독일어·프랑스어·스페인어·이탈리아어·네덜란드어·폴란드어), 단어별 시작·종료 시간과 확률을 디코더의 어텐션을 통해 반환한다. 또한 인코더 출력은 80ms 프레임 단위의 음성 임베딩으로 제공되어 디코드 없이 임베딩만 추출할 수 있다. 프런트엔드는 25ms 창·10ms 홉, 80 로그멜 빈, 250–3500Hz 대역 제한으로 30초는 3000프레임이 되고, 컨볼루션 스템(128채널, 커널9)으로 프레임 수를 세 차례 반으로 줄여 최종 375프레임을 처리한다.
모델 내부는 인코더 8개의 Simple Attention 블록(비인과적 어텐션, mHC 레지듀얼 레인과 Monarch Hadamard MLP)과 디코더 8개의 Laddered Simple Attention 블록(폭 512, 쿼리 8헤드→KV 2헤드, 쿼리/키 48차원·값 64차원, Q/K/V에 3탭 인과적 컨볼루션, 레이어 3·7에서 18,432 슬롯의 인그램 룩업)을 사용한다. 디코더는 레이어별 학습된 게이트를 통해 인코더를 읽는 gated cross-attention을 추가하고, 한 번 투영한 K·V를 전체 디코드 동안 유지해 빔 수 증가가 오디오 재처리를 요구하지 않게 설계됐다. 디코딩은 5빔, 트랜스크립트 상한 320토큰, 어휘 8,192 텍스트 조각과 언어 토큰 7개를 쓰며 Aho-Corasick 기반 키워드 바이어싱을 제공한다. 검증에서는 LibriSpeech(테스트-clean/other), SPGISpeech, Earnings-22, FLEURS 평균에서 Whistle이 앞섰고, Whisper base(145.3MB)는 TED-LIUM·AMI·MLS 평균에서 우세했다. 지연 측정은 오디오 길이에 따라 선형으로, 예시로 5초 입력에서 첫 토큰 5.9ms, 30초에서 36.3ms를 보고한다. 무음 판단 시 빔 서치 진입 없이 빈 전사를 반환하며, 86,174 발화에 대한 WER 측정과 테스트 오디오가 학습에 포함되지 않았음을 오디오 체크섬·스피커 ID 비교로 검증한 점도 제시된다. 통합 측면에서는 needle_load/needle_transcribe/needle_embed 같은 C API와 needle_complete의 JSON 반환, 17개 플랫폼용 사전빌드 바이너리, Hugging Face의 가중치 및 GitHub 소스 제공으로 모바일·임베디드·브라우저 환경에서 즉시 실험·배포할 수 있는 구성이 특징이다.

[Hacker News에서 원문 읽기 →](https://cactuscompute.com/blog/whistle)

