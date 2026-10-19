import React, {useEffect, useMemo, useRef, useState} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Link from '@docusaurus/Link';
import {useHistory, useLocation} from '@docusaurus/router';
import DateCard from '@site/src/components/DateCard';
import ServiceIcon from '@site/src/components/ServiceIcon';
import LoadingSpinner from '@site/src/components/LoadingSpinner';

import styles from './styles.module.css';

const LABELS = {
  ko: {
    all: '전체',
    service: '서비스',
    period: '기간',
    periods: ['전체', '7일', '14일', '30일'],
    fetchError: '브리핑 데이터를 불러오지 못했습니다',
    loading: '브리핑 불러오는 중…',
    unknownDate: '날짜 미상',
    missingExcerpt: '브리핑을 열어 내용을 확인하세요.',
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
  const location = useLocation();
  const history = useHistory();
  const params = new URLSearchParams(location.search);
  const pageKey = `${mode}-${fixedServiceKey}-page`;
  const serviceParam = mode === 'all' ? params.get('service') || fixedServiceKey : fixedServiceKey;
  const selectedServiceKey = serviceParam;
  const resultsRef = useRef(null);
  const [reservedHeight, setReservedHeight] = useState(0);
  useEffect(() => {
    let width = window.innerWidth;
    const resetHeight = () => {
      if (window.innerWidth !== width) { width = window.innerWidth; setReservedHeight(0); }
    };
    window.addEventListener('resize', resetHeight);
    return () => window.removeEventListener('resize', resetHeight);
  }, []);
  const periodDays = PERIOD_DAYS.includes(Number(params.get('days'))) ? Number(params.get('days')) || null : null;
  const page = Math.max(1, Number.parseInt(params.get(pageKey), 10) || 1);
  function updateFilters(values) {
    // Preserve the list's footprint so shorter results cannot clamp the page's scroll position.
    const height = resultsRef.current?.getBoundingClientRect().height || 0;
    setReservedHeight((previous) => Math.max(previous, height));
    const next = new URLSearchParams(location.search);
    Object.entries(values).forEach(([key, value]) => {
      if (value === null || value === 'all' || value === 1) next.delete(key);
      else next.set(key, String(value));
    });
    const search = next.size ? `?${next}` : '';
    if (search === location.search) return;
    history.replace({...location, search});
  }
  const setPage = (value) => updateFilters({[pageKey]: value});
  const setSelectedServiceKey = (value) => updateFilters({service: value, [pageKey]: 1});
  const setPeriodDays = (value) => updateFilters({days: value, [pageKey]: 1});
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

  if (error) {
    return (
      <div className="alert alert--warning">
        {labels.fetchError}: {error}
      </div>
    );
  }

  if (!data) {
    return <LoadingSpinner label={labels.loading} />;
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
                  aria-pressed={serviceKey === 'all'}
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
                    aria-pressed={serviceKey === key}
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
                  aria-pressed={periodDays === days}
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
      <div className={styles.results} ref={resultsRef} style={{minHeight: reservedHeight || undefined}}>
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
        <div className={styles.emptyState} role="status"><p>{labels.empty}</p></div>
      )}
      </div>
    </section>
  );
}

function BriefingCard({item}) {
  const {i18n} = useDocusaurusContext();
  const labels = LABELS[i18n.currentLocale] || LABELS.ko;
  const href = useBaseUrl(toDocHref(item.href));
  const location = useLocation();
  const history = useHistory();

  return (
    <Link className={styles.card} to={href} onClick={(event) => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      history.push(href, {briefingReturnTo: `${location.pathname}${location.search}${location.hash}`});
    }}>
      <div className={styles.cardMeta}>
        <ServiceIcon
          serviceKey={item.service_key}
          label={item.service_name}
          iconOnly
          size="compact"
        />
        <span>{item.service_name}</span>
      </div>
      <h3>
        <span>{item.title}</span>
      </h3>
      <p>{item.excerpt || labels.missingExcerpt}</p>
      <div className={styles.cardFooter}>
        <DateCard value={item.published_at || item.briefed_at} />
      </div>
    </Link>
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
  if (totalPages <= 7) {
    return Array.from({length: totalPages}, (_, index) => index + 1);
  }
  const visible = new Set([1, totalPages]);
  const start = currentPage <= 3 ? 2 : currentPage >= totalPages - 2 ? totalPages - 3 : currentPage - 1;
  const end = currentPage <= 3 ? 4 : currentPage >= totalPages - 2 ? totalPages - 1 : currentPage + 1;
  for (let page = start; page <= end; page += 1) visible.add(page);
  const pages = Array.from(visible).sort((left, right) => left - right);
  return pages.flatMap((page, index) => {
    const previous = pages[index - 1];
    if (!index || page === previous + 1) return [page];
    return page === previous + 2 ? [previous + 1, page] : ['ellipsis', page];
  });
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
