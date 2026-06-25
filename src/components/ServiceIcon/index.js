import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

import styles from './styles.module.css';

const SERVICE_ICONS = {
  'hacker-news': {
    light: '/img/services/hacker-news.light.svg',
    dark: '/img/services/hacker-news.dark.svg',
  },
  'github-blog': {
    light: '/img/services/github-blog.light.svg',
    dark: '/img/services/github-blog.dark.svg',
  },
  'google-blog': {
    light: '/img/services/google-blog.light.svg',
    dark: '/img/services/google-blog.dark.svg',
  },
  'openai-blog': {
    light: '/img/services/openai-blog.light.svg',
    dark: '/img/services/openai-blog.dark.svg',
  },
  'anthropic-blog': {
    light: '/img/services/anthropic-blog.light.svg',
    dark: '/img/services/anthropic-blog.dark.svg',
  },
};

export default function ServiceIcon({serviceKey, label, href, iconOnly = false, size = 'default'}) {
  const iconPaths = SERVICE_ICONS[serviceKey];
  const lightIconUrl = useBaseUrl(iconPaths?.light || '/');
  const darkIconUrl = useBaseUrl(iconPaths?.dark || '/');
  const iconFrameClassName =
    size === 'compact' ? `${styles.iconFrame} ${styles.compactIconFrame}` : styles.iconFrame;
  const iconOnlyClassName =
    size === 'compact' ? `${styles.iconOnly} ${styles.compactIconOnly}` : styles.iconOnly;

  if (!iconPaths) {
    return href ? <a href={href}>{label}</a> : <span>{label}</span>;
  }

  const content = (
    <>
      <span className={iconFrameClassName}>
        <img
          className={`${styles.icon} ${styles.lightIcon}`}
          src={lightIconUrl}
          alt=""
          aria-hidden="true"
        />
        <img
          className={`${styles.icon} ${styles.darkIcon}`}
          src={darkIconUrl}
          alt=""
          aria-hidden="true"
        />
      </span>
      {!iconOnly && <span>{label}</span>}
    </>
  );

  if (href) {
    return (
      <a className={styles.serviceLink} href={href} aria-label={label}>
        {content}
      </a>
    );
  }

  return (
    <span
      className={iconOnly ? iconOnlyClassName : styles.serviceLabel}
      aria-label={iconOnly ? `${label} 브랜드 아이콘` : undefined}>
      {content}
    </span>
  );
}
