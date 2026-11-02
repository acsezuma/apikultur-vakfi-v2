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
    ("gelecek-burslari", "Gelecek Bursları"), ("genc-bilim", "Genç Bilim"), ("arastir", "Araştır"),
    ("dunyaya-acil", "Dünyaya Açıl"), ("sahada-gelecek", "Sahada Gelecek"),
]
_items = ''.join(
    f'<li><a href="gelecek.html#{pid}" class="group flex items-center justify-between gap-4 border-t border-white/15 py-5">'
    f'<span class="font-headline-md text-xl group-hover:text-amber transition-colors">{name}</span>'
    f'<span class="material-symbols-outlined text-[20px] text-amber/70 group-hover:text-amber group-hover:translate-x-1 transition-all">arrow_forward</span></a></li>' for pid, name in GELECEK_PROGS)
GELECEK_HOME = f'''<!-- Apikültür Gelecek -->
<section class="relative isolate overflow-hidden py-32 text-white" id="gelecek"><div class="absolute inset-0 -z-10" aria-hidden="true"><img src="assets/img/youth-frame.jpg" alt="" class="w-full h-full object-cover" loading="lazy" style="filter:blur(6px);transform:scale(1.1)"/><div class="absolute inset-0" style="background:linear-gradient(160deg, rgba(51,38,27,0.94), rgba(40,29,20,0.91) 55%, rgba(28,20,13,0.95))"></div></div>
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-12 lg:gap-16 items-start">
<div class="lg:col-span-6 reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl leading-[1.12] mb-6">Apikültür Gelecek</h2>
<p class="text-white/75 text-lg leading-relaxed mb-10">Öğrencileri, genç araştırmacıları ve nitelikli bilimsel çalışmaları burs, araştırma ve uluslararası gelişim destekleriyle buluşturan destek programımız.</p>
<div class="flex flex-wrap gap-4"><a href="gelecek.html" class="inline-flex items-center gap-2 bg-amber text-espresso px-8 py-4 rounded-full font-bold hover:-translate-y-0.5 transition-all group">Apikültür Gelecek’i Keşfet {ARROW}</a><a href="gelecek.html#programlar" class="bg-white/10 border border-white/25 text-white px-8 py-4 rounded-full font-bold hover:bg-white/20 transition-all">Açık Programlar</a></div>
</div>
<ul class="lg:col-span-6 border-b border-white/15 reveal-on-scroll">{_items}</ul>
</div>
</section>
'''
idx = once(idx, '<!-- Projeler -->\n', GELECEK_HOME + '<!-- Projeler -->\n', "home-gelecek")

# Destek bölümü: "Eğitim ve Araştırma Desteği" maddesinin altına Apikültür Gelecek bağlantısı
idx = once(idx, '<h3 class="font-headline-md text-xl mb-3">Eğitim ve Araştırma Desteği</h3><p class="text-white/70 leading-relaxed">Bilimsel ve eğitim faaliyetlerinin gelişmesine destek olabilirsiniz.</p>',
           '<h3 class="font-headline-md text-xl mb-3">Eğitim ve Araştırma Desteği</h3><p class="text-white/70 leading-relaxed">Bilimsel ve eğitim faaliyetlerinin gelişmesine destek olabilirsiniz.</p>'
           '<a class="mt-3 inline-flex items-center gap-1.5 text-amber font-bold text-sm group" href="gelecek.html#destekle">Apikültür Gelecek’i Destekle <span class="material-symbols-outlined text-[18px] group-hover:translate-x-1 transition-transform">arrow_forward</span></a>', "destek-gelecek")
