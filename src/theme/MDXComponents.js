import DateCard from '@site/src/components/DateCard';
import {MetadataQuote, MetadataListItem} from '@site/src/components/DateCard/MarkdownDates';
import MDXComponents from '@theme-original/MDXComponents';
import BriefingList from '@site/src/components/BriefingList';
import ServiceHeader from '@site/src/components/ServiceHeader';
import ServiceIcon from '@site/src/components/ServiceIcon';

export default {
  ...MDXComponents,
  DateCard,
  blockquote: MetadataQuote,
  li: MetadataListItem,
  BriefingList,
  ServiceHeader,
  ServiceIcon,
};
