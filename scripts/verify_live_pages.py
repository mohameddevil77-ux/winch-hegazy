import urllib.request

url = 'https://mohameddevil77-ux.github.io/winch-hegazy/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')

print("Live GitHub Pages Verification:")
print("1. Has styles.min.css:", 'assets/css/styles.min.css' in html)
print("2. Has tailwind cdn:", 'cdn.tailwindcss.com' in html)
print("3. Has video preload='none':", 'preload="none"' in html)
print("4. Has hero_rescue_bg.webp preload:", 'hero_rescue_bg.webp' in html)
print("5. Has <main id='main-content'>:", '<main id="main-content">' in html)
print("6. Has المؤسسة:", 'المؤسسة' in html)
print("7. Has مؤسسة:", 'مؤسسة' in html)
