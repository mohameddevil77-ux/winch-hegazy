import urllib.request

url = 'https://winchawladhegazy.com/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8')
    print("winchawladhegazy.com verification:")
    print("1. Has styles.min.css:", 'assets/css/styles.min.css' in html)
    print("2. Has video preload='none':", 'preload="none"' in html)
    print("3. Has hero_rescue_bg.webp:", 'hero_rescue_bg.webp' in html)
except Exception as e:
    print("Custom domain check error:", e)
