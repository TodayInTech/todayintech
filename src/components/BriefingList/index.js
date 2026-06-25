import React, {useEffect, useMemo, useState} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import ServiceIcon from '@site/src/components/ServiceIcon';

import styles from './styles.module.css';

const LABELS = {
  ko: {
    all: '전체',
    service: '서비스',
    period: '기간',
    periods: ['전체', '7일', '14일', '30일'],
    fetchError: '브리핑 데이터를 불러오지 못했습니다',
    loading: '브리핑 데이터를 불러오는 중입니다.',
    unknownDate: '날짜 미상',
    missingExcerpt: '요약 본문을 추출할 수 없습니다. 상세 문서에서 브리핑 내용을 확인하세요.',
    empty: '조건에 맞는 브리핑 글이 없습니다.',
    total: '총',
    items: '개',
    previous: '이전',
    next: '다음',
    previousAria: '이전 페이지',
    nextAria: '다음 페이지',
    paginationAria: '브리핑 페이지',
  },
  en: {
    all: 'All',
    service: 'Service',
    period: 'Period',
    periods: ['All', '7D', '14D', '30D'],
    fetchError: 'Failed to load briefing data',
    loading: 'Loading briefing data.',
    unknownDate: 'Unknown date',
    missingExcerpt: 'No excerpt is available. Open the article briefing for details.',
    empty: 'No briefing articles match the selected filters.',
    total: 'Total',
    items: ' items',
    previous: 'Previous',
    next: 'Next',
    previousAria: 'Previous page',
    nextAria: 'Next page',
    paginationAria: 'Briefing pages',
  },
};

const PERIOD_DAYS = [null, 7, 14, 30];

const PAGE_SIZE = 6;

