import re

with open(r'D:\winch-hegazy\scripts\build_articles_engine.py', 'r', encoding='utf-8') as f:
    c = f.read()

matches = [m.start() for m in re.finditer(r'application/ld\+json', c)]
print('Matches:', matches)
for m in matches:
    print('---')
    print(c[m-50:m+250])
