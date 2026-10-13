# build_pages.py içinden exec edilir (hero, head2, cta, shell, MAILTO, ARROW hazır).
# =====================================================================
# APİKÜLTÜR GELECEK (gelecek.html)
# =====================================================================
G_PROGS = [
 ("gelecek-burslari", "school", "Gelecek Bursları", "Eğitimine devam et.", "Öğrencilerin eğitim yolculuklarını destekleyen dönemsel burs programları."),
 ("genc-bilim", "biotech", "Genç Bilim", "Araştırmacı yolculuğunu geliştir.", "Yüksek lisans, doktora ve kariyerinin erken dönemindeki araştırmacılara yönelik destekler."),
 ("arastir", "science", "Araştır", "Bir sorunun peşinden git.", "Tez, saha araştırması, bilimsel proje ve araştırma faaliyetlerine yönelik destekler."),
 ("dunyaya-acil", "travel_explore", "Dünyaya Açıl", "Bilgini dünyayla buluştur.", "Kongre, bilimsel toplantı, araştırma ziyareti ve uluslararası hareketlilik desteği."),
 ("sahada-gelecek", "agriculture", "Sahada Gelecek", "Bilgiyi uygulamaya taşı.", "Arıcı, çiftçi ve saha uygulayıcılarının eğitim ve kapasite gelişimini destekleyen programlar."),
]
def g_card(k, pid, icon, name, tag, desc):
    span = "lg:col-span-2" + (" lg:col-start-2" if k == 3 else "")
    return (f'<div id="{pid}" class="feat-card p-9 rounded-3xl reveal-on-scroll {span}">'
            f'<div class="w-14 h-14 rounded-2xl bg-ekru flex items-center justify-center mb-7"><span class="material-symbols-outlined text-terracotta text-3xl">{icon}</span></div>'
            f'<h3 class="font-headline-md text-2xl text-espresso mb-2">{name}</h3>'
            f'<p class="font-headline-md text-lg text-terracotta mb-4">{tag}</p>'
            f'<p class="text-on-surface-variant leading-relaxed" data-ozet>{desc}</p></div>')

SEL = 'w-full rounded-xl border-outline-variant/70 bg-white px-4 py-3 text-espresso focus:border-terracotta focus:ring-terracotta'
LBL = 'block text-sm font-semibold text-espresso mb-2'
def sel(name, label, opts):
    o = '<option value="">Seçiniz</option>' + ''.join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<div><label class="{LBL}" for="b-{name}">{label}</label><select id="b-{name}" name="{name}" class="{SEL}">{o}</select></div>'

FINDER = f'''<section class="py-24 md:py-32 bg-ekru/30" id="bulucu">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Size uygun destek hangisi?", ["Üç kısa soruyu yanıtlayın; size uygun olabilecek destek yollarını gösterelim. Bu aşama başvuru değildir, sizi doğru programa yönlendirir."], "mb-12")}
<form id="bulucu-form" class="reveal-on-scroll bg-white rounded-3xl border border-outline-variant/30 shadow-sm p-7 md:p-10" novalidate>
<div class="grid md:grid-cols-3 gap-6 mb-8">
{sel("kim", "Siz kimsiniz?", [("ogrenci", "Öğrenci"), ("lisansustu", "Yüksek lisans / doktora öğrencisi"), ("arastirmaci", "Araştırmacı / akademisyen"), ("arici", "Arıcı"), ("ciftci", "Çiftçi"), ("diger", "Diğer")])}
{sel("ihtiyac", "Ne için destek arıyorsunuz?", [("egitim", "Eğitim"), ("arastirma", "Araştırma"), ("kongre", "Kongre / seyahat"), ("saha", "Saha eğitimi"), ("proje", "Proje")])}
{sel("alan", "Çalışma alanınız nedir?", [("aricilik", "Arıcılık"), ("ari-sagligi", "Arı sağlığı"), ("polinasyon", "Polinasyon"), ("biyocesitlilik", "Biyoçeşitlilik"), ("tarim", "Tarım"), ("gida", "Gıda"), ("cevre", "Çevre / iklim"), ("ilgili", "İlgili başka bir alan")])}
</div>
<button type="submit" class="inline-flex items-center gap-2 bg-terracotta text-white px-8 py-4 rounded-full font-bold hover:shadow-lg transition-all group">Uygun Destekleri Göster {ARROW}</button>
<p id="bulucu-uyari" class="mt-5 text-terracotta font-semibold" hidden>Lütfen ilk iki soruyu yanıtlayın.</p>
<div id="bulucu-sonuc" class="mt-10 pt-8 border-t border-outline-variant/40" hidden>
<h3 class="font-headline-md text-2xl text-espresso mb-6">Size uygun olabilecek programlar</h3>
<ul id="bulucu-liste" class="space-y-5 mb-6"></ul>
<p id="bulucu-alan" class="text-on-surface-variant mb-2" hidden>Seçtiğiniz çalışma alanı Apikültür Gelecek programlarının kapsamındadır.</p>
<p class="text-on-surface-variant">Bu programların başvuruya açık çağrıları <a class="text-terracotta font-semibold hover:underline underline-offset-4" href="#programlar">Açık Programlar</a> bölümünde yayımlanır.</p>
</div>
</form>
</div>
</section>
'''

