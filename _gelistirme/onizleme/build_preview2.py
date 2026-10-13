#!/usr/bin/env python3
"""index.html'den çevrimdışı, birebir stilli önizleme üretir (Play CDN yerine derlenmiş Tailwind v3)."""
import re, subprocess, os, sys
SCR = os.environ.get("ONIZLEME_CALISMA", os.path.join(os.path.dirname(os.path.abspath(__file__)), "calisma"))  # tw/ (npm) ve fonts/ burada
TW = f"{SCR}/tw"; FN = f"{SCR}/fonts"; REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGES=["index.html","gelecek.html","faaliyet.html","vakif.html","genclik.html","akademi.html","projeler.html","yonetim.html","en/index.html","en/future.html","en/about.html","en/areas-of-work.html","en/youth.html","en/academy.html","en/projects.html","en/governance.html"]
src = open(f"{REPO}/index.html", encoding="utf-8").read()

cfg = re.search(r'tailwind\.config\s*=\s*(\{.*?\})\s*</script>', src, re.S).group(1)
open(f"{TW}/tailwind.config.js","w").write(
    "module.exports = Object.assign(" + cfg + ", {content:['" + f"{TW}/preview*.html" + "'],"
    " plugins:[require('@tailwindcss/forms'),require('@tailwindcss/container-queries')]});\n")
open(f"{TW}/in.css","w").write("@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")

def ff(fam, path, w):
    return f"@font-face{{font-family:'{fam}';src:url('file://{path}') format('woff2');font-weight:{w};font-style:normal}}\n"
faces = ""
FONTCSS = ""
for pkg,ws in (("outfit",(400,500,600,700)),("hanken-grotesk",(400,500,600,700)),("ibm-plex-mono",(500,))):
    for w in ws:
        FONTCSS += f'<link rel="stylesheet" href="file://{FN}/fontsource-{pkg}-5.3.0/{w}.css">'

for w in ():
    p = f"{FN}/fontsource-outfit-5.3.0/files/outfit-latin-ext-{w}-normal.woff2"
    if os.path.exists(p): faces += ff("Outfit", p, w)
for w in ():
    p = f"{FN}/fontsource-hanken-grotesk-5.3.0/files/hanken-grotesk-latin-ext-{w}-normal.woff2"
    if os.path.exists(p): faces += ff("Hanken Grotesk", p, w)
0 and ff("IBM Plex Mono", f"{FN}/fontsource-ibm-plex-mono-5.3.0/files/ibm-plex-mono-latin-ext-500-normal.woff2", 500)
faces += (f"@font-face{{font-family:'Material Symbols Outlined';src:url('file://{TW}/node_modules/material-symbols/material-symbols-outlined.woff2') format('woff2');font-weight:100 700}}\n"
          ".material-symbols-outlined{font-family:'Material Symbols Outlined';font-weight:normal;font-style:normal;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';font-feature-settings:'liga'}\n"
          ".reveal-on-scroll{opacity:1!important;transform:none!important}\n")

for pg in PAGES:
    p = open(f"{REPO}/{pg}", encoding="utf-8").read()
    p = re.sub(r'<script src="https://cdn\.tailwindcss\.com[^"]*"></script>', f'<link rel="stylesheet" href="file://{TW}/tw.css">', p)
    p = re.sub(r'<script id="tailwind-config">.*?</script>', '', p, flags=re.S)
    p = re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^>]*>', FONTCSS + f'<style>{faces}</style>', p)
    p = p.replace('<head>', f'<head><base href="file://{REPO}/{os.path.dirname(pg)+"/" if "/" in pg else ""}">', 1)
    open(f"{TW}/preview-"+pg.split(".")[0].replace("/","-")+".html","w",encoding="utf-8").write(p)
    
r = subprocess.run([f"{TW}/node_modules/.bin/tailwindcss","-c",f"{TW}/tailwind.config.js","-i",f"{TW}/in.css","-o",f"{TW}/tw.css"],
                   capture_output=True, text=True, cwd=TW)
print(r.stderr.strip()[-400:])
print("tw.css boyut:", os.path.getsize(f"{TW}/tw.css"))
