/* ========== IMAGES (placeholder SVGs with monospace label) ========== */
/* Toned, striped placeholders labeled for what should go there.
   Referenced as CSS variables. Swap for real photography when available. */
function placeholder({label, h1, h2, stripeOp = 0.05}){
  const svg = `
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 1000' preserveAspectRatio='xMidYMid slice'>
  <defs>
    <linearGradient id='g' x1='0' y1='0' x2='0' y2='1'>
      <stop offset='0' stop-color='${h1}'/>
      <stop offset='1' stop-color='${h2}'/>
    </linearGradient>
    <pattern id='s' width='14' height='14' patternUnits='userSpaceOnUse' patternTransform='rotate(22)'>
      <rect width='14' height='14' fill='transparent'/>
      <line x1='0' y1='0' x2='0' y2='14' stroke='#ffffff' stroke-opacity='${stripeOp}' stroke-width='1'/>
    </pattern>
    <radialGradient id='v' cx='50%' cy='45%' r='70%'>
      <stop offset='.55' stop-color='#000' stop-opacity='0'/>
      <stop offset='1' stop-color='#000' stop-opacity='.55'/>
    </radialGradient>
  </defs>
  <rect width='1600' height='1000' fill='url(#g)'/>
  <rect width='1600' height='1000' fill='url(#s)'/>
  <rect width='1600' height='1000' fill='url(#v)'/>
  <g font-family='JetBrains Mono, monospace' font-size='20' fill='#ffffff' fill-opacity='.55'>
    <text x='40' y='60'>[ image ]</text>
    <text x='40' y='960'>${label}</text>
  </g>
</svg>`.trim();
  return `url("data:image/svg+xml;utf8,${encodeURIComponent(svg)}")`;
}

const rootPrefix = document.body.dataset.root || '';
const img = (name) => `url("${rootPrefix}img/${name}")`;

const imgs = {
  hero:   img('hero-oak.jpg'),
  about:  img('lodge-exterior.jpg'),
  room1:  img('lodge-wide.jpg'),
  room2:  img('bunkhouse-porch.jpg'),
  room3:  img('dining-table.jpg'),
  j1:     img('pointer.jpg'),
  j2:     img('creek.jpg'),
  j3:     img('clays-station.jpg'),
  cta:    img('pond.jpg'),
};

const r = document.documentElement.style;
r.setProperty('--hero-img', imgs.hero);
r.setProperty('--about-img', imgs.about);
r.setProperty('--room1', imgs.room1);
r.setProperty('--room2', imgs.room2);
r.setProperty('--room3', imgs.room3);
r.setProperty('--j1', imgs.j1);
r.setProperty('--j2', imgs.j2);
r.setProperty('--j3', imgs.j3);
r.setProperty('--cta-img', imgs.cta);
r.setProperty('--news-img', img('pond.jpg'));

/* ========== BEHAVIOR ========== */

/* ---------- Slide-out drawer (extras menu) ---------- */
const drawer = document.getElementById('drawer');
const drawerBackdrop = document.getElementById('drawerBackdrop');
const menuBtn = document.getElementById('menuBtn');
const drawerClose = document.getElementById('drawerClose');
function openDrawer(){
  drawer.classList.add('open');
  drawerBackdrop.removeAttribute('hidden');
  requestAnimationFrame(() => drawerBackdrop.classList.add('open'));
  drawer.setAttribute('aria-hidden', 'false');
  menuBtn.setAttribute('aria-expanded', 'true');
  document.body.classList.add('menu-open');
  document.body.style.overflow = 'hidden';
}
function closeDrawer(){
  drawer.classList.remove('open');
  drawerBackdrop.classList.remove('open');
  drawer.setAttribute('aria-hidden', 'true');
  menuBtn.setAttribute('aria-expanded', 'false');
  document.body.classList.remove('menu-open');
  document.body.style.overflow = '';
  setTimeout(() => { if (!drawer.classList.contains('open')) drawerBackdrop.setAttribute('hidden', ''); }, 460);
}
if (menuBtn && drawer && drawerBackdrop){
  menuBtn.addEventListener('click', () => {
    drawer.classList.contains('open') ? closeDrawer() : openDrawer();
  });
  drawerClose.addEventListener('click', closeDrawer);
  drawerBackdrop.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && drawer.classList.contains('open')) closeDrawer(); });
  drawer.querySelectorAll('a').forEach(a => a.addEventListener('click', closeDrawer));
}