INP = 'w-full rounded-xl border-outline-variant/70 bg-white px-4 py-3 text-espresso placeholder:text-espresso/40 focus:border-terracotta focus:ring-terracotta'
def fld(fid, label, typ="text", span="", req=False, extra=""):
    star = ' *' if req else ''
    r = ' required' if req else ''
    return (f'<div class="{span}"><label class="{LBL}" for="{fid}">{label}{star}</label>'
            f'<input id="{fid}" name="{fid}" type="{typ}" class="{INP}" data-alan{r}{extra}/></div>')

PROG_OPTS = ''.join(f'<option value="{p[0]}">{p[2]}</option>' for p in G_PROGS) + '<option value="emin-degil">Henüz emin değilim</option>'
ONKAYIT = f'''<div id="on-kayit" class="mt-16 grid lg:grid-cols-12 gap-10 lg:gap-16 reveal-on-scroll">
<div class="lg:col-span-4">
<h3 class="font-headline-md text-3xl text-espresso mb-4">Ön kayıt</h3>
<p class="text-on-surface-variant text-lg leading-relaxed mb-4">Programlar açıldığında sizinle iletişime geçebilmemiz için kısa ön kayıt formunu doldurabilirsiniz.</p>
<p class="text-on-surface-variant leading-relaxed">Ön kayıt, başvuru yerine geçmez. Başvurular ilgili program ilanında belirtilen koşullarla alınır.</p>
</div>
<form id="onkayit-form" class="lg:col-span-8 bg-white rounded-3xl border border-outline-variant/30 shadow-sm p-7 md:p-10">
<div class="grid md:grid-cols-2 gap-6">
{fld("ok-ad", "Ad", req=True, extra=' autocomplete="given-name"')}
{fld("ok-soyad", "Soyad", req=True, extra=' autocomplete="family-name"')}
{fld("ok-yas", "Yaş", "number", req=True, extra=' min="10" max="99"')}
{fld("ok-telefon", "Telefon", "tel", req=True, extra=' autocomplete="tel"')}
{fld("ok-eposta", "E-posta", "email", "md:col-span-2", req=True, extra=' autocomplete="email"')}
{fld("ok-okul", "Okul / kurum", req=True)}
{fld("ok-bolum", "Bölüm")}
<div class="md:col-span-2"><label class="{LBL}" for="ok-program">İlgilendiğiniz destek</label><select id="ok-program" name="ok-program" class="{SEL}" data-alan><option value="">Seçiniz</option>{PROG_OPTS}</select></div>
<div class="md:col-span-2"><label class="{LBL}" for="ok-proje">Proje veya çalışma konunuz</label><textarea id="ok-proje" name="ok-proje" rows="3" class="{INP}" data-alan placeholder="Kısaca anlatın"></textarea></div>
</div>
<label class="mt-7 flex items-start gap-3 text-sm text-on-surface-variant leading-relaxed"><input type="checkbox" required class="mt-0.5 rounded border-outline-variant text-terracotta focus:ring-terracotta"/><span>Bu formdaki bilgilerimin, ön kaydımın değerlendirilmesi ve benimle iletişime geçilmesi amacıyla Apikültür Vakfı tarafından işlenmesini kabul ediyorum. 18 yaşından küçüksem formu velimin onayıyla gönderiyorum.</span></label>
<div class="mt-8 flex flex-col sm:flex-row sm:items-center gap-5">
<button type="submit" class="shrink-0 whitespace-nowrap inline-flex items-center justify-center gap-2 bg-terracotta text-white px-8 py-4 rounded-full font-bold hover:shadow-lg transition-all group">Ön Kaydı Gönder {ARROW}</button>
<p class="text-sm text-on-surface-variant leading-relaxed">Gönder’e bastığınızda bilgileriniz e-posta uygulamanızda hazır bir e-posta olarak açılır; göndermeniz yeterlidir.</p>
</div>
<p id="onkayit-tamam" class="mt-6 text-terracotta font-semibold" hidden>E-posta taslağınız hazırlandı. Gönderdiğinizde ön kaydınız bize ulaşır.</p>
<span id="onkayit-konu" hidden>Apikültür Gelecek Ön Kayıt</span>
</form>
</div>
'''

