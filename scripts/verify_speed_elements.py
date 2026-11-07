with open(r"D:\winch-hegazy\index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("Has <main id=\"main-content\">:", '<main id="main-content">' in text)
print("Has </main>:", '</main>' in text)
print("Has hero_rescue_bg.webp preload:", 'rel="preload" as="image" href="assets/images/hero_rescue_bg.webp"' in text)
print("Has styles.min.css:", 'href="assets/css/styles.min.css"' in text)
print("Has tailwind cdn:", 'cdn.tailwindcss.com' in text)
