#!/usr/bin/env python3
"""Red Bank Outfitters — static site. Copy is assembled from their published facts."""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE = "(530) 529-9435"
TEL = "tel:+15305299435"
EMAIL = "Hunting@RedBankOutfitters.com"
# Canonical origin for canonical tags, robots.txt and sitemap.xml.
# Change this one line when a custom domain is pointed at the site.
SITE_URL = "https://red-bank-outfitters.netlify.app"
# The ranch OS. Served at /os on this domain via a Netlify proxy rewrite,
# so it stays one URL for the client while deploying as its own project.
# Set to None until the OS is actually deployed — a Ranch Login that 404s
# on a live client site is worse than no link. Set it back to "/os" and
# rebuild the moment the proxy resolves.
OS_PATH = None

def r(depth, p):
    return ("../" * depth) + p

def nav(depth, active=""):
    p = lambda x: r(depth, x)
    def item(href, label, key):
        on = ' aria-current="page"' if active == key else ""
        return f'<a class="link" href="{href}"{on}>{label}</a>'
    return f'''
<nav class="nav" id="nav">
  <div class="nav-inner">
    <a class="logo" href="{p('index.html')}">
      <img class="mark" src="{p('img/mark.svg')}" alt="">
      <span class="logo-text">RED BANK <em>OUTFITTERS</em></span>
    </a>
    <div class="nav-center">
      <div class="nav-item has-menu">
        {item(p("upland.html"), 'Upland Game <span class="caret" aria-hidden="true">▾</span>', "upland")}
        <div class="submenu" role="menu">
          <a href="{p("upland/bobwhite.html")}">Southern-Style Bob White</a>
          <a href="{p("upland/valley-quail.html")}">Valley Quail</a>
          <a href="{p("upland/mountain-quail.html")}">Mountain Quail</a>
          <a href="{p("upland/chukar.html")}">Chukar</a>
          <a href="{p("upland/pheasant.html")}">Walk-Up Pheasant</a>
          <a href="{p("upland/european-drive.html")}">European-Style Drive</a>
          <a href="{p("upland/turkey.html")}">Wild Turkey</a>
        </div>
      </div>
      <div class="nav-item has-menu">
        {item(p("big-game.html"), 'Big Game <span class="caret" aria-hidden="true">▾</span>', "big")}
        <div class="submenu" role="menu">
          <a href="{p("hunts/blacktail.html")}">Blacktail Deer</a>
          <a href="{p("hunts/wild-hog.html")}">Wild Hog</a>
          <a href="{p("rates.html")}">Rates</a>
        </div>
      </div>
      <div class="nav-item has-menu">
        {item(p("bass.html"), 'Bass &amp; Clays <span class="caret" aria-hidden="true">▾</span>', "bass")}
        <div class="submenu" role="menu">
          <a href="{p("bass.html")}">Bass Fishing</a>
          <a href="{p("clays.html")}">Sporting Clays</a>
          <a href="{p("kennels.html")}">Kennels</a>
        </div>
      </div>
      <div class="nav-item has-menu">
        {item(p("lodge.html"), 'The Lodge <span class="caret" aria-hidden="true">▾</span>', "stay")}
        <div class="submenu" role="menu">
          <a href="{p("lodge.html")}">Lodge</a>
          <a href="{p("bunkhouse.html")}">Bunkhouse</a>
          <a href="{p("dining.html")}">Dining</a>
          <a href="{p("weddings.html")}">Weddings</a>
        </div>
      </div>
    </div>
    <div class="nav-right">
      <a class="book-btn" href="{p("contact.html")}">Book a Hunt</a>
      <button class="menu-btn" id="menuBtn" type="button" aria-label="Open menu" aria-controls="drawer" aria-expanded="false">
        <span class="menu-btn-lines" aria-hidden="true"><span></span><span></span><span></span></span>
        <span class="menu-btn-label mono">Menu</span>
      </button>
    </div>
  </div>
</nav>'''

def drawer(depth):
    p = lambda x: r(depth, x)
    return f'''
<div class="drawer-backdrop" id="drawerBackdrop" hidden></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-label="Site menu">
  <div class="drawer-head">
    <span class="mono drawer-eyebrow">Red Bank Outfitters — Est. 1965</span>
    <button class="drawer-close" id="drawerClose" type="button" aria-label="Close menu">&times;</button>
  </div>
  <div class="drawer-body">
    <nav class="drawer-col" aria-label="Pursuits">
      <h4 class="mono">Pursuits</h4>
      <a href="{p("hunts.html")}">The Hunt</a>
      <a href="{p("upland.html")}">Upland Game</a>
      <a href="{p("big-game.html")}">Big Game</a>
      <a href="{p("bass.html")}">Bass Fishing</a>
      <a href="{p("clays.html")}">Sporting Clays</a>
      <a href="{p("upland/turkey.html")}">Wild Turkey</a>
    </nav>
    <nav class="drawer-col" aria-label="The Ranch">
      <h4 class="mono">The Ranch</h4>
      <a href="{p("the-ranch.html")}">The Ranch</a>
      <a href="{p("lodge.html")}">Lodge</a>
      <a href="{p("bunkhouse.html")}">Bunkhouse</a>
      <a href="{p("dining.html")}">Dining</a>
      <a href="{p("weddings.html")}">Weddings</a>
      <a href="{p("kennels.html")}">Kennels</a>
      <a href="{p("rates.html")}">Rates</a>
    </nav>
    <nav class="drawer-col" aria-label="Media">
      <h4 class="mono">Media</h4>
      <a href="{p("gallery.html")}">Gallery</a>
      <a href="{p("news.html")}">News</a>
    </nav>
    <nav class="drawer-col" aria-label="Academy">
      <h4 class="mono">Academy</h4>
      <a href="https://redbankoutdooracademy.com/" target="_blank" rel="noopener">Red Bank Outdoor Academy <span class="ext">↗</span></a>
      <a href="{p("contact.html")}">Contact</a>
    </nav>
  </div>
  <div class="drawer-foot">
    <div class="drawer-contact"><div class="mono k">Phone</div><a class="v" href="{TEL}">{PHONE}</a></div>
    <div class="drawer-contact"><div class="mono k">Location</div><div class="v">18875 Red Bank Rd., Red Bluff CA</div></div>
    <div class="drawer-contact"><div class="mono k">Mail</div><div class="v">PO Box 8295, Red Bluff CA</div></div>
  </div>
</aside>'''

def announce(depth=0):
    return f'''
<div class="announce" id="announce">
  <div class="announce-inner">
    <span class="announce-text">Now accepting reservations for the 26–27 season and lodge accommodations.</span>
    <a class="announce-cta" href="{r(depth, "lodge.html")}">Reserve dates</a>
    <button class="announce-close" id="announceClose" aria-label="Dismiss announcement">&times;</button>
  </div>
</div>'''

def consent():
    return '''
<aside id="consent-banner" class="consent hidden" role="dialog" aria-modal="false" aria-labelledby="consent-title">
  <div class="consent-card">
    <div class="consent-copy">
      <div class="mono consent-kicker">Privacy Choices</div>
      <h2 id="consent-title">Website tracking and privacy choices</h2>
      <p>We use cookies and similar technologies on this website. Some are necessary to operate and secure the site. Others are optional and are used only with your consent — they may collect information such as your IP address, device and browser details, pages visited, and interactions, which may be shared with analytics and marketing providers. Under California law this may be considered a &ldquo;sale&rdquo; or &ldquo;sharing&rdquo; of personal information, even though we do not sell personal information for money.</p>
      <p>You may reject optional technologies or change your choice at any time via <strong>Privacy Choices</strong> in the footer. We honor Global Privacy Control signals where required by law.</p>
    </div>
    <div class="consent-actions">
      <button type="button" data-consent-accept class="btn-primary">Accept all</button>
      <button type="button" data-consent-reject class="btn-ghost">Reject optional</button>
    </div>
  </div>
</aside>'''

def footer(depth):
    p = lambda x: r(depth, x)
    return f'''
<footer>
  <div class="foot-inner">
    <div class="foot-top">
      <div class="brand">
        <div class="logo" style="color:var(--bone)"><span class="logo-text">RED BANK <em>OUTFITTERS</em></span></div>
        <p>A private California hunting ranch on Red Bank Creek, west of Red Bluff. Opened to an exclusive clientele in 1965. Groups are not mixed.</p>
      </div>
      <div class="foot-col">
        <h4>Pursuits</h4>
        <a href="{p("upland.html")}">Upland Game</a>
        <a href="{p("big-game.html")}">Big Game</a>
        <a href="{p("bass.html")}">Bass Fishing</a>
        <a href="{p("clays.html")}">Sporting Clays</a>
      </div>
      <div class="foot-col">
        <h4>The House</h4>
        <a href="{p("lodge.html")}">The Lodge</a>
        <a href="{p("bunkhouse.html")}">Bunkhouse</a>
        <a href="{p("dining.html")}">The Table</a>
        <a href="{p("weddings.html")}">Weddings</a>
      </div>
      <div class="foot-col">
        <h4>The Lodge</h4>
        <a href="{TEL}">{PHONE}</a>
        <a href="{p("contact.html")}">18875 Red Bank Rd.<br>Red Bluff, CA 96080</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="https://redbankoutdooracademy.com/" target="_blank" rel="noopener">Outdoor Academy</a>
      </div>
    </div>
    <div class="wordmark">Red <em>Bank</em></div>
    <div class="foot-bot">
      <span>&copy; Red Bank Outfitters · Est. 1965</span>
      <span class="mono">Red Bluff, California · 18,000 ac</span>
      <a href="#" data-open-consent>Privacy Choices</a>
      {f'<a class="os-login" href="{OS_PATH}">Ranch Login</a>' if OS_PATH else ""}
    </div>
  </div>
</footer>
<div class="bookbar" id="bookbar">
  <div class="bb-text">
    <span class="k">Plan Your Visit</span>
    <span class="v">Upland, big game, bass &amp; clays — {PHONE}</span>
  </div>
  <a class="bb-btn" href="{p("contact.html")}">Request Info</a>
  <button class="bb-close" id="bbClose" type="button" aria-label="Dismiss">&times;</button>
</div>'''