PROGRAMS_SEC = f'''<section class="py-24 md:py-32 bg-background" id="programlar">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Açık programlar", ["Apikültür Gelecek destekleri dönemsel programlar halinde açılır. Her program için kimlerin başvurabileceği, destek kapsamı, başvuru tarihleri, değerlendirme kriterleri ve sonuç süreci program ilanında açıklanır."], "mb-12")}
<div id="program-listesi" class="grid md:grid-cols-2 gap-8" hidden></div>
<div id="program-yok" class="rounded-3xl border border-outline-variant/40 bg-ekru/40 p-8 md:p-10 reveal-on-scroll">
<h3 class="font-headline-md text-2xl text-espresso mb-3">Yeni programlarımız hazırlanıyor.</h3>
<p class="text-on-surface-variant text-lg leading-relaxed max-w-3xl">Şu anda başvuruya açık bir Apikültür Gelecek programı bulunmuyor. Yeni burs ve destek programları açıldığında bu sayfada duyurulur.</p>
</div>
<template id="program-etiketleri"><span data-k="acik">Başvuruya açık</span><span data-k="yakinda">Yakında</span><span data-k="kapandi">Başvurular kapandı</span><span data-k="sonuclandi">Sonuçlandı</span><span data-k="kimler">Kimler için:</span><span data-k="destek">Destek:</span><span data-k="son">Son başvuru:</span><span data-k="incele">Programı İncele ve Başvur</span></template>
{ONKAYIT}
</div>
</section>
'''

STEPS = [("Programını bul", "Açık programları incele ve sana uygun destek programını seç."),
         ("Koşulları incele", "Başvuru şartlarını, takvimi, destek kapsamını ve değerlendirme kriterlerini incele."),
         ("Başvurunu tamamla", "Başvurunu çevrim içi olarak tamamla. Başvuru ücretsizdir."),
         ("Değerlendirme", "Başvurun, ilgili program için önceden belirlenmiş kriterler doğrultusunda değerlendirilir."),
         ("Tahsis", "Destekler; değerlendirme sonuçları, program bütçesi ve kontenjan çerçevesinde Vakfın yetkili karar süreciyle tahsis edilir. Sonuç, program ilanında belirtilen kanal üzerinden bildirilir."),
         ("Destek ve izleme", "Destek tahsis edilen adaylar gerekli doğrulama işlemlerinin ardından programa dahil edilir; süreç programın niteliğine göre izlenir.")]
steps_html = ''.join(f'<li class="border-t-2 border-terracotta/60 pt-5"><span class="block font-headline-lg text-3xl text-terracotta/70 mb-3">{k:02d}</span>'
                     f'<h3 class="font-headline-md text-xl text-espresso mb-2">{t}</h3><p class="text-on-surface-variant leading-relaxed">{p}</p></li>'
                     for k, (t, p) in enumerate(STEPS, 1))
BASVURU = f'''<section class="py-24 md:py-32 bg-ekru/30" id="basvuru">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Nasıl başvurulur?", ["Başvurular ücretsizdir. Değerlendirme kriterleri program açılmadan önce belirlenir. Programın niteliğine göre değerlendirme dosyaları kimlik bilgilerinden ayrıştırılabilir ve birden fazla değerlendirici kullanılabilir."], "mb-14")}
<ol class="grid md:grid-cols-2 lg:grid-cols-3 gap-x-10 gap-y-12 reveal-on-scroll">{steps_html}</ol>
<div class="mt-16 grid lg:grid-cols-12 gap-8 lg:gap-16 pt-12 border-t border-outline-variant/40 reveal-on-scroll">
<h3 class="lg:col-span-4 font-headline-md text-2xl text-espresso">Başvuruda neler istiyoruz?</h3>
<div class="lg:col-span-8 space-y-4 text-on-surface-variant text-lg leading-relaxed">
<p>Başvuru sahiplerinden yalnızca program için gerekli bilgileri istemeyi amaçlıyoruz. Programın niteliğine göre eğitim bilgileri, akademik veya mesleki bilgiler, motivasyon, ekonomik durum ve araştırma veya proje bilgileri talep edilebilir.</p>
<p>Her belgenin ilk aşamada yüklenmesi gerekmeyebilir. Kimlik doğrulama, banka bilgileri ve benzeri yalnızca sonraki aşamalarda gerekli olacak bilgiler, ihtiyaç oluştuğunda talep edilir.</p>
</div>
</div>
</div>
</section>
'''