/* ---------- Announcement bar dismiss ---------- */
const announce = document.getElementById('announce');
const announceClose = document.getElementById('announceClose');
if (announce && announceClose){
  if (sessionStorage.getItem('rbh-announce-dismissed') === '1'){
    announce.classList.add('dismissed');
    document.documentElement.style.setProperty('--announce-h', '0px');
  }
  announceClose.addEventListener('click', () => {
    announce.classList.add('dismissed');
    document.documentElement.style.setProperty('--announce-h', '0px');
    try { sessionStorage.setItem('rbh-announce-dismissed', '1'); } catch(e){}
  });
}

/* ---------- Nav solid on scroll + sticky booking bar ---------- */
const nav = document.getElementById('nav');
const bookbar = document.getElementById('bookbar');
let bbDismissed = false;
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  nav.classList.toggle('solid', y > 60);
  if (!bbDismissed) {
    bookbar.classList.toggle('visible', y > window.innerHeight * 0.85);
  }
});
const bbClose = document.getElementById('bbClose');
if (bbClose) bbClose.addEventListener('click', () => {
  bbDismissed = true; bookbar.classList.remove('visible');
});

/* ---------- Hero still: photography carries the open. Film is a CTA. ---------- */

/* ---------- Hero word rotator ---------- */
const rotWords = document.querySelectorAll('.rot-word');
if (rotWords.length){
  let rotIdx = 0;
  setInterval(() => {
    const cur = rotWords[rotIdx];
    rotIdx = (rotIdx + 1) % rotWords.length;
    const next = rotWords[rotIdx];
    cur.classList.remove('active'); cur.classList.add('leaving');
    setTimeout(() => cur.classList.remove('leaving'), 700);
    next.classList.add('active');
  }, 2600);
}

/* ---------- Reveal on scroll ---------- */
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, {threshold: 0.12});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

/* ---------- Animated counters ----------
   Replace the element's content with a text node + the preserved <sup>.
   Only the number (computed locally) is ever assigned as text. */
const counters = document.querySelectorAll('[data-counter]');
const cio = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const target = parseInt(el.dataset.counter, 10);
    const sup = el.querySelector('sup');
    const numNode = document.createTextNode('0');
    el.replaceChildren(numNode);
    if (sup) el.appendChild(sup);
    const fmt = (n) => n.toLocaleString('en-US');
    const dur = 1800;
    const start = performance.now();
    function step(now){
      const t = Math.min(1, (now - start)/dur);
      const eased = 1 - Math.pow(1 - t, 3);
      numNode.nodeValue = fmt(Math.round(target * eased));
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
    cio.unobserve(el);
  });
}, {threshold: 0.4});
counters.forEach(el => cio.observe(el));

/* ---------- Hover parallax on .tilt cards ---------- */
document.querySelectorAll('.tilt').forEach(card => {
  if (card.classList.contains('hunt-card')) return;  // hunt grid sits still
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left)/rect.width - 0.5;
    const y = (e.clientY - rect.top)/rect.height - 0.5;
    card.style.transform = `perspective(900px) rotateY(${x*3}deg) rotateX(${-y*3}deg) translateZ(0)`;
  });
  card.addEventListener('mouseleave', () => { card.style.transform = ''; });
});

