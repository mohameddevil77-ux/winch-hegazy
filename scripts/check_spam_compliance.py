# -*- coding: utf-8 -*-
import re

with open(r'D:\winch-hegazy\blog\winch-obour-city.html', 'r', encoding='utf-8') as f:
    c = f.read()

schema_faq = re.findall(r'"@type":\s*"Question"', c)
print('FAQ questions in schema:', len(schema_faq))

body_content = c[c.find('<body'):]
q_text = "ما هي تكلفة طلب ونش إنقاذ سيارات في"
print('Is FAQ question text present in visible HTML body?', q_text in body_content)

# Check customer reviews in index.html
with open(r'D:\winch-hegazy\index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

print('Has aggregateRating in schema:', 'aggregateRating' in idx_content)
print('Has visible testimonials/reviews section in index:', 'آراء العملاء' in idx_content or 'تقييمات العملاء' in idx_content)
