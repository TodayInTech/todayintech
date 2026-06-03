// @ts-check

const config = {
  title: 'Today in Tech',
  tagline: 'AI-curated technology news briefings',
  favicon: 'img/favicon.ico',

  url: 'https://todayintech.github.io',
  baseUrl: '/todayintech/',

  organizationName: 'TodayInTech',
  projectName: 'todayintech',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'ko',
    locales: ['ko', 'en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Today in Tech',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'briefingSidebar',
          position: 'left',
          label: 'Briefings',
        },
      ],
    },
  },
};

export default config;