def news_modal():
    return '''
<div class="news-backdrop" id="newsBackdrop" hidden></div>
<div class="news-modal" id="newsModal" role="dialog" aria-modal="true" aria-labelledby="newsTitle" aria-hidden="true" hidden>
  <button class="news-close" id="newsClose" type="button" aria-label="Close">&times;</button>
  <div class="news-grid">
    <aside class="news-media" aria-hidden="true">
      <div class="news-media-ph"></div>
      <div class="news-badge mono">Contact Us</div>
      <div class="news-media-cap mono">Season dates by phone</div>
    </aside>
    <div class="news-body">
      <div class="mono news-eyebrow">— From the 1965 Society</div>
      <h3 id="newsTitle">The 1965 <em>Society</em></h3>
      <p class="news-sub">Leave a name. The lodge will send season dates when they go out — never a list we sell.</p>
      <form class="news-form" id="newsForm" novalidate>
        <div class="news-row">
          <div class="news-field"><label for="newsName">First name</label><input type="text" id="newsName" name="name" autocomplete="given-name" required></div>
          <div class="news-field"><label for="newsEmail">Email</label><input type="email" id="newsEmail" name="email" autocomplete="email" required></div>
        </div>
        <div class="news-field"><label for="newsPhone">Mobile number</label><input type="tel" id="newsPhone" name="phone" autocomplete="tel" inputmode="tel" required></div>
        <label class="news-opt"><input type="checkbox" id="newsSms" name="sms" checked><span>Text me season openers. Msg &amp; data rates may apply. Reply STOP to unsubscribe.</span></label>
        <button type="submit" class="news-submit">Join the list</button>
        <p class="news-fine mono">We never share your info. For reservations and pricing, contact us at (530) 529-9435.</p>
      </form>
      <div class="news-thanks" id="newsThanks" hidden>
        <div class="mono news-eyebrow" style="color:var(--brass)">— Confirmed</div>
        <h3>Thank you.</h3>
        <p>Need dates this week? Contact us at (530) 529-9435 and we will make it work.</p>
      </div>
    </div>
  </div>
</div>'''

def head(depth, title, desc, extra=""):
    p = lambda x: r(depth, x)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" href="{p("img/mark.svg")}" type="image/svg+xml">
<link rel="stylesheet" href="{p("styles.css")}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"SportsActivityLocation","name":"Red Bank Outfitters","telephone":"+1-530-529-9435","email":"Hunting@RedBankOutfitters.com","foundingDate":"1965","address":{{"@type":"PostalAddress","streetAddress":"18875 Red Bank Rd","addressLocality":"Red Bluff","addressRegion":"CA","postalCode":"96080","addressCountry":"US"}}}}
</script>
{extra}
</head>'''

def wrap(depth, title, desc, body, active="", inner=True):
    root = "../" * depth
    cls = "inner" if inner else ""
    return f'''{head(depth, title, desc)}
<body class="{cls}" data-root="{root}">
{announce(depth)}
{nav(depth, active)}
{drawer(depth)}
{body}
{footer(depth)}
{consent()}
{news_modal()}
<script src="{r(depth, "script.js")}"></script>
<!-- Marker.io feedback widget (preview only) -->
<script>
window.markerConfig = {{ project: '6a9080636ccdf9c4f8369305', source: 'snippet' }};
!function(e,r,a){{if(!e.__Marker){{e.__Marker={{}};var t=[],n={{__cs:t}};["show","hide","isVisible","capture","cancelCapture","unload","reload","isExtensionInstalled","setReporter","clearReporter","setCustomData","on","off"].forEach(function(e){{n[e]=function(){{var r=Array.prototype.slice.call(arguments);r.unshift(e),t.push(r)}}}}),e.Marker=n;var s=r.createElement("script");s.async=1,s.src="https://edge.marker.io/latest/shim.js";var i=r.getElementsByTagName("script")[0];i.parentNode.insertBefore(s,i)}}}}(window,document);
</script>
</body>
</html>
'''

def crumbs(items):
    parts = []
    for label, href in items[:-1]:
        parts.append(f'<a href="{href}">{label}</a><span>/</span>')
    parts.append(f'<span>{items[-1][0]}</span>')
    return '<div class="crumb mono">' + "".join(parts) + "</div>"

def facts_html(rows):
    cells = "".join(f'<div class="f"><div class="n">{n}</div><div class="l mono">{l}</div></div>' for n, l in rows)
    return f'<div class="facts">{cells}</div>'

def aside(extra_rows=None):
    rows = extra_rows or []
    base = [
        ("Phone", f'<a href="{TEL}">{PHONE}</a>'),
        ("Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
        ("Address", "18875 Red Bank Rd.<br>Red Bluff, CA 96080"),
    ] + rows
    rows_html = "".join(f'<div class="row"><span>{k}</span><b>{v}</b></div>' for k, v in base)
    return f'''<aside class="aside">
      <h3>Booking and Reservations</h3>
      <p>Contact us for reservations and pricing. Groups are never mixed, and there is no minimum party size.</p>
      {rows_html}
      <a class="btn-primary" href="{TEL}" style="margin-top:20px;width:100%;text-align:center">Call Us at {PHONE}</a>
      <a class="btn-ghost" href="mailto:{EMAIL}" style="margin-top:10px;width:100%;text-align:center;justify-content:center">Send message</a>
    </aside>'''

def related_html(depth, cards):
    p = lambda x: r(depth, x)
    bits = []
    for href, img, title, blurb in cards:
        bits.append(f'''<a class="rel" href="{p(href)}"><div class="img" style="background-image:url('{p("img/"+img)}')"></div><h3>{title}</h3><p>{blurb}</p></a>''')
    return f'<div class="related"><h2>Also on the ranch</h2><div class="rel-grid">{"".join(bits)}</div></div>'

def page(depth, title, desc, active, crumb, h1, lead, meta, img, img_alt, prose, factrows, related, extra_aside=None, generated=False, gen_note=None):
    p = lambda x: r(depth, x)
    meta_html = "".join(f'<div><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in meta)
    gen = f'<p class="gen-note">{gen_note or "Atmosphere photograph of Tehama County oak country — not a picture of a Red Bank hunt."}</p>' if generated else ""
    body = f'''
<header class="page-hero">
  <div class="ph-bg" style="background-image:url('{p("img/"+img)}')" role="img" aria-label="{img_alt}"></div>
  <div class="page-hero-inner">
    {crumbs(crumb)}
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="ph-meta">{meta_html}</div>
  </div>
</header>
<div class="page-body">
  <article class="prose">
    {prose}
    {facts_html(factrows) if factrows else ""}
    {gen}
  </article>
  {aside(extra_aside)}
</div>
{related_html(depth, related)}
'''
    return wrap(depth, title, desc, body, active=active, inner=True)

DEFAULT_REL = [
    ("upland.html", "pointer.jpg", "Upland <em>birds</em>", "Bobwhite, valley and mountain quail, pheasant, chukar, turkey."),
    ("hunts.html", "creek.jpg", "The <em>hunt</em>", "Two guns, one guide, three or four dogs."),
    ("lodge.html", "lodge.jpg", "The <em>Lodge</em>", "Sleeps 14. Fireplace, kitchen, porch, kennel on site."),
]

# ---------------- Homepage ----------------
INDEX = wrap(0, "Red Bank Outfitters — Est. 1965, Red Bluff",
"A private California hunting ranch on Red Bank Creek, west of Red Bluff. Eighteen thousand acres. Groups are not mixed. Est. 1965.",
f'''
<header class="hero" id="top">
  <div class="hero-media" id="heroMedia"></div>
  <div class="hero-grain" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="hero-eyebrow">
      <span class="dash"></span>
      <span class="mono">Est. 1965 · Red Bluff, California</span>
    </div>
    <h1 id="heroH1">
      The private Southern-style quail hunting ranch.
      <br>Since 1965.
    </h1>
    <p class="hero-sub">
      The premier California hunting and outfitters destination — eighteen thousand acres on the banks of Red Bank Creek in Red Bluff, greater Northern California.
    </p>
    <div class="hero-foot">
      <div class="hero-cta-row">
        <a class="btn-primary" href="contact.html">Book a Hunt</a>
        <a class="btn-ghost" href="#ranch">Explore the Ranch</a>
      </div>
      <div class="hero-meta">
        <div class="cell"><div class="k">Ranch</div><div class="v">18,000 ac</div></div>
        <div class="cell"><div class="k">Ponds</div><div class="v">11</div></div>
        <div class="cell"><div class="k">Clays</div><div class="v">18</div></div>
      </div>
    </div>
  </div>
</header>

<section class="seenin" aria-label="As seen on">
  <div class="seenin-label-row">
    <span class="seenin-label"><span class="rule-sm"></span>As seen on<span class="rule-sm"></span></span>
  </div>
  <div class="marquee">
    <div class="marquee-track">
      <div class="marquee-group">
        <div class="seenin-logo"><span class="seenin-word">OUTDOOR</span><span class="seenin-sub">Channel</span></div>
        <div class="seenin-logo"><span class="seenin-word seenin-ser">Sportsman</span><span class="seenin-sub">Channel</span></div>
        <div class="seenin-logo"><span class="seenin-word seenin-ser">Field <em>&amp;</em> Stream</span></div>
        <div class="seenin-logo"><span class="seenin-mark">OLN</span><span class="seenin-sub">Outdoor Life Network</span></div>
        <div class="seenin-logo"><span class="seenin-script">Engel&rsquo;s</span><span class="seenin-sub">Outdoor Experience</span></div>
      </div>
      <div class="marquee-group" aria-hidden="true">
        <div class="seenin-logo"><span class="seenin-word">OUTDOOR</span><span class="seenin-sub">Channel</span></div>
        <div class="seenin-logo"><span class="seenin-word seenin-ser">Sportsman</span><span class="seenin-sub">Channel</span></div>
        <div class="seenin-logo"><span class="seenin-word seenin-ser">Field <em>&amp;</em> Stream</span></div>
        <div class="seenin-logo"><span class="seenin-mark">OLN</span><span class="seenin-sub">Outdoor Life Network</span></div>
        <div class="seenin-logo"><span class="seenin-script">Engel&rsquo;s</span><span class="seenin-sub">Outdoor Experience</span></div>
      </div>
    </div>
  </div>
