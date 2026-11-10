import urllib.request

url = "http://winchawladhegazy.com/services.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode("utf-8")

import re
matches = re.findall(r'<link rel="canonical"[^>]*>', html)
print("Live Canonical in services.html:", matches)
