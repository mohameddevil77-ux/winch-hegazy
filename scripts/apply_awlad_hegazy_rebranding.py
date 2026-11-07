# -*- coding: utf-8 -*-
import os, re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# =====================================================================
# 1. Update build_winch_helpers.py
# =====================================================================
helpers_path = os.path.join(scripts_dir, "build_winch_helpers.py")
with open(helpers_path, "r", encoding="utf-8") as f:
    h = f.read()

# Replace Domain & Location name
h = h.replace('winch-hegazy.com', 'awladhegazy.com')
h = h.replace('مركز ارتكاز ونش حجازي - كارفور العبور وجولف سيتي مول', 'مركز ارتكاز أوناش أولاد حجازي - كارفور العبور وجولف سيتي مول')
h = h.replace('نقطة تمركز ونش حجازي الرسمية (كارفور العبور)', 'نقطة تمركز أوناش أولاد حجازي الرسمية (كارفور العبور)')

# Header logo text
h = h.replace(
    '<span>ونش إنقاذ</span>\n            <span class="text-amber-400">حجازي</span>',
    '<span>أوناش إنقاذ</span>\n            <span class="text-amber-400">أولاد حجازي</span>'
)
h = h.replace('شعار ونش إنقاذ حجازي', 'شعار أوناش إنقاذ أولاد حجازي')
h = h.replace('شعار ونش حجازي', 'شعار أوناش أولاد حجازي')

# Header subtext
h = h.replace('أسرع وأرخص ونش إنقاذ سيارات في مصر', 'الأسطول الهيدروليكي المعتمد لإنقاذ وسحب السيارات في مصر')

# Meta site name
h = h.replace('<meta property="og:site_name" content="ونش إنقاذ حجازي">', '<meta property="og:site_name" content="أوناش إنقاذ أولاد حجازي">')

# Footer brand info
h = h.replace(
    'ونش إنقاذ <span class="text-amber-400">حجازي</span>',
    'أوناش إنقاذ <span class="text-amber-400">أولاد حجازي</span>'
)

# Schema LocalBusiness
h = h.replace('"name": "ونش إنقاذ حجازي - لإنقاذ السيارات 24 ساعة"', '"name": "أوناش إنقاذ أولاد حجازي - لإنقاذ السيارات 24 ساعة"')
h = h.replace(
    '"alternateName": ["Winch Hegazy", "ونش حجازي", "ونش إنقاذ سيارات مصر"]',
    '"alternateName": ["أوناش إنقاذ أولاد حجازي", "ونش إنقاذ أولاد حجازي", "أولاد حجازي", "Awlad Hegazy", "Winch Awlad Hegazy", "ونش أولاد حجازي", "أوناش أولاد حجازي"]'
)

# Video Schema
h = h.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
h = h.replace('ونش حجازي', 'أوناش أولاد حجازي')

with open(helpers_path, "w", encoding="utf-8") as f:
    f.write(h)
print("SUCCESS: Updated build_winch_helpers.py with Awlad Hegazy branding!")


# =====================================================================
# 2. Update generate_winch_hegazy_site.py
# =====================================================================
site_gen_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_gen_path, "r", encoding="utf-8") as f:
    s = f.read()

s = s.replace('winch-hegazy.com', 'awladhegazy.com')
s = s.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
s = s.replace('ونش حجازي', 'أوناش أولاد حجازي')
s = s.replace('Winch Hegazy', 'Awlad Hegazy')

with open(site_gen_path, "w", encoding="utf-8") as f:
    f.write(s)
print("SUCCESS: Updated generate_winch_hegazy_site.py with Awlad Hegazy branding!")


# =====================================================================
# 3. Update build_articles_engine.py
# =====================================================================
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    e = f.read()

e = e.replace('winch-hegazy.com', 'awladhegazy.com')
e = e.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
e = e.replace('ونش حجازي', 'أوناش أولاد حجازي')
e = e.replace('Winch Hegazy', 'Awlad Hegazy')

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(e)
print("SUCCESS: Updated build_articles_engine.py with Awlad Hegazy branding!")


# =====================================================================
# 4. Update generate_all_winch_pages.py
# =====================================================================
all_pages_path = os.path.join(scripts_dir, "generate_all_winch_pages.py")
with open(all_pages_path, "r", encoding="utf-8") as f:
    a = f.read()

a = a.replace('winch-hegazy.com', 'awladhegazy.com')
a = a.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
a = a.replace('ونش حجازي', 'أوناش أولاد حجازي')
a = a.replace('Winch Hegazy', 'Awlad Hegazy')

with open(all_pages_path, "w", encoding="utf-8") as f:
    f.write(a)
print("SUCCESS: Updated generate_all_winch_pages.py with Awlad Hegazy branding!")


# =====================================================================
# 5. Update generate_cairo_competitor_pages.py
# =====================================================================
cairo_path = os.path.join(scripts_dir, "generate_cairo_competitor_pages.py")
with open(cairo_path, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace('winch-hegazy.com', 'awladhegazy.com')
c = c.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
c = c.replace('ونش حجازي', 'أوناش أولاد حجازي')
c = c.replace('Winch Hegazy', 'Awlad Hegazy')

with open(cairo_path, "w", encoding="utf-8") as f:
    f.write(c)
print("SUCCESS: Updated generate_cairo_competitor_pages.py with Awlad Hegazy branding!")


# =====================================================================
# 6. Update expand_eastern_cities.py
# =====================================================================
east_path = os.path.join(scripts_dir, "expand_eastern_cities.py")
with open(east_path, "r", encoding="utf-8") as f:
    east = f.read()

east = east.replace('winch-hegazy.com', 'awladhegazy.com')
east = east.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
east = east.replace('ونش حجازي', 'أوناش أولاد حجازي')
east = east.replace('Winch Hegazy', 'Awlad Hegazy')

with open(east_path, "w", encoding="utf-8") as f:
    f.write(east)
print("SUCCESS: Updated expand_eastern_cities.py with Awlad Hegazy branding!")


# =====================================================================
# 7. Update create_promotional_article.py
# =====================================================================
promo_path = os.path.join(scripts_dir, "create_promotional_article.py")
with open(promo_path, "r", encoding="utf-8") as f:
    pr = f.read()

pr = pr.replace('winch-hegazy.com', 'awladhegazy.com')
pr = pr.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
pr = pr.replace('ونش حجازي', 'أوناش أولاد حجازي')
pr = pr.replace('Winch Hegazy', 'Awlad Hegazy')

with open(promo_path, "w", encoding="utf-8") as f:
    f.write(pr)
print("SUCCESS: Updated create_promotional_article.py with Awlad Hegazy branding!")


# =====================================================================
# 8. Update Backlinks and SEO Markdown Files
# =====================================================================
for root_target in [os.path.join(base_dir, "backlinks"), os.path.join(base_dir, "seo")]:
    for fname in os.listdir(root_target):
        if fname.endswith(".md") or fname.endswith(".json"):
            fp = os.path.join(root_target, fname)
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace('winch-hegazy.com', 'awladhegazy.com')
            content = content.replace('ونش إنقاذ حجازي', 'أوناش إنقاذ أولاد حجازي')
            content = content.replace('ونش حجازي', 'أوناش أولاد حجازي')
            content = content.replace('Winch Hegazy', 'Awlad Hegazy')
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"SUCCESS: Updated {fname} with Awlad Hegazy branding!")
