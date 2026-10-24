import assert from 'node:assert/strict';
import test from 'node:test';
import {articlePagination, compareBriefings} from '../../src/lib/briefing-order.mjs';

test('list and article order uses briefing date, source-date fallback, score and stable path', () => {
  const items = [
    {href: './services/a/z.md', briefed_at: '2026-10-20', score: 5},
    {href: './services/a/b.md', briefed_at: '2026-10-21', score: 5},
    {href: './services/a/a.md', briefed_at: '2026-10-21', score: 5},
    {href: './services/a/c.md', published_at: '2026-10-21', score: 8},
    {href: './services/a/unknown.md', published_at: 'invalid', score: 100},
  ];
  assert.deepEqual(items.sort(compareBriefings).map((item) => item.href), [
    './services/a/c.md', './services/a/a.md', './services/a/b.md',
    './services/a/z.md', './services/a/unknown.md',
  ]);
  assert.equal(compareBriefings({href: './services/a/a.md'}, {href: 'services/a/a'}), 0);
});

test('main, service indexes and every trace view have no article pagination', () => {
  for (const id of ['index', 'services/a', 'operations/index', 'operations/services',
    'operations/collection', 'operations/preprocessing', 'operations/enrichment', 'operations/writer']) {
    assert.deepEqual(articlePagination({id}), {});
  }
});

test('article navigation stays inside its service for both locales and at boundaries', () => {
  for (const locale of ['', 'en/']) {
    const base = `/todayintech/${locale}services/a/`;
    const previous = {permalink: `${base}newer/`, title: 'Newer'};
    const next = {permalink: `${base}older`, title: 'Older'};
    const metadata = {id: 'services/a/current', permalink: `${base}current/`, previous, next};
    assert.deepEqual(articlePagination(metadata), {previous, next});
    assert.deepEqual(articlePagination({...metadata, previous: {permalink: base}}),
      {previous: undefined, next});
    assert.deepEqual(articlePagination({...metadata, next: {permalink: base.replace('/a/', '/b/') + 'other'}}),
      {previous, next: undefined});
  }
});
