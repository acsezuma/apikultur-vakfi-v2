# Apikültür Vakfı — Web Sitesi (v2)

Apikültür Vakfı'nın resmî web sitesi. **Doğayı Geleceğe Taşır.**

Bu sürüm (**v2**), `apikültürsitedeneme2` tasarımını (Outfit + Hanken Grotesk tipografisi, terracotta/amber/espresso paleti) esas alır ve kurumsal kimliği birebir yansıtır.

Yayın hedefi: **https://acsezuma.github.io/apikultur-vakfi-v2/**
(apikulturvakfi.com bağlandığında güncellenecek)

## Yapı

Tek dosyalık statik bir site — derleme adımı ya da bağımlılık yok. Stil, Tailwind CDN + `tailwind.config` üzerinden marka token'larıyla (renkler, tipografi, spacing) tanımlıdır.

| Dosya | İçerik |
|---|---|
| `index.html` | Sitenin tamamı: içerik, Tailwind yapılandırması, davranış (vanilla JS) |
| `senet.html` | Vakıf senedinin tam metni (yazdırılabilir; PDF: `assets/vakif-senedi.pdf`) |
| `assets/logo-mark.svg` | Marka rozeti (bee "A"), terracotta `#B82618` — kendi sunucumuzda barınır |
| `assets/` | favicon, apple-touch-icon, og-image, senet PDF'i |
| `assets/img/` | Bölüm ve proje fotoğrafları (self-hosted) |
| `robots.txt`, `sitemap.xml` | Arama motoru dosyaları |

## Kurumsal kimlik (tasarım token'ları)

- **Renkler:** terracotta `#B82618`, amber `#EA8512`, espresso `#33261B`, ekru `#F9EFE3`, background `#fff8f5`, primary `#950602`
- **Tipografi:** Başlık/Display → **Outfit**; Gövde → **Hanken Grotesk**; Etiket/mono → **IBM Plex Mono**
- **Logo:** bee "A" rozeti + "APİKÜLTÜR / VAKFI" kelime markası (`assets/logo-mark.svg`)

> Not: Orijinal tasarımdaki geçici görsel adresleri (`lh3.googleusercontent.com/aida…`) kalıcı değildi; hepsi `assets/img/` altındaki kendi dosyalarımızla değiştirildi. Vakfın nihai saha fotoğrafları geldiğinde aynı adlarla değiştirilebilir.

## Güncelleme

1. `index.html` içindeki metni/görseli düzenleyin.
2. İlgili dala commit + push yapın. GitHub Pages (Actions) otomatik yeniden yayınlar (1-2 dk).

## Alan adı bağlanacağı zaman

1. Repo → Settings → Pages → Custom domain
2. DNS `A`/`CNAME` kayıtlarını GitHub Pages'e yönlendirin
3. `index.html` içindeki canonical / `og:url` / `og:image` + `robots.txt` + `sitemap.xml` adreslerini güncelleyin (head'de `NOT:` yorumuyla işaretli).
