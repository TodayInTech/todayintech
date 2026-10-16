import React from 'react';
import DateCard from './index';

// Keep archive Markdown and its feed extraction format intact; decorate metadata at render time.
function datesInMetadata(children) {
  return React.Children.map(children, (child) => {
    if (typeof child === 'string') {
      return child.split(/(\b\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?)?\b)/g)
        .map((part, index) => /^\d{4}-\d{2}-\d{2}/.test(part) ? <DateCard key={index} value={part} withTime={part.includes('T')} /> : part);
    }
    if (React.isValidElement(child) && child.props.children && !['code', 'a', 'pre'].includes(child.type)) {
      return React.cloneElement(child, {}, datesInMetadata(child.props.children));
    }
    return child;
  });
}

export function MetadataQuote({children, ...props}) {
  return <blockquote {...props}>{datesInMetadata(children)}</blockquote>;
}

export function MetadataListItem({children, ...props}) {
  const text = React.Children.toArray(children).filter((child) => typeof child === 'string').join('');
  return <li {...props}>{/수집일|Collected(?: at| on)?/.test(text) ? datesInMetadata(children) : children}</li>;
}