EVAL = [("Önceden belirlenmiş kriterler", "Her programın değerlendirme kriterleri başvurular açılmadan önce ilan edilir."),
        ("Tarafsız değerlendirme", "Değerlendiriciler etik, gizlilik ve çıkar çatışması kurallarına tabidir."),
        ("Gerektiğinde kimlikten arındırma", "Değerlendirme için gerekli olmayan kimlik bilgileri mümkün olduğunca değerlendiriciden ayrıştırılır."),
        ("Kurumsal karar", "Değerlendirici görüşleri ve Komisyon önerileri nihai tahsis kararı değildir; tahsis Vakfın yetkili karar süreciyle gerçekleştirilir.")]
eval_html = ''.join(f'<div class="border-t-2 border-terracotta/60 pt-6"><h3 class="font-headline-md text-2xl text-espresso mb-3">{t}</h3><p class="text-on-surface-variant text-lg leading-relaxed">{p}</p></div>' for t, p in EVAL)
TRUST = [("Başvuru ücretsizdir.", "Hiçbir başvuru sahibinden değerlendirme veya tahsis karşılığında ücret alınmaz."),
         ("Kişisel veriler ölçülü işlenir.", "Başvuruda yalnızca süreç için gerekli bilgiler istenir."),
         ("Bağışçı ile değerlendirme ayrıdır.", "Finansman sağlamak, başvuru sahibini seçme yetkisi vermez."),
         ("İnsan kararı korunur.", "Nihai destek tahsisi yalnızca otomatik bir sistem veya yapay zekâ tarafından yapılmaz.")]
trust_html = ''.join(f'<div class="border-t-2 border-amber/60 pt-5"><h3 class="font-headline-md text-xl mb-3">{t}</h3><p class="text-white/70 leading-relaxed">{p}</p></div>' for t, p in TRUST)
DEGER = f'''<section class="py-24 md:py-32 bg-background" id="degerlendirme">
<div class="max-w-[1180px] mx-auto px-7">
{head2("Nasıl değerlendiriyoruz?", [])}
<div class="grid md:grid-cols-2 gap-x-16 gap-y-12 reveal-on-scroll">{eval_html}</div>
</div>
</section>
<section class="py-24 md:py-28 bg-espresso text-white" id="ilkeler">
<div class="max-w-[1180px] mx-auto px-7">
<h2 class="font-headline-lg text-4xl md:text-5xl leading-[1.12] mb-14 reveal-on-scroll">Güven ilkelerimiz</h2>
<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-x-10 gap-y-10 reveal-on-scroll">{trust_html}</div>
</div>
</section>
'''

AG = f'''<section class="py-24 md:py-32 bg-background" id="ag">
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-10 lg:gap-16">
<div class="lg:col-span-5 reveal-on-scroll"><h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12]">Destek bittiğinde bağ bitmiyor.</h2></div>
<div class="lg:col-span-7 reveal-on-scroll">
<p class="text-on-surface-variant text-lg leading-relaxed mb-10">Apikültür Gelecek’in amacı yalnızca finansal destek sağlamak değildir. Programın niteliğine göre yararlanıcıların eğitim, bilimsel çalışma veya gelişim süreçleri izlenir. Sonuçlarımızı yalnızca dağıtılan kaynakla değil; eğitim, bilim, araştırma ve saha üzerindeki çıktılarla değerlendiririz.</p>
<div class="border-t border-outline-variant/40 pt-7">
<h3 class="font-headline-md text-2xl text-espresso mb-3">Gelecek Ağı</h3>
<p class="text-on-surface-variant text-lg leading-relaxed mb-3">Desteklenen öğrenciler, araştırmacılar ve diğer yararlanıcılar isterlerse Gelecek Ağı’na katılarak bilgi paylaşımı, mentorluk, bilimsel iş birliği ve uluslararası bağlantılardan oluşan gönüllü bir topluluğun parçası olabilir.</p>
<p class="text-on-surface-variant text-lg leading-relaxed">Gelecek Ağı’na katılım gönüllüdür ve burs veya destek koşulu değildir.</p>
</div>
</div>
</div>
</section>
<section class="py-24 md:py-32 bg-ekru/30" id="destekle">
<div class="max-w-[1180px] mx-auto px-7 grid lg:grid-cols-12 gap-10 lg:gap-16 items-center">
<div class="lg:col-span-7 reveal-on-scroll">
<h2 class="font-headline-lg text-4xl md:text-5xl text-espresso leading-[1.12] mb-6">Bir öğrencinin değil, bir geleceğin yanında olun.</h2>
<p class="text-on-surface-variant text-lg leading-relaxed mb-4">Apikültür Gelecek yalnızca destek arayanların değil, geleceğe kaynak ayırmak isteyen kişi ve kurumların da buluşma noktasıdır. Bireyler ve kurumlar eğitim, bilim, araştırma veya belirli tematik alanlara kaynak sağlayabilir.</p>
</div>
<div class="lg:col-span-5 reveal-on-scroll">
<div class="bg-white rounded-3xl border border-outline-variant/30 shadow-sm p-8 md:p-10">
<h3 class="font-headline-md text-2xl text-espresso mb-3">Gelecek Fonu</h3>
<p class="text-on-surface-variant leading-relaxed mb-7">Bağışçılar destek alanını belirleyebilir; yararlanıcı seçimi Vakfın bağımsız değerlendirme ve tahsis sistemi içinde yürütülür.</p>
<a href="{MAILTO}Gelecek%20Fonu" class="inline-flex items-center gap-2 bg-terracotta text-white px-7 py-3.5 rounded-full font-bold hover:shadow-lg transition-all group">Gelecek Fonu’nu Destekle {ARROW}</a>
</div>
</div>
</div>
</section>
'''

