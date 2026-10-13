#!/usr/bin/env python3
"""Ana sayfa bağlantılarını iç sayfalara bağlar ve tüm iç sayfaları üretir.
Her çalıştırmada index_base.html'den (7406807 sürümü) başlar; tekrar çalıştırılabilir."""
import re, sys, os
SCR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo kökü (_gelistirme/..)
BASE_URL = "https://acsezuma.github.io/apikultur-vakfi-v2/"
idx = open(f"{SCR}/index_base.html", encoding="utf-8").read()

def once(s, old, new, label, count=1):
    n = s.count(old)
    if n != count: print(f"!! HATA [{label}]: beklenen {count}, bulunan {n}"); sys.exit(1)
    return s.replace(old, new)

MAILTO = "mailto:info@apikulturvakfi.org?subject="
ARROW = '<span class="material-symbols-outlined text-[20px] group-hover:translate-x-1 transition-transform">arrow_forward</span>'
NAVC = 'class="nav-link text-[12px] font-semibold text-espresso uppercase tracking-wide"'
MOBC = 'class="py-3.5 border-b border-outline-variant/15 text-espresso font-semibold uppercase tracking-wider text-sm"'
FTC = 'class="hover:text-terracotta transition-colors"'

# =====================================================================
# 1) ANA SAYFA: menü, footer ve bölüm butonları iç sayfalara
# =====================================================================
idx = once(idx, "section[id] { scroll-margin-top: 96px; }", "[id] { scroll-margin-top: 104px; }", "scroll-margin")
EN_SLUG = {"index.html": "index.html", "vakif.html": "about.html", "faaliyet.html": "areas-of-work.html", "genclik.html": "youth.html",
           "akademi.html": "academy.html", "projeler.html": "projects.html", "yonetim.html": "governance.html", "gelecek.html": "future.html"}
LANG_BTN = ('<a href="__LANG__" hreflang="en" lang="en" title="English" aria-label="English version" class="inline-flex items-center justify-center w-11 h-11 '
            'rounded-full border border-outline-variant/60 text-espresso text-[12px] font-bold tracking-wider hover:border-terracotta hover:text-terracotta transition-colors">EN</a>\n')
idx = once(idx, '<a href="senet.html" title="Vakıf Senedi"', LANG_BTN + '<a href="senet.html" title="Vakıf Senedi"', "lang-btn")
ALT = '\n<link rel="alternate" hreflang="tr" href="__ALT_TR__"/>\n<link rel="alternate" hreflang="en" href="__ALT_EN__"/>\n<link rel="alternate" hreflang="x-default" href="__ALT_TR__"/>'
idx = re.sub(r'(<link rel="canonical" href="[^"]*"/>)', lambda m: m.group(1) + ALT, idx, count=1)
def fill_lang(s, fname):
    return (s.replace("__LANG__", "en/" + EN_SLUG[fname]).replace("__ALT_TR__", BASE_URL + (fname if fname != "index.html" else ""))
             .replace("__ALT_EN__", BASE_URL + "en/" + (EN_SLUG[fname] if fname != "index.html" else "")))
# Header: dil butonu eklenince mobilde "Bağış Yap" kırılıyordu -> sıkılaştırma
idx = once(idx, '<div class="max-w-[1180px] mx-auto flex justify-between items-center px-7 h-24">', '<div class="max-w-[1180px] mx-auto flex justify-between items-center px-5 sm:px-7 h-24">', "hdr-px")
idx = once(idx, 'class="bg-terracotta text-white px-5 sm:px-7 py-3.5 rounded-full font-bold text-sm tracking-wide', 'class="whitespace-nowrap bg-terracotta text-white px-4 sm:px-7 py-3.5 rounded-full font-bold text-sm tracking-wide', "hdr-bagis")
idx = once(idx, 'inline-flex items-center justify-center gap-2 w-11 h-11 xl:w-auto xl:h-auto', 'inline-flex items-center justify-center gap-2 w-10 h-10 sm:w-11 sm:h-11 xl:w-auto xl:h-auto', "hdr-senet")
idx = once(idx, 'class="inline-flex items-center justify-center w-11 h-11 rounded-full border border-outline-variant/60', 'class="inline-flex items-center justify-center w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-outline-variant/60', "hdr-lang")
idx = once(idx, 'class="lg:hidden inline-flex items-center justify-center w-11 h-11 rounded-full', 'class="lg:hidden inline-flex items-center justify-center w-10 h-10 sm:w-11 sm:h-11 rounded-full', "hdr-menu")
idx = once(idx, '<div class="flex items-center gap-2 sm:gap-3">', '<div class="flex items-center gap-1.5 sm:gap-3">', "hdr-gap")
idx = once(idx, '.nav-link { position: relative; padding: 0.5rem 0; }', '.nav-link { position: relative; padding: 0.5rem 0; white-space: nowrap; }', "nav-nowrap")
idx = once(idx, '.nav-link { position: relative; padding: 0.5rem 0; white-space: nowrap; }', '.nav-link { position: relative; padding: 0.5rem 0; white-space: nowrap; }\n        @media (min-width:1024px) and (max-width:1279px){ .nav-link{ font-size:11px !important; letter-spacing:0.01em !important; } }', "nav-lg")
idx = once(idx, '<nav class="hidden lg:flex items-center gap-4 xl:gap-5">', '<nav class="hidden lg:flex items-center gap-3.5 xl:gap-5">', "nav-gap-lg")
# Şablon imzası gibi duran mono/büyük harf etiketler: kaldır ya da sade metne çevir
idx = once(idx, '\n<p class="font-label-mono text-[11px] tracking-[0.2em] leading-loose uppercase text-white/70">Bilim · Eğitim · Sürdürülebilirlik · Gençlik · Kültür</p>', '', "hero-slogan")
idx = once(idx, '<div class="flex flex-wrap gap-4 mb-10"><a class="bg-amber text-espresso px-9', '<div class="flex flex-wrap gap-4"><a class="bg-amber text-espresso px-9', "hero-btn-mb")
idx = once(idx, '<span class="scroll-cue__label">Keşfet</span>', '', "scroll-label")
idx, n = re.subn(r'<div class="font-label-mono text-\[11px\] tracking-widest uppercase text-amber mb-2" lang="en">([^<]+)</div><h4 class="font-headline-md text-xl mb-3">([A-Z]+)</h4>',
                 r'<h4 class="font-headline-md text-xl mb-1">\2</h4><p class="text-sm text-white/55 mb-3" lang="en">\1</p>', idx)
if n != 2: print("!! icyb etiket", n); sys.exit(1)
idx = once(idx, '<p class="font-label-mono text-[12px] tracking-widest uppercase text-amber">Yaş grubu: 12–18</p>', '<p class="text-white/60">Yaş grubu: 12–18</p>', "yas-grubu")
idx, n = re.subn(r'<div class="font-label-mono text-\[11px\] tracking-widest uppercase text-terracotta mb-4">([^<]+)</div>', r'<h3 class="font-headline-md text-lg text-espresso mb-4">\1</h3>', idx)
if n != 3: print("!! isbirligi etiket", n); sys.exit(1)
idx = once(idx, 'og-image.png?v=2', 'og-image.png?v=3', 'og-surum', 2)
# Mobil menü: bg-white/98 Tailwind ölçeğinde yok -> saydam kalıyordu
idx = once(idx, 'bg-white/98', 'bg-white', "menu-bg")
# Footer başlıkları h4 -> h2 (başlık hiyerarşisi)
fi = idx.index('<footer')
foot = idx[fi:]
foot = once(foot, '<h4 class="font-bold text-xs uppercase tracking-widest text-terracotta mb-8">', '<h2 class="font-bold text-xs uppercase tracking-widest text-terracotta mb-8">', "footer-h", 4)
foot = re.sub(r'(<h2 class="font-bold text-xs[^"]*">[^<]*)</h4>', r'\1</h2>', foot)
idx = idx[:fi] + foot
# Ana sayfa faaliyet kartları -> faaliyet.html#eksen
AX_IDS = {"science": "bilim-arastirma", "school": "egitim-bilgi", "eco": "surdurulebilir-aricilik", "diversity_3": "genclik-gelecek", "public": "kultur-uluslararasi"}
def feat_link(m):
    cls, inner = m.group(1), m.group(2)
    icon = re.search(r'text-3xl">([a-z_0-9]+)</span>', inner).group(1)
    return f'<a href="faaliyet.html#{AX_IDS[icon]}" class="block feat-card {cls}">{inner}</p></a>'
