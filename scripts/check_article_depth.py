# -*- coding: utf-8 -*-
import os, re

base_dir = r"D:\winch-hegazy\blog"
articles = [f for f in os.listdir(base_dir) if f.endswith('.html') and f != 'index.html']

print(f"Total articles to audit: {len(articles)}")
for a in articles:
    fp = os.path.join(base_dir, a)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Extract visible text from article body
    body = c[c.find('<article'):c.find('</article>')]
    clean_text = re.sub(r'<.*?>', ' ', body)
    words = clean_text.split()
    print(f"- {a}: {len(words)} words in article body")
