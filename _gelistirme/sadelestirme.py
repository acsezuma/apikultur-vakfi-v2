# build_pages.py içinden exec edilir (idx, once, ARROW, re, sys hazır).
# ---- Ana sayfa sadeleştirmesi (Kasım 2026): her bölüm kısa bir özet + ilgili sayfaya bağlantı ----
# Ayrıntılar (ICYB/IMYB kutusu, kurul kartları, Gelecek programlarının açıklamaları vb.) yalnızca iç sayfalarda.

def swap_section(s, comment, new, label):
    """'<!-- comment -->' ile başlayan bölümü (ilk </section>'a kadar) new ile değiştirir; new boşsa siler."""
    start = f'<!-- {comment} -->\n'
    if s.count(start) != 1: print(f"!! HATA [{label}]: yorum {s.count(start)}"); sys.exit(1)
    i = s.index(start); j = s.index('</section>\n', i) + len('</section>\n')
    return s[:i] + new + s[j:]

# Vizyon ve misyon (kurul onaylı metinler, Kasım 2026)
VIZYON = "Arının, arıcılığın ve arı ürünlerinin insana ve ekosistemde kattığı değeri bilimle görünür kılan; tüketiciden üreticiye tüm tarafların başvurduğu küresel bir referans ve denge merkezi olmak."
MISYON = "Arı ve arı ürünlerinin biyoyararlılığı ile arıların koloni kayıplarına yol açan ve sürdürülebilirliğini tehdit eden faktörleri bilimsel araştırmalarla ortaya koymak, bu hususlarda toplumsal bilinç ve farkındalık yaratmak, arı ürünlerinin değerini yükseltmek."

# Beş eksen: (id, ikon, başlık, ana sayfa için kısa metin)
EKSENLER_KISA = [
    ("koloni-sagligi", "health_and_safety", "Koloni Sağlığı ve Kayıpların Önlenmesi", "Koloni kayıplarına yol açan etkenlerin araştırılması ve önlenmesi."),
    ("biyocesitlilik-verimlilik", "eco", "Biyoçeşitlilik ve Tarımsal Verimlilik", "Tozlayıcıların korunması ve polinasyon yoluyla tarımsal verimlilik."),
    ("genclik-modern-aricilik", "diversity_3", "Gençlik ve Sürdürülebilir Modern Arıcılık", "Gençleri odağa alan, verimliliği ve geliri artıran modern arıcılık."),
    ("etik-aricilik", "verified", "Etik Arıcılık ve Arı Ürünlerine Güven", "Kaynağından izlenebilir, güvenilir üretim ve bilinçli tüketici."),
    ("is-birligi", "public", "Ulusal ve Uluslararası İş Birliği", "Bu alanlarda güvenilir bir referans merkezi olma hedefi."),
]

# 1) Hero: tek paragraf (eski iki paragraf ve üç satırlık slogan kaldırıldı)
idx, n = re.subn(r'<div class="hidden md:block">\n<p class="font-body-lede.*?</div>\n',
                 '<p class="font-body-lede text-white/85 mb-10 max-w-2xl">Apikültür Vakfı; arıların ve arı ürünlerinin değerini bilimle ortaya koymak, koloni kayıplarına karşı toplumsal bilinç oluşturmak ve arıcılığın geleceğine katkı sağlamak için çalışır.</p>\n',
                 idx, count=1, flags=re.S)
if n != 1: print("!! hero", n); sys.exit(1)

# 2) Biz Kimiz + Vakıf Hakkında -> tek bölüm
idx = swap_section(idx, "Biz Kimiz", '', "bizkimiz")
idx = swap_section(idx, "Vakıf Hakkında: Vizyon/Misyon", f'''<!-- Vakıf Hakkında -->
<section class="relative isolate overflow-hidden py-32 bg-background" id="hakkimizda"><div class="honeycomb-accent" aria-hidden="true"></div>
<div class="max-w-[1180px] mx-auto px-7">
<div class="grid lg:grid-cols-2 gap-16 lg:gap-20 items-center">
<div class="reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-8">Arıcılığın ötesine bakıyoruz.</h2>
<p class="text-on-surface-variant text-lg leading-relaxed">Arıcılık; gıda üretiminden biyoçeşitliliğe, kırsal yaşamdan kültürel mirasa kadar birçok alanla bağlantılıdır. Vakfımız bu bütünü bilimsel araştırma, toplumsal bilinç ve iş birliğiyle ele alır.</p>
<a href="vakif.html" class="mt-8 inline-flex items-center gap-2 text-terracotta font-bold group">Vakıf Hakkında {ARROW}</a>
</div>
<div class="grid gap-6 reveal-on-scroll" style="transition-delay: 200ms">
<div class="bg-white p-8 md:p-10 rounded-3xl border border-outline-variant/30 shadow-sm"><h3 class="font-headline-md text-xl text-espresso mb-4">Vizyon</h3><p class="text-on-surface-variant text-lg leading-relaxed">{VIZYON}</p></div>
<div class="bg-white p-8 md:p-10 rounded-3xl border border-outline-variant/30 shadow-sm"><h3 class="font-headline-md text-xl text-espresso mb-4">Misyon</h3><p class="text-on-surface-variant text-lg leading-relaxed">{MISYON}</p></div>
</div>
</div>
</div>
</section>
''', "vakif-hakkinda")

