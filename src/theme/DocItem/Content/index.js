import React from 'react';
import Content from '@theme-original/DocItem/Content';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import Link from '@docusaurus/Link';
import {useLocation} from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function DocItemContent(props) {
  const {metadata} = useDoc();
  const {i18n} = useDocusaurusContext();
  const location = useLocation();
  const parts = metadata.id.split('/');
  const serviceUrl = `${metadata.permalink.split('/services/')[0]}/services/${parts[1] || ''}`;
  const localeRoot = useBaseUrl('/');
  const isArticle = parts[0] === 'services' && parts.length > 2;
  const origin = location.state?.briefingReturnTo;
  const returnTo = typeof origin === 'string' && origin.startsWith(localeRoot) && !origin.startsWith('//')
    ? origin : serviceUrl;
  if (!isArticle) return <Content {...props} />;
  const backLink = <Link className="article-return" to={returnTo}><span aria-hidden="true">←</span> {i18n.currentLocale === 'ko' ? '목록으로' : 'Back to articles'}</Link>;
  return <div className="article-reader">{backLink}<Content {...props} /></div>;
}
