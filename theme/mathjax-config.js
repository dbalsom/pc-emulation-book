// MathJax Configuration for mdbook
// This ensures formulas render correctly on all deployment platforms

window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams',
    packages: {'[+]': ['ams', 'newcommand', 'configmacros']}
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process'
  },
  startup: {
    ready: () => {
      console.log('MathJax is loaded and ready');
      MathJax.startup.defaultReady();
    }
  }
};

// Load MathJax from CDN
(function() {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js';
  script.async = true;
  document.head.appendChild(script);
})();