FAQ_TOP = [
 ("Kimler başvurabilir?", "Hedef grup programa göre değişir. Öğrenciler, lisansüstü öğrenciler, genç araştırmacılar, arıcılar, çiftçiler veya belirli programların kapsamına giren diğer adaylar için farklı çağrılar açılabilir. Kesin koşullar her program ilanında belirtilir."),
 ("Başvurular ücretli mi?", "Hayır. Apikültür Gelecek programlarına başvuru ücretsizdir. Başvuru veya değerlendirme karşılığında herhangi bir ücret talep edilmez."),
 ("Başka bir burs veya destek alıyorsam başvurabilir miyim?", "Bu durum ilgili programın koşullarına göre değerlendirilir. Başka bir kurumdan burs veya destek almak, aksi program ilanında açıkça belirtilmedikçe, tek başına Apikültür Gelecek programlarına başvurmaya engel değildir."),
 ("Başvurular nasıl değerlendiriliyor?", "Başvurular ilgili program için önceden belirlenen kriterler doğrultusunda değerlendirilir. Programın niteliğine göre ön inceleme, bağımsız değerlendirici değerlendirmesi ve kurumsal karar aşamaları uygulanabilir."),
 ("Burs veya destek geri ödemeli mi?", "Program ilanında aksi açıkça belirtilmedikçe Apikültür Gelecek kapsamındaki burs ve destekler karşılıksızdır. Belirli amaçlı araştırma veya proje desteklerinde kaynağın tahsis amacına uygun kullanılması ve gerekli raporlamanın yapılması istenebilir."),
 ("Kişisel bilgilerimi değerlendiriciler görüyor mu?", "Programın niteliği elverdiği ölçüde değerlendirme için gerekli olmayan kimlik ve iletişim bilgilerinin değerlendiricilerden ayrıştırılması hedeflenir."),
]
FAQ_REST = [
 ("Apikültür Gelecek nedir?", "Apikültür Gelecek; Apikültür Vakfı’nın öğrencileri, genç araştırmacıları ve nitelikli eğitim, bilim, araştırma ve gelişim çalışmalarını desteklemek amacıyla oluşturduğu Eğitim, Bilim ve Gelecek Destek Programıdır."),
 ("Programlar sürekli açık mı?", "Hayır. Burs ve destek programları dönemsel olarak açılır. Başvuruya açık programlar Apikültür Gelecek sayfasında yayımlanır."),
 ("Hangi burs ve destekler veriliyor?", "Döneme göre öğrenci bursları, genç araştırmacı destekleri, tez ve araştırma destekleri, bilimsel toplantı ve hareketlilik destekleri ile eğitim ve saha gelişimine yönelik programlar açılabilir."),
 ("Başvuru için hangi belgeler gerekiyor?", "İstenen belgeler programa göre değişir. Başvuru sırasında yalnızca değerlendirme için gerekli bilgi ve belgelerin talep edilmesi amaçlanır. Kimlik doğrulama, banka bilgileri veya ek belgeler sürecin ilerleyen aşamalarında istenebilir."),
 ("Değerlendirme kriterlerini önceden görebilir miyim?", "Evet. İlgili programda kullanılacak temel değerlendirme kriterleri ve varsa ağırlıkları program ilanında açıklanır."),
 ("Başvurumu yaptıktan sonra bilgilerimi değiştirebilir miyim?", "Başvuru süresi içinde sistemin izin verdiği alanlarda değişiklik yapılabilir. Başvuru kapandıktan sonraki düzeltme veya belge tamamlama imkânları ilgili programın kurallarına göre belirlenir."),
 ("Başvuru yapmak destek almaya hak kazandırır mı?", "Hayır. Başvuru yapmak veya belirlenen asgari değerlendirme puanını aşmak tek başına destek hakkı oluşturmaz. Destekler değerlendirme sonuçları, program bütçesi, kontenjan ve Vakfın yetkili karar süreci çerçevesinde tahsis edilir."),
 ("Sonuçları nasıl öğreneceğim?", "Sonuçlar ilgili program ilanında belirtilen kanal üzerinden başvuru sahiplerine bildirilir."),
 ("Destek alamazsam nedenini öğrenebilir miyim?", "Programın yapısına göre başvuru statüsü ve uygun olduğu ölçüde değerlendirme bilgileri paylaşılabilir. Hesaplama, sistem veya belge işleme gibi maddi bir hata bulunduğu düşünülüyorsa program ilanında öngörülen maddi hata inceleme mekanizması kullanılabilir."),
 ("Yedek listede olmak ne anlama geliyor?", "Yedek statüsü, başvurunun desteklenebilir bulunduğunu ancak mevcut tahsis aşamasında asil listeye alınmadığını ifade eder. Yedek listede bulunmak kesin destek hakkı oluşturmaz."),
 ("Burs karşılığında Vakıf için çalışmam gerekir mi?", "Hayır. Burs veya destek karşılığında zorunlu çalışma, hizmet, bağış veya Vakıftan mal ya da hizmet satın alma yükümlülüğü getirilmez."),
 ("Araştırma desteği alırsam çalışmamın fikrî hakları Vakfa mı geçer?", "Yalnızca destek sağlanması, araştırmanın fikrî mülkiyetinin veya bilimsel yazarlık haklarının kendiliğinden Apikültür Vakfı’na geçmesi anlamına gelmez. Özel bir proje farklı bir düzenleme gerektiriyorsa koşullar ayrıca belirtilir."),
 ("Başvurular yapay zekâ tarafından mı değerlendiriliyor?", "Dijital araçlar başvuru sürecinin düzenlenmesi ve bazı kontroller için kullanılabilir; nihai destek tahsisi yalnızca otomatik bir sistem veya yapay zekâ sonucuna bırakılmaz."),
 ("Bağışçılar bursiyerleri veya desteklenecek araştırmacıları seçebilir mi?", "Bağışçılar belirli eğitim, bilim veya araştırma alanlarının desteklenmesine katkı sağlayabilir. Yararlanıcıların değerlendirilmesi ve destek tahsisi ise Vakfın kurumsal süreçleri içinde yürütülür."),
 ("Destek aldıktan sonra ne oluyor?", "Programın niteliğine göre eğitim, araştırma veya gelişim süreci belirli aralıklarla izlenebilir. Amaç yalnızca kaynak aktarmak değil, desteğin oluşturduğu sonuçları da takip etmektir."),
 ("Apikültür Gelecek Ağı nedir?", "Öğrencileri, araştırmacıları, akademisyenleri, arıcıları ve ilgili alan uzmanlarını bilgi paylaşımı, mentorluk ve iş birliği amacıyla bir araya getirmeyi hedefleyen gönüllü bir ağdır."),
 ("Gelecek Ağı’na katılmak zorunlu mu?", "Hayır. Katılım tamamen gönüllüdür. Katılmamak mevcut veya gelecekteki burs ve destek değerlendirmelerinde olumsuz bir unsur olarak kullanılamaz."),
 ("Şu anda açık program yoksa ne yapmalıyım?", "Yeni programlar açıldığında bu sayfadaki Açık Programlar bölümünde yayımlanır. Bu süre içinde ön kayıt formunu doldurabilirsiniz."),
]
def faq_item(q, a):
    return ('<details class="faq border-t border-outline-variant/40"><summary class="flex items-center justify-between gap-6 py-6 cursor-pointer">'
            f'<span class="font-headline-md text-xl text-espresso">{q}</span><span class="material-symbols-outlined faq-ico text-terracotta transition-transform" aria-hidden="true">add</span></summary>'
            f'<p class="pb-7 -mt-1 text-on-surface-variant text-lg leading-relaxed max-w-3xl">{a}</p></details>')