</section>

<section class="about" id="ranch">
  <div class="sec">
    <div class="sec-head reveal">
      <div class="mono label">01 — The Ranch</div>
      <h2>The premier <em>California hunting destination</em> — eighteen thousand acres on the banks of Red Bank Creek, west of Red Bluff.</h2>
    </div>
    <div class="about-grid">
      <div class="about-copy reveal">
        <p>Red Bank opened its land in 1965 to an exclusive clientele. It is still run that way. One party at a time. Southern hospitality. The grand tradition of the hunt.</p>
        <p>Behind the gate: bobwhite, valley and mountain quail, chukar, pheasant, Rio Grande turkey, Columbia blacktail, and wild hog. Between hunts, eleven bass ponds, an 18-station clays course, and a long table by the fire.</p>
        <div class="about-stats">
          <div class="stat"><div class="num" data-counter="18000">0<sup>ac</sup></div><div class="lbl mono">Working ranch</div></div>
          <div class="stat"><div class="num" data-counter="1965">0<sup>yr</sup></div><div class="lbl mono">Since 1965</div></div>
          <div class="stat"><div class="num" data-counter="11">0</div><div class="lbl mono">Bass ponds</div></div>
        </div>
      </div>
      <a class="about-img reveal" href="lodge.html" aria-label="See the Lodge">
        <div class="ph" style="background-image:url('img/lodge-landscape.jpg')"></div>
        <div class="cap"><span class="d"></span><span class="mono">Explore Lodge</span><span class="arr" aria-hidden="true">&rarr;</span></div>
      </a>
    </div>
  </div>
</section>

<section class="pursuits">
  <div class="pursuits-inner">
    <div class="sec-head reveal">
      <div class="mono label">02 — The Hunt</div>
      <h2>Two guns, one guide, three or four dogs. <em>We do not mix groups.</em></h2>
    </div>
    <div class="hunt-ticker marquee">
      <div class="marquee-track">
        <div class="marquee-group"><span class="tk">Southern-Style Bobwhite Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Valley Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Mountain Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Chukar</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Walk-Up Pheasant</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">European-Style Drives</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Rio Grande Turkey</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Columbia Blacktail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Wild Hog</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Bass Fishing — Eleven Ponds</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Sporting Clays — Eighteen Stations</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Bird Dogs &amp; Kennels</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">The Lodge</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Dining at the Long Table</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Ranch Weddings</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Corporate Retreats</span><span class="dm" aria-hidden="true">&#9670;</span></div>
        <div class="marquee-group" aria-hidden="true"><span class="tk">Southern-Style Bobwhite Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Valley Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Mountain Quail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Chukar</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Walk-Up Pheasant</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">European-Style Drives</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Rio Grande Turkey</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Columbia Blacktail</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Wild Hog</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Bass Fishing — Eleven Ponds</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Sporting Clays — Eighteen Stations</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Bird Dogs &amp; Kennels</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">The Lodge</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Dining at the Long Table</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Ranch Weddings</span><span class="dm" aria-hidden="true">&#9670;</span><span class="tk">Corporate Retreats</span><span class="dm" aria-hidden="true">&#9670;</span></div>
      </div>
    </div>
    <div class="hunt-grid">
      <a class="hunt-card wide tilt" href="upland.html">
        <div class="bg" style="background-image:url('img/pointer.jpg')"></div>
        <div class="veil"></div>
        <div class="txt">
          <div class="k mono">Upland</div>
          <h3>The <em>birds</em></h3>
          <p>Bobwhite walked up. A European drive. Wild valley quail north of the ranch. Mountain quail in the chaparral.</p>
        </div>
      </a>
      <a class="hunt-card tilt" href="hunts/blacktail.html">
        <div class="bg" style="background-image:url('img/creek.jpg')"></div>
        <div class="veil"></div>
        <div class="txt"><div class="k mono">Big game</div><h3>Blacktail</h3><p>Three days. Guide, lodging, meals.</p></div>
      </a>
      <a class="hunt-card tilt" href="hunts/wild-hog.html">
        <div class="bg" style="background-image:url('img/ranch-hills.jpg')"></div>
        <div class="veil"></div>
        <div class="txt"><div class="k mono">Big game</div><h3>Wild hog</h3><p>Oaks, draws, manzanita.</p></div>
      </a>
      <a class="hunt-card tilt" href="bass.html">
        <div class="bg" style="background-image:url('img/pond.jpg')"></div>
        <div class="veil"></div>
        <div class="txt"><div class="k mono">Water</div><h3>Eleven ponds</h3></div>
      </a>
      <a class="hunt-card tilt" href="clays.html">
        <div class="bg" style="background-image:url('img/clays-station.jpg')"></div>
        <div class="veil"></div>
        <div class="txt"><div class="k mono">Clays</div><h3>Eighteen stations</h3></div>
      </a>
    </div>
  </div>
</section>


<section class="lodge" id="lodge">
  <div class="sec">
    <div class="sec-head reveal">
      <div class="mono label">03 — Accommodations</div>
      <h2>Quiet rooms when the day is done — and a long table <em>worth coming in for.</em></h2>
    </div>
    <div class="rooms">
      <a class="room reveal tilt" href="lodge.html">
        <div class="tag">Main House</div>
        <div class="img" style="background-image:var(--room1)"></div>
        <div class="body"><div class="name">The <em>Lodge</em></div><div class="rate">Sleeps 14</div></div>
        <p class="desc">Gathering rooms, a fireplace, a full kitchen, a poker table, and a porch. Three showers. Wifi, satellite, kennel, barbecue.</p>
        <div class="meta"><span>Private groups</span><span>Fine dining</span></div>
      </a>
      <a class="room reveal tilt" href="bunkhouse.html">
        <div class="tag">Hunters' Quarters</div>
        <div class="img" style="background-image:var(--room2)"></div>
        <div class="body"><div class="name">The <em>Bunkhouse</em></div><div class="rate">Sleeps 6</div></div>
        <p class="desc">Classic ranch bunkhouse — stone columns on the porch, a dog kennel, and the coffee on by 4 a.m.</p>
        <div class="meta"><span>Parties welcome</span><span>Kennels on site</span></div>
      </a>
      <a class="room reveal tilt" href="dining.html">
        <div class="tag">Dining</div>
        <div class="img" style="background-image:var(--room3)"></div>
        <div class="body"><div class="name">The <em>Table</em></div><div class="rate">By arrangement</div></div>
        <p class="desc">Household staff, California wines, breakfasts before the walk-up. Day shooters: two days' notice, arrive by 1 p.m.</p>
        <div class="meta"><span>Fine dining</span><span>Events</span></div>
      </a>
    </div>
  </div>
</section>

<section class="quotes">
  <div class="quotes-inner">
    <div class="quote-nav">
      <div class="mono label">04 — What guests keep saying</div>
      <div class="quote-arrows">
        <button class="q-arr" id="qPrev" type="button" aria-label="Previous"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M15 18l-6-6 6-6"/></svg></button>
        <button class="q-arr" id="qNext" type="button" aria-label="Next"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 18l6-6-6-6"/></svg></button>
      </div>
    </div>
    <div class="q-slider" id="qSlider">
      <div class="q-slide active">
        <div class="q-text">Any serious bow hunter looking to challenge their skill levels in the art of spot-and-stalk cunning Northern California black-tail deer will find their fill at Red Bank Outfitters.</div>
        <div class="q-attr"><div class="q-name">Roger Sabette</div><div class="q-role">Bow hunter</div><div class="q-loc mono">Blacktail deer</div></div>
      </div>
      <div class="q-slide">
        <div class="q-text">I was able to harvest my first turkey and check off another item off my bucket list. Thank you for your patience and time you invested into the hunt, Bobby Hassel.</div>
        <div class="q-attr"><div class="q-name">Jordy</div><div class="q-role">First-turkey guest</div><div class="q-loc mono">Rio Grande turkey</div></div>
      </div>
      <div class="q-slide">
        <div class="q-text">We had a great time hunting the California Dove Opener this morning at Red Bank Outfitters. Can't wait to come back for quail season.</div>
        <div class="q-attr"><div class="q-name">Callie</div><div class="q-role">Opening-day party</div><div class="q-loc mono">California dove</div></div>
      </div>
    </div>
    <div class="q-dots" id="qDots">
      <button class="q-dot active" type="button" data-i="0" aria-label="Testimonial 1"></button>
      <button class="q-dot" type="button" data-i="1" aria-label="Testimonial 2"></button>
      <button class="q-dot" type="button" data-i="2" aria-label="Testimonial 3"></button>
    </div>
  </div>
</section>

<section class="journal" id="journal">
  <div class="journal-inner">
    <div class="sec-head reveal">
      <div class="mono label">05 — From the ranch</div>
      <h2>Dispatches from the <em>newsletter</em> — seasons, birds, and life on the place.</h2>
    </div>
    <div class="journal-grid">
      <article class="article reveal tilt">
        <div class="img"><div style="background-image:var(--j1)"></div></div>
        <div class="meta"><span class="mono">October 2020</span><span class="mono">· Newsletter</span></div>
        <h3>Around the Ranch — Red Bank Newsletter, October 2020</h3>
        <a class="link" href="news.html">Read the archive <span class="arr">→</span></a>
      </article>
      <article class="article reveal tilt">
        <div class="img"><div style="background-image:var(--j2)"></div></div>
        <div class="meta"><span class="mono">November 2019</span><span class="mono">· Newsletter</span></div>
        <h3>Around the Ranch — Red Bank Newsletter, November 2019</h3>
        <a class="link" href="news.html">Read the archive <span class="arr">→</span></a>
      </article>
      <article class="article reveal tilt">
        <div class="img"><div style="background-image:var(--j3)"></div></div>
        <div class="meta"><span class="mono">March 2018</span><span class="mono">· Upland</span></div>
        <h3>Upland bird hunting in full swing at Red Bank</h3>
        <a class="link" href="news.html">Read the archive <span class="arr">→</span></a>
      </article>
    </div>
  </div>