idx, n = re.subn(r'<div class="feat-card ([^"]*)">(.*?)</p></div>', feat_link, idx, flags=re.S)
if n != 5: print("!! faaliyet kartı", n); sys.exit(1)
for old, new in (("#hakkimizda", "vakif.html"), ("#genclik", "genclik.html"), ("#akademi", "akademi.html"),
                 ("#projeler", "projeler.html"), ("#yonetim", "yonetim.html")):
    idx = once(idx, f'<a {NAVC} href="{old}">', f'<a {NAVC} href="{new}">', "nav " + old)
    idx = once(idx, f'<a {MOBC} href="{old}">', f'<a {MOBC} href="{new}">', "mob " + old)
for text, old, new in (("Vakıf Hakkında", "#vakif-hakkinda", "vakif.html"), ("Yönetim &amp; Şeffaflık", "#yonetim", "yonetim.html"),
                       ("Faaliyet Raporları", "#yonetim", "yonetim.html#seffaflik"), ("Gençlik", "#genclik", "genclik.html"),
                       ("Akademi &amp; Bilim", "#akademi", "akademi.html"), ("Projeler", "#projeler", "projeler.html"),
                       ("Bilgi Merkezi", "#akademi", "akademi.html#bilgi-merkezi"), ("Yayınlar", "#akademi", "akademi.html#bilgi-merkezi"),
                       ("Haberler", "#", "genclik.html#takvim"), ("Etkinlikler", "#", "genclik.html#takvim")):
    idx = once(idx, f'<a {FTC} href="{old}">{text}</a>', f'<a {FTC} href="{new}">{text}</a>', "footer " + text)

# Biz Kimiz -> Vakıf Hakkında sayfası
idx = once(idx, '<a href="#vakif-hakkinda" class="inline-flex items-center gap-2 bg-white/10', '<a href="vakif.html" class="inline-flex items-center gap-2 bg-white/10', "bizkimiz-btn")
# Vakıf Hakkında bölümü: hikâye bağlantısı
idx = once(idx, '<p>Vakfımız, bilgi üretmeyi, bilgiyi paylaşmayı, gençleri desteklemeyi ve farklı paydaşlar arasında iş birliği geliştirmeyi temel faaliyet araçları olarak görür.</p>\n</div>\n',
           '<p>Vakfımız, bilgi üretmeyi, bilgiyi paylaşmayı, gençleri desteklemeyi ve farklı paydaşlar arasında iş birliği geliştirmeyi temel faaliyet araçları olarak görür.</p>\n</div>\n'
           f'<a href="vakif.html#hikaye" class="mt-8 inline-flex items-center gap-2 text-terracotta font-bold group">Vakfın Hikâyesi {ARROW}</a>\n', "vakif-hikaye-link")
# Gençlik: brief [Gençlik Çalışmalarımız] ve [Gençlik Kulüplerini İncele]
idx = once(idx, '<p class="text-white/75 text-lg leading-relaxed max-w-3xl mb-14 reveal-on-scroll">Gençlik çalışmalarımızı tek bir proje olarak değil, Vakfın gelecek nesillerin gelişimine katkı sağlama sorumluluğunun bir parçası olarak görüyoruz.</p>',
           '<div class="max-w-3xl mb-14 reveal-on-scroll"><p class="text-white/75 text-lg leading-relaxed mb-8">Gençlik çalışmalarımızı tek bir proje olarak değil, Vakfın gelecek nesillerin gelişimine katkı sağlama sorumluluğunun bir parçası olarak görüyoruz.</p>'
           f'<a href="genclik.html" class="inline-flex items-center gap-2 bg-white/10 border border-white/25 text-white px-8 py-4 rounded-full font-bold hover:bg-white/20 transition-all group">Gençlik Çalışmalarımız {ARROW}</a></div>', "genclik-btn")
idx = once(idx, '<div class="flex flex-wrap gap-4 lg:justify-end"><a href="#iletisim" class="bg-amber text-espresso px-7 py-4 rounded-full font-bold text-sm hover:-translate-y-0.5 transition-all">Gençlik Kulübü Kurmak İstiyorum</a></div>',
           f'<div class="flex flex-wrap gap-4 lg:justify-end"><a href="genclik.html#kulupler" class="border border-white/30 text-white px-7 py-4 rounded-full font-bold text-sm hover:bg-white/10 transition-all">Gençlik Kulüplerini İncele</a><a href="{MAILTO}Gen%C3%A7lik%20Kul%C3%BCb%C3%BC" class="bg-amber text-espresso px-7 py-4 rounded-full font-bold text-sm hover:-translate-y-0.5 transition-all">Gençlik Kulübü Kurmak İstiyorum</a></div>', "kulup-btn")
# Bilim ve gelenek kartı
idx = once(idx, '<a href="#akademi" class="text-terracotta font-bold flex items-center gap-2 group w-max">', '<a href="akademi.html" class="text-terracotta font-bold flex items-center gap-2 group w-max">', "bilim-gelenek")
# Akademi: 3 öğe tıklanabilir (brief: [Akademi] [Araştırmalar] [Bilgi Merkezi])
for icon, title, href in (("school", "Apikültür Akademi", "akademi.html#akademi-egitim"), ("science", "Araştırma &amp; Bilim", "akademi.html#arastirma"),
                          ("menu_book", "Bilgi Merkezi", "akademi.html#bilgi-merkezi")):
    old = f'<div class="flex gap-6"><span class="material-symbols-outlined text-terracotta text-4xl shrink-0">{icon}</span><div><h3 class="font-headline-md text-2xl text-espresso mb-2">{title}</h3>'
    new = f'<a href="{href}" class="flex gap-6 group"><span class="material-symbols-outlined text-terracotta text-4xl shrink-0">{icon}</span><div><h3 class="font-headline-md text-2xl text-espresso mb-2 group-hover:text-terracotta transition-colors inline-flex items-center gap-2">{title} <span class="material-symbols-outlined text-[20px] text-terracotta opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all">arrow_forward</span></h3>'
    idx = once(idx, old, new, "akademi " + icon)
    i = idx.index(new) + len(new); j = idx.index('</p></div></div>', i)
    idx = idx[:j] + '</p></div></a>' + idx[j + len('</p></div></div>'):]
# Projeler: kartlar proje sayfasına
PROJ_IDS = {"p1-bee-friend": "ari-dostum", "p3-corridor-lavender": "ari-koridoru", "p4-women-planting": "kadin-genc-arici",
            "p5-honey-jar": "cografi-isaret", "p6-meadow": "apiterapi-apiturizm"}
def card_link(m):
    cls, inner = m.group(1), m.group(2)
    pid = next(v for k, v in PROJ_IDS.items() if k in inner)
    return (f'<a href="projeler.html#{pid}" class="group block {cls}">{inner}</p>'
            f'<span class="mt-4 inline-flex items-center gap-1.5 text-terracotta text-sm font-bold">Projeyi İncele <span class="material-symbols-outlined text-[18px] group-hover:translate-x-1 transition-transform">arrow_forward</span></span></a>')
idx, n = re.subn(r'<div class="group (reveal-on-scroll shrink-0 basis-\[80%\][^"]*)">(.*?)</p></div>', card_link, idx, flags=re.S)
if n != 5: print("!! proje kartı", n); sys.exit(1)
idx = once(idx, '<p class="mt-8 text-sm text-on-surface-variant/70 reveal-on-scroll">Projelere ait katılımcı, okul ve etkinlik sayıları yalnızca ilgili projenin kendi kapsamında paylaşılır.</p>',
           '<div class="mt-8 flex flex-col md:flex-row md:items-center md:justify-between gap-6 reveal-on-scroll"><p class="text-sm text-on-surface-variant/70">Projelere ait katılımcı, okul ve etkinlik sayıları yalnızca ilgili projenin kendi kapsamında paylaşılır.</p>'
           f'<a href="projeler.html" class="shrink-0 inline-flex items-center gap-2 border border-terracotta text-terracotta px-7 py-3.5 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all group">Tüm Projeler {ARROW}</a></div>', "tum-projeler")
# Yönetim: brief §18 [Yönetim & Şeffaflık]
idx = once(idx, '<p class="text-on-surface-variant leading-relaxed mb-3">Alan uzmanlarının ve paydaşların görüş ve deneyimleriyle Vakfın çalışmalarına katkı sunar.</p>\n</div>\n</div>\n',
           '<p class="text-on-surface-variant leading-relaxed mb-3">Alan uzmanlarının ve paydaşların görüş ve deneyimleriyle Vakfın çalışmalarına katkı sunar.</p>\n</div>\n</div>\n'
           f'<a href="yonetim.html" class="mt-14 inline-flex items-center gap-2 border border-terracotta text-terracotta px-8 py-4 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all group">Yönetim &amp; Şeffaflık {ARROW}</a>\n', "yonetim-btn")