SSS = f'''<section class="py-24 md:py-32 bg-background" id="sss">
<div class="max-w-[960px] mx-auto px-7">
{head2("Sık sorulan sorular", [], "mb-10")}
<div class="reveal-on-scroll">{''.join(faq_item(q, a) for q, a in FAQ_TOP)}
<div id="sss-diger" hidden>{''.join(faq_item(q, a) for q, a in FAQ_REST)}</div>
<div class="border-t border-outline-variant/40 pt-8"><button id="sss-tumu" type="button" class="inline-flex items-center gap-2 border border-terracotta text-terracotta px-7 py-3.5 rounded-full font-bold hover:bg-terracotta hover:text-white transition-all">Tüm Soruları Gör <span class="material-symbols-outlined text-[20px]">expand_more</span></button></div>
</div>
</div>
</section>
'''

G_STYLE = '''<style>
.faq > summary { list-style: none; } .faq > summary::-webkit-details-marker { display: none; }
.faq[open] .faq-ico { transform: rotate(45deg); }
#bulucu-liste a { font-family:'Outfit',sans-serif; }
</style>
'''
G_SCRIPT = r'''<script>
(function(){
  var lang = document.documentElement.lang || 'tr';
  var more = document.getElementById('sss-tumu');
  if (more) more.addEventListener('click', function(){ document.getElementById('sss-diger').hidden = false; more.parentNode.hidden = true; });

  var f = document.getElementById('bulucu-form');
  if (f) f.addEventListener('submit', function(e){
    e.preventDefault();
    var kim = f.elements.kim.value, ih = f.elements.ihtiyac.value, alan = f.elements.alan.value;
    var out = document.getElementById('bulucu-sonuc'), warn = document.getElementById('bulucu-uyari'), list = document.getElementById('bulucu-liste');
    if (!kim || !ih) { warn.hidden = false; out.hidden = true; return; }
    warn.hidden = true;
    var r = []; function add(x){ if (r.indexOf(x) === -1) r.push(x); }
    var saha = (kim === 'arici' || kim === 'ciftci'), lis = (kim === 'lisansustu' || kim === 'arastirmaci');
    if (ih === 'egitim') { if (saha) add('sahada-gelecek'); else if (kim === 'arastirmaci') add('genc-bilim'); else add('gelecek-burslari'); if (kim === 'lisansustu') add('genc-bilim'); }
    if (ih === 'arastirma' || ih === 'proje') { add('arastir'); if (lis) add('genc-bilim'); if (saha && ih === 'proje') add('sahada-gelecek'); }
    if (ih === 'kongre') add('dunyaya-acil');
    if (ih === 'saha') add('sahada-gelecek');
    list.textContent = '';
    r.forEach(function(id){
      var card = document.getElementById(id); if (!card) return;
      var li = document.createElement('li'), a = document.createElement('a'), s = document.createElement('span');
      a.href = '#' + id; a.className = 'text-xl text-terracotta font-semibold hover:underline underline-offset-4'; a.textContent = card.querySelector('h3').textContent;
      s.className = 'block text-on-surface-variant mt-1'; s.textContent = card.querySelector('[data-ozet]').textContent;
      li.appendChild(a); li.appendChild(s); list.appendChild(li);
    });
    document.getElementById('bulucu-alan').hidden = !alan;
    out.hidden = false;
  });

  var box = document.getElementById('program-listesi'), none = document.getElementById('program-yok'), tpl = document.getElementById('program-etiketleri');
  if (box && tpl && window.fetch) {
    var L = function(k){ var el = tpl.content.querySelector('[data-k="' + k + '"]'); return el ? el.textContent : k; };
    fetch(new URL((lang === 'en' ? '../' : '') + 'assets/programlar.json', location.href)).then(function(res){ return res.json(); }).then(function(items){
      if (!Array.isArray(items)) return;
      items.forEach(function(p){
        var t = p[lang] || p.tr; if (!t) return;
        var c = document.createElement('article'); c.className = 'bg-white rounded-3xl border border-outline-variant/30 shadow-sm p-8';
        var st = document.createElement('span'); st.className = 'inline-block text-[11px] font-bold px-3 py-1 rounded-full mb-5 ' + (p.durum === 'acik' ? 'bg-terracotta text-white' : 'bg-ekru text-espresso'); st.textContent = L(p.durum); c.appendChild(st);
        var h = document.createElement('h3'); h.className = 'font-headline-md text-2xl text-espresso mb-3'; h.textContent = t.ad || ''; c.appendChild(h);
        if (t.ozet) { var o = document.createElement('p'); o.className = 'text-on-surface-variant leading-relaxed mb-5'; o.textContent = t.ozet; c.appendChild(o); }
        [['kimler', t.kimler], ['destek', t.destek], ['son', t.son_basvuru]].forEach(function(x){ if (!x[1]) return; var d = document.createElement('p'); d.className = 'text-espresso mb-1'; var b = document.createElement('strong'); b.textContent = L(x[0]) + ' '; d.appendChild(b); d.appendChild(document.createTextNode(x[1])); c.appendChild(d); });
        if (t.link) { var a = document.createElement('a'); a.href = t.link; a.className = 'mt-6 inline-flex items-center gap-2 text-terracotta font-bold'; a.textContent = L('incele') + ' →'; c.appendChild(a); }
        box.appendChild(c);
      });
      if (box.children.length) { box.hidden = false; none.hidden = true; }
    }).catch(function(){});
  }

  var k = document.getElementById('onkayit-form');
  if (k) k.addEventListener('submit', function(e){
    e.preventDefault();
    if (!k.checkValidity()) { k.reportValidity(); return; }
    var lines = [];
    k.querySelectorAll('[data-alan]').forEach(function(el){
      var lab = k.querySelector('label[for="' + el.id + '"]');
      var v = el.tagName === 'SELECT' ? (el.value ? el.options[el.selectedIndex].text : '') : el.value.trim();
      lines.push((lab ? lab.textContent.replace(/\s*\*$/, '') : el.name) + ': ' + v);
    });
    var subj = document.getElementById('onkayit-konu').textContent;
    location.href = 'mailto:info@apikulturvakfi.org?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(lines.join('\n'));
    document.getElementById('onkayit-tamam').hidden = false;
  });
})();
</script>
'''

