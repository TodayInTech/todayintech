# SERVICES

이 문서는 Today in Tech가 현재 지원하는 서비스와 서비스별 수집 방식을 추적한다.
서비스 구현, 수집 조건, collector strategy가 변경되면 이 문서를 반드시 함께 업데이트한다.

## 관리 원칙

- 서비스 구현 기준은 `src/sources/implementations/`에 둔다.
- 서비스 생성 등록 기준은 `src/sources/factory.py`에 둔다.
- 수집 알고리즘 기준은 `src/collection/strategies/`에 둔다.
- RSS를 지원하지 않는 서비스는 제3자 RSS를 사용하지 않고 공식 sitemap, 공식 API, HTML metadata 등 공식 출처 기반 strategy를 사용한다.
- 수집 결과 확인은 `make collect SERVICE={service_key}`로 수행한다.
- Collector는 매일 source snapshot을 저장하는 계층이다. 같은 글이 여러 날짜에 반복 수집되는 것은 정상이며, 재처리 방지는 전처리 단계의 `briefed_articles` 상태가 담당한다.
- 서비스별 feed가 과도하게 큰 경우 source 설정에 `collection_limit` 또는 `lookback_days`를 추가한다.

## 현재 지원 서비스

| 서비스 | service_key | 수집 방식 | 출처 URL | 수집 조건 범위 | 상태 |
| --- | --- | --- | --- | --- | --- |
| Hacker News | `hacker-news` | RSS | `https://hnrss.org/frontpage` | RSS feed에 포함된 frontpage snapshot 전체를 `Article`로 정규화. HN rank, points, comments를 후보 랭킹 signal로 추출 | 지원 중 |
| GitHub Blog | `github-blog` | RSS | `https://github.blog/feed/` | RSS feed에 포함된 최신 GitHub Blog snapshot을 `Article`로 정규화 | 지원 중 |
| Google Blog | `google-blog` | RSS | `https://blog.google/technology/rss/` | Google Technology RSS feed snapshot을 `Article`로 정규화 | 지원 중 |
| OpenAI Blog | `openai-blog` | RSS | `https://openai.com/news/rss.xml` | OpenAI News RSS feed에서 최근 90일 이내 후보 중 최신 50개까지 `Article`로 정규화 | 지원 중 |
| Anthropic Blog | `anthropic-blog` | Sitemap + page metadata | `https://www.anthropic.com/sitemap.xml` | sitemap URL 중 path가 `/news/`로 시작하는 항목만 포함하고 최신순 최대 20개 page metadata를 수집 | 지원 중 |

## Collector Strategy 조건

### RSS

- 사용 구현체: `RssCollector`
- 대상 서비스: Hacker News, GitHub Blog, Google Blog, OpenAI Blog
- 수집 기준:
  - `source.source_url`을 feedparser로 파싱한다.
  - title과 link가 없는 항목은 제외한다.
  - published 또는 updated 값을 `published_at`으로 변환한다.
  - authors, tags, summary가 있으면 보존한다.
  - 기본적으로 feed snapshot 전체를 수집한다.
  - `source_config()`에 `collection_limit`이 있으면 정규화된 article 수가 해당 개수에 도달할 때 수집을 중단한다.
  - `source_config()`에 `lookback_days`가 있으면 `published_at`이 기준일보다 오래된 article을 제외한다.
  - Hacker News는 RSS 순서를 `rss_rank`로 저장하고, summary에서 points/comments/comments URL을 metadata로 추출한다.

### Sitemap

- 사용 구현체: `SitemapCollector`
- 대상 서비스: Anthropic Blog
- 수집 기준:
  - 공식 sitemap XML을 가져온다.
  - `url_prefixes` 조건에 맞는 URL만 포함한다.
  - `lastmod` 기준 최신순으로 정렬한다.
  - `collection_limit` 개수만큼 page metadata를 조회한다.
  - HTML title, og:title, description, og:description을 사용해 `Article`을 구성한다.

## 확장 시 업데이트 체크리스트

- [ ] `src/sources/implementations/{source}.py` 추가 또는 변경
- [ ] `NewsSourceFactory` registry 추가 또는 변경
- [ ] 필요한 collector strategy 추가 또는 설정 변경
- [ ] 이 문서의 서비스 표와 조건 범위 업데이트
- [ ] `notes/en/harness/service/SERVICES.md` 동시 업데이트
- [ ] collector 단일 실행으로 수집 결과 확인

## 전처리 연계 정책

- Collector raw에는 중복이 남을 수 있다.
- Preprocessor는 normalized URL, title fingerprint, `briefed_articles` 상태를 기준으로 이미 처리된 글을 제외한다.
- Agent는 전처리를 통과한 신규 후보만 처리한다.
- 원문 URL 하나는 최대 하나의 article 문서로 발행한다.
