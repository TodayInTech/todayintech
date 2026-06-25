import React, {useEffect, useMemo, useRef, useState} from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

import styles from './styles.module.css';

const PERIODS = [
  {label: 'Latest', days: 'latest'},
  {label: '7D', days: 7},
  {label: '14D', days: 14},
  {label: '30D', days: 30},
  {label: 'All', days: null},
];

const STAGE_LABELS = {
  collection: 'Collection',
  preprocessing: 'Preprocessing',
  enrichment: 'Enrichment',
  writer: 'Writer',
};

export default function OperationsDashboard({view = 'overview'}) {
  const dataUrl = useBaseUrl('/data/operations/trace-metrics.json');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [periodDays, setPeriodDays] = useState('latest');
  const [serviceKey, setServiceKey] = useState('all');

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

  const filtered = useMemo(() => filterData(data, periodDays, serviceKey), [
    data,
    periodDays,
    serviceKey,
  ]);

  if (error) {
    return (
      <div className="alert alert--warning">
        Operations 데이터를 불러오지 못했습니다: {error}
      </div>
    );
  }

  if (!data) {
    return <div className="alert alert--secondary">Operations 데이터를 불러오는 중입니다.</div>;
  }

  const serviceOptions = Object.entries(data.service_names || {}).sort(([left], [right]) =>
    left.localeCompare(right),
  );

  return (
    <section className={styles.dashboard}>
      <FilterBar
        periodDays={periodDays}
        setPeriodDays={setPeriodDays}
        serviceKey={serviceKey}
        setServiceKey={setServiceKey}
        serviceOptions={serviceOptions}
      />
      <p className={styles.sourceNote}>
        Source: <code>{data.source}</code> · Range: {data.date_range?.start || '-'} ~{' '}
        {data.date_range?.end || '-'} · Generated: {formatDateTime(data.generated_at)}
      </p>
      {view === 'services' ? (
        <ServicesView services={filtered.services} />
      ) : view === 'collection' ? (
        <StageView stage="collection" services={filtered.services} runs={filtered.runs} />
      ) : view === 'preprocessing' ? (
        <StageView stage="preprocessing" services={filtered.services} runs={filtered.runs} />
      ) : view === 'enrichment' ? (
        <StageView stage="enrichment" services={filtered.services} runs={filtered.runs} />
      ) : view === 'writer' ? (
        <StageView stage="writer" services={filtered.services} runs={filtered.runs} />
      ) : (
        <OverviewView runs={filtered.runs} services={filtered.services} />
      )}
    </section>
  );
}

function FilterBar({periodDays, setPeriodDays, serviceKey, setServiceKey, serviceOptions}) {
  return (
    <div className={styles.filterBar}>
      <div>
        <span className={styles.filterLabel}>Period</span>
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
      <ServiceDropdown
        serviceKey={serviceKey}
        setServiceKey={setServiceKey}
        serviceOptions={serviceOptions}
      />
    </div>
  );
}

