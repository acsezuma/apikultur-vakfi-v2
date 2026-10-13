# build_pages.py içinden exec edilir (idx, once, NAVC, MOBC, FTC, ARROW, re, sys hazır).
# ---- Apikültür Gelecek: menü, footer, ana sayfa bölümü, Destek bağlantısı ----

# Menü 9 öğeye çıktı: masaüstü menü xl'den (1280) itibaren, altında hamburger
idx = once(idx, '<nav class="hidden lg:flex items-center gap-3.5 xl:gap-5">', '<nav class="hidden xl:flex items-center gap-4">', "nav-xl")
idx = once(idx, 'class="lg:hidden inline-flex items-center justify-center w-10 h-10', 'class="xl:hidden inline-flex items-center justify-center w-10 h-10', "menubtn-xl")
idx = once(idx, '<div id="mobile-menu" class="lg:hidden fixed', '<div id="mobile-menu" class="xl:hidden fixed', "mobilemenu-xl")

idx = once(idx, f'<a {NAVC} href="akademi.html">Akademi &amp; Bilim</a>\n',
           f'<a {NAVC} href="akademi.html">Akademi &amp; Bilim</a>\n<a {NAVC} href="gelecek.html">Apikültür Gelecek</a>\n', "nav-gelecek")
idx = once(idx, f'<a {MOBC} href="akademi.html">Akademi &amp; Bilim</a>\n',
           f'<a {MOBC} href="akademi.html">Akademi &amp; Bilim</a>\n<a {MOBC} href="gelecek.html">Apikültür Gelecek</a>\n', "mob-gelecek")
idx = once(idx, f'<li><a {FTC} href="akademi.html">Akademi &amp; Bilim</a></li>',
           f'<li><a {FTC} href="akademi.html">Akademi &amp; Bilim</a></li><li><a {FTC} href="gelecek.html">Apikültür Gelecek</a></li>', "footer-gelecek")

GELECEK_PROGS = [
    ("gelecek-burslari", "Gelecek Bursları", "Öğrencilerin eğitim yolculuğunu destekleyen burs programları."),
    ("genc-bilim", "Genç Bilim", "Yüksek lisans, doktora ve genç araştırmacılara yönelik bilimsel gelişim destekleri."),
    ("arastir", "Araştır", "Tez, araştırma, saha çalışması ve bilimsel proje destekleri."),
    ("dunyaya-acil", "Dünyaya Açıl", "Kongre, bilimsel toplantı, araştırma ziyareti ve uluslararası hareketlilik destekleri."),
    ("sahada-gelecek", "Sahada Gelecek", "Arıcılar, çiftçiler ve saha uygulayıcılarına yönelik eğitim ve kapasite geliştirme destekleri."),
]
_items = ''.join(
    f'<a href="gelecek.html#{pid}" class="group block border-t-2 border-amber/60 pt-5 hover:border-amber transition-colors">'
    f'<h3 class="font-headline-md text-xl mb-3 group-hover:text-amber transition-colors">{name}</h3>'
    f'<p class="text-white/70 leading-relaxed">{desc}</p></a>' for pid, name, desc in GELECEK_PROGS)
GELECEK_HOME = f'''<!-- Apikültür Gelecek -->
<section class="relative isolate overflow-hidden py-32 text-white" id="gelecek"><div class="absolute inset-0 -z-10" aria-hidden="true"><img src="assets/img/youth-frame.jpg" alt="" class="w-full h-full object-cover" loading="lazy" style="filter:blur(6px);transform:scale(1.1)"/><div class="absolute inset-0" style="background:linear-gradient(160deg, rgba(51,38,27,0.94), rgba(40,29,20,0.91) 55%, rgba(28,20,13,0.95))"></div></div>
<div class="max-w-[1180px] mx-auto px-7">
<div class="max-w-3xl mb-16 reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl leading-[1.12] mb-6">Apikültür Gelecek</h2>
<p class="text-2xl md:text-[1.7rem] text-white/90 leading-snug mb-8">Bilgiyi destekliyoruz. Bilimi büyütüyoruz. Geleceğe yatırım yapıyoruz.</p>
<p class="text-white/75 text-lg leading-relaxed mb-4">Apikültür Gelecek; arılar, arıcılık, polinasyon, biyolojik çeşitlilik, tarım, gıda, çevre ve kırsal kalkınmanın geleceğine katkı sağlayacak öğrencileri, genç araştırmacıları ve nitelikli çalışmaları desteklemek amacıyla oluşturulan eğitim, bilim ve gelecek destek programıdır.</p>
<p class="text-white/75 text-lg leading-relaxed">Eğitim burslarından genç araştırmacı desteklerine, bilimsel araştırmalardan uluslararası hareketliliğe kadar farklı destek yollarını tek bir yapı altında buluşturuyoruz.</p>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-x-8 gap-y-10 mb-16 reveal-on-scroll">{_items}</div>
<div class="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 pt-10 border-t border-white/10 reveal-on-scroll">
<div class="max-w-xl"><h3 class="font-headline-md text-2xl mb-3">Hangi destek size uygun?</h3><p class="text-white/70 text-lg leading-relaxed">Açık programları inceleyin, başvuru koşullarını öğrenin ve size uygun destek yolunu keşfedin.</p></div>
<div class="flex flex-wrap gap-4"><a href="gelecek.html" class="inline-flex items-center gap-2 bg-amber text-espresso px-8 py-4 rounded-full font-bold hover:-translate-y-0.5 transition-all group">Apikültür Gelecek’i Keşfet {ARROW}</a><a href="gelecek.html#programlar" class="bg-white/10 border border-white/25 text-white px-8 py-4 rounded-full font-bold hover:bg-white/20 transition-all">Açık Programlar</a></div>
</div>
</div>
</section>
'''
idx = once(idx, '<!-- Projeler -->\n', GELECEK_HOME + '<!-- Projeler -->\n', "home-gelecek")

# Destek bölümü: Gelecek'e küçük bağlantı (butonların hemen üstünde)
idx = once(idx, '<div class="flex flex-wrap gap-4 reveal-on-scroll">\n<a href="mailto:info@apikulturvakfi.org?subject=Ba%C4%9F%C4%B1%C5%9F"',
           '<div class="mb-12 max-w-3xl border-l-2 border-amber pl-5 reveal-on-scroll"><h3 class="font-headline-md text-xl mb-2">Eğitim ve Bilimi Destekleyin</h3>'
           '<p class="text-white/75 leading-relaxed mb-3">Apikültür Gelecek kapsamında öğrencilerin, genç araştırmacıların ve nitelikli bilimsel çalışmaların desteklenmesine katkıda bulunun.</p>'
           f'<a class="inline-flex items-center gap-2 text-amber font-bold group" href="gelecek.html#destekle">Apikültür Gelecek’i Destekle {ARROW}</a></div>\n'
           '<div class="flex flex-wrap gap-4 reveal-on-scroll">\n<a href="mailto:info@apikulturvakfi.org?subject=Ba%C4%9F%C4%B1%C5%9F"', "destek-gelecek")
