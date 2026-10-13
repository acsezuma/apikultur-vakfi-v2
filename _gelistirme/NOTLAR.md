# Geliştirme notları

Bu klasör sitenin **kaynağıdır**. Alt çizgiyle başladığı için GitHub Pages (Jekyll) tarafından yayımlanmaz.

## 1. Site nasıl üretiliyor?

```
_gelistirme/index_base.html   ─┐
_gelistirme/build_pages.py     ├─▶ index.html + vakif, faaliyet, genclik, akademi, gelecek, projeler, yonetim (.html) + sitemap.xml
_gelistirme/gelecek_index.py   │   (Apikültür Gelecek'in ana sayfa/menü/footer eklemeleri)
_gelistirme/gelecek_page.py   ─┘   (gelecek.html sayfası)

_gelistirme/build_en.py  + en_text.py  ─▶  en/ altındaki İngilizce sayfalar
```

Çalıştırma (repo kökünden, Python 3, ek paket gerekmez):

```bash
python3 _gelistirme/build_pages.py
python3 _gelistirme/build_en.py
```

Kontrol: `build_en.py` çıktısında **`kullanılmayan sözlük anahtarı: 0`** ve **`SORUNLAR: 0`** görülmeli. Betikler canlı dosyaları birebir yeniden üretir (`git diff` boş olmalı).

> **Önemli:** Üretilen `.html` dosyalarını elle düzenlemeyin; bir sonraki üretimde ezilir. Değişikliği betiklerde yapın.
> İstisnalar (elle düzenlenir): `senet.html`, `assets/programlar.json`, görseller.

### Türkçe bir metin değişince