# 3) Faaliyet alanları: yeni beş eksen, kısa kartlar
def _kart(k, e):
    sid, icon, title, short = e
    start = ' lg:col-start-2' if k == 3 else ''
    return (f'<a href="faaliyet.html#{sid}" class="block feat-card p-10 rounded-3xl reveal-on-scroll group relative overflow-hidden lg:col-span-2{start}">'
            '<div class="absolute top-0 right-0 w-28 h-28 bg-terracotta/5 rounded-bl-[3rem] -mr-10 -mt-10 group-hover:bg-terracotta/10 transition-colors"></div>'
            '<div class="flex items-center justify-between mb-8"><div class="w-16 h-16 rounded-2xl bg-ekru flex items-center justify-center group-hover:bg-terracotta group-hover:-rotate-6 transition-all duration-500">'
            f'<span class="material-symbols-outlined text-terracotta group-hover:text-white text-3xl">{icon}</span></div><span class="font-label-mono text-terracotta/30 font-bold text-lg">0{k + 1}</span></div>'
            f'<h3 class="font-headline-md text-xl mb-4 text-espresso group-hover:text-terracotta transition-colors">{title}</h3><p class="text-on-surface-variant leading-relaxed">{short}</p></a>')
idx = swap_section(idx, "Faaliyet Alanlarımız", f'''<!-- Faaliyet Alanlarımız -->
<section class="relative isolate overflow-hidden py-32 bg-ekru/30" id="faaliyet"><div class="absolute inset-0 -z-10" aria-hidden="true"><img src="assets/img/apiary-smoker.jpg" alt="" class="w-full h-full object-cover opacity-[0.09] blur-[3px] scale-110"/><div class="absolute inset-0 bg-gradient-to-b from-background via-ekru/50 to-background"></div></div>
<div class="max-w-[1180px] mx-auto px-7">
<div class="max-w-2xl mb-16 reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Çatı ilkemiz: ekosistemin sürdürülebilirliği.</h2><p class="mt-6 text-on-surface-variant text-lg">Çalışmalarımız bu ilke etrafında birbiriyle bağlantılı beş eksende şekillenir.</p></div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-8">
{chr(10).join(_kart(k, e) for k, e in enumerate(EKSENLER_KISA))}
</div>
<div class="mt-14 text-center reveal-on-scroll"><a href="faaliyet.html" class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-8 py-4 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all group">Faaliyet Alanlarımız {ARROW}</a></div>
</div>
</section>
''', "faaliyet")

# 4) Gençlik: tek paragraf + iki bağlantı (ICYB/IMYB ayrıntısı ve kulüp modeli genclik.html'de)
idx = swap_section(idx, "Gençlik & Uluslararası Temsil", f'''<!-- Gençlik & Uluslararası Temsil -->
<section class="py-32 bg-gradient-to-b from-night to-[#57130d] text-white overflow-hidden" id="genclik">
<div class="max-w-[1180px] mx-auto px-7">
<div class="max-w-3xl reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl mb-6">Gençlik &amp; Uluslararası Temsil</h2>
<p class="text-white/75 text-lg leading-relaxed mb-10">Gençlerin arıcılıkta eğitim, deneyim ve uluslararası bağlantı kazanmasını destekliyoruz. Okul temelli Apikültür Gençlik Kulüpleri ile Türkiye’nin ICYB ve IMYB süreçlerine katılımı bu çalışmaların merkezinde yer alır.</p>
<div class="flex flex-wrap gap-4"><a href="genclik.html" class="inline-flex items-center gap-2 bg-amber text-espresso px-8 py-4 rounded-full font-bold hover:-translate-y-0.5 transition-all group">Gençlik Çalışmalarımız {ARROW}</a><a href="genclik.html#kulupler" class="border border-white/30 text-white px-8 py-4 rounded-full font-bold hover:bg-white/10 transition-all">Gençlik Kulüpleri</a></div>
</div>
</div>
</section>
''', "genclik")

