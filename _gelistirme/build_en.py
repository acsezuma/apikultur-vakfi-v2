#!/usr/bin/env python3
"""TR sayfalardan en/ altında İngilizce sayfaları üretir (build_pages.py'den sonra çalışır)."""
import re, sys, os, json
from urllib.parse import quote, unquote
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
from en_text import T, SUBJ
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo kökü (_gelistirme/..)
BASE = "https://acsezuma.github.io/apikultur-vakfi-v2/"
SLUG = {"index.html": "index.html", "vakif.html": "about.html", "faaliyet.html": "areas-of-work.html", "genclik.html": "youth.html",
        "akademi.html": "academy.html", "projeler.html": "projects.html", "yonetim.html": "governance.html", "gelecek.html": "future.html"}
ALLOWED_TR = ["Türkiye", "Düzce", "Şişli", "İzzetpaşa", "Yıldırım", "Mh.", "Sk.", "Apikültür"]
os.makedirs(f"{REPO}/en", exist_ok=True)
used = set(); problems = []

NGO_EN = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Apiculture Foundation",
  "alternateName": "Apikültür Vakfı",
  "url": "https://acsezuma.github.io/apikultur-vakfi-v2/en/",
  "logo": "https://acsezuma.github.io/apikultur-vakfi-v2/assets/logo.png",
  "email": "info@apikulturvakfi.org",
  "telephone": "+90 212 222 0 222",
  "description": "An independent, non-profit foundation working through science, education and cooperation for beekeeping, pollination and sustainable living."
}
</script>'''

def tr_text(m):
    pre, txt, post = m.group(1), m.group(2), m.group(3)
    if txt in T:
        used.add(txt); return f">{pre}{T[txt]}{post}<"
    return m.group(0)

def build(fname):
    s = open(f"{REPO}/{fname}", encoding="utf-8").read()
    en = SLUG[fname]
    en_url = BASE + "en/" + (en if en != "index.html" else "")
    # dil butonu: EN -> TR
    s, n = re.subn(r'<a href="en/[^"]*" hreflang="en" lang="en" title="English" aria-label="English version"',
                   f'<a href="../{fname}" hreflang="tr" lang="tr" title="Türkçe" aria-label="Türkçe sürüm"', s)
    if n != 1: problems.append(f"{fname}: dil butonu {n}")
    s = s.replace('text-[12px] font-bold tracking-wider hover:border-terracotta hover:text-terracotta transition-colors">EN</a>',
                  'text-[12px] font-bold tracking-wider hover:border-terracotta hover:text-terracotta transition-colors">TR</a>')
    # dil, locale, canonical
    s = s.replace('<html class="scroll-smooth" lang="tr">', '<html class="scroll-smooth" lang="en">')
    s = s.replace('<meta property="og:locale" content="tr_TR"/>', '<meta property="og:locale" content="en_GB"/>\n<meta property="og:locale:alternate" content="tr_TR"/>')
    s = re.sub(r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{en_url}"/>', s)
    s = re.sub(r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{en_url}"/>', s)
    # JSON-LD
    if fname == "index.html":
        s = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: NGO_EN, s, count=1, flags=re.S)
    else:
        def ld(m):
            j = m.group(0)
            j = j.replace('"name": "Ana Sayfa", "item": "' + BASE + '"', '"name": "Home", "item": "' + BASE + 'en/"')
            j = re.sub(r'"name": "([^"]+)", "item": "' + re.escape(BASE + fname) + '"',
                       lambda k: f'"name": "{T.get(k.group(1).replace("&", "&amp;"), k.group(1)).replace("&amp;", "&")}", "item": "{en_url}"', j)
            return j
        s = re.sub(r'<script type="application/ld\+json">.*?</script>', ld, s, flags=re.S)
    # metin düğümleri
    s = re.sub(r'>(\s*)([^<>]*?[^\s<>])(\s*)<', tr_text, s)
    # öznitelikler
    def attr(m):
        v = m.group(2)
        if v in T: used.add(v); return f'{m.group(1)}="{T[v]}"'
        return m.group(0)
    s = re.sub(r'\b(alt|aria-label|title|placeholder)="([^"]+)"', attr, s)
    def meta(m):
        v = m.group(2)
        if v in T: used.add(v); return f'{m.group(1)}"{T[v]}"/>'
        problems.append(f"{fname}: meta çevrilmedi: {v[:60]}"); return m.group(0)
    s = re.sub(r'(<meta (?:name|property)="(?:description|og:title|og:description|twitter:title|twitter:description)" content=)"([^"]+)"/>', meta, s)
    # masaüstü menüde kısa etiketler (tek satıra sığsın)
    SHORT = {"Foundation": "About", "Our Areas of Work": "Our Work", "Academy &amp; Science": "Academy", "Governance &amp; Transparency": "Governance"}
    s = re.sub(r'(<a class="nav-link[^"]*" href="[^"]*"(?: aria-current="page")?>)([^<]+)</a>', lambda m: m.group(1) + SHORT.get(m.group(2), m.group(2)) + '</a>', s)
    s = s.replace('<span class="hidden xl:inline">Foundation Charter</span>', '<span class="hidden xl:inline">Charter</span>')
    s = s.replace('>14.895<', '>14,895<')  # İngilizce binlik ayracı
    assert s.count('assets/og-image.png?v=3') == 2
    s = s.replace('assets/og-image.png?v=3', 'assets/og-image-en.png?v=1')
    # e-posta konuları
    def subj(m):
        v = unquote(m.group(1))
        if v not in SUBJ: problems.append(f"{fname}: konu çevrilmedi: {v}"); return m.group(0)
        return "subject=" + quote(SUBJ[v])
    s = re.sub(r'(?<=href="mailto:info@apikulturvakfi.org\?)subject=([^"]*)', subj, s)
    # yollar: varlıklar ve senet üst dizinde, sayfalar İngilizce adlarla
    s = re.sub(r'(src|href)="assets/', r'\1="../assets/', s)
    s = s.replace('href="senet.html"', 'href="../senet.html"')
    s = re.sub(r'href="(vakif|faaliyet|genclik|akademi|projeler|yonetim|gelecek)\.html', lambda m: 'href="' + SLUG[m.group(1) + ".html"], s)
    # mobil menüde de masaüstüyle aynı 'About' etiketi
    s, n = re.subn(r'(<a class="py-3.5 border-b[^"]*" href="about.html"[^>]*>)Foundation</a>', r'\1About</a>', s)
    if n != 1: problems.append(f"{fname}: mobil About {n}")
    # kalan Türkçe denetimi
    body = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
    for t in re.findall(r'>\s*([^<>]*?[^\s<>])\s*<', body) + re.findall(r'\b(?:alt|aria-label|title)="([^"]+)"', body):
        tt = t
        for a in ALLOWED_TR: tt = tt.replace(a, "")
        if re.search(r'[çğıöşüÇĞİÖŞÜ]', tt) and t not in ("Türkçe", "Türkçe sürüm"):
            problems.append(f"{fname}: TR kaldı: {t[:90]}")
    open(f"{REPO}/en/{en}", "w", encoding="utf-8").write(s)
    print(f"OK  en/{en}", len(s))

for f in SLUG: build(f)
unused = [k for k in T if k not in used]
print("kullanılmayan sözlük anahtarı:", len(unused))
for u in unused: print("   -", u[:90])
print("SORUNLAR:", len(problems))
for p in problems: print("   !", p)
# sitemap'e EN sayfaları
sm = open(f"{REPO}/sitemap.xml", encoding="utf-8").read()
if "/en/" not in sm:
    extra = ''.join(f'  <url><loc>{BASE}en/{(v if v != "index.html" else "")}</loc><lastmod>2026-09-28</lastmod></url>\n' for v in SLUG.values())
    open(f"{REPO}/sitemap.xml", "w", encoding="utf-8").write(sm.replace("</urlset>", extra + "</urlset>"))
    print("OK  sitemap.xml + EN")
