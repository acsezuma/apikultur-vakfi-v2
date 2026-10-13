# Apikültür Vakfı — Web Sitesi (v2)

Apikültür Vakfı'nın resmî web sitesi. **Doğayı Geleceğe Taşır.**

Bu sürüm (**v2**), `apikültürsitedeneme2` tasarımını (Outfit + Hanken Grotesk tipografisi, terracotta/amber/espresso paleti) esas alır ve kurumsal kimliği birebir yansıtır.

Yayın hedefi: **https://acsezuma.github.io/apikultur-vakfi-v2/**
(apikulturvakfi.com bağlandığında güncellenecek)

## Yapı

Çok sayfalı statik bir site (Türkçe + İngilizce). Stil, Tailwind CDN + `tailwind.config` üzerinden marka token'larıyla tanımlıdır. Sayfalar `_gelistirme/` klasöründeki Python betikleriyle üretilir; ayrıntılar **[`_gelistirme/NOTLAR.md`](_gelistirme/NOTLAR.md)** dosyasında.

| Dosya | İçerik |
|---|---|
| `index.html` | Ana sayfa |
| `vakif.html`, `faaliyet.html`, `genclik.html`, `akademi.html`, `gelecek.html`, `projeler.html`, `yonetim.html` | İç sayfalar |
| `en/` | İngilizce sayfalar (`index`, `about`, `areas-of-work`, `youth`, `academy`, `future`, `projects`, `governance`) |
| `senet.html` | Vakıf senedinin tam metni (yazdırılabilir; PDF: `assets/vakif-senedi.pdf`), elle düzenlenir |
| `assets/programlar.json` | Apikültür Gelecek açık programları (elle düzenlenir) |
| `assets/` | logo, favicon, paylaşım görselleri (`og-image.png`, `og-image-en.png`), senet PDF'i |
| `assets/img/` | Bölüm ve proje fotoğrafları (self-hosted) |
| `robots.txt`, `sitemap.xml` | Arama motoru dosyaları |
| `_gelistirme/` | Üretici betikler ve geliştirme notları (yayımlanmaz) |

## Kurumsal kimlik (tasarım token'ları)

- **Renkler:** terracotta `#B82618`, amber `#EA8512`, espresso `#33261B`, ekru `#F9EFE3`, background `#fff8f5`, primary `#950602`
- **Tipografi:** Başlık/Display → **Outfit**; Gövde → **Hanken Grotesk**; Etiket/mono → **IBM Plex Mono**
- **Logo:** bee "A" rozeti + "APİKÜLTÜR / VAKFI" kelime markası (`assets/logo-mark.svg`)

> Not: Orijinal tasarımdaki geçici görsel adresleri (`lh3.googleusercontent.com/aida…`) kalıcı değildi; hepsi `assets/img/` altındaki kendi dosyalarımızla değiştirildi. Vakfın nihai saha fotoğrafları geldiğinde aynı adlarla değiştirilebilir.

## Güncelleme

1. Metni `_gelistirme/` içindeki betiklerde değiştirin (üretilen `.html` dosyalarını elle düzenlemeyin, bir sonraki üretimde ezilir).
2. `python3 _gelistirme/build_pages.py && python3 _gelistirme/build_en.py`
3. `main` dalına commit + push yapın. GitHub Pages otomatik yeniden yayınlar (1-2 dk).

Apikültür Gelecek'e açık program eklemek için yalnızca `assets/programlar.json` düzenlenir (biçim: `_gelistirme/NOTLAR.md`).

## Alan adı bağlanacağı zaman

1. Repo → Settings → Pages → Custom domain
2. DNS `A`/`CNAME` kayıtlarını GitHub Pages'e yönlendirin
3. `_gelistirme/build_pages.py` (`BASE_URL`), `_gelistirme/build_en.py` (`BASE`) ve `_gelistirme/index_base.html` içindeki canonical / `og:url` / `og:image` / JSON-LD adreslerini ve `robots.txt`'yi güncelleyip sayfaları yeniden üretin.