/* ---------- Testimonial slider ---------- */
const slides = document.querySelectorAll('.q-slide');
const dots = document.querySelectorAll('.q-dot');
let qi = 0;
function go(i){
  qi = (i + slides.length) % slides.length;
  slides.forEach((s,k) => s.classList.toggle('active', k===qi));
  dots.forEach((d,k) => d.classList.toggle('active', k===qi));
}
const qPrev = document.getElementById('qPrev');
const qNext = document.getElementById('qNext');
if (qPrev) qPrev.addEventListener('click', () => go(qi-1));
if (qNext) qNext.addEventListener('click', () => go(qi+1));
dots.forEach(d => d.addEventListener('click', () => go(+d.dataset.i)));
if (slides.length) setInterval(() => go(qi+1), 7000);

/* ---------- Newsletter popup at 10% scroll ---------- */
const newsModal = document.getElementById('newsModal');
const newsBackdrop = document.getElementById('newsBackdrop');
const newsClose = document.getElementById('newsClose');
const newsForm = document.getElementById('newsForm');
const newsThanks = document.getElementById('newsThanks');
const NEWS_KEY = 'rbh-news-shown';
let newsShown = false;

function openNews(){
  if (newsShown) return;
  if (sessionStorage.getItem(NEWS_KEY) === '1') { newsShown = true; return; }
  newsShown = true;
  try { sessionStorage.setItem(NEWS_KEY, '1'); } catch(e){}
  newsModal.hidden = false;
  newsBackdrop.hidden = false;
  newsModal.setAttribute('aria-hidden', 'false');
  requestAnimationFrame(() => {
    newsBackdrop.classList.add('open');
    newsModal.classList.add('open');
  });
}
function closeNews(){
  newsModal.classList.remove('open');
  newsBackdrop.classList.remove('open');
  newsModal.setAttribute('aria-hidden', 'true');
  setTimeout(() => {
    newsModal.hidden = true;
    newsBackdrop.hidden = true;
  }, 420);
}

if (newsModal){
  const onScrollNews = () => {
    const doc = document.documentElement;
    const max = (doc.scrollHeight - window.innerHeight) || 1;
    const pct = window.scrollY / max;
    if (pct >= 0.10) {
      openNews();
      window.removeEventListener('scroll', onScrollNews);
    }
  };
  /* Luxury: no interrupt. The list is offered, never forced. */
  newsClose.addEventListener('click', closeNews);
  newsBackdrop.addEventListener('click', closeNews);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && newsModal.classList.contains('open')) closeNews();
  });
  newsForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('newsEmail');
    const phone = document.getElementById('newsPhone');
    const name = document.getElementById('newsName');
    if (!name.value.trim() || !email.checkValidity() || !phone.value.trim()){
      [name, email, phone].forEach(f => { if (!f.checkValidity() || !f.value.trim()) f.style.borderColor = '#b8381f'; });
      return;
    }
    newsForm.hidden = true;
    newsThanks.hidden = false;
    setTimeout(closeNews, 4200);
  });
}

const inquire = document.getElementById('inquireForm');
if (inquire){
  inquire.addEventListener('submit', (e) => {
    e.preventDefault();
    const fd = new FormData(inquire);
    const body = [...fd.entries()].map(([k,v]) => `${k}: ${v}`).join('\n');
    const mail = `mailto:Hunting@RedBankOutfitters.com?subject=${encodeURIComponent('Hunt inquiry — Red Bank Outfitters')}&body=${encodeURIComponent(body)}`;
    inquire.classList.add('sent');
    window.location.href = mail;
  });
}

/* ---------- Smooth anchor scroll ---------- */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    const id = a.getAttribute('href');
    if (id.length < 2) return;
    const t = document.querySelector(id);
    if (!t) return;
    e.preventDefault();
    window.scrollTo({top: t.getBoundingClientRect().top + window.scrollY - 60, behavior:'smooth'});
  });
});

/* ==========================================================================
   HERO VIDEO + FLOATING UI
   Injected at runtime so all 25 pages get it with no HTML edits.
   (Astro serves this file from public/ — it is never rewritten by the build.)
   ========================================================================== */
