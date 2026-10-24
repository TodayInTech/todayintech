// @ts-check

import fs from 'node:fs';
import path from 'node:path';
import {compareBriefings} from './src/lib/briefing-order.mjs';

const docsDir = path.resolve('docs');
const servicesDir = path.join(docsDir, 'services');
const statePath = path.resolve('data/briefed_articles.json');
const archive = fs.existsSync(statePath)
  ? Object.values(JSON.parse(fs.readFileSync(statePath, 'utf8')).articles || {})
  : [];
const recordsByPath = new Map(archive.map((record) => [record.article_doc_path, record]));

function articleItems(articlePath, articleDir) {
  if (!fs.existsSync(articlePath)) return [];
  return fs.readdirSync(articlePath)
    .filter((fileName) => fileName.endsWith('.md') || fileName.endsWith('.mdx'))
    .map((fileName) => {
      const content = fs.readFileSync(path.join(articlePath, fileName), 'utf8');
      const record = recordsByPath.get(`docs/${articleDir}/${fileName}`);
      const publishedAt = content.match(/^>[^\n]*·\s*(\d{4}-\d{2}-\d{2})\s*·/m)?.[1];
      return {
        id: `${articleDir}/${fileName.replace(/\.mdx?$/, '')}`,
        href: `${articleDir}/${fileName.replace(/\.mdx?$/, '')}`,
        briefed_at: record?.briefed_at?.slice(0, 10),
        published_at: publishedAt,
        score: record?.candidate_score || 0,
      };
    })
    .sort(compareBriefings)
    .map(({id}) => ({type: 'doc', id}));
}

function frontMatterTitle(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^title:\s*(.+)$/m);
  if (!match) {
    return path.basename(filePath, '.md');
  }

  try {
    return JSON.parse(match[1]);
  } catch {
    return match[1].replace(/^["']|["']$/g, '');
  }
}

const serviceItems = fs
  .readdirSync(servicesDir)
  .filter((fileName) => fileName.endsWith('.md'))
  .sort()
  .map((fileName) => {
    const serviceKey = path.basename(fileName, '.md');
    const articleDir = `services/${serviceKey}`;
    const articlePath = path.join(docsDir, articleDir);

    return {
      type: 'category',
      label: frontMatterTitle(path.join(servicesDir, fileName)),
      className: `service-sidebar-item service-sidebar-${serviceKey}`,
      customProps: {
        serviceKey,
      },
      link: {
        type: 'doc',
        id: `services/${serviceKey}`,
      },
      items: articleItems(articlePath, articleDir),
    };
  });

const sidebars = {
  briefingSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Today in Tech',
      className: 'todayintech-sidebar-home',
    },
    ...serviceItems,
  ],
  operationsSidebar: [
    {
      type: 'doc',
      id: 'operations/index',
      label: '트레이스',
      className: 'operations-sidebar-item',
    },
    'operations/services',
    'operations/collection',
    'operations/preprocessing',
    'operations/enrichment',
    'operations/writer',
  ],
};

export default sidebars;