export default function BriefingList({mode = 'all', serviceKey: fixedServiceKey = 'all'}) {
  const {i18n} = useDocusaurusContext();
  const labels = LABELS[i18n.currentLocale] || LABELS.ko;
  const dataUrl = useBaseUrl('/data/briefings/index.json');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [selectedServiceKey, setSelectedServiceKey] = useState(fixedServiceKey);
  const [periodDays, setPeriodDays] = useState(null);
  const [page, setPage] = useState(1);
  const serviceKey = fixedServiceKey === 'all' ? selectedServiceKey : fixedServiceKey;

  useEffect(() => {
    let cancelled = false;
    fetch(dataUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        return response.json();
      })
      .then((payload) => {
        if (!cancelled) {
          setData(payload);
        }
      })
      .catch((fetchError) => {
        if (!cancelled) {
          setError(fetchError.message);
        }
      });
    return () => {
      cancelled = true;
    };
  }, [dataUrl]);

  const items = useMemo(
    () => filterItems(data?.items || [], {mode, serviceKey, periodDays}),
    [data, mode, periodDays, serviceKey],
  );
  const services = useMemo(() => Object.entries(data?.services || {}), [data]);
  const totalPages = Math.max(Math.ceil(items.length / PAGE_SIZE), 1);
  const currentPage = Math.min(page, totalPages);
  const paginatedItems = items.slice((currentPage - 1) * PAGE_SIZE, currentPage * PAGE_SIZE);

  useEffect(() => {
    setPage(1);
  }, [mode, periodDays, serviceKey]);

  if (error) {
    return (
      <div className="alert alert--warning">
        {labels.fetchError}: {error}
      </div>
    );
  }

  if (!data) {
    return <div className="alert alert--secondary">{labels.loading}</div>;
  }

  return (
    <section className={styles.briefingList}>
      {mode === 'all' && (
        <div className={styles.filterBar}>
          {fixedServiceKey === 'all' && (
            <div className={styles.filterField}>
              <span>{labels.service}</span>
              <div className={styles.serviceFilters}>
                <button
                  className={
                    serviceKey === 'all' ? styles.activeServiceButton : styles.serviceButton
                  }
                  onClick={() => setSelectedServiceKey('all')}
                  type="button">
                  {labels.all}
                </button>
                {services.map(([key, name]) => (
                  <button
                    className={
                      serviceKey === key ? styles.activeServiceButton : styles.serviceButton
                    }
                    key={key}
                    onClick={() => setSelectedServiceKey(key)}
                    type="button">
                    <ServiceIcon serviceKey={key} label={name} iconOnly size="compact" />
                    {name}
                  </button>
                ))}
              </div>
            </div>
          )}
          <div className={styles.filterField}>
            <span>{labels.period}</span>
            <div className={styles.segmented}>
              {PERIOD_DAYS.map((days, index) => (
                <button
                  className={periodDays === days ? styles.activeButton : styles.button}
                  key={labels.periods[index]}
                  onClick={() => setPeriodDays(days)}
                  type="button">
                  {labels.periods[index]}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
      {paginatedItems.length ? (
        <>
          <div className={styles.cardGrid}>
            {paginatedItems.map((item) => (
              <BriefingCard item={item} key={item.href} />
            ))}
          </div>
          <Pagination
            currentPage={currentPage}
            labels={labels}
            onPageChange={setPage}
            totalItems={items.length}
            totalPages={totalPages}
          />
        </>
      ) : (
        <p className={styles.emptyState}>{labels.empty}</p>
      )}
    </section>
  );
}

function BriefingCard({item}) {
  const {i18n} = useDocusaurusContext();
  const labels = LABELS[i18n.currentLocale] || LABELS.ko;
  const href = useBaseUrl(toDocHref(item.href));

  return (
    <a className={styles.card} href={href}>
      <div className={styles.cardMeta}>
        <ServiceIcon
          serviceKey={item.service_key}
          label={item.service_name}
          iconOnly
          size="compact"
        />
        <span>{item.service_name}</span>
        <span>{item.published_at || item.briefed_at || labels.unknownDate}</span>
      </div>
      <h3>
        <span>{item.title}</span>
      </h3>
      <p>{item.excerpt || labels.missingExcerpt}</p>
      <div className={styles.cardFooter}>
        <span className={styles.status}>{item.status}</span>
        <span>score {item.score}</span>
      </div>
    </a>
  );
}

function Pagination({currentPage, labels, onPageChange, totalItems, totalPages}) {
  if (totalPages <= 1) {
    return (
      <p className={styles.pageSummary}>
        {labels.total} {totalItems}
        {labels.items}
      </p>
    );
  }
  const pageItems = compactPageItems(currentPage, totalPages);

  return (
    <nav className={styles.pagination} aria-label={labels.paginationAria}>
      <span className={styles.pageSummary}>
        {labels.total} {totalItems}
        {labels.items} · {currentPage}/{totalPages}
      </span>
      <div className={styles.pageButtons}>
        <button
          aria-label={labels.previousAria}
          className={styles.pageNavButton}
          disabled={currentPage === 1}
          onClick={() => onPageChange(currentPage - 1)}
          type="button">
          {labels.previous}
        </button>
        {pageItems.map((pageItem, index) =>
          pageItem === 'ellipsis' ? (
            <span className={styles.pageEllipsis} key={`ellipsis-${index}`}>
              …
            </span>
          ) : (
            <button
              aria-current={currentPage === pageItem ? 'page' : undefined}
              className={currentPage === pageItem ? styles.activePageButton : styles.pageButton}
              key={pageItem}
              onClick={() => onPageChange(pageItem)}
              type="button">
              {pageItem}
            </button>
          ),
        )}
        <button
          aria-label={labels.nextAria}
          className={styles.pageNavButton}
          disabled={currentPage === totalPages}
          onClick={() => onPageChange(currentPage + 1)}
          type="button">
          {labels.next}
        </button>
      </div>
    </nav>
  );
}

function compactPageItems(currentPage, totalPages) {
  if (totalPages <= 5) {
    return Array.from({length: totalPages}, (_, index) => index + 1);
  }

  if (currentPage <= 2) {
    return [1, 2, 'ellipsis', totalPages];
  }

  if (currentPage >= totalPages - 1) {
    return [1, 'ellipsis', totalPages - 1, totalPages];
  }

  return [1, 'ellipsis', currentPage, 'ellipsis', totalPages];
}

function filterItems(items, {mode, serviceKey, periodDays}) {
  const baseItems = items.filter((item) => {
    if (serviceKey !== 'all' && item.service_key !== serviceKey) {
      return false;
    }
    if (mode === 'featured') {
      return item.featured;
    }
    if (mode === 'new') {
      return item.new;
    }
    return withinPeriod(item.briefed_at || item.published_at, periodDays);
  });
  return [...baseItems].sort(
    (left, right) =>
      dateValue(right.briefed_at || right.published_at) -
        dateValue(left.briefed_at || left.published_at) ||
      Number(right.score) - Number(left.score),
  );
}

function withinPeriod(dateString, periodDays) {
  if (!periodDays || !dateString) {
    return true;
  }
  const latest = new Date();
  const cutoff = new Date(latest);
  cutoff.setDate(latest.getDate() - periodDays + 1);
  return dateValue(dateString) >= cutoff.getTime();
}

function dateValue(dateString) {
  if (!dateString) {
    return 0;
  }
  const value = new Date(dateString).getTime();
  return Number.isNaN(value) ? 0 : value;
}

function toDocHref(value) {
  return value.replace(/^\.\//, '/').replace(/\.md$/, '');
}
