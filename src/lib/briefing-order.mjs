export function compareBriefings(left, right) {
  const date = (item) => {
    const value = Date.parse(item.briefed_at || item.published_at || '');
    return Number.isNaN(value) ? 0 : value;
  };
  const byDate = date(right) - date(left);
  const byScore = (Number(right.score) || 0) - (Number(left.score) || 0);
  const normalizedPath = (item) => (item.href || '').replace(/^\.\//, '').replace(/\.mdx?$/, '');
  const leftPath = normalizedPath(left);
  const rightPath = normalizedPath(right);
  return byDate || byScore || (leftPath < rightPath ? -1 : leftPath > rightPath ? 1 : 0);
}

export function articlePagination(metadata) {
  const parts = metadata.id.split('/');
  if (parts[0] !== 'services' || parts.length < 3) return {};
  const currentPath = metadata.permalink.replace(/\/+$/, '');
  const prefix = currentPath.slice(0, currentPath.lastIndexOf('/') + 1);
  const sameService = (entry) => {
    if (!entry?.permalink.startsWith(prefix)) return undefined;
    const suffix = entry.permalink.slice(prefix.length).replace(/\/+$/, '');
    return suffix && !suffix.includes('/') ? entry : undefined;
  };
  return {previous: sameService(metadata.previous), next: sameService(metadata.next)};
}