(function () {
  'use strict';

  var ROOT  = document.body.dataset.root || '';
  var PHONE = '(530) 529-9435';
  var TEL   = '+15305299435';
  var EMAIL = 'Hunting@RedBankOutfitters.com';
  var ADDR  = '18875 Red Bank Rd., Red Bluff CA 96080';
  var href  = function (p) { return ROOT + p; };

  /* ---------------- 1. Hero flythrough video ---------------- */
  (function heroVideo() {
    var hero = document.querySelector('header.hero');
    if (!hero) return;                                   // page-heroes keep their stills
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    /* Phones get a lighter 720p cut rather than being excluded. Still bail
       out on Save-Data or a genuinely slow link. */
    var conn = navigator.connection;
    if (conn && (conn.saveData || /^(slow-)?2g$/.test(conn.effectiveType || ''))) return;
    var small = window.matchMedia('(max-width: 899px)').matches;

    var wrap = document.createElement('div');
    wrap.className = 'hero-video';
    var v = document.createElement('video');
    v.muted = true; v.defaultMuted = true;
    v.loop = true; v.autoplay = true; v.playsInline = true;
    v.setAttribute('muted', '');
    v.setAttribute('playsinline', '');
    v.setAttribute('aria-hidden', 'true');
    v.preload = 'metadata';
    v.poster = href('img/flythrough-poster.jpg');
    v.src = href(small ? 'video/lodge-flythrough-mobile.mp4' : 'video/lodge-flythrough.mp4');
    wrap.appendChild(v);
    hero.insertBefore(wrap, hero.firstChild);

    v.addEventListener('playing', function () { hero.classList.add('video-ready'); });
    /* Deliberately no 'pause' handler that hides the video: browsers park
       background video intermittently, and dropping the class each time
       would cross-fade the hero back and forth. A paused video just holds
       its frame, which is fine. Only a real load error falls back. */
    v.addEventListener('error', function () { hero.classList.remove('video-ready'); });
    v.addEventListener('pause', function () { setTimeout(attempt, 400); });

    /* Browsers may refuse or pause a muted background video (Chrome parks
       video-only media to save power when the tab is hidden). Never delete
       the element for that — the still stays visible underneath, and we
       simply try again when the page is shown or the user interacts. */
    function attempt() {
      if (!v.paused) return;
      var pr = v.play();
      if (pr && pr.catch) pr.catch(function () {});
    }
    attempt();
    document.addEventListener('visibilitychange', function () {
      if (!document.hidden) attempt();
    });
    ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (evt) {
      window.addEventListener(evt, attempt, { once: true, passive: true });
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) attempt(); else v.pause(); });
      }, { threshold: 0.1 }).observe(hero);
    }
  })();

  /* ---------------- 2. Header phone button + call popover ---------------- */
  (function callButton() {
    var navRight = document.querySelector('.nav-right');
    if (!navRight) return;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'call-btn';
    btn.setAttribute('aria-label', 'Call the lodge — ' + PHONE);
    btn.setAttribute('aria-expanded', 'false');
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 ' +
      '19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91' +
      'a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>';

    var pop = document.createElement('div');
    pop.className = 'rb-panel call-pop';
    pop.innerHTML =
      '<button class="rb-x" type="button" aria-label="Close">&times;</button>' +
      '<span class="rb-k">Call us</span>' +
      '<a class="num" href="tel:' + TEL + '">' + PHONE + '</a>' +
      '<p>Hunts and lodging are by reservation.</p>' +
      '<p class="dim">' + ADDR + '</p>' +
      '<div class="rule"></div>' +
      '<a class="row" href="' + href('contact') + '">Request information <span>&rarr;</span></a>' +
      '<a class="row" href="mailto:' + EMAIL + '">Or send an email <span>&rarr;</span></a>';

    navRight.insertBefore(btn, navRight.querySelector('.menu-btn') || null);
    navRight.appendChild(pop);
    navRight.style.position = navRight.style.position || 'relative';

    function setOpen(on) {
      pop.classList.toggle('open', on);
      btn.setAttribute('aria-expanded', String(on));
    }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(!pop.classList.contains('open'));
    });
    pop.addEventListener('click', function (e) { e.stopPropagation(); });
    pop.querySelector('.rb-x').addEventListener('click', function () { setOpen(false); });
    document.addEventListener('click', function () { setOpen(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  })();

  /* ---------------- 3. Concierge chat (bottom right) ----------------
     Answers from the ranch's own published facts. This is a scripted
     concierge, not a live language model: a static site on GitHub Pages
     has no server to hold an API key. Wire KB to a serverless proxy to
     make it live. Nothing here invents rates, seasons or guarantees. */
  (function chat() {
    var KB = [
      { k: ['rate','price','cost','how much','pricing','fee','deposit'],
        a: '<strong>Personalized experiences.</strong> Rates are quoted by telephone — the price depends on the hunt, the party size and the dates. Call <a href="tel:' + TEL + '">' + PHONE + '</a> or see the <a href="' + href('rates') + '">rates page</a>.' },
      { k: ['quail','bobwhite','valley','mountain'],
        a: 'Three quail: <a href="' + href('upland/bobwhite') + '">bobwhite</a> southern-style over dogs, <a href="' + href('upland/valley-quail') + '">valley quail</a> and <a href="' + href('upland/mountain-quail') + '">mountain quail</a>. Quail has been the point of this ranch since 1965.' },
      { k: ['chukar','pheasant','turkey','european','driven','upland','bird'],
        a: 'Upland runs to seven birds — quail, <a href="' + href('upland/chukar') + '">chukar</a>, <a href="' + href('upland/pheasant') + '">pheasant</a>, <a href="' + href('upland/turkey') + '">wild turkey</a> and a <a href="' + href('upland/european-drive') + '">European driven shoot</a>. The full list is on the <a href="' + href('upland') + '">upland page</a>.' },
      { k: ['deer','blacktail','black-tail','big game','elk'],
        a: 'Black-tail deer and wild hog are the big game here — see <a href="' + href('hunts/blacktail') + '">blacktail</a> and <a href="' + href('hunts/wild-hog') + '">wild hog</a>.' },
      { k: ['hog','pig','boar'],
        a: '<a href="' + href('hunts/wild-hog') + '">Wild hog</a> is hunted across the 18,000 acres. Call the lodge for current conditions.' },
      { k: ['bass','fish','fishing','pond'],
        a: 'Eleven ponds hold bass — details on the <a href="' + href('bass') + '">bass fishing page</a>.' },
      { k: ['clay','sporting','shotgun','station','trap','skeet'],
        a: 'An 18-station <a href="' + href('clays') + '">sporting clays</a> course runs through the ranch.' },
      { k: ['dog','kennel','pointer','retriev'],
        a: 'The ranch keeps its own dogs and <a href="' + href('kennels') + '">kennels</a> on site, so you do not need to bring one.' },
      { k: ['lodge','sleep','stay','room','accommodat','bed','bunk'],
        a: 'The <a href="' + href('lodge') + '">lodge</a> sleeps fourteen with three showers and a full kitchen; the <a href="' + href('bunkhouse') + '">bunkhouse</a> sleeps six. Groups are never mixed — the house is yours.' },
      { k: ['eat','food','meal','dining','dinner','cook','chef','breakfast'],
        a: 'Meals are served in the lodge — see <a href="' + href('dining') + '">dining</a>.' },
      { k: ['wedding','event','venue','marry','reception'],
        a: 'The ranch hosts weddings and events. The <a href="' + href('weddings') + '">weddings page</a> has the detail, then call to hold a date.' },
      { k: ['where','address','direction','located','location','map','drive','red bluff'],
        a: 'Red Bank Outfitters is at ' + ADDR + ' — 18,000 acres west of Red Bluff on Red Bank Creek. Full detail on the <a href="' + href('contact') + '">contact page</a>.' },
      { k: ['season','when','date','open','availab','book','reserv','calendar'],
        a: 'Season dates and availability are handled by phone — call <a href="tel:' + TEL + '">' + PHONE + '</a>. Hunts and lodging are by reservation.' },
      { k: ['group','party','minimum','how many','people','size','solo','alone'],
        a: 'There is no minimum party size, and groups are not mixed with strangers. The lodge holds fourteen, the bunkhouse six.' },
      { k: ['contact','phone','call','email','reach','number','talk'],
        a: 'Call <a href="tel:' + TEL + '">' + PHONE + '</a> or email <a href="mailto:' + EMAIL + '">' + EMAIL + '</a>.' },
      { k: ['acre','big','size of','how large','ranch','land','history','1965','old'],
        a: 'Eighteen thousand acres west of Red Bluff, in the family and hunted since 1965. More on <a href="' + href('the-ranch') + '">the ranch</a>.' },
      { k: ['academy','kid','youth','camp','class','learn','course'],
        a: 'Youth and instruction run through the <a href="https://redbankoutdooracademy.com/" target="_blank" rel="noopener">Red Bank Outdoor Academy</a>.' },
      { k: ['photo','gallery','picture','image','video','film','see'],
        a: 'The <a href="' + href('gallery') + '">gallery</a> has photographs of the ranch and the lodge.' },
      { k: ['licen','tag','legal','regulat','permit'],
        a: 'Licensing and tags depend on the species and the season — the lodge will walk you through it. Call <a href="tel:' + TEL + '">' + PHONE + '</a>.' },
      { k: ['hello','hi','hey','howdy','good morning','good evening'],
        a: 'Good day. Ask me about the birds, the big game, the lodge or getting here — or call <a href="tel:' + TEL + '">' + PHONE + '</a>.' },
      { k: ['thank','thanks','appreciate','cheers'],
        a: 'A pleasure. Call <a href="tel:' + TEL + '">' + PHONE + '</a> whenever you are ready to put dates down.' }
    ];
    var FALLBACK = 'I can only speak to what is published here — the hunts, the lodge, the ranch and how to reach it. For anything else, the lodge will know: <a href="tel:' + TEL + '">' + PHONE + '</a> or <a href="' + href('contact') + '">request information</a>.';

    function answer(q) {
      var s = q.toLowerCase(), best = null, score = 0;
      KB.forEach(function (e) {
        var n = 0;
        e.k.forEach(function (kw) { if (s.indexOf(kw) !== -1) n += kw.length; });
        if (n > score) { score = n; best = e; }
      });
      return best ? best.a : FALLBACK;
    }

    var fab = document.createElement('button');
    fab.type = 'button';
    fab.className = 'rb-fab chat-fab';
    fab.setAttribute('aria-label', 'Open the ranch concierge');
    fab.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
      'stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 ' +
      '8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 ' +
      '8.48 0 0 1 8 8v.5z"/></svg><span class="lbl">Ask the ranch</span>';

    var panel = document.createElement('div');
    panel.className = 'rb-panel chat-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Ranch concierge');
    panel.innerHTML =
      '<div class="chat-head">' +
        '<button class="rb-x" type="button" aria-label="Close">&times;</button>' +
        '<span class="rb-k">Red Bank</span>' +
        '<h3>Ask us a question</h3>' +
      '</div>' +
      '<div class="chat-log" id="rbChatLog" aria-live="polite"></div>' +
      '<div class="chat-chips">' +
        '<button type="button">What birds do you have?</button>' +
        '<button type="button">What does it cost?</button>' +
        '<button type="button">Where are you?</button>' +
        '<button type="button">Where do we sleep?</button>' +
      '</div>' +
      '<form class="chat-form"><input type="text" autocomplete="off" placeholder="Ask about the ranch…" ' +
      'aria-label="Ask about the ranch"><button type="submit">Send</button></form>' +
      '<div class="chat-actions">' +
        '<a class="ca" href="tel:' + TEL + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call ' + PHONE + '</a>' +
        '<a class="ca" href="' + href('contact') + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>Contact form</a>' +
      '</div>' +
      '<div class="chat-foot"><strong>Lasso</strong> · Powered by AI Wrangler</div>';

    document.body.appendChild(fab);
    document.body.appendChild(panel);

    var log = panel.querySelector('.chat-log');
    var form = panel.querySelector('.chat-form');
    var input = panel.querySelector('.chat-form input');

    function push(html, who) {
      var d = document.createElement('div');
      d.className = 'msg ' + who;
      d.innerHTML = html;
      log.appendChild(d);
      log.scrollTop = log.scrollHeight;
      return d;
    }
    function ask(q) {
      push(q.replace(/[<>]/g, ''), 'me');
      var t = push('<span></span><span></span><span></span>', 'bot typing');
      setTimeout(function () { t.remove(); push(answer(q), 'bot'); }, 420);
    }
    function setOpen(on) {
      panel.classList.toggle('open', on);
      fab.classList.toggle('hidden', on);
      if (on) {
        if (!log.children.length) {
          push('Welcome to Red Bank. Ask about the hunts, the lodge or how to find us — or call <a href="tel:' + TEL + '">' + PHONE + '</a>.', 'bot');
        }
        setTimeout(function () { input.focus(); }, 260);
      }
    }
    fab.addEventListener('click', function () { setOpen(true); });
    panel.querySelector('.rb-x').addEventListener('click', function () { setOpen(false); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var q = input.value.trim();
      if (!q) return;
      input.value = '';
      ask(q);
    });
    panel.querySelectorAll('.chat-chips button').forEach(function (b) {
      b.addEventListener('click', function () { ask(b.textContent); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('open')) setOpen(false);
    });
  })();

  /* ---------------- 4. Newsletter tab (bottom left) ----------------
     No backend on GitHub Pages, so the address is held in this browser
     only and never transmitted. Point ENDPOINT at a form service
     (Formspree, Buttondown, Mailchimp) to start actually collecting. */
  (function newsletter() {
    var ENDPOINT = null;                       // e.g. 'https://formspree.io/f/xxxxxxx'
    var STORE = 'rb-newsletter';

    var tab = document.createElement('button');
    tab.type = 'button';
    tab.className = 'rb-fab news-tab';
    tab.textContent = 'The Journal';
    tab.setAttribute('aria-label', 'Subscribe to the Red Bank journal');

    var panel = document.createElement('div');
    panel.className = 'rb-panel news-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Subscribe to the journal');
    panel.innerHTML =
      '<button class="rb-x" type="button" aria-label="Close">&times;</button>' +
      '<span class="rb-k">The Journal</span>' +
      '<h3>Word from the ranch.</h3>' +
      '<p>Season openings, bird counts and the odd photograph. A few times a year — never more.</p>' +
      '<form class="news-form">' +
        '<input type="email" required autocomplete="email" placeholder="you@example.com" aria-label="Email address">' +
        '<button type="submit">Subscribe</button>' +
      '</form>' +
      '<div class="news-note">Preview build — this form is not yet wired to a mailing list.</div>';

    document.body.appendChild(tab);
    document.body.appendChild(panel);

    function setOpen(on) { panel.classList.toggle('open', on); }
    tab.addEventListener('click', function () { setOpen(!panel.classList.contains('open')); });
    panel.querySelector('.rb-x').addEventListener('click', function () { setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('open')) setOpen(false);
    });

    panel.querySelector('.news-form').addEventListener('submit', function (e) {
      e.preventDefault();
      var email = panel.querySelector('input[type=email]').value.trim();
      if (!email) return;
      var done = function () {
        panel.querySelector('.news-form').remove();
        panel.querySelector('.news-note').remove();
        var ok = document.createElement('p');
        ok.className = 'news-ok';
        ok.textContent = 'Thank you — we have you down. The lodge will be in touch before the season.';
        panel.appendChild(ok);
      };
      try { localStorage.setItem(STORE, email); } catch (err) {}
      if (!ENDPOINT) { done(); return; }
      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ email: email })
      }).then(done).catch(done);
    });
  })();

})();

