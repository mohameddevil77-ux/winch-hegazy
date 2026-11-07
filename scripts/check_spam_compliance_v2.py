# -*- coding: utf-8 -*-
with open(r'D:\winch-hegazy\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

has_visible_reviews = ('تقييمات وتجارب العملاء' in c) and ('1420 قائد سيارة' in c) and ('أحمد ممدوح' in c)
print('Visible customer reviews verified on index.html:', has_visible_reviews)

with open(r'D:\winch-hegazy\blog\winch-obour-city.html', 'r', encoding='utf-8') as f:
    b = f.read()

has_visible_faqs = 'الأسئلة الشائعة حول خدمات أوناش أولاد حجازي' in b
print('Visible FAQ section verified on blog articles:', has_visible_faqs)
