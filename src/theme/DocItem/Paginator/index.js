import React from 'react';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import DocPaginator from '@theme/DocPaginator';
import {articlePagination} from '@site/src/lib/briefing-order.mjs';

export default function DocItemPaginator() {
  const {metadata} = useDoc();
  const {previous, next} = articlePagination(metadata);
  if (!previous && !next) return null;
  return <DocPaginator className="docusaurus-mt-lg" previous={previous} next={next} />;
}