/* ---------- Cookie consent (mirrors the C2 pattern: privacy-first, GPC-aware) ---------- */
(function () {
  var STORAGE_KEY = 'rbo-consent';
  var banner = document.getElementById('consent-banner');
  if (!banner) return;

  function readChoice() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; }
  }
  function writeChoice(value) {
    try { localStorage.setItem(STORAGE_KEY, value); } catch (_) {}
    window.__rboConsent = value;
    window.dispatchEvent(new CustomEvent('rbo:consent', { detail: { choice: value } }));
  }
  function show() { banner.classList.remove('hidden'); }
  function hide() { banner.classList.add('hidden'); }

  /* Global Privacy Control counts as a standing reject; the visitor can override. */
  var gpc = (navigator.globalPrivacyControl === true);
  var initial = readChoice();
  window.__rboConsent = initial || (gpc ? 'rejected' : null);

  if (!initial) { setTimeout(show, 600); }

  banner.querySelector('[data-consent-accept]').addEventListener('click', function () {
    writeChoice('accepted'); hide();
  });
  banner.querySelector('[data-consent-reject]').addEventListener('click', function () {
    writeChoice('rejected'); hide();
  });

  document.querySelectorAll('[data-open-consent]').forEach(function (el) {
    el.addEventListener('click', function (e) { e.preventDefault(); show(); });
  });
})();

