import React from 'react';

import ServiceIcon from '@site/src/components/ServiceIcon';
import styles from './styles.module.css';

export default function ServiceHeader({serviceKey, title}) {
  return (
    <header className={styles.header}>
      <ServiceIcon serviceKey={serviceKey} label={title} iconOnly />
      <h1 className={styles.title}>{title}</h1>
    </header>
  );
}