# ---- Vakıf Senedi: header butonu yerine menüde "Vakıf" altında; ana sayfa içeriğinde tek yer (Yönetim butonu) ----
idx, n = re.subn(r'<a href="senet.html" title="Vakıf Senedi"[^>]*>.*?</a>\n', '', idx, count=1, flags=re.S)
if n != 1: print("!! header senet", n); sys.exit(1)
DD_A = 'class="flex items-center gap-2 px-5 py-2.5 text-[13px] font-semibold text-espresso hover:text-terracotta hover:bg-ekru/60 transition-colors"'
idx = once(idx, f'<a {NAVC} href="vakif.html">Vakıf</a>\n',
           '<div class="relative group/vakif flex items-center gap-0.5">\n'
           f'<a {NAVC} href="vakif.html">Vakıf</a><span class="material-symbols-outlined text-[16px] text-espresso/50 group-hover/vakif:text-terracotta transition-colors" aria-hidden="true">expand_more</span>\n'
           '<div class="absolute left-[-1.25rem] top-full pt-3 opacity-0 invisible group-hover/vakif:opacity-100 group-hover/vakif:visible group-focus-within/vakif:opacity-100 group-focus-within/vakif:visible transition-all duration-200">\n'
           '<div class="min-w-[210px] bg-white rounded-2xl shadow-xl shadow-espresso/10 border border-outline-variant/30 py-2">\n'
           f'<a {DD_A} href="vakif.html">Vakıf Hakkında</a>\n'
           f'<a {DD_A} href="senet.html"><span class="material-symbols-outlined text-[18px] text-terracotta">description</span>Vakıf Senedi</a>\n'
           '</div>\n</div>\n</div>\n', "nav-dropdown")
idx = once(idx, '<a class="py-3.5 inline-flex items-center gap-2 text-terracotta font-bold" href="senet.html"><span class="material-symbols-outlined text-[20px]">description</span>Vakıf Senedi</a>\n', '', "mob-senet-eski")
idx = once(idx, f'<a {MOBC} href="vakif.html">Vakıf</a>\n',
           f'<a {MOBC} href="vakif.html">Vakıf</a>\n'
           '<a class="py-3 pl-5 border-b border-outline-variant/15 text-espresso/80 font-semibold text-sm inline-flex items-center gap-2" href="senet.html"><span class="material-symbols-outlined text-[18px] text-terracotta">description</span>Vakıf Senedi</a>\n', "mob-senet-alt")
# Kurul kartları: senet bağlantısı ve "Senette incele" kaldırıldı (Yönetim butonu yeterli)
idx, n = re.subn(r'<a href="senet.html" class="group block border-t-2 border-terracotta/70 pt-5">(.*?)<span class="inline-flex items-center gap-1 text-terracotta text-sm font-bold opacity-0 group-hover:opacity-100 transition-opacity">Senette incele <span class="material-symbols-outlined text-\[16px\]">arrow_forward</span></span>\n</a>',
                 lambda m: '<div class="group block border-t-2 border-terracotta/70 pt-5">' + m.group(1).replace(' group-hover:text-terracotta transition-colors', '') + '</div>', idx, flags=re.S)
if n != 2: print("!! kurul senet", n); sys.exit(1)
# Destek: Md.16 cümlesi ve senet bağlantısı kaldırıldı (bilgi Yönetim & Şeffaflık sayfasında)
idx, n = re.subn(r'<p class="[^"]*">Vakıf senedinin 16\. maddesi gereği Vakfın <b[^>]*>[^<]*</b>[^<]*<a href="senet.html"[^>]*>[^<]*</a></p>\n', '', idx)
if n != 1: print("!! destek md16", n); sys.exit(1)
idx = once(idx, '<li>ICYB</li><li>FAO</li><li>Apimondia</li></ul>', '<li>ICYB</li><li>FAO</li><li>Apimondia</li><li>COLOSS</li></ul>', 'coloss')
idx = once(idx, 'text-espresso">Tamamlandı</span>', 'text-espresso">Devam ediyor</span>', 'aridostum-durum')
exec(open(f'{SCR}/gelecek_index.py', encoding='utf-8').read())
open(f"{REPO}/index.html", "w", encoding="utf-8").write(fill_lang(idx, "index.html"))
print("OK  index.html")

# =====================================================================
# 2) ORTAK KABUK
# =====================================================================
HEAD = idx[:idx.index('</head>')]
HEADER = idx[idx.index('<!-- Header -->'):idx.index('<main>')]
FOOTER = idx[idx.index('<footer'):]

def to_home(s):
    s = s.replace('href="#top"', 'href="index.html"')
    return re.sub(r'href="#([a-z][^"]*)"', r'href="index.html#\1"', s)

