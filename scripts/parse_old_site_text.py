import re

with open(r'D:\winch-hegazy\scripts\fetch_old_site.py', 'r', encoding='utf-8') as f:
    pass

import urllib.request
req = urllib.request.Request('https://awladhegazy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Extract clean text from paragraphs
paragraphs = re.findall(r'<p.*?>(.*?)</p>', html, re.I | re.S)
for p in paragraphs[:15]:
    clean = re.sub(r'<.*?>', '', p).strip()
    if clean:
        print('-', clean[:150])