</section>

<section class="cta" id="contact">
  <div class="cta-bg"></div>
  <div class="cta-inner">
    <h2 class="reveal">A private season. <em>Book yours today.</em></h2>
    <div class="cta-side reveal">
      <p>Contact us for reservations and pricing. We will help you build a hunt, a weekend, or a private event around the days that suit you.</p>
      <div class="season-picker">
        <div class="sp-cell"><div class="k">Phone</div><a class="v" href="{TEL}">{PHONE}</a></div>
        <div class="sp-cell"><div class="k">Location</div><div class="v">18875 Red Bank Rd., Red Bluff CA 96080</div></div>
        <div class="sp-cell"><div class="k">Mail</div><div class="v">PO Box 8295, Red Bluff CA</div></div>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn-primary" href="contact.html">Inquire</a>
        <a class="btn-ghost" href="{TEL}">{PHONE}</a>
      </div>
    </div>
  </div>
</section>
''', active="home", inner=False)

# ---------------- Inner pages ----------------
PAGES = []

def add(path, html):
    PAGES.append((path, html))

add("index.html", INDEX)

add("the-ranch.html", page(0, "The Ranch — Red Bank Outfitters",
"18,000 acres on Red Bank Creek west of Red Bluff. Founded in 1965 as Red Bank Ale & Quail.",
"stay",
[("Home","index.html"),("The Ranch","")],
"The Ranch",
"West of Red Bluff in Tehama County. One of the oldest hunting clubs in California, opened to an exclusive clientele in 1965.",
[("Founded","1965"),("Acres","18,000"),("County","Tehama")],
"creek.jpg", "Red earth bluffs over a Northern California creek in oak country",
'''<p class="deck">Formerly Red Bank Ale &amp; Quail Game Bird Club. Brian Riley, who started here as a teenager just out of high school, bought the hunting operation with his wife Shellie. They expanded the original 5,000-acre ranch by acquiring rights to close to 11,000 more.</p>
<p>The ranch sits six miles from town. From Interstate 5 take exit 647, west on Luther, left on Paskenta, right on Live Oak. Live Oak becomes Red Bank. The gate is on the left.</p>
<p>Today the focus is quail habitat, the lodge and facilities, and the farming that keeps the place working. Between hunts: eleven bass and bluegill ponds, an 18-station sporting clays course, a 40-dog kennel at the academy, a wild-game processing room, and a 4,000-square-foot covered patio in front of the lodge.</p>
<p>The ranch has hosted hunters including astronauts, Hollywood figures, and sports celebrities, and it runs corporate events. Summer camps are a separate operation: Red Bank Outdoor Academy, on the same land.</p>
<h2>What sits behind the gate</h2>
<ul>
<li>Upland — bobwhite, valley, mountain and Gambel's quail, chukar, pheasant, Rio Grande turkey</li>
<li>Big game — Columbia blacktail deer and wild hog</li>
<li>Eleven bass ponds, osprey and golden eagles overhead</li>
<li>18-station clays through oaks and over water</li>
<li>Lodge for 14, bunkhouse for 6, kennels at both buildings</li>
</ul>''',
[("18,000","Acres"),("11","Bass ponds"),("6 mi","From town")],
DEFAULT_REL, generated=True))

add("hunts.html", page(0, "The Hunt — Red Bank Outfitters",
"Two guests, one guide, three or four dogs. Groups are not mixed. Since 1965 in Red Bluff.",
"upland",
[("Home","index.html"),("Hunting","")],
"Southern-style quail hunting",
"Thoughts of Southern-style quail hunting call up field edges and head-high brush. It does not have to be a memory.",
[],
"hunt-ridge.jpg", "Oak savanna ridges west of Red Bluff at first light, fog in the creek bottom",
'''<p class="deck">Since 1965 the goal at Red Bank has been the quail hunt. We do not mix groups. That is the whole point of coming.</p>
<p>We can put 14 people in the main lodge and 6 in the bunkhouse. There is no minimum group size. The trip is about your enjoyment.</p>
<p>A typical upland party is two guests, one guide, and three or four dogs. The guides have years on these dogs and this ground. If you bring your own dogs they are welcome — there is a kennel at both buildings.</p>
<p>There are few sights in the outdoors more reverent than a brace of bird dogs on point. It is almost better than the shooting.</p>
<h2>What to hunt</h2>
<ul>
<li><a href="upland/bobwhite.html">Southern-style bobwhite quail</a> — the plantation walk-up</li>
<li><a href="upland/valley-quail.html">Wild valley quail</a> — October through January, 5,000 acres north of the ranch</li>
<li><a href="upland/mountain-quail.html">Mountain quail</a> — a 30-minute drive into chaparral</li>
<li><a href="upland/pheasant.html">Walk-up pheasant</a> and the <a href="upland/european-drive.html">European-style drive</a></li>
<li><a href="upland/turkey.html">Rio Grande turkey</a> — fall or spring, under California seasons</li>
<li><a href="hunts/blacktail.html">Blacktail deer</a> — three days, all inclusive</li>
<li><a href="hunts/wild-hog.html">Wild hog</a> — UTV or on foot, 18,000 acres</li>
</ul>''',
[],
DEFAULT_REL))

add("upland.html", page(0, "Upland Game — Red Bank Outfitters",
"Bobwhite, valley and mountain quail, chukar, pheasant, European-style drives, and Rio Grande turkey in Red Bluff, California.",
"upland",
[("Home","index.html"),("Upland","")],
"Upland Game",
"A menu of California birds, walked up or driven, with dogs that live for it.",
[("Species","7"),("Dogs","On site"),("Season","Inquire")],
"upland-cover.jpg", "Golden bunch grass and brush at the edge of a blue oak grove",
'''<p class="deck">Red Bank was built as a quail club. Everything else on the ranch grew out of that.</p>
<p>Bobwhite is the plantation walk-up: two guns, a guide, a brace of dogs, field edges and flats of head-height brush. Valley quail is a different animal — wild birds, a short California season from October through January, hunted Texas-style on 5,000 acres just north of the ranch, groups of up to four, out of utility vehicles. Mountain quail live in the chaparral a 30-minute drive west; you listen at daylight for a bird more often heard than seen.</p>
<p>Pheasant comes two ways: a walk-up (minimum two shooters) and a European-style drive with pegs, beaters, and pickers-up, four to twelve guns, at least a hundred birds. Chukar run the steep banks. Rio Grande turkey has a fall season (tom or hen) and a spring season (bearded gobblers only), under California Fish and Wildlife rules.</p>
<ul>
<li><a href="upland/bobwhite.html">Southern-style bobwhite</a></li>
<li><a href="upland/valley-quail.html">Valley quail</a></li>
<li><a href="upland/mountain-quail.html">Mountain quail</a></li>
<li><a href="upland/chukar.html">Chukar</a></li>
<li><a href="upland/pheasant.html">Walk-up pheasant</a></li>
<li><a href="upland/european-drive.html">European-style drive</a></li>
<li><a href="upland/turkey.html">Wild turkey</a></li>
</ul>''',
[("2+1","Guns and a guide"),("Oct–Jan","Valley quail"),("4–12","Drive guns")],
DEFAULT_REL, generated=True))

add("big-game.html", page(0, "Big Game — Red Bank Outfitters",
"Blacktail deer and wild hog hunts on 18,000 acres west of Red Bluff, California.",
"big",
[("Home","index.html"),("Big Game","")],
"Big Game",
"A managed blacktail herd on more than 10,000 acres, and wild hog on the whole ranch.",
[("Deer","3-day"),("Hog","Year-round*"),("Cold storage","Walk-in")],
"deer.jpg", "A Columbia blacktail buck taken at Red Bank",
'''<p class="deck">Columbia blacktail on a ranch they manage for a healthy buck-to-doe ratio. Wild hog from rolling oaks to manzanita draws to a eucalyptus grove if you want it close.</p>
<p>The blacktail hunt is three days, all inclusive: guide, lodging, meals, and field dressing ready for the butcher. Walk-in cold storage is on the ranch. They will prepare a trophy for the taxidermist and can put you with a local shop. On a typical hunt you will see a lot of wildlife and average 6 to 10 bucks a day.</p>
<p>Hogs are the other California staple here. From open oak hills to poison oak and manzanita bedding cover, then thicker studded oaks on flatter ground. For the brave, a thousand-acre eucalyptus grove with dogs and an open-sight big-bore.</p>
<ul>
<li><a href="hunts/blacktail.html">Blacktail deer hunts</a></li>
<li><a href="hunts/wild-hog.html">Wild hog</a></li>
</ul>
<p style="font-size:13px;color:var(--ash)">*Confirm current California seasons and tags when you call. Blacktail is a limited hunt.</p>''',
[("10,000+","Deer acres"),("6–10","Bucks seen / day"),("3","Days, all-in")],
[("hunts/blacktail.html","deer.jpg","Blacktail <em>deer</em>","Three days. Guide, lodge, meals, field dressing."),
 ("hunts/wild-hog.html","hog.jpg","Wild <em>hog</em>","Oaks, draws, manzanita. UTV or on foot."),
 ("lodge.html","lodge.jpg","The <em>Lodge</em>","Sleeps 14.")]))

add("bass.html", page(0, "Bass Fishing — Red Bank Outfitters",
"Largemouth bass on 11 ponds at Red Bank Outfitters, Red Bluff. One-day packages include lodging. California fishing license required.",
"bass",
[("Home","index.html"),("Bass","")],
"Bass Fishing",
"Fish between hunts. Osprey, golden eagles, deer, turkey, hogs, coyotes, migratory ducks and Canada geese use the same water.",
[("Ponds","11"),("License","CA required"),("Package","Day + lodging")],
"pond.jpg", "A still bass pond in Northern California oak hills at dusk",
'''<p class="deck">Largemouth bass take the eleven ponds. One-day packages include lodging. Bring a California fishing license.</p>
<p>The water is also a wildlife sit. Osprey and golden eagles. Upland birds, deer, wild turkeys, wild hogs, coyotes. Migratory ducks and Canada geese. Songbirds including the western kingbird and Lewis's woodpecker.</p>
<p>Contact us for dates. A fishing day is often stacked with clays or an afternoon walk-up.</p>''',
[("11","Ponds"),("1","Day packages"),("CA","License")],
[("clays.html","clays-station.jpg","Sporting <em>clays</em>","18 stations over water and through oaks."),
 ("upland.html","dogs-water.jpg","Upland <em>game</em>","Birds the same week."),
 ("lodge.html","lodge.jpg","Stay <em>over</em>","Lodge or bunkhouse.")], generated=True))

add("clays.html", page(0, "Sporting Clays — Red Bank Outfitters",
"18-station sporting clays course at Red Bank Outfitters, Red Bluff. Over water, through brush and valley oaks. Loaner shotguns and ammunition available.",
"bass",
[("Home","index.html"),("Clays","")],
"Sporting Clays",
"Practice and competition over water, through brush, and under valley oaks. Loaner shotguns, ammunition, ear plugs, and shooting glasses on site.",
[("Stations","18"),("Loaners","Yes"),("Safety","On site")],
"clays-station.jpg", "A sporting clays stand under valley oaks on a Northern California ranch",
'''<p class="deck">An 18-station course. You will be shot at from every angle the oak country can invent.</p>
<p>Targets run over water, through brush, and under valley oaks. Loaner shotguns and ammunition are available, plus ear plugs and shooting glasses.</p>
<p>The photograph of a gun over a pond is from the ranch. Ask us about a clays-only afternoon, or add it between hunts.</p>''',
[("18","Stations"),("Oaks","The course"),("Loaners","Guns & shells")],
[("bass.html","pond.jpg","Bass <em>ponds</em>","Eleven of them."),
 ("upland.html","dogs-water.jpg","Then <em>birds</em>","Warm up the gun."),
 ("dining.html","dining.jpg","Lunch <em>after</em>","Day shooters welcome.")], generated=True))

add("kennels.html", page(0, "Kennels — Red Bank Outfitters",
"Over 30 professionally trained bird dogs at Red Bank Outfitters. Training, breeding, pointers, and kennels at both the lodge and bunkhouse.",
"bass",
[("Home","index.html"),("Kennels","")],
"Kennels",
"Over 30 professionally trained bird dogs. Training, breeding, pointers. Kennels at both buildings. Your own dogs are welcome.",
[("Dogs","30+"),("Buildings","2 kennels"),("Your dogs","Welcome")],
"dogs-water.jpg", "A pointer and a Labrador in a ranch pond under oaks",
'''<p class="deck">A brace of bird dogs on point is almost better than the shooting. Red Bank keeps the string to make that true.</p>
<p>The kennel holds more than 30 professionally trained bird dogs. They offer training, breeding, and pointers for the hunt. There is a kennel at the lodge and at the bunkhouse. Bring your own dogs if you want — they have a place to sleep.</p>
<p>The Outdoor Academy lists a 40-dog kennel on the same ranch. Call if you are looking for a pup or a week of training rather than a hunt.</p>''',
[("30+","Trained dogs"),("2","Kennel buildings"),("Yes","Your dogs")],
DEFAULT_REL))


GRAND_LODGE_BODY = f'''
<header class="hero">
  <div class="hero-media" style="background-image:url('img/lodge-exterior.jpg')"></div>
  <div class="hero-grain" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="hero-eyebrow">
      <span class="dash"></span>
      <span class="mono">Opening Fall 2026 · Accepting Reservations</span>
    </div>
    <h1>The Lodge</h1>
    <p class="hero-sub">
      The newly built, state-of-the-art lodge on Red Bank Creek — fourteen beds,
      one private party at a time.
    </p>
    <div class="hero-foot">
      <div class="hero-cta-row">
        <a class="btn-primary" href="contact.html">Book Your Stay</a>
        <a class="btn-ghost" href="{TEL}">Call Us at {PHONE}</a>
      </div>
    </div>
  </div>
