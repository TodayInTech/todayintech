import React, {useEffect, useId, useMemo, useRef, useState} from 'react';
import {METRIC_HINTS, useCopy} from './copy';
import Tooltip from '@site/src/components/Tooltip';
import useBaseUrl from '@docusaurus/useBaseUrl';
import DateCard from '@site/src/components/DateCard';
import ServiceIcon from '@site/src/components/ServiceIcon';

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
  const t = useCopy();
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
        {t("Could not load traces")}: {error}
      </div>
    );
  }

  if (!data) {
    return <div className="alert alert--secondary">{t("Loading traces…")}</div>;
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
        {t("History")} <DateCard value={data.generated_at} label={t("Updated")} withTime />
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
  const t = useCopy();
  return (
    <div className={styles.filterBar}>
      <div className={styles.filterField}>
        <span className={styles.filterLabel}>{t("Period")}</span>
        <div className={styles.segmented}>
          {PERIODS.map((period) => (
            <button
              aria-pressed={periodDays === period.days}
              className={periodDays === period.days ? styles.activeButton : styles.button}
              key={t(period.label)}
              onClick={() => setPeriodDays(period.days)}
              type="button">
              {t(period.label)}
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
  const t = useCopy();
  const id = useId();
  const root = useRef(null);
  const trigger = useRef(null);
  const [open, setOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);
  const options = [['all', t("All services")], ...serviceOptions];
  const selectedIndex = Math.max(options.findIndex(([key]) => key === serviceKey), 0);
  const selected = options[selectedIndex];
  const show = () => { setActiveIndex(selectedIndex); setOpen(true); };
  const choose = (index) => {
    setServiceKey(options[index][0]);
    setOpen(false);
    trigger.current?.focus();
  };
  useEffect(() => {
    if (!open) return undefined;
    const outside = (event) => { if (!root.current?.contains(event.target)) setOpen(false); };
    document.addEventListener('pointerdown', outside);
    return () => document.removeEventListener('pointerdown', outside);
  }, [open]);
  const onKeyDown = (event) => {
    if (event.key === 'Escape') { event.preventDefault(); setOpen(false); return; }
    if (event.key === 'Tab') { setOpen(false); return; }
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      if (open) choose(activeIndex); else show();
      return;
    }
    if (['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(event.key)) {
      event.preventDefault();
      if (!open) { show(); return; }
      setActiveIndex((index) => event.key === 'Home' ? 0 : event.key === 'End' ? options.length - 1
        : (index + (event.key === 'ArrowDown' ? 1 : -1) + options.length) % options.length);
    } else if (event.key.length === 1) {
      const index = options.findIndex(([, name]) => name.toLowerCase().startsWith(event.key.toLowerCase()));
      if (index >= 0) { event.preventDefault(); setActiveIndex(index); setOpen(true); }
    }
  };
  return (
    <div className={styles.dropdownField} ref={root}>
      <span className={styles.filterLabel} id={`${id}-label`}>{t("Service")}</span>
      <button ref={trigger} type="button" role="combobox" aria-labelledby={`${id}-label`}
        aria-expanded={open} aria-haspopup="listbox" aria-controls={`${id}-options`}
        aria-activedescendant={open ? `${id}-option-${activeIndex}` : undefined}
        className={styles.dropdownTrigger} onKeyDown={onKeyDown}
        onClick={() => open ? setOpen(false) : show()}
        onBlur={(event) => { if (!root.current?.contains(event.relatedTarget)) setOpen(false); }}>
        <ServiceLabel serviceKey={selected[0]} serviceName={selected[1]} />
        <svg aria-hidden="true" className={styles.chevron} data-open={open} width="14" height="14" viewBox="0 0 16 16"><path d="m4 6 4 4 4-4" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" /></svg>
      </button>
      {open && <div className={styles.dropdownMenu} id={`${id}-options`} role="listbox" aria-labelledby={`${id}-label`}>
        {options.map(([key, name], index) => <div key={key} id={`${id}-option-${index}`} role="option"
          aria-selected={serviceKey === key} data-active={index === activeIndex}
          className={styles.dropdownOption} onMouseDown={(event) => event.preventDefault()}
          onPointerMove={() => setActiveIndex(index)} onClick={() => choose(index)}>
          <ServiceLabel serviceKey={key} serviceName={name} />
          <span className={styles.optionCheck} aria-hidden="true">{serviceKey === key ? '✓' : ''}</span>
        </div>)}
      </div>}
    </div>
  );
}

function ServiceLabel({serviceKey, serviceName}) {
  if (serviceKey === 'all') {
    return (
      <span className={styles.serviceLabel}>
        <span>{serviceName}</span>
      </span>
    );
  }

  return (
    <span className={styles.serviceLabel}>
      <ServiceIcon serviceKey={serviceKey} label={serviceName} iconOnly size="compact" />
      <span>{serviceName}</span>
    </span>
  );
}

function OverviewView({runs, services}) {
  const t = useCopy();
  const totals = summarize(runs, services);
  const latest = [...runs].sort((left, right) => right.date.localeCompare(left.date))[0];
  return (
    <>
      <div className={styles.cardGrid}>
        <MetricCard label={t("Runs")} value={runs.length} />
        <MetricCard label={t("Raw articles")} value={totals.rawArticles} />
        <MetricCard label={t("Candidates")} value={totals.candidates} />
        <MetricCard label={t("Writer-ready (traced)")} value={totals.writerReady} />
        <MetricCard label={t("Published (traced)")} value={totals.published} />
        <MetricCard label={t("Publish rate")} value={`${rate(totals.published, totals.decisions)}%`} />
        <MetricCard
          label={t("Enrichment trace coverage")}
          value={`${totals.enrichmentTraceRuns}/${runs.length}`}
        />
        <MetricCard label={t("Writer trace coverage")} value={`${totals.writerTraceRuns}/${runs.length}`} />
      </div>
      <section className={styles.panel}>
        <h2>{t("Latest run")}</h2>
        {latest ? (
          <dl className={styles.definitionGrid}>
            <dt>{t("Date")}</dt>
            <dd><DateCard value={latest.date} /></dd>
            <dt>{t("Status")}</dt>
            <dd>
              <StatusBadge status={latest.status} />
            </dd>
            <dt>{t("GitHub run")}</dt>
            <dd>{latest.github_run_id || '-'}</dd>
            <dt>{t("Commit")}</dt>
            <dd>{latest.git_sha ? latest.git_sha.slice(0, 7) : '-'}</dd>
          </dl>
        ) : (
          <p>{t("No remote trace runs found.")}</p>
        )}
      </section>
      <section className={styles.panel}>
        <h2>{t("Pipeline funnel")}</h2>
        <HorizontalBarChart
          rows={[
            {label: t("Raw articles"), value: totals.rawArticles},
            {label: t("Candidates"), value: totals.candidates},
            {label: t("Writer-ready (traced)"), value: totals.writerReady},
            {label: t("Published (traced)"), value: totals.published},
          ]}
        />
      </section>
      <section className={styles.chartGrid}>
        <SparklinePanel
          title={t("Candidate trend")}
          rows={runs}
          value={(run) => services.filter((service) => service.date === run.date).reduce((total, service) => total + (service.preprocessing?.candidate_count || 0), 0)}
        />
        <SparklinePanel
          title={t("Published trend")}
          rows={runs}
          value={(run) => services.filter((service) => service.date === run.date).reduce((total, service) => total + (service.writer?.published_count || 0), 0)}
        />
      </section>
      <RecentRunsTable runs={runs} services={services} />
    </>
  );
}

function ServicesView({services}) {
  const t = useCopy();
  const rows = serviceMetricRows(services);

  return (
    <>
      <section className={styles.panel}>
        <h2>{t("Service funnel")}</h2>
        <GroupedBarChart
          rows={rows.map((row) => ({
            serviceKey: row.service_key,
            label: row.service_name,
            values: [
              {label: t("Raw"), value: row.raw},
              {label: t("Candidates"), value: row.candidates},
              {label: t("Writer-ready"), value: row.writerReady},
              {label: t("Published"), value: row.published},
            ],
          }))}
        />
      </section>
      <section className={styles.panel}>
        <h2>{t("Service metrics")}</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>{t("Service")}</th>
                <th className={styles.numeric}>{t("Raw")}</th>
                <th className={styles.numeric}>{t("Candidates")}</th>
                <th className={styles.numeric}>{t("Writer-ready")}</th>
                <th className={styles.numeric}>{t("Published")}</th>
                <th className={styles.numeric}>{t("Candidate rate")}</th>
                <th className={styles.numeric}>{t("Publish rate")}</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row.service_key}>
                  <td>
                    <ServiceLabel serviceKey={row.service_key} serviceName={row.service_name} />
                  </td>
                  <td className={styles.numeric}>{row.raw}</td>
                  <td className={styles.numeric}>{row.candidates}</td>
                  <td className={styles.numeric}>{row.writerReady}</td>
                  <td className={styles.numeric}>{row.published}</td>
                  <td className={styles.numeric}>{rate(row.candidates, row.raw)}%</td>
                  <td className={styles.numeric}>{rate(row.published, row.decisions)}%</td>
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
  const t = useCopy();
  const totals = summarize(runs, services);
  return (
    <>
      <div className={styles.cardGrid}>
        {stage === 'collection' && (
          <>
            <MetricCard label={t("Raw articles")} value={totals.rawArticles} />
            <MetricCard label={t("Collection failures")} value={totals.collectionFailures} />
            <MetricCard label={t("Warnings")} value={totals.warnings} />
          </>
        )}
        {stage === 'preprocessing' && (
          <>
            <MetricCard label={t("Raw articles")} value={totals.rawArticles} />
            <MetricCard label={t("Candidates")} value={totals.candidates} />
            <MetricCard label={t("Candidate rate")} value={`${rate(totals.candidates, totals.rawArticles)}%`} />
          </>
        )}
        {stage === 'enrichment' && (
          <>
            <MetricCard label={t("Enrichment candidates")} value={totals.enrichmentCandidates} />
            <MetricCard label={t("Writer-ready")} value={totals.writerReady} />
            <MetricCard label={t("Writer-ready rate")} value={`${rate(totals.writerReady, totals.enrichmentCandidates)}%`} />
          </>
        )}
        {stage === 'writer' && (
          <>
            <MetricCard label={t("Decisions")} value={totals.decisions} />
            <MetricCard label={t("Published")} value={totals.published} />
            <MetricCard label={t("Publish rate")} value={`${rate(totals.published, totals.decisions)}%`} />
          </>
        )}
      </div>
      <StageCharts stage={stage} services={services} />
      <section className={styles.panel}>
        <h2>{t(STAGE_LABELS[stage])} · {t("Service")}</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>{t("Date")}</th>
                <th>{t("Service")}</th>
                <th>{t("Status")}</th>
                <th className={styles.numeric}>{t("Raw")}</th>
                <th className={styles.numeric}>{t("Candidates")}</th>
                <th className={styles.numeric}>{t("Writer-ready")}</th>
                <th className={styles.numeric}>{t("Published")}</th>
                <th>{t("Failure / reason")}</th>
              </tr>
            </thead>
            <tbody>
              {services.map((service) => (
                <tr key={`${service.date}:${service.service_key}`}>
                  <td><DateCard value={service.date} /></td>
                  <td>
                    <ServiceLabel
                      serviceKey={service.service_key}
                      serviceName={service.service_name}
                    />
                  </td>
                  <td>
                    <StatusBadge status={service[stage]?.status || service.collection?.status} />
                  </td>
                  <td className={styles.numeric}>{service.preprocessing?.raw_count || service.collection?.article_count || 0}</td>
                  <td className={styles.numeric}>{service.preprocessing?.candidate_count || service.enrichment?.candidate_count || 0}</td>
                  <td className={styles.numeric}>{service.enrichment?.writer_ready_count || 0}</td>
                  <td className={styles.numeric}>{service.writer?.published_count || 0}</td>
                  <td className={styles.reasonCell}>{topReason(service, stage)}</td>
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
  const t = useCopy();
  if (stage === 'collection') {
    const rows = serviceMetricRows(services).map((row) => ({
      serviceKey: row.service_key,
      label: row.service_name,
      value: row.raw,
    }));
    return (
      <section className={styles.panel}>
        <h2>{t("Collected articles by service")}</h2>
        <HorizontalBarChart rows={rows} />
      </section>
    );
  }

  if (stage === 'preprocessing') {
    return (
      <section className={styles.panel}>
        <h2>{t("Candidate conversion by service")}</h2>
        <GroupedBarChart
          rows={serviceMetricRows(services).map((row) => ({
            serviceKey: row.service_key,
            label: row.service_name,
            values: [
              {label: t("Raw"), value: row.raw},
              {label: t("Candidates"), value: row.candidates},
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
          <h2>{t("Input strategy distribution")}</h2>
          <HorizontalBarChart rows={countRows(services, 'enrichment', 'strategy_counts')} />
        </div>
        <div className={styles.panel}>
          <h2>{t("Failure reasons")}</h2>
          <HorizontalBarChart rows={countRows(services, 'enrichment', 'failure_reason_counts')} />
        </div>
      </section>
    );
  }

  if (stage === 'writer') {
    return (
      <section className={styles.chartGrid}>
        <div className={styles.panel}>
          <h2>{t("Decision distribution")}</h2>
          <HorizontalBarChart rows={countRows(services, 'writer', 'decision_counts')} />
        </div>
        <div className={styles.panel}>
          <h2>{t("Summary scope")}</h2>
          <HorizontalBarChart rows={countRows(services, 'writer', 'summary_scope_counts')} />
        </div>
      </section>
    );
  }

  return null;
}

function RecentRunsTable({runs, services}) {
  const t = useCopy();
  const serviceKeys = new Set(services.map((service) => service.service_key));
  if (serviceKeys.size === 1) {
    const sortedServices = [...services].sort((left, right) => right.date.localeCompare(left.date));
    return (
      <section className={styles.panel}>
        <h2>{t("Recent service runs")}</h2>
        <div className={styles.tableWrap}>
          <table>
            <thead>
              <tr>
                <th>{t("Date")}</th>
                <th>{t("Service")}</th>
                <th>{t("Status")}</th>
                <th className={styles.numeric}>{t("Raw")}</th>
                <th className={styles.numeric}>{t("Candidates")}</th>
                <th className={styles.numeric}>{t("Writer-ready")}</th>
                <th className={styles.numeric}>{t("Published")}</th>
              </tr>
            </thead>
            <tbody>
              {sortedServices.map((service) => (
                <tr key={`${service.date}:${service.service_key}`}>
                  <td><DateCard value={service.date} /></td>
                  <td>
                    <ServiceLabel
                      serviceKey={service.service_key}
                      serviceName={service.service_name}
                    />
                  </td>
                  <td>
                    <StatusBadge status={service.collection?.status} />
                  </td>
                  <td className={styles.numeric}>{service.preprocessing?.raw_count || service.collection?.article_count || 0}</td>
                  <td className={styles.numeric}>{service.preprocessing?.candidate_count || 0}</td>
                  <td className={styles.numeric}>{service.enrichment?.writer_ready_count || 0}</td>
                  <td className={styles.numeric}>{service.writer?.published_count || 0}</td>
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
      <h2>{t("Recent runs")}</h2>
      <div className={styles.tableWrap}>
        <table>
          <thead>
            <tr>
              <th>{t("Date")}</th>
              <th>{t("Status")}</th>
              <th className={styles.numeric}>{t("Raw")}</th>
              <th className={styles.numeric}>{t("Candidates")}</th>
              <th className={styles.numeric}>{t("Writer-ready")}</th>
              <th className={styles.numeric}>{t("Published")}</th>
              <th>{t("Traces")}</th>
              <th>{t("Run")}</th>
            </tr>
          </thead>
          <tbody>
            {sortedRuns.map((run) => (
              <tr key={run.date}>
                <td><DateCard value={run.date} /></td>
                <td>
                  <StatusBadge status={run.status} />
                </td>
                <td className={styles.numeric}>{run.collection?.total_article_count || 0}</td>
                <td className={styles.numeric}>{run.preprocessing?.candidate_count || 0}</td>
                <td className={styles.numeric}>{run.enrichment?.writer_ready_count || 0}</td>
                <td className={styles.numeric}>{run.writer?.published_count || 0}</td>
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
  const t = useCopy();
  return (
    <div className={styles.card}>
      <span>{label}{METRIC_HINTS[label] && <Tooltip label={`${label} · ${t("About this metric")}`} content={t(METRIC_HINTS[label])} />}</span>
      <strong>{value}</strong>
    </div>
  );
}

function HorizontalBarChart({rows}) {
  const t = useCopy();
  const safeRows = rows.filter((row) => row.value > 0);
  const maxValue = Math.max(...safeRows.map((row) => row.value), 1);
  if (!safeRows.length) {
    return <p className={styles.emptyState}>{t("No metric data for the selected filter.")}</p>;
  }
  return (
    <div className={styles.barChart}>
      {safeRows.map((row) => (
        <div className={styles.barRow} key={row.label}>
          <span className={styles.barLabel}>
            {row.serviceKey ? (
              <ServiceLabel serviceKey={row.serviceKey} serviceName={row.label} />
            ) : (
              t(row.label)
            )}
          </span>
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
  const t = useCopy();
  const maxValue = Math.max(
    ...rows.flatMap((row) => row.values.map((value) => value.value)),
    1,
  );
  if (!rows.length) {
    return <p className={styles.emptyState}>{t("No service metric data for the selected filter.")}</p>;
  }
  return (
    <div className={styles.groupedChart}>
      <div className={styles.legend}>
        {rows[0]?.values.map((value, index) => (
          <span key={t(value.label)}>
            <i className={styles[`series${index}`]} />
            {t(value.label)}
          </span>
        ))}
      </div>
      {rows.map((row) => (
        <div className={styles.groupRow} key={row.label}>
          <span className={styles.groupLabel}>
            {row.serviceKey ? (
              <ServiceLabel serviceKey={row.serviceKey} serviceName={row.label} />
            ) : (
              t(row.label)
            )}
          </span>
          <div className={styles.groupBars}>
            {row.values.map((value, index) => (
              <div className={styles.groupBarLine} key={t(value.label)}>
                <span>{t(value.label)}</span>
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
  const t = useCopy();
  const sortedRows = [...rows].sort((left, right) => left.date.localeCompare(right.date));
  const values = sortedRows.map(value);
  const latest = values.at(-1) || 0;
  return (
    <div className={styles.panel}>
      <h2>{title}</h2>
      <Sparkline values={values} label={title} />
      <p className={styles.sparklineSummary}>
        {t("Latest")}: <strong>{latest}</strong> · {values.length} {t("Runs")}
      </p>
    </div>
  );
}

function Sparkline({values, label}) {
  const t = useCopy();
  if (!values.length) {
    return <p className={styles.emptyState}>{t("No trend data.")}</p>;
  }
  const maxValue = Math.max(...values, 1);
  const width = 320;
  const height = 88;
  const points = values
    .map((value, index) => {
      const x = values.length === 1 ? width / 2 : (index / (values.length - 1)) * width;
      const y = height - (value / maxValue) * (height - 10) - 5;
      return `${x},${y}`;
    })
    .join(' ');
  return (
    <svg className={styles.sparkline} viewBox={`0 0 ${width} ${height}`} role="img" aria-label={`${label}: ${values.join(", ")}`}>
      {values.length === 1 && <circle cx={width / 2} cy={height - (values[0] / maxValue) * (height - 10) - 5} r="4" fill="currentColor" />}
      <polyline points={points} fill="none" stroke="currentColor" strokeWidth="4" />
    </svg>
  );
}

function StatusBadge({status}) {
  const t = useCopy();
  const safeStatus = status || 'missing';
  return (
    <span className={`${styles.badge} ${styles[`status_${safeStatus}`] || ''}`}>
      {t(safeStatus)}
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