hero_actions = ('<div class="mt-9 flex flex-wrap gap-4"><a class="bg-amber text-espresso px-8 py-4 rounded-full font-bold hover:shadow-xl hover:-translate-y-1 transition-all" href="#programlar">Açık Programları Gör</a>'
                '<a class="bg-white/10 border border-white/25 text-white px-8 py-4 rounded-full font-bold hover:bg-white/20 transition-all" href="#bulucu">Hangi Destek Bana Uygun?</a></div>'
                '<p class="mt-6 text-white/65">Başvurular ücretsizdir. Programlar dönemsel olarak açılır.</p>')
main = hero("assets/img/p1-bee-friend.jpg", "Apikültür Gelecek", "Apikültür Gelecek",
            "Geleceği desteklemenin birden fazla yolu var.",
            "Öğrencilerden genç araştırmacılara, bilimsel araştırmalardan uluslararası deneyime kadar; bilgi üreten, öğrenen ve geleceğe katkı sağlayan insanları destekliyoruz.",
            [("destekler", "Destekler"), ("programlar", "Açık Programlar"), ("basvuru", "Nasıl Başvurulur?"), ("degerlendirme", "Değerlendirme"), ("sss", "SSS")],
            actions=hero_actions)
main += G_STYLE
main += f'''<section class="relative isolate overflow-hidden py-24 md:py-32 bg-background" id="destekler"><div class="honeycomb-accent" aria-hidden="true"></div>
<div class="max-w-[1180px] mx-auto px-7">
{head2("Geleceğe giden farklı yollar var.", ["Apikültür Gelecek; arılar, arıcılık, polinasyon, biyolojik çeşitlilik, tarım, gıda, çevre ve kırsal kalkınmanın geleceğine katkı sağlayacak öğrencileri, genç araştırmacıları ve nitelikli çalışmaları desteklemek amacıyla oluşturulan Apikültür Vakfı Eğitim, Bilim ve Gelecek Destek Programıdır.", "Eğitimin farklı aşamalarından bilimsel araştırmaya, uluslararası gelişimden saha çalışmalarına kadar farklı ihtiyaçlar için farklı destek yolları sunar."])}
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-8">{''.join(g_card(k, *p) for k, p in enumerate(G_PROGS))}</div>
</div>
</section>
'''
main += FINDER + PROGRAMS_SEC + BASVURU + DEGER + AG + SSS
main += cta("Geleceğe yer aç.", "Bilgiye, bilime ve onu ileriye taşıyacak insanlara yapılan yatırımın geleceği değiştirebileceğine inanıyoruz.",
            [("Açık Programları Gör", "#programlar"), ("Gelecek Fonu’nu Destekle", "#destekle")])
main += G_SCRIPT
shell("gelecek.html", "Apikültür Gelecek | Burs, Araştırma ve Bilim Destekleri",
      "Apikültür Gelecek; öğrencileri, genç araştırmacıları ve nitelikli çalışmaları burs, araştırma ve gelişim destekleriyle buluşturan destek programıdır.",
      "Apikültür Gelecek", main)