</header>

<section class="about">
  <div class="sec">
    <div class="sec-head reveal">
      <div class="mono label">01 — The House</div>
      <h2>Newly built. <em>State of the art.</em> Still run the old way.</h2>
    </div>
    <div class="about-grid">
      <div class="about-copy reveal">
        <p>The Lodge is the main house of the ranch — built new, appointed for the evening after the hunt, and never shared. Fourteen beds, three full showers, a great room under a fireplace wall, and the long table where the household staff serve supper.</p>
        <p>Groups are not mixed. The lodge is yours for the length of your stay, with kennels on site and the porch looking over the creek country.</p>
        <div class="about-stats">
          <div class="stat"><div class="num" data-counter="14">0</div><div class="lbl mono">Beds</div></div>
          <div class="stat"><div class="num" data-counter="3">0</div><div class="lbl mono">Full showers</div></div>
          <div class="stat"><div class="num" data-counter="1">0</div><div class="lbl mono">Party at a time</div></div>
        </div>
      </div>
      <div class="about-img reveal">
        <div class="ph" style="background-image:url('img/lodge.jpg')"></div>
        <div class="cap"><span class="d"></span><span class="mono">The great room</span></div>
      </div>
    </div>
  </div>
</section>

<div class="parallax-band" style="background-image:url('img/pavilion-dusk.jpg')" role="img" aria-label="The lodge pavilion at dusk — string lights over the covered patio"></div>

<section class="house">
  <div class="house-inner">
    <div class="sec-head reveal">
      <div class="mono label">02 — Appointments</div>
      <h2>Everything the evening needs <em>after the hunt.</em></h2>
    </div>
    <div class="house-grid">
      <div class="house-item">
        <span class="n mono">01</span>
        <h3>The great room</h3>
        <p>A fireplace wall, deep sofas, and a big screen with satellite.</p>
      </div>
      <div class="house-item">
        <span class="n mono">02</span>
        <h3>The loft</h3>
        <p>The game room upstairs — cards, the poker table, a nightcap.</p>
      </div>
      <div class="house-item">
        <span class="n mono">03</span>
        <h3>The kitchen</h3>
        <p>A full kitchen and the long table. Meals prepared by the household staff.</p>
      </div>
      <div class="house-item">
        <span class="n mono">04</span>
        <h3>The practical</h3>
        <p>Three full showers, wifi, a large porch, a barbecue, and kennels on site.</p>
      </div>
    </div>
  </div>
</section>

{related_html(0, [
 ("bunkhouse.html","bunkhouse-porch.jpg","The <em>Bunkhouse</em>","Sleeps six. Stone-column porch."),
 ("dining.html","dining.jpg","The <em>Table</em>","Household staff and California wine."),
 ("weddings.html","pavilion-dusk.jpg","Weddings","2,200 sq ft covered patio on the creek.")])}

<section class="cta">
  <div class="cta-bg"></div>
  <div class="cta-inner">
    <h2 class="reveal">The lodge is yours. <em>Book your stay.</em></h2>
    <div class="cta-side reveal">
      <p>Reservations for the 26–27 season are open now. Contact us for dates and pricing, and we will take care of the rest.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn-primary" href="contact.html">Book Your Stay</a>
        <a class="btn-ghost" href="{TEL}">{PHONE}</a>
      </div>
    </div>
  </div>
</section>
'''
add("lodge.html", wrap(0, "The Lodge — Red Bank Outfitters",
"The newly built, state-of-the-art lodge at Red Bank Outfitters, Red Bluff — opening fall 2026 and accepting reservations. Sleeps fourteen. One party at a time.",
GRAND_LODGE_BODY, active="stay", inner=False))

add("bunkhouse.html", page(0, "The Bunkhouse — Red Bank Outfitters",
"Deluxe bunkhouse at Red Bank Outfitters sleeps 6. Full kitchen, satellite TV, dog kennel, barbecue, wifi. Red Bluff, California.",
"stay",
[("Home","index.html"),("Bunkhouse","")],
"The Bunkhouse",
"After meals in the Grand Lodge, retire here. Satellite, a kitchen, a kennel, a barbecue, wifi.",
[("Sleeps","6"),("Kitchen","Full"),("Kennel","Yes")],
"bunkhouse-porch.jpg", "Covered porch of the Red Bank bunkhouse with river-stone columns",
'''<p class="deck">A ranch bunkhouse with river-stone columns on the porch. Six beds. The sign over the patio says Bunkhouse because that is what it is.</p>
<p>Inside: satellite television, a full kitchen, a dog kennel, a barbecue, wifi. The hunt page allows 6–8; the bunkhouse page itself lists six. Call if your party is on the line.</p>
<p>Use it with the lodge for a larger group, or take it as the quieter house.</p>
<ul>
<li>Sleeps up to six</li>
<li>Satellite TV, full kitchen, wifi</li>
<li>Dog kennel and barbecue</li>
</ul>''',
[("6","Beds"),("Stone","Porch columns"),("Kennel","On site")],
[("lodge.html","lodge.jpg","The <em>Lodge</em>","Sleeps 14."),
 ("dining.html","dining.jpg","Dining","Meals in the main house."),
 ("kennels.html","dogs-water.jpg","Dogs","Kennel here too.")]))

add("dining.html", page(0, "Dining — Red Bank Outfitters",
"Home-cooked meals and California wines at Red Bank Outfitters. Day shooters: two days' notice, arrive by 1 p.m.",
"stay",
[("Home","index.html"),("Dining","")],
"Dining",
"Meals prepared and served by the household staff. A selection of California wines. Breakfasts before the walk-up.",
[],
"lodge-wide.jpg", "The long dining table in the new lodge great room — candles lit, fireplace burning",
'''<p class="deck">Legendary home-cooked meals, in their words. Courteous household staff. California wines to match.</p>
<p>Day shooters eat before and after an afternoon hunt. Give two days' notice. Plan on arriving by 1 p.m. They will host lunch and the afternoon.</p>
<p>Weddings and corporate dinners use the same kitchen and the 2,200-square-foot covered patio.</p>''',
[("2 days","Notice"),("1 p.m.","Day-hunt arrival"),("CA","Wines")],
[("lodge.html","lodge.jpg","The <em>Lodge</em>","Where the table lives."),
 ("weddings.html","creek.jpg","Events","Patio and creek bluffs."),
 ("hunts.html","dogs-water.jpg","Then <em>out</em>","Birds after lunch.")]))

WEDDINGS_BODY = f'''
<header class="page-hero">
  <div class="ph-bg" style="background-image:url('img/wedding-venue-wide-01.jpg')" role="img" aria-label="Hay-bale ceremony seating and a vintage car beneath the Red Bank Creek bluffs at golden hour"></div>
  <div class="page-hero-inner">
    {crumbs([("Home","index.html"),("Weddings","")])}
    <h1>Weddings</h1>
    <p class="lead">A Northern California ranch wedding on Red Bank Creek — red bluffs, golden fields, and the whole ranch to yourselves.</p>
    <div class="ph-meta">
      <div><div class="k">Patio</div><div class="v">2,200 sq ft</div></div>
      <div><div class="k">Lodge</div><div class="v">1,800 sq ft</div></div>
      <div><div class="k">Tours</div><div class="v">By appointment</div></div>
    </div>
  </div>
