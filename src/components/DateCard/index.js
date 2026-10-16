import React from 'react';
import styles from './styles.module.css';

export default function DateCard({value, label, withTime = false}) {
  if (!value) return <span className={styles.unknown}>—</span>;
  const raw = String(value);
  const match = raw.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (!match) return <span className={styles.unknown}>{raw}</span>;
  const clock = withTime && raw.match(/[T ](\d{2}:\d{2})/);
  const zone = /Z$|\+00:00$/.test(raw) ? ' UTC' : '';
  return <span className={styles.dateCard}>
    {label && <span className={styles.label}>{label}</span>}
    <time dateTime={raw}>{match.slice(1).join('.')}{clock && <span className={styles.clock}> · {clock[1]}{zone}</span>}</time>
  </span>;
}
