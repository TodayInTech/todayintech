import React from 'react';
import styles from './styles.module.css';

export default function LoadingSpinner({label}) {
  return (
    <div className={styles.loading} role="status" aria-label={label}>
      <span className={styles.spinner} aria-hidden="true" />
    </div>
  );
}