</header>

<div class="wstory">

  <div class="wrow reveal">
    <div class="wimg"><div class="ph" style="background-image:url('img/wedding-edit18.jpg')" role="img" aria-label="The ceremony meadow and the red bluffs of Red Bank Creek"></div></div>
    <div class="wtxt">
      <div class="mono k">01 — The Setting</div>
      <h2>Married under the <em>red bluffs.</em></h2>
      <p>Red Bank sits on the banks of Red Bank Creek, west of Red Bluff. Since 1965 the ranch has hosted astronauts, Hollywood figures, and sports celebrities — and after years of requests, it opened its gates for weddings.</p>
      <p>The ceremony meadow faces the creek bluffs: a wall of red earth crowned with valley oaks that turns to gold in the evening light.</p>
    </div>
  </div>

  <div class="wrow flip reveal">
    <div class="wimg"><div class="ph" style="background-image:url('img/wedding-dress-hanging-01.jpg')" role="img" aria-label="A lace wedding dress hanging from the birch ceremony arch, bluffs behind"></div></div>
    <div class="wtxt">
      <div class="mono k">02 — The Morning</div>
      <h2>Room to get <em>ready.</em></h2>
      <p>The 1,800-square-foot lodge is yours for the day — a private suite and bathroom where the bridal party prepares, and separate quarters for the groomsmen.</p>
      <p>No rushing and no sharing. The house, the porch, and the morning belong to your party alone.</p>
    </div>
  </div>

  <div class="wrow reveal">
    <div class="wimg"><div class="ph" style="background-image:url('img/wedding-long-shot-alter-01.jpg')" role="img" aria-label="Birch arch with roses at the head of a hay-bale aisle, red bluffs behind"></div></div>
    <div class="wtxt">
      <div class="mono k">03 — The Ceremony</div>
      <h2>Vows in the <em>open air.</em></h2>
      <p>A birch arch dressed in roses. Hay-bale pews down a mown aisle. Wine barrels, shepherd's hooks, and a hand-painted welcome sign. Behind it all, the bluffs.</p>
      <p>It is the kind of rustic that cannot be staged in a ballroom, because none of it is staged.</p>
    </div>
  </div>

  <div class="wrow flip reveal">
    <div class="wimg"><div class="ph" style="background-image:url('img/wedding-centerpieces-01.jpg')" role="img" aria-label="Reception tables with peach roses and antler centerpieces"></div></div>
    <div class="wtxt">
      <div class="mono k">04 — The Evening</div>
      <h2>Dinner and dancing <em>under cover.</em></h2>
      <p>A 2,200-square-foot covered patio holds the reception — room for dinner, dancing, and the long toasts that follow.</p>
      <p>At one Red Bank wedding the sign read: &ldquo;Come as you are. Stay as long as you can. We&rsquo;re all family, so no seating plan.&rdquo; That is the spirit of the place.</p>
    </div>
  </div>

</div>

<div class="wmosaic reveal">
  <div class="m" style="background-image:url('img/wedding-overlook-01.jpg')" role="img" aria-label="The ranch and pavilion from the overlook"></div>
  <div class="m" style="background-image:url('img/wedding-wedding-cake-01.jpg')" role="img" aria-label="The wedding cake"></div>
  <div class="m" style="background-image:url('img/wedding-pick-a-seat-01.jpg')" role="img" aria-label="Pick a seat, not a side"></div>
  <div class="m" style="background-image:url('img/wedding-suits-hanging-01.jpg')" role="img" aria-label="The groomsmen's suits"></div>
  <div class="m" style="background-image:url('img/wedding-hamptonwed-2953.jpg')" role="img" aria-label="A Red Bank wedding"></div>
  <div class="m" style="background-image:url('img/wedding-ale-quail-front-gate-01.jpg')" role="img" aria-label="The front gate dressed for a wedding"></div>
</div>

{related_html(0, [
 ("dining.html","dining.jpg","The <em>kitchen</em>","The same household staff."),
 ("lodge.html","lodge.jpg","The <em>Lodge</em>","Bridal party rooms."),
 ("contact.html","ranch-gate.jpg","See it","Six miles from town.")])}

<section class="cta">
  <div class="cta-bg"></div>
  <div class="cta-inner">
    <h2 class="reveal">See it <em>for yourself.</em></h2>
    <div class="cta-side reveal">
      <p>Tours are by appointment. Contact us for available dates and pricing — and walk the patio, the meadow, and the bluffs before you decide a thing.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn-primary" href="contact.html">Schedule a Tour</a>
        <a class="btn-ghost" href="{TEL}">{PHONE}</a>
      </div>
    </div>
  </div>
</section>
'''
add("weddings.html", wrap(0, "Weddings — Red Bank Outfitters",
"Northern California outdoor ranch wedding venue on Red Bank Creek, Red Bluff. Red bluff backdrop, 2,200 sq ft covered patio, 1,800 sq ft lodge. Tours by appointment.",
WEDDINGS_BODY, active="stay"))

RATES_BODY = f'''
<header class="hero">
  <div class="hero-media" style="background-image:url('img/flythrough-poster.jpg')"></div>
  <div class="hero-grain" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="hero-eyebrow">
      <span class="dash"></span>
      <span class="mono">Request Information</span>
    </div>
    <h1>Rates &amp; Packages</h1>
    <p class="hero-sub">
      Every hunt at Red Bank is built around your party, so we quote rates personally.
      Reach out for current hunt and lodging pricing — we are happy to help you plan the trip.
      Blacktail hunts are three days, all inclusive: guide, lodging, meals, and field dressing.
    </p>
    <div class="hero-foot">
      <div class="hero-cta-row">
        <a class="btn-primary" href="{TEL}">Call Us at {PHONE}</a>
        <a class="btn-ghost" href="contact.html">Book a Hunt</a>
      </div>
    </div>
  </div>
</header>
'''
add("rates.html", wrap(0, "Rates & Packages — Red Bank Outfitters",
"Contact Red Bank Outfitters at (530) 529-9435 for reservations and current hunt and lodging rates. Blacktail hunts are 3-day all-inclusive.",
RATES_BODY, active="big", inner=False))

CONTACT_BODY = f'''
<div class="invite-page">
  <div class="invite-card">
    <img class="invite-mark" src="img/mark.svg" alt="" width="54" height="54">
    <div class="mono invite-eyebrow">Est. 1965 · Red Bluff, California</div>
    <h1 class="invite-h1">You are invited<br>to <em>Red Bank</em></h1>
    <p class="invite-sub">A private hunt, a weekend at the lodge, a table by the fire, or a wedding on the creek. The ranch receives one party at a time — and the next one could be yours.</p>
    <div class="invite-rule" aria-hidden="true"><span></span><span class="dm">&#9670;</span><span></span></div>
    <div class="invite-details">
      <div><span class="k mono">Telephone</span><a class="v" href="{TEL}">{PHONE}</a></div>
      <div><span class="k mono">Email</span><a class="v" href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div><span class="k mono">Located At</span><span class="v">18875 Red Bank Rd, Red Bluff</span></div>
    </div>
    <div class="invite-cta">
      <a class="btn-primary" href="{TEL}">Call Us at {PHONE}</a>
    </div>
    <div class="invite-rule" aria-hidden="true"><span></span><span class="dm">&#9670;</span><span></span></div>
    <div class="mono invite-rsvp">RSVP — or write the lodge</div>
    <form class="form invite-form" id="inquireForm">
      <div class="fields">
        <label for="n">Name</label><input id="n" name="Name" required>
        <label for="e">Email</label><input id="e" name="Email" type="email" required>
        <label for="ph">Phone</label><input id="ph" name="Phone" type="tel" required>
        <label for="w">Interest</label>
        <select id="w" name="Interest">
          <option>Upland hunt</option><option>Blacktail deer</option><option>Wild hog</option>
          <option>Bass fishing</option><option>Sporting clays</option><option>Lodge stay</option>
          <option>Wedding</option><option>Corporate</option>
        </select>
        <label for="d">Preferred dates</label><input id="d" name="Dates">
        <label for="m">Message</label><textarea id="m" name="Message"></textarea>
        <button class="btn-primary" type="submit" style="margin-top:8px">Send</button>
      </div>
      <p class="ok">Your mail app should open. If it does not, call {PHONE}.</p>
    </form>
    <p class="mono invite-fine">From I-5, take exit 647 · west on Luther · left on Paskenta · right on Live Oak, which becomes Red Bank · the ranch is on the left, six miles from town · Mail: PO Box 8295, Red Bluff, CA 96080</p>
  </div>