1. Metni `build_pages.py` / `gelecek_*.py` içinde (ana sayfa için çoğu zaman `index_base.html` + `build_pages.py`'deki `once(...)` değişiklikleri) değiştirin.
2. `en_text.py` içindeki sözlükte eski Türkçe anahtarı yenisiyle değiştirip İngilizcesini yazın.
3. `build_en.py`, Türkçe karakter içeren çevrilmemiş metinleri listeler; Türkçe karakter içermeyen kısa kelimeler (ör. "Proje") gözden kaçabilir, onları elle kontrol edin.

### İngilizce sayfa adları

| TR | EN |
|---|---|
| index.html | en/ |
| vakif.html | en/about.html |
| faaliyet.html | en/areas-of-work.html |
| genclik.html | en/youth.html |
| akademi.html | en/academy.html |
| gelecek.html | en/future.html |
| projeler.html | en/projects.html |
| yonetim.html | en/governance.html |

Senet yalnızca Türkçedir (`senet.html`); İngilizce sayfalar ona "(in Turkish)" notuyla bağlanır.

## 2. Apikültür Gelecek: açık program ekleme

Betik çalıştırmaya gerek yoktur. `assets/programlar.json` dosyası (GitHub web arayüzünden de) düzenlenir; kartlar `gelecek.html` ve `en/future.html` sayfalarında kendiliğinden görünür, liste boşken "Yeni programlarımız hazırlanıyor" kutusu çıkar.

```json
[
  {
    "durum": "acik",
    "tr": {"ad": "2027 Gelecek Bursları", "ozet": "Kısa açıklama", "kimler": "…", "destek": "…", "son_basvuru": "…", "link": "https://…"},
    "en": {"ad": "2027 Future Scholarships", "ozet": "Short description", "kimler": "…", "destek": "…", "son_basvuru": "…", "link": "https://…"}
  }
]
```

`durum`: `acik` (Başvuruya açık), `yakinda` (Yakında), `kapandi` (Başvurular kapandı), `sonuclandi` (Sonuçlandı).

Ön kayıt formu şu an bilgileri kullanıcının e-posta uygulamasında `info@apikulturvakfi.org` adresine hazır e-posta olarak açar (sunucu yok). İleride bir form servisi (Formspree, Tally vb.) bağlanabilir: `gelecek_page.py` içindeki `G_SCRIPT` bölümündeki gönderim kısmı değiştirilir.

## 3. Önizleme ve paylaşım görselleri (isteğe bağlı)

- `onizleme/build_preview2.py`: Tailwind CDN'e erişmeden birebir önizleme üretir. `onizleme/calisma/tw` altında `npm i tailwindcss@3.4.17 @tailwindcss/forms @tailwindcss/container-queries playwright-core material-symbols`, `onizleme/calisma/fonts` altında fontsource paketleri (outfit, hanken-grotesk, ibm-plex-mono) gerekir.
- `onizleme/og.html`, `og_en.html`: paylaşım görsellerinin kaynağı. `node onizleme/og.js <og.html yolu> assets/og-image.png` (EN için `assets/og-image-en.png`). Görsel değişince sayfalardaki `?v=` sürümünü artırın (`build_pages.py` → `og-surum`, `build_en.py`).

## 4. Tasarım ve editoryal kurallar

- Tasarım dili: Tailwind + `tailwind.config` token'ları; Outfit (başlık), Hanken Grotesk (gövde). Renkler: terracotta `#B82618`, amber `#EA8512`, espresso `#33261B`, ekru `#F9EFE3`, zemin `#fff8f5`.
- "Yapay zekâ kokmasın": chip/pill bulutu yok; mono büyük harf "eyebrow" etiketleri ve `Bilim · Eğitim · …` gibi noktalı slogan satırları yok; cümle ortasında " — " yok; büyük amber başlık yok; az sayıda, tutarlı kart tipi.
- Rakamlar: proje rakamları yalnızca ilgili projede ve dönemiyle (Arı Dostum: 30 okul, 14.895 öğrenci, 2024–2025, Kartal). Uydurma/boş "etki" sayacı yok.
- Vakıf / faaliyet / proje / iş birliği–temsil ayrımı korunur. ICYB header, hero ve footer'da yer almaz.
- "kamu yararı" / "public benefit" ifadesi kullanılmaz (hukuki statü çağrışımı). Senet Md.7: organlar Mütevelli Heyeti ve Yönetim Kurulu; Bilim ve Danışma Kurulu destek yapılarıdır.
- Yazım: "Apikültür" (sitenin her yerinde), "iş birliği" ayrı (TDK).

## 5. Alınan kararlar (özet)

- Menü: Vakıf (açılır: Vakıf Hakkında, Vakıf Senedi) · Faaliyet Alanlarımız · Gençlik · Akademi & Bilim · Apikültür Gelecek · Projeler · Yönetim & Şeffaflık · İletişim · Bağış Yap. 9 öğe olduğu için masaüstü menü 1280px'ten itibaren, altında hamburger.
- Header'da ayrı Vakıf Senedi butonu yok; ana sayfa içeriğinde senet yalnızca Yönetim bölümündeki butonda.
- Header'da EN/TR dil butonu; varsayılan Türkçe, otomatik yönlendirme yok.
- Apikültür Gelecek: 5 program (Gelecek Bursları, Genç Bilim, Araştır, Dünyaya Açıl, Sahada Gelecek). AKG dokümanları hazır; değerlendirme ve SSS taahhütleri bunlara dayanır. Ayrı "Etki" bölümü yok.
- Beş faaliyet alanının 01–05 numaraları korunur; diğer süs numaraları kaldırıldı.
- Arı Dostum Olur Musun? durumu: Devam ediyor. COLOSS uluslararası ağlar listesinde.

## 6. Vakıftan beklenenler

- KVKK aydınlatma metni, Gizlilik ve Çerez politikaları (footer bağlantıları boş; ön kayıt formunun onay kutusu bu metne bağlanmalı).
- Adres: Şişli mi, senetteki Beylikdüzü mü?
- FAO, Apimondia, COLOSS ile ilişkinin türü; ICYB ifadesi (özellikle İngilizce).
- Takvim (19 Mayıs 2026, 23 Nisan 2027, Temmuz 2027 / DAGEM) ve kulüp modeli bilgilerinin teyidi.
- Diğer dört projenin durum etiketleri (Planlama / Geliştirme / Araştırma).
- Kuruluş paragrafı (Muzaffer Yıldırım, Yıldırım Plastik, Apimaye).
- Bizim yaptığımız İngilizce çevirilerin ve program adlarının (Apiculture Future, Future Scholarships, Young Science, Research Grants, Go Global, Future in the Field, Future Network, Future Fund) onayı.
- SSS / değerlendirme metinlerinin AKG ile birebir uyumu ("Komisyon", maddi hata inceleme, fikrî haklar).
- ICYB logosu; genç ve insan odaklı fotoğraflar.

## 7. Sonraki işler

- **Apikültür Akademi** ayrı başlık/sayfa olacak (şu an Akademi & Bilim sayfasında bir bölüm).
- Alan adı (apikulturvakfi.org/.com) bağlandığında: `build_pages.py` → `BASE_URL`, `build_en.py` → `BASE`, `index_base.html` içindeki canonical / og / JSON-LD adresleri, `robots.txt`.
- Ön kayıt formuna gerçek bir form servisi bağlanması (KVKK metniyle birlikte).
- Program sayısı artınca alt program sayfaları.