/* ---------- Floating mobile menu bar (Tehama pattern) ---------- */
(function () {
  if (document.getElementById('rbMobileBar')) return;
  var ROOT = document.body.getAttribute('data-root') || '';
  function href(p) { return ROOT + p; }
  var S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"';
  var bar = document.createElement('nav');
  bar.id = 'rbMobileBar';
  bar.className = 'mob-bar';
  bar.setAttribute('aria-label', 'Quick navigation');
  bar.innerHTML =
    '<a href="' + href('') + '"><svg viewBox="0 0 24 24" ' + S + '><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg><span>Home</span></a>' +
    '<a href="' + href('hunts') + '"><svg viewBox="0 0 24 24" ' + S + '><circle cx="12" cy="12" r="7"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg><span>Hunts</span></a>' +
    '<a class="mb-center" href="' + href('contact') + '"><span class="circ"><svg viewBox="0 0 24 24" ' + S + '><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></span><span>Book</span></a>' +
    '<a href="' + href('lodge') + '"><svg viewBox="0 0 24 24" ' + S + '><path d="M2 20v-8a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8"/><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"/><path d="M2 17h20"/></svg><span>Lodge</span></a>' +
    '<button type="button" data-mob-chat><svg viewBox="0 0 24 24" ' + S + '><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg><span>Chat</span></button>';
  document.body.appendChild(bar);
  bar.querySelector('[data-mob-chat]').addEventListener('click', function () {
    var fab = document.querySelector('.chat-fab');
    if (fab) fab.click();
  });
})();

/* ---------- Fading parallax bands (lodge page) ---------- */
(function () {
  var mobile = window.matchMedia('(max-width: 900px)').matches;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.parallax-fade, .img-fade').forEach(function (wrap) {
    var layers = wrap.querySelectorAll('.pf, .ph');
    if (!layers.length) return;
    layers[0].classList.add('on');
    if (layers.length < 2 || reduced) return;
    /* The band above Experience only rotates on phones; on desktop it
       holds its first frame and the lower band does the fading. */
    if (wrap.classList.contains('pfade-mobile') && !mobile) return;
    var i = 0;
    setInterval(function () {
      layers[i].classList.remove('on');
      i = (i + 1) % layers.length;
      layers[i].classList.add('on');
    }, 5000);
  });
})();
