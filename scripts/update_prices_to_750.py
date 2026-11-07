import re

active_scripts = [
    r"D:\winch-hegazy\scripts\build_winch_helpers.py",
    r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py",
    r"D:\winch-hegazy\scripts\build_articles_engine.py",
    r"D:\winch-hegazy\scripts\generate_all_winch_pages.py",
    r"D:\winch-hegazy\scripts\generate_cairo_competitor_pages.py",
    r"D:\winch-hegazy\scripts\expand_eastern_cities.py",
    r"D:\winch-hegazy\scripts\create_promotional_article.py"
]

# Patterns to replace:
# 600 جنيه -> 750 جنيه
# 600 ج.م -> 750 ج.م
# EGP 600 -> EGP 750
# 600 - 750 -> 750 - 950
# 600 إلى -> 750 إلى
# "minPrice": "600" -> "minPrice": "750"
# "price": "600" -> "price": "750"

replacements = [
    ("600 - 750 ج.م", "750 - 950 ج.م"),
    ("600 - 750", "750 - 950"),
    ("600 إلى 850", "750 إلى 1000"),
    ("600 إلى 750", "750 إلى 950"),
    ("600 ج.م", "750 ج.م"),
    ("600 جنيه", "750 جنيه"),
    ("EGP 600", "EGP 750"),
    ('"minPrice": "600"', '"minPrice": "750"'),
    ('"price": "600"', '"price": "750"'),
    ('"price": 600', '"price": 750'),
    ("سعر 600", "سعر 750"),
    ("من 600", "من 750"),
    ("تبدأ من 600", "تبدأ من 750"),
    ("يبدأ من 600", "يبدأ من 750")
]

for s in active_scripts:
    with open(s, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    for old, new in replacements:
        text = text.replace(old, new)
        
    if text != orig:
        with open(s, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✓ Updated prices in {s.split('\\')[-1]}")
    else:
        print(f"- No price replacements needed in {s.split('\\')[-1]}")