def shell(fname, title, desc, crumb, main):
    url = BASE_URL + fname
    h = HEAD
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h)
    for pat, val in ((r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{desc}"/>'),
                     (r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>'),
                     (r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{url}"/>'),
                     (r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{title}"/>'),
                     (r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{desc}"/>'),
                     (r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{title}"/>'),
                     (r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{desc}"/>')):
        h = re.sub(pat, val, h)
    h = re.sub(r'<!-- NOT:[^>]*-->\n', '', h)
    crumb_plain = crumb.replace('&amp;', '&')
    ld = ('<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n'
          f'    {{"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "{BASE_URL}"}},\n'
          f'    {{"@type": "ListItem", "position": 2, "name": "{crumb_plain}", "item": "{url}"}}\n  ]\n}}\n</script>')
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: ld, h, flags=re.S)
    h = h.replace('    </style>', '        .nav-link[aria-current="page"] { color:#B82618; }\n        .nav-link[aria-current="page"]::after { width:100%; }\n    </style>')
    hd = to_home(HEADER)
    if f'<a {NAVC} href="{fname}">' in hd:
        hd = once(hd, f'<a {NAVC} href="{fname}">', f'<a {NAVC} href="{fname}" aria-current="page">', "active " + fname)
        hd = once(hd, f'<a {MOBC} href="{fname}">', f'<a {MOBC.replace("text-espresso", "text-terracotta")} href="{fname}" aria-current="page">', "mob-active " + fname)
    page = (h + '</head>\n<body class="bg-background text-on-background font-body-md overflow-x-hidden selection:bg-terracotta/10 selection:text-terracotta">\n'
            + hd + '<main>\n' + main + '</main>\n' + to_home(FOOTER))
    open(f"{REPO}/{fname}", "w", encoding="utf-8").write(fill_lang(page, fname))
    print(f"OK  {fname}", len(page))

# ---------- bileşenler ----------
def hero(img, crumb, h1, lead, sub, toc, actions=''):
    toc_html = ''
    if toc:
        cols = {3: 'lg:grid-cols-3', 4: 'lg:grid-cols-4', 5: 'lg:grid-cols-5'}[len(toc)]
        toc_html = (f'<ol class="mt-14 md:mt-16 grid gap-x-8 gap-y-5 sm:grid-cols-2 {cols}">' + ''.join(
            f'<li><a href="#{i}" class="group flex items-baseline gap-3 border-t border-white/20 pt-4 hover:border-amber transition-colors">'
            f'<span class="font-headline-md text-white/90 group-hover:text-white leading-snug">{t}</span></a></li>'
            for n, (i, t) in enumerate(toc, 1)) + '</ol>')
    sub_html = f'<p class="text-white/70 text-lg leading-relaxed max-w-2xl">{sub}</p>' if sub else ''
    return f'''<!-- Sayfa başı -->
<section class="relative isolate overflow-hidden pt-40 pb-16 md:pt-48 md:pb-20" id="top">
<div class="absolute inset-0 -z-10" aria-hidden="true"><img src="{img}" alt="" class="w-full h-full object-cover"/><div class="absolute inset-0" style="background:linear-gradient(100deg, rgba(51,38,27,0.94) 0%, rgba(51,38,27,0.80) 50%, rgba(51,38,27,0.55) 100%)"></div></div>
<div class="max-w-[1180px] mx-auto px-7">
<nav aria-label="Sayfa konumu" class="mb-8"><ol class="flex flex-wrap items-center gap-2 text-sm text-white/60"><li><a class="hover:text-white transition-colors" href="index.html">Ana Sayfa</a></li><li aria-hidden="true">/</li><li class="text-white/90" aria-current="page">{crumb}</li></ol></nav>
<div class="max-w-3xl">
<h1 class="font-display-hero text-5xl md:text-6xl text-white leading-[1.05] mb-8">{h1}</h1>
<p class="text-xl md:text-2xl text-white/90 leading-snug max-w-2xl mb-5">{lead}</p>
{sub_html}
{actions}
</div>
{toc_html}
</div>
</section>
'''

def block(t, p, extra=''):
    return (f'<div class="border-t border-outline-variant/40 py-7"><h3 class="font-headline-md text-xl text-espresso mb-2">{t}</h3>'
            f'<p class="text-on-surface-variant leading-relaxed">{p}</p>{extra}</div>')

def feature(i, sid, img, alt, icon, no, title, lead, blocks_html, more=None, badge=None, extra_top='', tail=''):
    bg = "bg-background" if i % 2 == 0 else "bg-ekru/30"
    order = "" if i % 2 == 0 else " lg:order-2"
    badge_html = f'<span class="text-[11px] font-bold px-3 py-1 rounded-full bg-ekru text-espresso">{badge}</span>' if badge else ''
    no_html = f'<span class="font-label-mono text-terracotta/40 font-bold text-lg">{no}</span>' if no else ''
    more_html = ''.join(f'<a class="mt-6 mr-8 inline-flex items-center gap-2 text-terracotta font-bold group" href="{h}">{t} {ARROW}</a>' for t, h in (more or []))
    blocks_wrap = f'<div class="border-b border-outline-variant/40">{blocks_html}</div>' if blocks_html else ''
    return f'''<section class="py-24 md:py-32 {bg}" id="{sid}">
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-10 lg:gap-16 items-start">
<div class="lg:col-span-5{order} lg:sticky lg:top-32 reveal-on-scroll"><img src="{img}" alt="{alt}" loading="lazy" class="w-full aspect-[16/10] lg:aspect-[4/5] object-cover rounded-3xl shadow-xl shadow-espresso/10"/></div>
<div class="lg:col-span-7 reveal-on-scroll">
<div class="flex items-center gap-4 mb-6"><span class="w-12 h-12 rounded-2xl bg-ekru flex items-center justify-center"><span class="material-symbols-outlined text-terracotta text-2xl">{icon}</span></span>{no_html}{badge_html}</div>
<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-6">{title}</h2>
<p class="text-on-surface-variant text-lg leading-relaxed mb-10 max-w-2xl">{lead}</p>
{extra_top}{blocks_wrap}
{more_html}
{tail}
</div>
</div>
</section>
'''

def cta(h2, p, buttons):
    btns = ''
    for k, (t, h) in enumerate(buttons):
        cls = ("bg-amber text-espresso px-9 py-4 rounded-full font-bold hover:shadow-xl hover:-translate-y-1 transition-all" if k == 0
               else "bg-white/10 border border-white/25 text-white px-9 py-4 rounded-full font-bold hover:bg-white/20 transition-all")
        btns += f'<a class="{cls}" href="{h}">{t}</a>'
    return f'''<!-- Kapanış -->
<section class="py-24 md:py-28 bg-gradient-to-b from-night to-[#57130d] text-white" id="birlikte">
<div class="max-w-[960px] mx-auto px-7 text-center reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl leading-[1.12] mb-6">{h2}</h2>
<p class="text-white/80 text-lg leading-relaxed max-w-2xl mx-auto mb-10">{p}</p>
<div class="flex flex-wrap justify-center gap-4">{btns}</div>
</div>
</section>
'''

def head2(h2, ps, cls="mb-14"):
    return (f'<div class="max-w-3xl {cls} reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-6">{h2}</h2>'
            + ''.join(f'<p class="text-on-surface-variant text-lg leading-relaxed mb-4">{p}</p>' for p in ps) + '</div>')

def promo(h3, p, link_text, href):
    return (f'<div class="rounded-3xl border border-outline-variant/40 bg-white shadow-sm p-8 md:p-10 reveal-on-scroll">'
            f'<h3 class="font-headline-md text-2xl text-espresso mb-3">{h3}</h3><p class="text-on-surface-variant text-lg leading-relaxed mb-6 max-w-2xl">{p}</p>'
            f'<a class="inline-flex items-center gap-2 text-terracotta font-bold group" href="{href}">{link_text} {ARROW}</a></div>')

def proj_link(name, pid):
    return f'<p class="mt-3 text-sm text-espresso/70">İlgili proje: <a class="text-terracotta font-semibold hover:underline underline-offset-4" href="projeler.html#{pid}">{name}</a></p>'

# =====================================================================
# 3) FAALİYET ALANLARIMIZ
# =====================================================================
AXES = [
 ("bilim-arastirma", "assets/bee-9712039_1280.jpg", "Mavi bir çiçekte polen toplayan arı", "science", "01", "Bilim &amp; Araştırma",
  "Arı sağlığı, polinasyon, biyoçeşitlilik, iklim, çevre ve arıcılığın geleceğine ilişkin bilimsel çalışmaların desteklenmesine ve yaygınlaştırılmasına katkı sağlarız.",
  [("Bilimsel Araştırma", "Arıcılık ve bal üretimiyle ilgili bilimsel araştırmaları destekleyerek inovatif ve geleneksel yöntemlerin entegrasyonunu sağlamak.", None),
   ("Apiterapi &amp; Apiturizm", "Arı ürünlerinin insan sağlığı üzerindeki faydalarını araştıran çalışmaları desteklemek; apiturizm modelleriyle kırsal kalkınmaya katkı sağlamak.", ("Apiterapi &amp; Apiturizm Araştırmaları", "apiterapi-apiturizm")),
   ("Dijital Dönüşüm &amp; Veri", "Arıcılıkta yeni teknolojilerin ve yenilikçi ürünlerin geliştirilmesini teşvik etmek.", None)],
  [("Araştırma &amp; Bilim", "akademi.html#arastirma")]),
 ("egitim-bilgi", "assets/img/p2-club-frame.jpg", "Kovandan çıkarılan petekli çerçeve", "school", "02", "Eğitim &amp; Bilgi",
  "Arıcıların, gençlerin, öğrencilerin ve toplumun doğru ve güncel bilgiye erişimini destekleyen eğitim ve kapasite geliştirme çalışmalarını yürütürüz.",
  [("Eğitim Programları", "Arıcılıkla ilgilenen bireyler, çiftçiler ve girişimciler için sürekli eğitim programları düzenlemek.", ("Arı Dostum Olur Musun?", "ari-dostum"))],
  [("Apikültür Akademi", "akademi.html#akademi-egitim")]),
 ("surdurulebilir-aricilik", "assets/img/p3-corridor-lavender.jpg", "Çiçek açmış lavanta tarlası", "eco", "03", "Sürdürülebilir Arıcılık",
  "Arıcılığın doğal kaynaklarla uyum içinde gelişmesini, iyi uygulamaların yaygınlaşmasını ve arıcılığın çevresel sürdürülebilirliğinin güçlendirilmesini destekleriz.",
  [("İyi Arıcılık Uygulamaları", "Çevre dostu, sürdürülebilir ve etik arıcılık yöntemlerinin yaygınlaştırılması için arıcılara rehberlik etmek.", None),
   ("Polinasyon &amp; Tarım", "Arıcılar ile çiftçiler arasındaki iş birliğini teşvik ederek polinasyonun tarım üzerindeki olumlu etkilerini artıracak projeler geliştirmek.", ("Türkiye Arı Koridoru", "ari-koridoru"))],
  None),
 ("genclik-gelecek", "assets/img/p1-bee-friend.jpg", "Petekli çerçeveyi inceleyen genç arıcı", "diversity_3", "04", "Gençlik &amp; Gelecek",
  "Gençlerin arıcılık alanında bilgi, deneyim ve uluslararası bağlantılar kazanmasını destekler; Türkiye’nin genç arıcılarının uluslararası platformlarda temsil edilmesine katkı sağlarız.",
  [("Gençlik &amp; Kadın Programları", "Kadın ve genç girişimciler için eğitim programları ve mentorluk hizmetleri sunmak.", ("Kadın ve Genç Arıcı Programı", "kadin-genc-arici"))],
  [("Gençlik ve Uluslararası Temsil", "genclik.html")]),
 ("kultur-uluslararasi", "assets/img/p5-honey-jar.jpg", "Kavanozdaki bal ve bal kaşığı", "public", "05", "Kültür &amp; Uluslararası İş Birliği",
  "Arıcılığın kültürel mirasını korumaya, yerel değerleri görünür kılmaya ve ulusal ve uluslararası kurumlarla bilgi ve deneyim paylaşımını geliştirmeye çalışırız.",
  [("Coğrafi İşaret &amp; Yerel Değerler", "Coğrafi işaret tescili ile yerel arı ürünlerinin tanınırlığını artırmak ve geleneksel üretim yöntemlerini korumak.", ("Coğrafi İşaret &amp; Yerel Değerler", "cografi-isaret")),
   ("Uluslararası İş Birlikleri", "Arıcılık vakıfları, enstitüler ve kurumlarla iş birliği yaparak küresel ölçekte arıcılığın gelişimine katkıda bulunmak.", None)],
  [("İş birliklerimiz", "index.html#isbirligi")]),
]
main = hero("assets/img/youth-frame.jpg", "Faaliyet Alanlarımız", "Faaliyet Alanlarımız",
            "Vakfımızın çalışmaları birbiriyle bağlantılı beş temel alanda şekillenir.",
            "Her alanın altında sürekli yürüttüğümüz çalışma başlıkları yer alır. Belirli süresi ve kapsamı olan çalışmalar ise Projeler sayfasında ayrıca anlatılır.",
            [(a[0], a[5]) for a in AXES])
for k, a in enumerate(AXES):
    blocks = ''.join(block(t, p, proj_link(*pr) if pr else '') for t, p, pr in a[7])
    main += feature(k, a[0], a[1], a[2], a[3], a[4], a[5], a[6], blocks, a[8])
main += cta("Bu alanlarda birlikte çalışalım.", "Araştırma, eğitim, gençlik ve kültür çalışmalarında kurumlar, uzmanlar ve gönüllülerle iş birliğine açığız.",
            [("İş Birliği Öner", MAILTO + "%C4%B0%C5%9F%20Birli%C4%9Fi"), ("Projelerimiz", "projeler.html")])
shell("faaliyet.html", "Faaliyet Alanlarımız | Apikültür Vakfı",
      "Apikültür Vakfı’nın beş faaliyet alanı: bilim ve araştırma, eğitim ve bilgi, sürdürülebilir arıcılık, gençlik ve gelecek, kültür ve uluslararası iş birliği.",
      "Faaliyet Alanlarımız", main)

# =====================================================================
# 4) VAKIF HAKKINDA
# =====================================================================
main = hero("assets/img/hero-beekeeper.jpg", "Vakıf Hakkında", "Apikültür Vakfı",
            "Apikültür Vakfı; arıcılığın bilimsel, çevresel, ekonomik ve kültürel boyutlarının geliştirilmesine katkı sağlamak amacıyla faaliyet gösteren bir vakıftır.",
            None, [("biz-kimiz", "Biz kimiz?"), ("vizyon-misyon", "Vizyon ve misyon"), ("hikaye", "Vakfın hikâyesi"), ("yapi", "Kurumsal yapı")])
main += '''<section class="relative isolate overflow-hidden py-24 md:py-32 bg-background" id="biz-kimiz"><div class="honeycomb-accent" aria-hidden="true"></div>
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-10 lg:gap-16">
<div class="lg:col-span-5 reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Biz kimiz?</h2></div>
<div class="lg:col-span-7 space-y-6 text-on-surface-variant text-lg md:text-xl leading-relaxed reveal-on-scroll">
<p>Arıcılığın yalnızca üretimden ibaret olmadığına; bilim, eğitim, çevre, tarım, biyoçeşitlilik, kültür ve insan kaynağıyla birlikte ele alınması gerektiğine inanıyoruz.</p>
<p>Vakfımız, bilgi üretmeyi, bilgiyi paylaşmayı, gençleri desteklemeyi ve farklı paydaşlar arasında iş birliği geliştirmeyi temel faaliyet araçları olarak görür.</p>
<p>Bu çalışmalar birbiriyle bağlantılı beş faaliyet alanında şekillenir: bilim ve araştırma, eğitim ve bilgi, sürdürülebilir arıcılık, gençlik ve gelecek, kültür ve uluslararası iş birliği.</p>
<a href="faaliyet.html" class="inline-flex items-center gap-2 text-terracotta font-bold group">Faaliyet Alanlarımız ''' + ARROW + '''</a>
</div>
</div>
</section>
<section class="py-24 md:py-32 bg-ekru/30" id="vizyon-misyon">
<div class="max-w-[1180px] mx-auto px-7">
<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-14 reveal-on-scroll">Vizyon ve misyon</h2>
<div class="grid md:grid-cols-2 gap-12 md:gap-16 reveal-on-scroll">
<div class="border-t-2 border-terracotta/70 pt-7"><h3 class="font-headline-md text-xl text-terracotta mb-5">Vizyonumuz</h3><p class="font-headline-md text-2xl md:text-[1.7rem] text-espresso leading-snug">Arıyı, polinasyonu ve biyoçeşitliliği merkeze alarak bilim, eğitim, teknoloji ve kültürü buluşturan; arıcılığın geleceğine kalıcı katkı sağlayan bir vakıf olmak.</p></div>
<div class="border-t-2 border-terracotta/70 pt-7"><h3 class="font-headline-md text-xl text-terracotta mb-5">Misyonumuz</h3><p class="font-headline-md text-2xl md:text-[1.7rem] text-espresso leading-snug">Arıcılığı eğitim, araştırma, sürdürülebilirlik, gençlik, inovasyon ve kültürel mirasın korunması eksenlerinde destekleyerek yaşamın devamlılığına katkı sağlamak.</p></div>
</div>
</div>
</section>
'''
main += feature(0, "hikaye", "assets/img/p4-women-planting.jpg", "Kovan başında çalışan arıcı", "history_edu", None,
                "Birikimden kurumsal faydaya.",
                "Apikültür Vakfı’nın kuruluş hikâyesi, arıcılık alanında yıllar içinde oluşan bilgi, deneyim ve birikimin daha geniş bir toplumsal faydaya dönüştürülmesi fikrine dayanır.",
                block("Kuruluş", "Vakfın kurucusu Muzaffer Yıldırım’dır. Kuruluş fikri, Yıldırım Plastik’ten doğan aile girişimi Apimaye’nin arıcılık ekipmanları alanında yıllar içinde edindiği deneyime uzanır. Polimer işleme bilgisiyle tasarlanan bir petek çerçevesi, bu birikimin ilk adımlarından biri oldu.")
                + block("Bugün", "Vakfın kuruluş sürecinde oluşan deneyim; bugün bilim, eğitim, gençlik, sürdürülebilirlik ve uluslararası iş birlikleri alanlarında geliştirilen çalışmalar için bir başlangıç noktasıdır.")
                + block("Bağımsız bir yapı", "Vakfın kurumsal kimliği, herhangi bir ticari markanın devamı veya uzantısı değil; kendi amaçları, organları ve vakıf senedi doğrultusunda faaliyet gösteren bağımsız bir yapıdır."))
main += '''<section class="relative isolate overflow-hidden py-28 md:py-36 text-white" id="manifesto">
<div class="absolute inset-0 -z-10" aria-hidden="true"><img src="assets/img/p6-meadow.jpg" alt="" class="w-full h-full object-cover" loading="lazy"/><div class="absolute inset-0" style="background:linear-gradient(180deg, rgba(51,38,27,0.86), rgba(51,38,27,0.92))"></div></div>
<div class="max-w-[960px] mx-auto px-7 text-center reveal-on-scroll">
<p class="font-display-hero text-4xl md:text-6xl leading-[1.1]">Mesele sadece bal değil.<br/><span class="text-white/70">Mesele, yaşamın ta kendisi.</span></p>
<p class="mt-8 text-white/75 text-lg leading-relaxed max-w-2xl mx-auto">Bir arının çiçekten çiçeğe yolculuğu, koca bir ekosistemi ayakta tutar. Arıcılığı bu bütünün parçası olarak görüyoruz.</p>
</div>
</section>
<section class="py-24 md:py-32 bg-background" id="yapi">
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-10 lg:gap-16">
<div class="lg:col-span-5 reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Kurumsal yapı</h2></div>
<div class="lg:col-span-7 reveal-on-scroll">
<p class="text-on-surface-variant text-lg md:text-xl leading-relaxed mb-5">Apikültür Vakfı’nın yönetim ve faaliyet yapısı vakıf senedi ve ilgili mevzuat çerçevesinde yürütülür.</p>
<p class="text-on-surface-variant text-lg md:text-xl leading-relaxed mb-10">Vakıf senedine göre Vakfın organları Mütevelli Heyeti ve Yönetim Kurulu’dur (Md.7); Bilim Kurulu ve Danışma Kurulu ise destek yapılarıdır.</p>
<div class="flex flex-wrap gap-4">
<a href="yonetim.html" class="inline-flex items-center gap-2 bg-terracotta text-white px-7 py-3.5 rounded-full font-bold hover:shadow-lg transition-all group">Yönetim &amp; Şeffaflık ''' + ARROW + '''</a>
<a href="senet.html" class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-7 py-3.5 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all"><span class="material-symbols-outlined text-[20px]">description</span>Vakıf Senedi</a>
</div>
</div>
</div>
</section>
'''
main += cta("Arıcılığın geleceğine katkıda bulunun.",
            "Apikültür Vakfı’nın amaçları doğrultusundaki çalışmalarını bağışınız, gönüllülüğünüz, uzmanlığınız veya kurumsal iş birliklerinizle destekleyebilirsiniz.",
            [("Destek Olun", "index.html#destek"), ("Bize Ulaşın", "index.html#iletisim")])
shell("vakif.html", "Apikültür Vakfı Hakkında | Vizyon, Misyon ve Yönetim",
      "Apikültür Vakfı, arıcılığın bilimsel, çevresel, ekonomik ve kültürel gelişimine katkı sağlayan bağımsız bir vakıftır. Vizyonumuz, misyonumuz ve hikâyemiz.",
      "Vakıf Hakkında", main)

# =====================================================================
# 5) GENÇLİK
# =====================================================================
FOCUS = ["Eğitim", "Deneyim paylaşımı", "Gençlik kulüpleri", "Ulusal etkinlikler", "Uluslararası buluşmalar", "Mentorluk", "Gönüllülük", "Kültürlerarası iletişim"]
focus_html = ''.join(f'<li class="border-t border-outline-variant/40 pt-4 flex items-baseline gap-3"><span class="font-headline-md text-lg md:text-xl text-espresso">{f}</span></li>' for k, f in enumerate(FOCUS, 1))
main = hero("assets/img/apiary-smoker.jpg", "Gençlik", "Gençlik ve Uluslararası Temsil",
            "Gençler yalnızca geleceğin değil, bugünün de paydaşıdır.",
            "Gençlerin arıcılıkla erken yaşta tanışması; doğa, bilim, tarım ve sürdürülebilirlik arasındaki bağlantıları anlamaları ve uluslararası deneyim kazanmaları arıcılığın geleceği açısından önemlidir.",
            [("odak", "Odak alanları"), ("temsil", "ICYB ve IMYB"), ("kulupler", "Gençlik Kulüpleri"), ("takvim", "Takvim ve duyurular")])
main += f'''<section class="py-24 md:py-32 bg-background" id="odak">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Gençlik çalışmalarımızın odağı", ["Apikültür Vakfı, gençlik çalışmalarında aşağıdaki alanlara odaklanır."])}
<ol class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-10 gap-y-8 reveal-on-scroll">{focus_html}</ol>
<p class="mt-16 text-on-surface-variant text-lg leading-relaxed max-w-3xl reveal-on-scroll">Gençlik çalışmalarımızı tek bir proje olarak değil, Vakfın gelecek nesillerin gelişimine katkı sağlama sorumluluğunun bir parçası olarak görüyoruz.</p>
</div>
</section>
<section class="py-24 md:py-32 bg-gradient-to-b from-night to-[#57130d] text-white" id="temsil">
<div class="max-w-[1180px] mx-auto px-7">
<div class="max-w-3xl mb-16 reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl leading-[1.12] mb-6">Türkiye’nin genç arıcılarının uluslararası temsilini destekliyoruz.</h2><p class="text-white/75 text-lg leading-relaxed">Vakfımız, International Confederation of Young Beekeepers (ICYB) ile ilişkili çalışmalar kapsamında Türkiye’nin genç arıcılarının uluslararası genç arıcılar ağıyla bağlantısını ve Türkiye’nin International Meeting of Young Beekeepers (IMYB) sürecindeki katılımını destekler.</p></div>
<div class="grid md:grid-cols-2 gap-12 md:gap-16 reveal-on-scroll">
<div id="icyb" class="border-t-2 border-amber/70 pt-6"><h3 class="font-headline-md text-3xl mb-1">ICYB</h3><p class="text-sm text-white/55 mb-5" lang="en">International Confederation of Young Beekeepers</p><p class="text-white/75 text-lg leading-relaxed mb-4">ICYB, genç arıcılar arasındaki uluslararası iletişim, deneyim paylaşımı ve iş birliğinin gelişmesine yönelik bir uluslararası ağdır.</p><p class="text-white/75 text-lg leading-relaxed">Apikültür Vakfı, Türkiye’deki genç arıcıların bu uluslararası ekosistemle bağlantısını geliştirmeyi ve Türkiye’nin uluslararası genç arıcılar platformundaki temsilini desteklemeyi amaçlar.</p></div>
<div id="imyb" class="border-t-2 border-amber/70 pt-6"><h3 class="font-headline-md text-3xl mb-1">IMYB</h3><p class="text-sm text-white/55 mb-5" lang="en">International Meeting of Young Beekeepers</p><p class="text-white/75 text-lg leading-relaxed mb-4">International Meeting of Young Beekeepers, farklı ülkelerden genç arıcıların bir araya gelerek bilgi, deneyim ve kültür paylaşımında bulunduğu uluslararası bir buluşmadır.</p><p class="text-white/75 text-lg leading-relaxed">Türkiye’nin bu uluslararası platformdaki katılımının geliştirilmesi, gençlerin yalnızca arıcılık bilgilerini değil; iletişim, takım çalışması ve kültürlerarası deneyimlerini de geliştirmelerine olanak sağlar.</p></div>
</div>
<p class="mt-14 text-sm text-white/55 max-w-3xl reveal-on-scroll">Uluslararası organizasyonlara ilişkin katılım bilgileri, ilgili dönem ve kaynak belirtilerek paylaşılır.</p>
</div>
</section>
'''
MODEL = [("Arı Dostluk Kovanı", "Her kulüp, okulda tahsis edilen bir Arı Dostluk Kovanı çevresinde kurulur."),
         ("Kulüp Yöneticisi", "Kulübün faaliyetlerini okuldaki bir kulüp yöneticisi koordine eder."),
         ("Üyeler", "En az altı genç üye arıcılık ve sürdürülebilirlik eğitimi alır. Yaş grubu: 12–18."),
         ("Destekçiler", "Firmalar ve kişiler yıllık katkılarıyla kulüplere destek olabilir.")]
main += feature(0, "kulupler", "assets/img/p2-club-frame.jpg", "Kovandan çıkarılan petekli çerçeve", "groups", None,
                "Apikültür Gençlik Kulüpleri",
                "Okullarda ve gençlik ortamlarında arıcılık, doğa, polinasyon ve sürdürülebilirlik konularında öğrenme ve deneyim paylaşımını destekleyen bir model geliştirmeyi hedefliyoruz. Kulüpler; gençlerin arıcılıkla tanışmasına, doğayı gözlemlemesine ve ekip çalışması içinde öğrenmesine olanak sağlayan faaliyetler etrafında şekillenir.",
                ''.join(block(t, p) for t, p in MODEL),
                [("Gençlik Kulübü Kurmak İstiyorum", MAILTO + "Gen%C3%A7lik%20Kul%C3%BCb%C3%BC"), ("Kulüplere Destek Olun", MAILTO + "Gen%C3%A7lik%20Kul%C3%BCb%C3%BC%20Deste%C4%9Fi")],
                extra_top='<h3 class="font-headline-md text-2xl text-espresso mb-2">Kulüp modelinin ana hatları</h3>')
EVENTS = [("19 Mayıs 2026", "Kulüp başvuruları", "Apikültür Gençlik Kulüpleri için başvurular açıldı. Başvuru için bizimle iletişime geçebilirsiniz."),
          ("23 Nisan 2027", "Türkiye ön yarışması", "Türkiye ön yarışması Düzce’de, Düzce Üniversitesi DAGEM’de düzenlenecek."),
          ("Temmuz 2027", "15. Uluslararası Genç Arıcılar Buluşması (IMYB)", "Buluşma, DAGEM ev sahipliğinde düzenlenecek.")]
ev_html = ''.join(f'<li class="grid md:grid-cols-12 gap-2 md:gap-8 border-t border-outline-variant/40 py-7"><div class="md:col-span-3 font-headline-md text-terracotta text-lg">{d}</div><div class="md:col-span-9"><h3 class="font-headline-md text-xl text-espresso mb-2">{t}</h3><p class="text-on-surface-variant leading-relaxed">{p}</p></div></li>' for d, t, p in EVENTS)
main += f'''<section class="py-24 md:py-32 bg-ekru/30" id="takvim">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Takvim ve duyurular", ["Gençlik programlarına ilişkin güncel tarihler bu bölümde duyurulur."])}
<ol class="border-b border-outline-variant/40 reveal-on-scroll">{ev_html}</ol>
<p class="mt-8 text-sm text-on-surface-variant/80 reveal-on-scroll">Tarihler, düzenleyici kurumların duyurularına göre güncellenebilir.</p>
</div>
</section>
'''
main += ('<section class="py-20 md:py-24 bg-background" id="gelecek-yonlendirme"><div class="max-w-[1180px] mx-auto px-7">'
         + promo("Eğitim ve gelişim desteği mi arıyorsunuz?", "Apikültür Gelecek kapsamında öğrenciler ve gençler için dönemsel burs, bilimsel gelişim ve hareketlilik destekleri açılabilir.", "Apikültür Gelecek’i Keşfet", "gelecek.html")
         + '</div></section>\n')
main += cta("Gençlik çalışmalarına destek olun.", "Gençlerin eğitim, deneyim ve uluslararası bağlantı fırsatlarına erişimini destekleyebilirsiniz.",
            [("Destek Olun", MAILTO + "Gen%C3%A7lik"), ("Bize Ulaşın", "index.html#iletisim")])
shell("genclik.html", "Gençlik ve Uluslararası Temsil | Apikültür Vakfı",
      "Gençlerin arıcılıkta eğitim, deneyim ve uluslararası bağlantılar kazanmasını; Türkiye’nin ICYB ve IMYB süreçlerindeki katılımını destekliyoruz.",
      "Gençlik", main)

# =====================================================================
# 6) AKADEMİ & BİLİM
# =====================================================================
main = hero("assets/img/bee-flower.jpg", "Akademi &amp; Bilim", "Akademi &amp; Bilim",
            "Bilginin üretildiği ve paylaşıldığı merkez.",
            "Arıcılığın geleceği, doğru bilgiye ve bu bilginin paylaşılmasına bağlıdır. Apikültür Vakfı; eğitim, araştırma, bilimsel iletişim ve bilgi paylaşımını faaliyetlerinin temel unsurlarından biri olarak görür.",
            [("akademi-egitim", "Apikültür Akademi"), ("arastirma", "Araştırma &amp; Bilim"), ("bilgi-merkezi", "Bilgi Merkezi")])
main += feature(0, "akademi-egitim", "assets/img/youth-frame.jpg", "Petekli çerçeveyi inceleyen arıcı", "school", None, "Apikültür Akademi",
                "Arıcılığa ilişkin temel ve ileri düzey bilgi, uygulama ve kapasite geliştirme çalışmalarını destekleyen eğitim yapısı.",
                block("Kapsam", "Temel arıcılıktan ana arı yetiştiriciliğine, arı ürünlerinden apiterapiye kadar arıcılığın farklı konuları.")
                + block("Kimler için", "Arıcılar, arıcılığa yeni başlayanlar, gençler, öğrenciler, çiftçiler ve girişimciler."),
                [("Eğitim &amp; Bilgi faaliyet alanı", "faaliyet.html#egitim-bilgi")])
main += feature(1, "arastirma", "assets/bee-9712039_1280.jpg", "Mavi bir çiçekte polen toplayan arı", "science", None, "Araştırma &amp; Bilim",
                "Üniversiteler, araştırmacılar, uzmanlar ve farklı kurumlarla arı sağlığı, polinasyon, sürdürülebilirlik, çevre ve arıcılığın geleceğine ilişkin bilimsel çalışmalar geliştirilmesini destekleriz.",
                block("Çalışma konuları", "Arı sağlığı, polinasyon, biyoçeşitlilik, iklim, çevre ve sürdürülebilir arıcılık.")
                + block("Araştırma iş birlikleri", "Üniversiteler, araştırma merkezleri ve alan uzmanlarıyla bilgi ve deneyim paylaşımı."),
                [("Bilim &amp; Araştırma faaliyet alanı", "faaliyet.html#bilim-arastirma")],
                tail='<div class="mt-10">' + promo("Araştırmanız için destek mi arıyorsunuz?", "Apikültür Gelecek kapsamında genç araştırmacılar, lisansüstü çalışmalar, bilimsel araştırmalar ve uluslararası bilimsel gelişim için dönemsel destek programları açılabilir.", "Bilim &amp; Araştırma Desteklerini Gör", "gelecek.html#programlar") + '</div>')
main += feature(2, "bilgi-merkezi", "assets/img/p4-women-planting.jpg", "Kovan başında çalışan arıcı", "menu_book", None, "Bilgi Merkezi",
                "Bilimsel yayınlar, teknik dokümanlar, rehberler, raporlar ve arıcılıkla ilgili güvenilir bilgi kaynaklarını erişilebilir hale getirmeyi amaçlarız.",
                block("İçerik türleri", "Bilimsel yayınlar, teknik dokümanlar, rehberler ve raporlar. Yayınlar hazır oldukça dönem ve kaynak bilgileriyle birlikte bu bölüme eklenir."))
main += cta("Bilgiyi birlikte büyütelim.", "Eğitim, araştırma ve yayın çalışmalarına katkı sunmak isteyen kurumlar ve uzmanlarla iletişim kurmaktan memnuniyet duyarız.",
            [("Akademik İş Birliği Öner", MAILTO + "Akademi%20%26%20Bilim"), ("Bize Ulaşın", "index.html#iletisim")])
shell("akademi.html", "Akademi &amp; Bilim | Apikültür Vakfı",
      "Apikültür Akademi, Araştırma &amp; Bilim ve Bilgi Merkezi: Apikültür Vakfı’nın eğitim, araştırma ve bilgi paylaşımı çalışmaları.",
      "Akademi &amp; Bilim", main)

# =====================================================================
# 7) PROJELER
# =====================================================================
STATS = '''<div class="mb-10 rounded-3xl border border-outline-variant/40 bg-white p-7 md:p-8">
<h3 class="font-headline-md text-lg text-espresso mb-6">Proje çıktıları · 2024–2025</h3>
<dl class="grid grid-cols-2 gap-6 md:gap-10 max-w-md">
<div class="flex flex-col-reverse"><dt class="text-on-surface-variant mt-2">okul</dt><dd class="font-headline-lg text-4xl md:text-5xl text-terracotta leading-none">30</dd></div>
<div class="flex flex-col-reverse"><dt class="text-on-surface-variant mt-2">öğrenci</dt><dd class="font-headline-lg text-4xl md:text-5xl text-terracotta leading-none">14.895</dd></div>
</dl>
<p class="mt-6 pt-5 border-t border-outline-variant/30 text-sm text-on-surface-variant">Bu veriler yalnızca Arı Dostum Olur Musun? projesinin Kartal’da yürütülen 2024–2025 dönemi kapsamındaki çıktıları ifade eder.</p>
</div>
'''
PROJECTS = [
 ("ari-dostum", "assets/img/p1-bee-friend.jpg", "Petek çerçevesini tutan genç", "emoji_nature", "Devam ediyor", "Arı Dostum Olur Musun?",
  "Çocuklar ve gençlerle arılar, polinasyon, biyoçeşitlilik ve doğa arasındaki ilişkiyi anlatmayı amaçlayan eğitim ve farkındalık çalışması.",
  STATS, ("Eğitim &amp; Bilgi", "egitim-bilgi")),
 ("ari-koridoru", "assets/img/p3-corridor-lavender.jpg", "Mor lavanta tarlası", "route", "Planlama", "Türkiye Arı Koridoru",
  "Polinatörlerin yaşam alanlarının desteklenmesi, biyoçeşitliliğin korunması ve farklı paydaşların bir araya gelmesi amacıyla geliştirilen proje yaklaşımı.",
  '', ("Sürdürülebilir Arıcılık", "surdurulebilir-aricilik")),
 ("kadin-genc-arici", "assets/img/p4-women-planting.jpg", "Kovan başında arıcı", "diversity_3", "Geliştirme", "Kadın ve Genç Arıcı Programı",
  "Kadınların ve gençlerin arıcılık alanında bilgi, beceri, mentorluk ve girişimcilik fırsatlarına erişimini desteklemeye yönelik çalışmalar.",
  '', ("Gençlik &amp; Gelecek", "genclik-gelecek")),
 ("cografi-isaret", "assets/img/p5-honey-jar.jpg", "Bal kavanozu", "location_on", "Geliştirme", "Coğrafi İşaret &amp; Yerel Değerler",
  "Arıcılığın yerel bilgi, ürün ve kültürel değerlerinin korunması, görünür hale getirilmesi ve sürdürülebilir şekilde değerlendirilmesine yönelik çalışmalar.",
  '', ("Kültür &amp; Uluslararası İş Birliği", "kultur-uluslararasi")),
 ("apiterapi-apiturizm", "assets/img/p6-meadow.jpg", "Altın ışıkta arılar", "spa", "Araştırma", "Apiterapi &amp; Apiturizm Araştırmaları",
  "Arı ürünleri, arıcılık kültürü, doğa ve turizm arasındaki ilişkilerin bilimsel ve kültürel perspektiflerle ele alınmasına yönelik çalışmalar.",
  '', ("Bilim &amp; Araştırma", "bilim-arastirma")),
]
main = hero("assets/img/hero-beekeeper.jpg", "Projeler", "Projeler", "Amaçlarımızı sahada hayata geçiriyoruz.",
            "Apikültür Vakfı, faaliyet alanları doğrultusunda farklı kurumlar, uzmanlar, eğitim kuruluşları, kamu kurumları ve diğer paydaşlarla çeşitli projeler geliştirir ve destekler. Projelerimiz; eğitimden gençliğe, biyoçeşitlilikten yerel değerlere kadar farklı alanlara odaklanabilir.",
            [(p[0], p[5]) for p in PROJECTS])
main += '''<div class="bg-ekru/40 border-b border-outline-variant/30"><div class="max-w-[1180px] mx-auto px-7 py-6 flex gap-4 items-start text-on-surface-variant"><span class="material-symbols-outlined text-terracotta shrink-0">info</span><p>Her projenin süresi, ortakları ve çıktıları yalnızca o projeye ait bilgiler olarak paylaşılır. Bu rakamlar Apikültür Vakfı’nın toplam performansı veya kurumsal etki göstergesi olarak sunulmaz.</p></div></div>
'''
for k, p in enumerate(PROJECTS):
    info = block("İlgili faaliyet alanı", f'<a class="text-terracotta font-semibold hover:underline underline-offset-4" href="faaliyet.html#{p[8][1]}">{p[8][0]}</a>')
    from urllib.parse import quote
    subj = quote("Proje: " + p[5].replace("&amp;", "&"))
    main += feature(k + 1, p[0], p[1], p[2], p[3], None, p[5], p[6], info,
                    [("Proje hakkında bilgi alın", MAILTO + subj)], badge=p[4], extra_top=p[7])
main += cta("Proje ortağımız olun.", "Kurumunuzla birlikte ortak çalışmalar geliştirebilir, mevcut projelerimize katkı sunabilirsiniz.",
            [("Proje Ortaklığı Öner", MAILTO + "Proje%20Ortakl%C4%B1%C4%9F%C4%B1"), ("Faaliyet Alanlarımız", "faaliyet.html")])
shell("projeler.html", "Projeler | Apikültür Vakfı",
      "Apikültür Vakfı projeleri: Arı Dostum Olur Musun?, Türkiye Arı Koridoru ve diğerleri. Proje çıktıları yalnızca ilgili proje kapsamında paylaşılır.",
      "Projeler", main)

# =====================================================================
# 8) YÖNETİM & ŞEFFAFLIK
# =====================================================================
def organ(title, text, kind, senet):
    link = (f'<a href="senet.html" class="mt-5 inline-flex items-center gap-1.5 text-terracotta text-sm font-bold group">Senette incele <span class="material-symbols-outlined text-[18px] group-hover:translate-x-1 transition-transform">arrow_forward</span></a>' if senet else '')
    return (f'<div class="border-t-2 border-terracotta/70 pt-6"><p class="text-sm text-on-surface-variant mb-3">{kind}</p>'
            f'<h3 class="font-headline-md text-2xl text-espresso mb-3">{title}</h3><p class="text-on-surface-variant text-lg leading-relaxed">{text}</p>{link}</div>')
main = hero("assets/bee-9712039_1280.jpg", "Yönetim &amp; Şeffaflık", "Yönetim &amp; Şeffaflık",
            "Gücümüzü güvenilirlik ve şeffaflıktan alıyoruz.",
            "Apikültür Vakfı’nın yönetim ve faaliyet yapısı vakıf senedi ve ilgili mevzuat çerçevesinde yürütülür.",
            [("yapi", "Kurumsal yapı"), ("kurullar", "Karar ve danışma yapısı"), ("seffaflik", "Şeffaflık Merkezi")])
main += '''<section class="relative isolate overflow-hidden py-24 md:py-32 bg-background" id="yapi"><div class="honeycomb-accent" aria-hidden="true"></div>
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-2 gap-14 lg:gap-24">
<div class="reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-8">Bağımsız bir vakıf.</h2>
<p class="text-on-surface-variant text-lg leading-relaxed mb-5">Apikültür Vakfı, kendi amaçları, vakıf senedi ve yönetim organları doğrultusunda faaliyet gösteren bağımsız bir vakıftır. Vakfın kurumsal kimliği, herhangi bir ticari markanın devamı veya uzantısı değildir.</p>
<p class="text-on-surface-variant text-lg leading-relaxed mb-5">Vakfın karar, yönetim, bilimsel danışmanlık ve diğer destek mekanizmaları açık ve anlaşılır bir kurumsal yapı içerisinde ele alınır.</p>
<p class="text-on-surface-variant text-lg leading-relaxed">Vakıf; bilgi üretir, modeller geliştirir, eğitim ve iş birliklerini destekler.</p>
</div>
<div class="reveal-on-scroll lg:pt-3">
<div class="bg-white rounded-3xl border border-outline-variant/30 shadow-sm p-8 md:p-10">
<h3 class="font-headline-md text-2xl text-espresso mb-4">Gelirlerin kullanımı</h3>
<p class="text-on-surface-variant text-lg leading-relaxed mb-6">Vakıf senedinin 16. maddesi gereği Vakfın yıllık brüt gelirinin en az üçte ikisi Vakfın amaçlarına tahsis edilir.</p>
<a href="senet.html" class="inline-flex items-center gap-2 text-terracotta font-bold group">Vakıf Senedini İncele ''' + ARROW + '''</a>
</div>
</div>
</div>
</section>
<section class="py-24 md:py-32 bg-ekru/30" id="kurullar">
<div class="max-w-[1180px] mx-auto px-7">
''' + head2("Karar ve danışma yapısı", ["Vakıf senedine göre Vakfın organları Mütevelli Heyeti ve Yönetim Kurulu’dur (Md.7); Bilim Kurulu ve Danışma Kurulu ise destek yapılarıdır."]) + '''
<div class="grid md:grid-cols-2 gap-x-16 gap-y-14 reveal-on-scroll">
''' + organ("Mütevelli Heyeti", "Vakfın en yüksek karar organıdır.", "Vakıf organı · Senet Md.7", True) \
    + organ("Yönetim Kurulu", "Vakfın idare ve icrasından sorumlu organdır.", "Vakıf organı · Senet Md.7", True) \
    + organ("Bilim Kurulu", "Bilimsel çalışmaların ve ilgili faaliyetlerin akademik açıdan değerlendirilmesine katkı sağlar.", "Destek yapısı", False) \
    + organ("Danışma Kurulu", "Alan uzmanlarının ve paydaşların görüş ve deneyimleriyle Vakfın çalışmalarına katkı sunar.", "Destek yapısı", False) + '''
</div>
</div>
</section>
<section class="py-24 md:py-32 bg-background" id="seffaflik">
<div class="max-w-[1180px] mx-auto px-7">
''' + head2("Şeffaflık Merkezi", ["Vakıf hakkında bilmek istediğiniz her şey.", "Kurumsal güvenin açık bilgi ve hesap verebilirlikle güçlendiğine inanıyoruz."]) + '''
<div class="reveal-on-scroll border-y border-outline-variant/40">
<div class="grid md:grid-cols-12 gap-5 md:gap-8 items-center py-8">
<div class="md:col-span-1"><span class="w-12 h-12 rounded-2xl bg-ekru flex items-center justify-center"><span class="material-symbols-outlined text-terracotta text-2xl">description</span></span></div>
<div class="md:col-span-7"><h3 class="font-headline-md text-2xl text-espresso mb-2">Vakıf Senedi</h3><p class="text-on-surface-variant leading-relaxed">Vakfın gayesi, faaliyetleri, organları ve gelirlerinin tahsisine ilişkin hükümler.</p></div>
<div class="md:col-span-4 flex flex-wrap gap-3 md:justify-end">
<a href="senet.html" class="inline-flex items-center gap-2 bg-terracotta text-white px-6 py-3 rounded-full font-bold text-sm hover:shadow-lg transition-all">Oku</a>
<a href="assets/vakif-senedi.pdf" download class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-6 py-3 rounded-full font-bold text-sm hover:bg-terracotta hover:text-white transition-all"><span class="material-symbols-outlined text-[18px]">download</span>PDF</a>
</div>
</div>
</div>
<p class="mt-10 text-on-surface-variant text-lg leading-relaxed max-w-3xl reveal-on-scroll">Faaliyet raporları, mali raporlar, denetim raporları, kurumsal politikalar, etik ilkeler, KVKK ve gizlilik politikası gibi belgeler hazır olduklarında tarih ve dönem bilgileriyle birlikte bu bölümde arşivlenir.</p>
</div>
</section>
'''
main += cta("Sorularınız için bize ulaşın.", "Vakfın yönetimi ve kurumsal belgeleri hakkındaki sorularınızı bize iletebilirsiniz.",
            [("Bize Yazın", MAILTO + "Genel%20Bilgi"), ("Vakıf Senedi", "senet.html")])
shell("yonetim.html", "Yönetim &amp; Şeffaflık | Apikültür Vakfı",
      "Apikültür Vakfı’nın yönetim yapısı, karar ve danışma organları, vakıf senedi ve kurumsal belgeleri.",
      "Yönetim &amp; Şeffaflık", main)

exec(open(f'{SCR}/gelecek_page.py', encoding='utf-8').read())

# =====================================================================
# 9) sitemap.xml
# =====================================================================
pages = ["", "vakif.html", "faaliyet.html", "genclik.html", "akademi.html", "gelecek.html", "projeler.html", "yonetim.html", "senet.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{BASE_URL}{p}</loc><lastmod>2026-09-28</lastmod></url>\n' for p in pages) + '</urlset>\n'
open(f"{REPO}/sitemap.xml", "w").write(sm)
print("OK  sitemap.xml")
