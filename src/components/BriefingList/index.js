import React, {useEffect, useMemo, useState} from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import ServiceIcon from '@site/src/components/ServiceIcon';

import styles from './styles.module.css';

const PERIODS = [
  {label: '전체', days: null},
  {label: '7일', days: 7},
  {label: '14일', days: 14},
  {label: '30일', days: 30},
];

const PAGE_SIZE = 6;

export default function BriefingList({mode = 'all', serviceKey: fixedServiceKey = 'all'}) {
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
    return <div className="alert alert--warning">브리핑 데이터를 불러오지 못했습니다: {error}</div>;
  }

  if (!data) {
    return <div className="alert alert--secondary">브리핑 데이터를 불러오는 중입니다.</div>;
  }

  return (
    <section className={styles.briefingList}>
      {mode === 'all' && (
        <div className={styles.filterBar}>
          {fixedServiceKey === 'all' && (
            <div className={styles.filterField}>
              <span>서비스</span>
              <div className={styles.serviceFilters}>
                <button
                  className={
                    serviceKey === 'all' ? styles.activeServiceButton : styles.serviceButton
                  }
                  onClick={() => setSelectedServiceKey('all')}
                  type="button">
                  전체
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
            <span>기간</span>
            <div className={styles.segmented}>
              {PERIODS.map((period) => (
                <button
                  className={periodDays === period.days ? styles.activeButton : styles.button}
                  key={period.label}
                  onClick={() => setPeriodDays(period.days)}
                  type="button">
                  {period.label}
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
            onPageChange={setPage}
            totalItems={items.length}
            totalPages={totalPages}
          />
        </>
      ) : (
        <p className={styles.emptyState}>조건에 맞는 브리핑 글이 없습니다.</p>
      )}
    </section>
  );
}

function BriefingCard({item}) {
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
        <span>{item.published_at || item.briefed_at || '날짜 미상'}</span>
      </div>
      <h3>
        <span>{item.title}</span>
      </h3>
      <p>{item.excerpt || '요약 본문을 추출할 수 없습니다. 상세 문서에서 브리핑 내용을 확인하세요.'}</p>
      <div className={styles.cardFooter}>
        <span className={styles.status}>{item.status}</span>
        <span>score {item.score}</span>
      </div>
    </a>
  );
}

function Pagination({currentPage, onPageChange, totalItems, totalPages}) {
  if (totalPages <= 1) {
    return <p className={styles.pageSummary}>총 {totalItems}개</p>;
  }
  const pageItems = compactPageItems(currentPage, totalPages);

  return (
    <nav className={styles.pagination} aria-label="브리핑 페이지">
      <span className={styles.pageSummary}>
        총 {totalItems}개 · {currentPage}/{totalPages}
      </span>
      <div className={styles.pageButtons}>
        <button
          aria-label="이전 페이지"
          className={styles.pageNavButton}
          disabled={currentPage === 1}
          onClick={() => onPageChange(currentPage - 1)}
          type="button">
          Previous
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
          aria-label="다음 페이지"
          className={styles.pageNavButton}
          disabled={currentPage === totalPages}
          onClick={() => onPageChange(currentPage + 1)}
          type="button">
          Next
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