</div>
'''
POSTCARD_BODY = f'''
<div class="pc-page">
  <div class="pc-intro">
    <div class="mono pc-label">Mock-up — Direct Mail Postcard · 6 &times; 4</div>
    <h1 class="pc-h1">The invitation, <em>by post.</em></h1>
  </div>

  <div class="mono pc-side-label">Front</div>
  <div class="pc-card pc-front">
    <div class="pc-photo" style="background-image:url('img/lodge-landscape.jpg')" role="img" aria-label="The new lodge at Red Bank, west of Red Bluff"></div>
    <div class="pc-front-foot">
      <div class="pc-wordmark">RED BANK <em>OUTFITTERS</em></div>
      <div class="mono pc-front-line">The private Southern-style quail hunting ranch · Est. 1965 · Red Bluff, California</div>
    </div>
  </div>

  <div class="mono pc-side-label">Back</div>
  <div class="pc-card pc-back">
    <div class="pc-letter">
      <p class="pc-salute">Dear Friend,</p>
      <p>Since 1965, Red Bank has opened its gate to one party at a time — eighteen thousand acres on Red Bank Creek, west of Red Bluff. This fall we finish something we have wanted to build for years: a new lodge worthy of the ground it sits on.</p>
      <p>I would like you to see it. Come walk the meadow, meet the dogs, and stay for supper at the long table. Bring your own party — we will never mix you with another.</p>
      <p>Reservations for the 26–27 season are open. Call us at <strong>{PHONE}</strong> — or <a href="contact.html">send us an email</a> — and we will hold your dates.</p>
      <p class="pc-sig">Brian Riley</p>
      <p class="mono pc-sig-title">Owner, Red Bank Outfitters</p>
    </div>
    <div class="pc-divider" aria-hidden="true"></div>
    <div class="pc-address">
      <div class="pc-stamp" aria-hidden="true">
        <img src="img/mark.svg" alt="" width="34" height="34">
        <span class="mono">EST.<br>1965</span>
      </div>
      <div class="pc-postmark mono" aria-hidden="true">RED BLUFF · CALIFORNIA · RED BANK CREEK ·</div>
      <div class="pc-lines" aria-hidden="true"><span></span><span></span><span></span></div>
      <div class="mono pc-return">Red Bank Outfitters · 18875 Red Bank Rd, Red Bluff, CA 96080 · RedBankOutfitters.com · {PHONE}</div>
    </div>
  </div>

  <div class="mono pc-side-label">Text message — copy &amp; send from your contacts</div>
  <div class="pc-sms">
    <p class="pc-bubble" id="pcSmsText">hey, it's brian out at red bank. the new lodge is finally open and we're booking the 26–27 season now. space is limited, take a look: https://red-bank-outfitters.netlify.app/lodge.html — call or text me if you want to book a hunt</p>
    <button class="btn-primary" type="button" id="pcCopyBtn">Copy message</button>
  </div>
</div>

<script>
(function () {{
  var btn = document.getElementById('pcCopyBtn');
  var txt = document.getElementById('pcSmsText');
  if (!btn || !txt) return;
  btn.addEventListener('click', function () {{
    var t = txt.textContent.replace(/\s+/g, ' ').trim();
    function done() {{ btn.textContent = 'Copied'; setTimeout(function () {{ btn.textContent = 'Copy message'; }}, 1600); }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(t).then(done, function () {{ fallback(); }});
    }} else {{ fallback(); }}
    function fallback() {{
      var ta = document.createElement('textarea');
      ta.value = t; document.body.appendChild(ta); ta.select();
      try {{ document.execCommand('copy'); done(); }} catch (e) {{}}
      document.body.removeChild(ta);
    }}
  }});
}})();
</script>
'''
# Marketing concept: no site chrome — just the head, the mock-up, done.
add("postcard.html", head(0, "Postcard Mock-up — Red Bank Outfitters",
"Direct-mail postcard mock-up: the new lodge on the front, a letter of invitation from owner Brian Riley on the back.")
+ f'''
<body class="inner" data-root="">
{POSTCARD_BODY}
</body>
</html>
''')

add("contact.html", wrap(0, "Contact — Red Bank Outfitters",
"Contact Red Bank Outfitters — (530) 529-9435. 18875 Red Bank Rd, Red Bluff CA 96080. I-5 exit 647, six miles from town.",
CONTACT_BODY, active="stay"))

add("gallery.html", wrap(0, "Gallery — Red Bank Outfitters",
"Photographs from Red Bank Outfitters: the ranch, the lodge, dogs, clays, blacktail, and hog.",
f'''
<header class="page-hero">
  <div class="ph-bg" style="background-image:url('img/clays-water.jpg')"></div>
  <div class="page-hero-inner">
    {crumbs([("Home","index.html"),("Gallery","")])}
    <h1>Gallery</h1>
    <p class="lead">Photographs from their own gallery and lodge. Landscape frames of oak and creek are labeled where they are generated scenery, not a hunt.</p>
  </div>
</header>
<div style="max-width:1440px;margin:0 auto;padding:48px 40px 8px">
  <div class="mono" style="color:var(--brass);font-size:10px;letter-spacing:0.24em;text-transform:uppercase;margin-bottom:14px">The Film</div>
  <div style="position:relative;aspect-ratio:16/9;background:var(--forest)">
    <iframe src="https://www.youtube-nocookie.com/embed/NSwut20idpI" title="The Red Bank Outfitters film" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
  </div>
</div>
<div class="gallery-grid" style="padding-top:40px">
  <figure><img src="img/lodge.jpg" alt="Lodge living room"><figcaption>Lodge — their photograph</figcaption></figure>
  <figure><img src="img/bunkhouse-porch.jpg" alt="Bunkhouse porch"><figcaption>Bunkhouse porch</figcaption></figure>
  <figure><img src="img/dining.jpg" alt="Lodge dining"><figcaption>The table</figcaption></figure>
  <figure><img src="img/ranch-dog.jpg" alt="Dog watching cattle"><figcaption>Ranch dog, Tehama hills</figcaption></figure>
  <figure><img src="img/dogs-water.jpg" alt="Pointers in a pond"><figcaption>Pointers</figcaption></figure>
  <figure><img src="img/clays-water.jpg" alt="Clays over a pond"><figcaption>Clays over water</figcaption></figure>
  <figure><img src="img/guests.jpg" alt="A hunting party at a pond"><figcaption>A party on the ranch</figcaption></figure>
  <figure><img src="img/deer.jpg" alt="Blacktail buck"><figcaption>Blacktail, 2010</figcaption></figure>
  <figure><img src="img/hog.jpg" alt="Wild hog harvest"><figcaption>Wild hog</figcaption></figure>
  <figure><img src="img/pointer.jpg" alt="A pointer working oak grass" data-generated="true"><figcaption>Pointer in oak grass — generated scenery</figcaption></figure>
  <figure><img src="img/after-supper.jpg" alt="Table after supper" data-generated="true"><figcaption>After supper — generated still life</figcaption></figure>
  <figure><img src="img/hero-oak.jpg" alt="Oak savanna and a snow peak" data-generated="true"><figcaption>Tehama oak country — generated scenery</figcaption></figure>
  <figure><img src="img/creek.jpg" alt="Creek bluffs" data-generated="true"><figcaption>Creek bluffs — generated scenery</figcaption></figure>
  <figure><img src="img/pond.jpg" alt="Bass pond at dusk" data-generated="true"><figcaption>A pond at dusk — generated scenery</figcaption></figure>