# 5) "Bilim ve gelenek" görsel bandı kaldırıldı (Akademi bölümüyle aynı mesaj)
idx = swap_section(idx, "Bilim ve gelenek", '', "bilim-gelenek")

# 6) Akademi: iki paragraf (biri akademi.html'deki metnin aynısı) yerine tek kısa cümle
idx = once(idx, '<p class="text-on-surface-variant text-lg leading-relaxed mb-4">Güçlü bir arıcılık, doğru bilgiye ve bu bilginin paylaşılmasına bağlıdır.</p>\n'
                '<p class="text-on-surface-variant text-lg leading-relaxed">Apikültür Vakfı; eğitim, araştırma, bilimsel iletişim ve bilgi paylaşımını faaliyetlerinin temel unsurlarından biri olarak görür.</p>\n',
           '<p class="text-on-surface-variant text-lg leading-relaxed">Eğitim, araştırma ve bilgi paylaşımı çalışmalarımız üç başlıkta toplanır.</p>\n', "akademi-p")

# 7) Projeler: giriş paragrafları, kart açıklamaları ve not kaldırıldı (hepsi projeler.html'de)
idx = once(idx, '<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Amaçlarımızı sahada hayata geçiriyoruz.</h2><p class="mt-6 text-on-surface-variant text-lg">Apikültür Vakfı, faaliyet alanları doğrultusunda farklı kurumlar, uzmanlar, eğitim kuruluşları, kamu kurumları ve diğer paydaşlarla çeşitli projeler geliştirir ve destekler.</p><p class="mt-4 text-on-surface-variant text-lg">Projelerimiz; eğitimden gençliğe, biyoçeşitlilikten yerel değerlere kadar farklı alanlara odaklanabilir.</p>',
           '<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Amaçlarımızı sahada hayata geçiriyoruz.</h2>', "projeler-p")
idx, n = re.subn(r'(<h3 class="font-headline-md text-xl mb-3 text-espresso">[^<]+</h3>)<p class="text-on-surface-variant">[^<]*</p>(<span class="mt-4)', r'\1\2', idx)
if n != 5: print("!! proje kart metni", n); sys.exit(1)
idx = once(idx, '<div class="mt-8 flex flex-col md:flex-row md:items-center md:justify-between gap-6 reveal-on-scroll"><p class="text-sm text-on-surface-variant/70">Projelere ait katılımcı, okul ve etkinlik sayıları yalnızca ilgili projenin kendi kapsamında paylaşılır.</p>',
           '<div class="mt-12 reveal-on-scroll">', "projeler-not")
idx = once(idx, 'class="shrink-0 inline-flex items-center gap-2 border border-terracotta text-terracotta px-7 py-3.5', 'class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-7 py-3.5', "projeler-btn")

# 8) İş birlikleri: genel geçer ilk cümle kaldırıldı
idx = once(idx, '<p class="mt-6 text-on-surface-variant text-lg">Arıcılığın karşı karşıya olduğu sorunlar sınırlarla sınırlı değildir.</p><p class="mt-4 text-on-surface-variant text-lg">',
           '<p class="mt-6 text-on-surface-variant text-lg">', "isbirligi-p")

# 9) Yönetim: kısa özet + tek buton (kurul kartları, senet ve kuruluş paragrafı iç sayfalarda)
idx = swap_section(idx, "Yönetim & Şeffaflık", f'''<!-- Yönetim & Şeffaflık -->
<section class="py-32 bg-background" id="yonetim">
<div class="max-w-[1180px] mx-auto px-7">
<div class="max-w-3xl reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-6">Gücümüzü güvenilirlik ve şeffaflıktan alıyoruz.</h2>
<p class="text-on-surface-variant text-lg leading-relaxed mb-10">Vakfın organları Mütevelli Heyeti ve Yönetim Kurulu’dur; Bilim Kurulu ve Danışma Kurulu çalışmalarımıza katkı sunar. Kurumsal belgeler Şeffaflık Merkezi’nde yer alır.</p>
<a href="yonetim.html" class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-8 py-4 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all group">Yönetim &amp; Şeffaflık {ARROW}</a>
</div>
</div>
</section>
''', "yonetim")
