/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

// List of projects/orgs using your project for the users page.
const users = [
  {
    caption: "IIT Palakkad",
    // You will need to prepend the image path with your baseUrl
    // if it is not '/', like: '/test-site/img/image.jpg'.
    image: "/img/logo.png",
    infoLink: "https://iitpkd.ac.in",
    pinned: true
  }
];

const siteConfig = {
  title: "MuftEducation", // Title for your website.
  tagline: "Free Open Source Education",
  url: "https://www.mufteducation.in", // Your website URL
  baseUrl: "/", // Base URL for your project */
  // For github.io type URLs, you would set the url and baseUrl like:
  //   url: 'https://facebook.github.io',
  //   baseUrl: '/test-site/',

  // Used for publishing and more
  projectName: "MuftEducation",
  organizationName: "Sourabh",
  // For top-level user or org sites, the organization is still the same.
  // e.g., for the https://JoelMarcey.github.io site, it would be set like...
  //   organizationName: 'JoelMarcey'
  editUrl: "https://github.com/sourabh2311/MuftEducation.in/tree/master/docs/",
  // For no header links in the top nav bar -> headerLinks: [],
  headerLinks: [
    { doc: "courses", label: "Courses" },
    {
      href: "https://github.com/sourabh2311/MuftEducation.in",
      label: "GitHub"
    },
    { doc: "contribute", label: "How To Contribute" },
    { search: true }
  ],

  // If you have users set above, you add it here:
  users,

  /* path to images for header/footer */
  headerIcon: "img/favicons.png",
  footerIcon: "img/favicons.png",
  favicon: "img/favicons.png",

  /* Colors for website */
  colors: {
    primaryColor: "#0e6d4b",
    secondaryColor: "#094c34"
  },

  /* Custom fonts for website */
  /*
  fonts: {
    myFont: [
      "Times New Roman",
      "Serif"
    ],
    myOtherFont: [
      "-apple-system",
      "system-ui"
    ]
  },
  */

  // This copyright info is used in /core/Footer.js and blog RSS/Atom feeds.
  copyright: `Copyright © ${new Date().getFullYear()} MuftEducation.in`,

  highlight: {
    // Highlight.js theme to use for syntax highlighting in code blocks.
    theme: "default"
  },

  // Add custom scripts here that would be placed in <script> tags.
  scripts: [
    "https://buttons.github.io/buttons.js",
    "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML",
    "/js/mathjax-config.js",
    "https://buttons.github.io/buttons.js"
  ],
  // On page navigation for the current documentation page.
  onPageNav: "separate",
  // No .html extensions for paths.
  cleanUrl: true,

  // Open Graph and Twitter card images.
  ogImage: "img/undraw_online.svg",
  twitterImage: "img/undraw_tweetstorm.svg",

  // Show documentation's last contributor's name.
  enableUpdateBy: true,

  // Show documentation's last update time.
  enableUpdateTime: true,

  // You may provide arbitrary config keys to be used as needed by your
  // template. For example, if you need your repo's URL...
  repoUrl: "https://github.com/sourabh2311/MuftEducation.in",
  markdownPlugins: [
    // Highlight admonitions.
    require("remarkable-admonitions")({ icon: "svg-inline" })
  ]
};

module.exports = siteConfig;