function ServiceDropdown({serviceKey, setServiceKey, serviceOptions}) {
  const [open, setOpen] = useState(false);
  const rootRef = useRef(null);
  const selectedLabel =
    serviceKey === 'all'
      ? 'All services'
      : serviceOptions.find(([key]) => key === serviceKey)?.[1] || serviceKey;
  const options = [['all', 'All services'], ...serviceOptions];

  useEffect(() => {
    if (!open) {
      return undefined;
    }

    function handlePointerDown(event) {
      if (!rootRef.current?.contains(event.target)) {
        setOpen(false);
      }
    }

    function handleKeyDown(event) {
      if (event.key === 'Escape') {
        setOpen(false);
      }
    }

    document.addEventListener('pointerdown', handlePointerDown);
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('pointerdown', handlePointerDown);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [open]);

  return (
    <div className={styles.dropdownField} ref={rootRef}>
      <span className={styles.filterLabel}>Service</span>
      <button
        aria-expanded={open}
        aria-haspopup="listbox"
        className={styles.dropdownToggle}
        onClick={() => setOpen((value) => !value)}
        type="button">
        <span>{selectedLabel}</span>
        <span className={open ? styles.dropdownChevronOpen : styles.dropdownChevron}>⌄</span>
      </button>
      {open && (
        <div className={styles.dropdownMenu} role="listbox">
          {options.map(([key, label]) => (
            <button
              aria-selected={serviceKey === key}
              className={serviceKey === key ? styles.dropdownOptionActive : styles.dropdownOption}
              key={key}
              onClick={() => {
                setServiceKey(key);
                setOpen(false);
              }}
              role="option"
              type="button">
              <span className={styles.dropdownCheck}>{serviceKey === key ? '✓' : ''}</span>
              <span>{label}</span>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function OverviewView({runs, services}) {
  const totals = summarize(runs, services);
  const latest = [...runs].sort((left, right) => right.date.localeCompare(left.date))[0];
  return (
    <>
      <div className={styles.cardGrid}>
        <MetricCard label="Runs" value={runs.length} />
        <MetricCard label="Raw articles" value={totals.rawArticles} />
        <MetricCard label="Candidates" value={totals.candidates} />
        <MetricCard label="Writer-ready (traced)" value={totals.writerReady} />
        <MetricCard label="Published (traced)" value={totals.published} />
        <MetricCard label="Publish rate" value={`${rate(totals.published, totals.decisions)}%`} />
        <MetricCard
          label="Enrichment trace coverage"
          value={`${totals.enrichmentTraceRuns}/${runs.length}`}
        />
        <MetricCard label="Writer trace coverage" value={`${totals.writerTraceRuns}/${runs.length}`} />
      </div>
      <section className={styles.panel}>
        <h2>Latest run</h2>
        {latest ? (
          <dl className={styles.definitionGrid}>
            <dt>Date</dt>
            <dd>{latest.date}</dd>
            <dt>Status</dt>
            <dd>
              <StatusBadge status={latest.status} />
            </dd>
            <dt>GitHub run</dt>
            <dd>{latest.github_run_id || '-'}</dd>
            <dt>Commit</dt>
            <dd>{latest.git_sha ? latest.git_sha.slice(0, 7) : '-'}</dd>
          </dl>
        ) : (
          <p>No remote trace runs found.</p>
        )}
      </section>
      <section className={styles.panel}>
        <h2>Pipeline funnel</h2>
        <HorizontalBarChart
          rows={[
            {label: 'Raw articles', value: totals.rawArticles},
            {label: 'Candidates', value: totals.candidates},
            {label: 'Writer-ready (traced)', value: totals.writerReady},
            {label: 'Published (traced)', value: totals.published},
          ]}
        />
      </section>
      <section className={styles.chartGrid}>
        <SparklinePanel
          title="Candidate trend"
          rows={runs}
          value={(run) => run.preprocessing?.candidate_count || 0}
        />
        <SparklinePanel
          title="Published trend"
          rows={runs}
          value={(run) => run.writer?.published_count || 0}
        />
      </section>
      <RecentRunsTable runs={runs} services={services} />
    </>
  );
}

function ServicesView({services}) {
  const rows = serviceMetricRows(services);

  return (
    <>
      <section className={styles.panel}>
        <h2>Service funnel</h2>
        <GroupedBarChart
          rows={rows.map((row) => ({
            label: row.service_name,
            values: [
              {label: 'Raw', value: row.raw},
              {label: 'Candidates', value: row.candidates},
              {label: 'Writer-ready', value: row.writerReady},
              {label: 'Published', value: row.published},
            ],
          }))}
        />
      </section>
      <section className={styles.panel}>
        <h2>Service metrics</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>Service</th>
                <th>Raw</th>
                <th>Candidates</th>
                <th>Writer-ready</th>
                <th>Published</th>
                <th>Candidate rate</th>
                <th>Publish rate</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row.service_key}>
                  <td>{row.service_name}</td>
                  <td>{row.raw}</td>
                  <td>{row.candidates}</td>
                  <td>{row.writerReady}</td>
                  <td>{row.published}</td>
                  <td>{rate(row.candidates, row.raw)}%</td>
                  <td>{rate(row.published, row.decisions)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </>
  );
}

function StageView({stage, services, runs}) {
  const totals = summarize(runs, services);
  return (
    <>
      <div className={styles.cardGrid}>
        {stage === 'collection' && (
          <>
            <MetricCard label="Raw articles" value={totals.rawArticles} />
            <MetricCard label="Collection failures" value={totals.collectionFailures} />
            <MetricCard label="Warnings" value={totals.warnings} />
          </>
        )}
        {stage === 'preprocessing' && (
          <>
            <MetricCard label="Raw articles" value={totals.rawArticles} />
            <MetricCard label="Candidates" value={totals.candidates} />
            <MetricCard label="Candidate rate" value={`${rate(totals.candidates, totals.rawArticles)}%`} />
          </>
        )}
        {stage === 'enrichment' && (
          <>
            <MetricCard label="Enrichment candidates" value={totals.enrichmentCandidates} />
            <MetricCard label="Writer-ready" value={totals.writerReady} />
            <MetricCard label="Writer-ready rate" value={`${rate(totals.writerReady, totals.enrichmentCandidates)}%`} />
          </>
        )}
        {stage === 'writer' && (
          <>
            <MetricCard label="Decisions" value={totals.decisions} />
            <MetricCard label="Published" value={totals.published} />
            <MetricCard label="Publish rate" value={`${rate(totals.published, totals.decisions)}%`} />
          </>
        )}
      </div>
      <StageCharts stage={stage} services={services} />
      <section className={styles.panel}>
        <h2>{STAGE_LABELS[stage]} by service</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Service</th>
                <th>Status</th>
                <th>Raw</th>
                <th>Candidates</th>
                <th>Writer-ready</th>
                <th>Published</th>
                <th>Failure / reason</th>
              </tr>
            </thead>
            <tbody>
              {services.map((service) => (
                <tr key={`${service.date}:${service.service_key}`}>
                  <td>{service.date}</td>
                  <td>{service.service_name}</td>
                  <td>
                    <StatusBadge status={service[stage]?.status || service.collection?.status} />
                  </td>
                  <td>{service.preprocessing?.raw_count || service.collection?.article_count || 0}</td>
                  <td>{service.preprocessing?.candidate_count || service.enrichment?.candidate_count || 0}</td>
                  <td>{service.enrichment?.writer_ready_count || 0}</td>
                  <td>{service.writer?.published_count || 0}</td>
                  <td>{topReason(service, stage)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </>
  );
}

function StageCharts({stage, services}) {
  if (stage === 'collection') {
    const rows = serviceMetricRows(services).map((row) => ({
      label: row.service_name,
      value: row.raw,
    }));
    return (
      <section className={styles.panel}>
        <h2>Collected articles by service</h2>
        <HorizontalBarChart rows={rows} />
      </section>
    );
  }

  if (stage === 'preprocessing') {
    return (
      <section className={styles.panel}>
        <h2>Candidate conversion by service</h2>
        <GroupedBarChart
          rows={serviceMetricRows(services).map((row) => ({
            label: row.service_name,
            values: [
              {label: 'Raw', value: row.raw},
              {label: 'Candidates', value: row.candidates},
            ],
          }))}
        />
      </section>
    );
  }

  if (stage === 'enrichment') {
    return (
      <section className={styles.chartGrid}>
        <div className={styles.panel}>
          <h2>Input strategy distribution</h2>
          <HorizontalBarChart rows={countRows(services, 'enrichment', 'strategy_counts')} />
        </div>
        <div className={styles.panel}>
          <h2>Failure reasons</h2>
          <HorizontalBarChart rows={countRows(services, 'enrichment', 'failure_reason_counts')} />
        </div>
      </section>
    );
  }

  if (stage === 'writer') {
    return (
      <section className={styles.chartGrid}>
        <div className={styles.panel}>
          <h2>Decision distribution</h2>
          <HorizontalBarChart rows={countRows(services, 'writer', 'decision_counts')} />
        </div>
        <div className={styles.panel}>
          <h2>Summary scope</h2>
          <HorizontalBarChart rows={countRows(services, 'writer', 'summary_scope_counts')} />
        </div>
      </section>
    );
  }

  return null;
}

function RecentRunsTable({runs, services}) {
  const serviceKeys = new Set(services.map((service) => service.service_key));
  if (serviceKeys.size === 1) {
    const sortedServices = [...services].sort((left, right) => right.date.localeCompare(left.date));
    return (
      <section className={styles.panel}>
        <h2>Recent service runs</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Service</th>
                <th>Status</th>
                <th>Raw</th>
                <th>Candidates</th>
                <th>Writer-ready</th>
                <th>Published</th>
              </tr>
            </thead>
            <tbody>
              {sortedServices.map((service) => (
                <tr key={`${service.date}:${service.service_key}`}>
                  <td>{service.date}</td>
                  <td>{service.service_name}</td>
                  <td>
                    <StatusBadge status={service.collection?.status} />
                  </td>
                  <td>{service.preprocessing?.raw_count || service.collection?.article_count || 0}</td>
                  <td>{service.preprocessing?.candidate_count || 0}</td>
                  <td>{service.enrichment?.writer_ready_count || 0}</td>
                  <td>{service.writer?.published_count || 0}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    );
  }
  const sortedRuns = [...runs].sort((left, right) => right.date.localeCompare(left.date));
  return (
    <section className={styles.panel}>
      <h2>Recent runs</h2>
      <div className={styles.tableWrap}>
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Status</th>
              <th>Raw</th>
              <th>Candidates</th>
              <th>Writer-ready</th>
              <th>Published</th>
              <th>Traces</th>
              <th>Run</th>
            </tr>
          </thead>
          <tbody>
            {sortedRuns.map((run) => (
              <tr key={run.date}>
                <td>{run.date}</td>
                <td>
                  <StatusBadge status={run.status} />
                </td>
                <td>{run.collection?.total_article_count || 0}</td>
                <td>{run.preprocessing?.candidate_count || 0}</td>
                <td>{run.enrichment?.writer_ready_count || 0}</td>
                <td>{run.writer?.published_count || 0}</td>
                <td>{stageCoverageLabel(run)}</td>
                <td>{run.github_run_id || '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function MetricCard({label, value}) {
  return (
    <div className={styles.card}>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function HorizontalBarChart({rows}) {
  const safeRows = rows.filter((row) => row.value > 0);
  const maxValue = Math.max(...safeRows.map((row) => row.value), 1);
  if (!safeRows.length) {
    return <p className={styles.emptyState}>No metric data for the selected filter.</p>;
  }
  return (
    <div className={styles.barChart}>
      {safeRows.map((row) => (
        <div className={styles.barRow} key={row.label}>
          <span className={styles.barLabel}>{row.label}</span>
          <div className={styles.barTrack}>
            <div
              className={styles.barFill}
              style={{width: `${Math.max((row.value / maxValue) * 100, 2)}%`}}
            />
          </div>
          <strong>{row.value}</strong>
        </div>
      ))}
    </div>
  );
}

function GroupedBarChart({rows}) {
  const maxValue = Math.max(
    ...rows.flatMap((row) => row.values.map((value) => value.value)),
    1,
  );
  if (!rows.length) {
    return <p className={styles.emptyState}>No service metric data for the selected filter.</p>;
  }
  return (
    <div className={styles.groupedChart}>
      <div className={styles.legend}>
        {rows[0]?.values.map((value, index) => (
          <span key={value.label}>
            <i className={styles[`series${index}`]} />
            {value.label}
          </span>
        ))}
      </div>
      {rows.map((row) => (
        <div className={styles.groupRow} key={row.label}>
          <span className={styles.groupLabel}>{row.label}</span>
          <div className={styles.groupBars}>
            {row.values.map((value, index) => (
              <div className={styles.groupBarLine} key={value.label}>
                <span>{value.label}</span>
                <div className={styles.barTrack}>
                  <div
                    className={`${styles.barFill} ${styles[`series${index}`]}`}
                    style={{width: `${Math.max((value.value / maxValue) * 100, 2)}%`}}
                  />
                </div>
                <strong>{value.value}</strong>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

function SparklinePanel({title, rows, value}) {
  const sortedRows = [...rows].sort((left, right) => left.date.localeCompare(right.date));
  const values = sortedRows.map(value);
  const latest = values.at(-1) || 0;
  return (
    <div className={styles.panel}>
      <h2>{title}</h2>
      <Sparkline values={values} />
      <p className={styles.sparklineSummary}>
        Latest: <strong>{latest}</strong> · Points: {values.length}
      </p>
    </div>
  );
}

function Sparkline({values}) {
  if (!values.length) {
    return <p className={styles.emptyState}>No trend data.</p>;
  }
  const maxValue = Math.max(...values, 1);
  const width = 320;
  const height = 88;
  const points = values
    .map((value, index) => {
      const x = values.length === 1 ? width : (index / (values.length - 1)) * width;
      const y = height - (value / maxValue) * (height - 10) - 5;
      return `${x},${y}`;
    })
    .join(' ');
  return (
    <svg className={styles.sparkline} viewBox={`0 0 ${width} ${height}`} role="img">
      <polyline points={points} fill="none" stroke="currentColor" strokeWidth="4" />
    </svg>
  );
}

function StatusBadge({status}) {
  const safeStatus = status || 'missing';
  return (
    <span className={`${styles.badge} ${styles[`status_${safeStatus}`] || ''}`}>
      {safeStatus}
    </span>
  );
}

function filterData(data, periodDays, serviceKey) {
  if (!data) {
    return {runs: [], services: []};
  }
  const latestDate = maxDate(data.runs || []);
  const cutoff =
    periodDays && periodDays !== 'latest' && latestDate
      ? addDays(latestDate, -periodDays + 1)
      : null;
  const withinPeriod = (date) => {
    if (periodDays === 'latest') {
      return date === latestDate;
    }
    return !cutoff || date >= cutoff;
  };
  return {
    runs: (data.runs || []).filter((run) => withinPeriod(run.date)),
    services: (data.services || []).filter(
      (service) =>
        withinPeriod(service.date) &&
        (serviceKey === 'all' || service.service_key === serviceKey),
    ),
  };
}

function summarize(runs, services) {
  if (services.length > 0) {
    return {
      rawArticles: sum(
        services,
        (service) => service.preprocessing?.raw_count || service.collection?.article_count,
      ),
      candidates: sum(services, (service) => service.preprocessing?.candidate_count),
      enrichmentCandidates: sum(services, (service) => service.enrichment?.candidate_count),
      writerReady: sum(services, (service) => service.enrichment?.writer_ready_count),
      decisions: sum(services, (service) => service.writer?.decision_count),
      published: sum(services, (service) => service.writer?.published_count),
      collectionFailures: sum(services, (service) =>
        service.collection?.status === 'failed' ? 1 : 0,
      ),
      warnings: sum(services, (service) => service.collection?.warning_count),
      enrichmentTraceRuns: uniqueDatesWithStage(services, 'enrichment'),
      writerTraceRuns: uniqueDatesWithStage(services, 'writer'),
      serviceRows: services.length,
    };
  }
  return {
    rawArticles: sum(runs, (run) => run.collection?.total_article_count),
    candidates: sum(runs, (run) => run.preprocessing?.candidate_count),
    enrichmentCandidates: sum(runs, (run) => run.enrichment?.candidate_count),
    writerReady: sum(runs, (run) => run.enrichment?.writer_ready_count),
    decisions: sum(runs, (run) => run.writer?.decision_count),
    published: sum(runs, (run) => run.writer?.published_count),
    collectionFailures: sum(runs, (run) => run.collection?.failed_service_count),
    warnings: sum(runs, (run) => run.collection?.warning_count),
    enrichmentTraceRuns: runs.filter((run) => run.enrichment?.available).length,
    writerTraceRuns: runs.filter((run) => run.writer?.available).length,
    serviceRows: services.length,
  };
}

function uniqueDatesWithStage(services, stage) {
  return new Set(
    services.filter((service) => service[stage]?.available).map((service) => service.date),
  ).size;
}

function stageCoverageLabel(run) {
  return [
    run.collection?.available ? 'C' : null,
    run.preprocessing?.available ? 'P' : null,
    run.enrichment?.available ? 'E' : null,
    run.writer?.available ? 'W' : null,
  ]
    .filter(Boolean)
    .join('/');
}

function serviceMetricRows(services) {
  return Object.values(
    services.reduce((acc, service) => {
      const key = service.service_key;
      acc[key] ||= {
        service_key: key,
        service_name: service.service_name,
        raw: 0,
        candidates: 0,
        writerReady: 0,
        decisions: 0,
        published: 0,
        failed: 0,
      };
      acc[key].raw += service.preprocessing?.raw_count || service.collection?.article_count || 0;
      acc[key].candidates += service.preprocessing?.candidate_count || 0;
      acc[key].writerReady += service.enrichment?.writer_ready_count || 0;
      acc[key].decisions += service.writer?.decision_count || 0;
      acc[key].published += service.writer?.published_count || 0;
      acc[key].failed +=
        (service.collection?.status === 'failed' ? 1 : 0) +
        (service.writer?.failed_count || 0);
      return acc;
    }, {}),
  ).sort((left, right) => left.service_name.localeCompare(right.service_name));
}

function countRows(services, stage, field) {
  const counts = services.reduce((acc, service) => {
    Object.entries(service[stage]?.[field] || {}).forEach(([key, value]) => {
      acc[key] = (acc[key] || 0) + (Number(value) || 0);
    });
    return acc;
  }, {});
  return Object.entries(counts)
    .map(([label, value]) => ({label, value}))
    .sort((left, right) => right.value - left.value || left.label.localeCompare(right.label));
}

function topReason(service, stage) {
  const source =
    stage === 'preprocessing'
      ? service.preprocessing?.excluded_reason_counts
      : stage === 'enrichment'
        ? service.enrichment?.failure_reason_counts
        : stage === 'writer'
          ? service.writer?.decision_counts
          : null;
  if (!source) {
    return '-';
  }
  const entries = Object.entries(source).sort((left, right) => right[1] - left[1]);
  return entries.length ? `${entries[0][0]}: ${entries[0][1]}` : '-';
}

function maxDate(runs) {
  return runs.reduce((latest, run) => (run.date > latest ? run.date : latest), '');
}

function addDays(dateString, days) {
  const date = new Date(`${dateString}T00:00:00Z`);
  date.setUTCDate(date.getUTCDate() + days);
  return date.toISOString().slice(0, 10);
}

function sum(items, getter) {
  return items.reduce((total, item) => total + (Number(getter(item)) || 0), 0);
}

function rate(value, total) {
  return total ? Math.round((value / total) * 1000) / 10 : 0;
}

function formatDateTime(value) {
  if (!value) {
    return '-';
  }
  return value.replace('T', ' ').replace(/\.\d+.*$/, ' UTC');
}
