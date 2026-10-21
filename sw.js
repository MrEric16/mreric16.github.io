// Service worker for Mr Eric's Lounge — caches the app shell so it still opens with no signal.
// Live data (weather, on-this-day, news links, videos) still needs a connection — the app
// already shows a "couldn't load" message gracefully in those spots when offline.
//
// STRATEGY: network-first, cache as fallback. This matters — cache-first would mean every
// push takes an extra reload to actually show up, since the stale cached copy would always
// win on the first load after a change. Network-first means you always get the latest push
// immediately when there's a connection; the cache only kicks in when there's genuinely none.

const CACHE_NAME = 'erics-lounge-v7';
const SHELL_FILES = [
  './',
  './index.html',
  './vocabulary.html',
  './grammar.html',
  './connections.html',
  './spellingbee.html',
  './writing.html',
  './writing-hub.html',
  './writing-models.html',
  './writing-band9.html',
  './mocktimer.html',
  './collocations.html',
  './wordforms.html',
  './speaking.html',
  './listening.html',
  './tashkent-route.html',
  './tashkent-today.html',
  './data/tashkent-transit.json',
  './lounge-core.js',
  './theme-pages.css',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(SHELL_FILES))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isShellFile = url.origin === self.location.origin;

  if (isShellFile) {
    // Same freshness as before (always checked with the server), but without throwing away the
    // browser's saved copy: pages and data files are revalidated (a tiny "unchanged" reply when
    // nothing moved, instead of re-downloading the whole file); images and audio may reuse the
    // browser cache. version.json stays strictly no-store - it is the update detector.
    const isVersion = url.pathname.endsWith('/version.json');
    const isMedia = /\.(png|jpe?g|gif|webp|svg|ico|mp3|m4a|ogg|wav|woff2?)$/i.test(url.pathname);
    // Grammar data is versioned by ?v=, so the browser's own copy is always right: reuse it.
    const isGrammarData = url.pathname.indexOf('/data/grammar/') !== -1;
    const mode = isVersion ? 'no-store' : ((isMedia || isGrammarData) ? 'default' : 'no-cache');
    event.respondWith(
      fetch(req, { cache: mode })
        .then((res) => {
          if (res && res.status === 200 && !req.headers.has('range')) {
            caches.open(CACHE_NAME).then((cache) => cache.put(req, res.clone()));
          }
          return res;
        })
        .catch(() =>
          caches.match(req, { ignoreSearch: true }).then((hit) =>
            hit || (req.mode === 'navigate' ? caches.match('./index.html', { ignoreSearch: true }) : undefined)
          )
        )
    );
  }
  // Everything else (weather API, Wikipedia, YouTube, news sites) — just let it
  // hit the network normally. No point caching data that changes every visit.
});
