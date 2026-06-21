// @ts-check

const config = {
  title: 'Today in Tech',
  tagline: 'AI-curated technology news briefings',
  favicon: 'img/brand/todayintech.light.svg',

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
      logo: {
        alt: 'Today in Tech',
        src: 'img/brand/todayintech.light.svg',
        srcDark: 'img/brand/todayintech.dark.svg',
        width: 32,
        height: 32,
      },
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
