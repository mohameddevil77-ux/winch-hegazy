import urllib.request
import re

url = 'https://winchawladhegazy.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    print('Fetched successfully, length:', len(html))
    title = re.findall(r'<title>(.*?)</title>', html, re.I)
    print('Title:', title)
    meta_desc = re.findall(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I)
    print('Description:', meta_desc)
    phones = set(re.findall(r'01[0125]\d{8}', html))
    print('Phones found:', phones)
    h1s = re.findall(r'<h1.*?>(.*?)</h1>', html, re.I | re.S)
    print('H1s:', [re.sub(r'<.*?>', '', h).strip() for h in h1s])
except Exception as e:
    print('Error:', e)