</div>
''', active="stay"))

add("news.html", page(0, "News — Red Bank Outfitters",
"Ranch newsletters and dispatches from Red Bank Outfitters, Red Bluff.",
"stay",
[("Home","index.html"),("News","")],
"News",
"The public archive runs 2018–2020. For this season's dates and news, get in touch.",
[("Archive","2018–2020"),("Now","Inquire")],
"ranch-gate.jpg", "A timber ranch gate on a golden hillside at dusk",
'''<p class="deck">Their published newsletters are still on the old WordPress. We are not inventing new ranch news.</p>
<ul>
<li>October 2020 — Around the Ranch newsletter</li>
<li>November 2019 — Around the Ranch newsletter</li>
<li>November 2018 — Around the Ranch newsletter</li>
<li>March 2018 — Upland bird hunting in full swing at Red Bank</li>
</ul>
<p>For current bird numbers, hog activity, and open weekends, contact us at {phone}.</p>'''.format(phone=PHONE),
[],
DEFAULT_REL, generated=True))

# Species
add("upland/bobwhite.html", page(1, "Southern-Style Bob White Quail — Red Bank Outfitters",
"Southern-style bobwhite quail hunts at Red Bank Outfitters. Two guests, one guide, 3–4 dogs. Groups not mixed.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Bobwhite","")],
"Southern-Style Bob White Quail",
"Men and dogs on field edges and flats of head-height brush. Two guests, one guide, three or four dogs.",
[("Party","2 + guide"),("Dogs","3–4"),("Groups","Not mixed")],
"dogs-water.jpg", "Pointers working cover",
'''<p class="deck">Thoughts of Southern-style quail hunting invoke field edges and explosive bobwhites. Since 1965 that has been the point of this ranch.</p>
<p>Red Bank does not mix groups. The lodge holds 14, the bunkhouse 6. No minimum party size.</p>
<p>We hunt with two guests, one guide, and three or four dogs. The dogs are the heart of it. Your own dogs are welcome; there is a kennel at both buildings.</p>''',
[("2","Guests"),("1","Guide"),("3–4","Dogs")],
DEFAULT_REL))

add("upland/valley-quail.html", page(1, "Valley Quail — Red Bank Outfitters",
"Wild valley quail hunted Texas-style, October through January, on 5,000 acres north of Red Bank. Groups of up to four.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Valley quail","")],
"Valley Quail",
"A short California season, October through January. Demand is high. Groups of up to four, out of utility vehicles, on 5,000 acres just north of the ranch.",
[("Season","Oct–Jan"),("Acres","5,000"),("Party","Up to 4")],
"ranch-hills.jpg", "Open ranch hills in Tehama County",
'''<p class="deck">Native birds. A limited season under California law. This is a test of quickness.</p>
<p>Valley quail are hunted on a 5,000-acre ranch just north of Red Bank. Groups of up to four ride utility vehicles to cover the ground. Call early. The window is short.</p>''',
[("Oct–Jan","Season"),("5,000","Acres"),("4","Max in a group")],
DEFAULT_REL))

add("upland/mountain-quail.html", page(1, "Mountain Quail — Red Bank Outfitters",
"Mountain quail hunts a 30-minute drive from Red Bank Outfitters. Chaparral birds, more often heard than seen.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Mountain quail","")],
"Mountain Quail",
"A 30-minute drive from the ranch into mountainous chaparral. Listen at daylight. They run the brush; flights are short and explosive.",
[("Drive","30 min"),("Cover","Chaparral"),("Flight","Short")],
"creek.jpg", "Steep country west of Red Bluff",
'''<p class="deck">The most challenging bird on the list. Mountain quail live in the chaparral west of the Rockies. From Red Bank you drive thirty minutes, listen at daylight, and work the back roads.</p>
<p>They are runners. Any flight is usually short and explosive, then a glide to the bottom of the canyon.</p>''',
[("30 min","From the lodge"),("Dawn","Listen"),("Runners","Not flushers")],
DEFAULT_REL, generated=True))

add("upland/chukar.html", page(1, "Chukar — Red Bank Outfitters",
"Chukar partridge hunts at Red Bank Outfitters. Running birds on steep banks.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Chukar","")],
"Chukar",
"A unique challenge: innate running ability, steep banks, a short flush, then a footrace.",
[("Flush","Short"),("Then","They run"),("Ground","Steep")],
"ranch-hills.jpg", "Steep ranch ground",
'''<p class="deck">Chukar partridge run. They climb a steep bank, flush a short distance, and try the quick-footed escape. That is the hunt.</p>
<p>Stack it with bobwhite or pheasant in the same trip. Contact us and we will put the right day together.</p>''',
[("Short","Flush"),("Steep","Banks"),("Contact","For dates")],
DEFAULT_REL))

add("upland/pheasant.html", page(1, "Walk-Up Pheasant — Red Bank Outfitters",
"Walk-up ring-necked pheasant hunts at Red Bank Outfitters. Minimum two shooters. Lean fliers that make multiple flights.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Pheasant","")],
"Walk-Up Pheasant",
"Ring-necked pheasants that burst cover and make multiple flights. Their squawks startle a field. Two shooters minimum.",
[("Min","2 shooters"),("Bird","Ring-neck"),("Style","Walk-up")],
"pheasant.jpg", "Pheasant hunt photograph from Red Bank",
'''<p class="deck">Walk-up pheasant, with a twist. Quality birds, lean fliers, multiple flights to safety.</p>
<p>Minimum two shooters. For a bigger party and a different rhythm, see the <a href="european-drive.html">European-style drive</a>.</p>''',
[("2","Minimum guns"),("Walk-up","The method"),("Drive","Also offered")],
DEFAULT_REL))

add("upland/european-drive.html", page(1, "European-Style Drive — Red Bank Outfitters",
"European-style driven pheasant at Red Bank Outfitters. 4 to 12 shooters, pegs, beaters, pickers-up. At least 100 birds.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Drive","")],
"European-Style Drive",
"Four to twelve guns. Beaters push pheasants. Pickers-up work behind. After each push, rotate. At least 100 birds released.",
[("Guns","4–12"),("Birds","100+"),("Style","Driven")],
"driven.jpg", "Driven pheasant at Red Bank",
'''<p class="deck">Imagine an English thicket: gentlemen at pegs, beaters pushing birds, pickers-up with retrievers behind the line. After each push, a pause, then rotate.</p>
<p>A squad of 4 to 12 shooters works every station and every angle. At least 100 birds are released. Additional pheasants are available.</p>
<p>On the old Sportsman's News film they drove birds off a bluff about a hundred feet up. Call if you want that shape of day.</p>''',
[("4–12","Shooters"),("100+","Birds"),("Pegs","Rotate")],
DEFAULT_REL))

add("upland/turkey.html", page(1, "Wild Turkey — Red Bank Outfitters",
"Rio Grande wild turkey hunts at Red Bank Outfitters. Fall: tom or hen. Spring: bearded gobblers only. California seasons.",
"upland",
[("Home","../index.html"),("Upland","../upland.html"),("Turkey","")],
"Wild Turkey",
"A California wildlife-management success story. Fall: tom or hen. Spring: gobblers with visible beards only. Guides will teach you to call.",
[("Fall","Tom or hen"),("Spring","Bearded toms"),("Regs","CA F&W")],
"guests.jpg", "A hunting party on the ranch",
'''<p class="deck">Wild turkeys are the shining success story for wildlife management in California, in their words. Red Bank keeps a sustainable, increasing flock.</p>
<p>Fall hunters may take a tom or a hen. In the spring only gobblers with visible beards may be taken. Championship-caliber guides will teach you to call. All hunts run under seasons established by the state.</p>
<p>Jordy killed his first turkey here. Call if that is the trip you want.</p>''',
[("2","Seasons"),("CA","Regulations"),("Guides","Call with you")],
DEFAULT_REL))

add("hunts/blacktail.html", page(1, "Blacktail Deer Hunts — Red Bank Outfitters",
"Columbia blacktail deer hunts at Red Bank Outfitters. 10,000+ acres, 6–10 bucks a day, 3-day all-inclusive: guide, lodging, meals, field dressing.",
"big",
[("Home","../index.html"),("Big Game","../big-game.html"),("Blacktail","")],
"Blacktail Deer",
"More than 10,000 acres of managed habitat. A healthy buck-to-doe ratio. Average 6 to 10 bucks a day. Guide, lodging, meals, field dressing included.",
[("Acres","10,000+"),("Days","3"),("Bucks / day","6–10")],
"deer.jpg", "A blacktail buck taken at Red Bank",
'''<p class="deck">We now offer over 10,000 acres of prime habitat for blacktail deer. The herd is managed closely through habitat work and the number of animals taken per year.</p>
<p>On your hunt you will see an abundance of wildlife and average 6 to 10 bucks a day. The three-day hunt includes guide, lodging, meals, and field dressing ready for the butcher. Walk-in cold storage is on the ranch. They will prepare a trophy for the taxidermist and can assist with a local shop.</p>
<p>Roger Sabette, after years of asking, became the first archery hunter Brian Riley permitted on a blacktail in 26 years of owning the ranch. Ric Gould guided him. Rifle season remains limited. Call.</p>''',
[("3","Days"),("6–10","Bucks seen"),("Incl.","Guide, bed, table")],
[("hunts/wild-hog.html","hog.jpg","Wild <em>hog</em>","Same ranch, different animal."),
 ("lodge.html","lodge.jpg","Lodge","Part of the package."),
 ("upland.html","dogs-water.jpg","Add <em>birds</em>","If dates allow.")]))

add("hunts/wild-hog.html", page(1, "Wild Hog — Red Bank Outfitters",
"Wild hog hunts on 18,000 acres at Red Bank Outfitters. Oaks, manzanita, poison oak draws, eucalyptus grove. UTV or on foot.",
"big",
[("Home","../index.html"),("Big Game","../big-game.html"),("Wild hog","")],
"Wild Hog",
"European wild boar, feral hogs, and crosses. Eighteen thousand acres from open oak hills to manzanita bedding cover.",
[("Acres","18,000"),("Method","UTV or foot"),("Grove","Eucalyptus option")],
"hog.jpg", "A wild hog taken at Red Bank Outfitters",
'''<p class="deck">From California's north coast to the eastern Sierra, European wild boar, feral hogs, and crosses range the most populated state in the union. At Red Bank you hunt them on 18,000 acres.</p>
<p>Open rolling hills dotted with oak. Deep draws of poison oak and manzanita — favorite bedding. Other ground is thicker studded oaks on flatter terrain. For the brave: a thousand-acre eucalyptus grove with dogs and an open-sight big-bore.</p>
<p>You will spend time on a UTV. Awkward-looking animals, well-built, and not to be underestimated. Confirm current California rules when you book.</p>''',
[("18,000","Acres"),("UTV","Standard"),("Dogs","Grove option")],
[("hunts/blacktail.html","deer.jpg","Blacktail","Three-day hunts."),
 ("lodge.html","lodge.jpg","Stay","Lodge or bunkhouse."),
 ("gallery.html","hog-record.jpg","440 lb","Ranch record, 2011.")]))

def canonical_for(rel):
    """Absolute canonical URL for a generated page. index.html canonicalises
    to the bare origin, not /index.html."""
    return SITE_URL + "/" + ("" if rel == "index.html" else rel)

def write_all():
    for rel, html in PAGES:
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        # head() has no idea which page it is building, so the canonical is
        # stamped here, where rel is known. Without it the copy still served
        # from GitHub Pages would read as duplicate content.
        tag = f'<link rel="canonical" href="{canonical_for(rel)}">\n'
        html = html.replace("</head>", tag + "</head>", 1)
        path.write_text(html)
        print("wrote", rel, "bytes", path.stat().st_size)

    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: " + SITE_URL + "/sitemap.xml\n")
    (ROOT / "llms.txt").write_text("""# Red Bank Outfitters
> Private hunting ranch, Red Bluff, California. Est. 1965.

- Phone: (530) 529-9435
- Email: Hunting@RedBankOutfitters.com
- Address: 18875 Red Bank Rd, Red Bluff, CA 96080
- Mail: PO Box 8295, Red Bluff, CA 96080
- Acres: 18,000 on Red Bank Creek, Tehama County
- Lodge sleeps 14; bunkhouse sleeps 6
- 11 bass ponds; 18-station sporting clays
- Upland: bobwhite, valley quail, mountain quail, chukar, pheasant, European drive, Rio Grande turkey
- Big game: Columbia blacktail deer (3-day all-inclusive), wild hog
- Groups are not mixed. 2 guests, 1 guide, 3–4 dogs on upland
- Reservations by phone. Rates not published online.
- Academy (separate): https://redbankoutdooracademy.com/
""")
    urls = [
        "index.html","the-ranch.html","hunts.html","upland.html","big-game.html",
        "bass.html","clays.html","kennels.html","lodge.html","bunkhouse.html",
        "dining.html","weddings.html","rates.html","contact.html","gallery.html","news.html",
        "upland/bobwhite.html","upland/valley-quail.html","upland/mountain-quail.html",
        "upland/chukar.html","upland/pheasant.html","upland/european-drive.html","upland/turkey.html",
        "hunts/blacktail.html","hunts/wild-hog.html",
    ]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{canonical_for(u)}</loc></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm))
    print("pages", len(PAGES))

if __name__ == "__main__":
    write_all()
