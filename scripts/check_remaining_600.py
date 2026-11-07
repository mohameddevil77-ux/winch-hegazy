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

remaining = []
for s in active_scripts:
    with open(s, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if "600" in line and not any(k in line for k in ["font-600", "wght@600", "rescue-600", "safety-600", "emerald-600", "amber-600", "duration-600"]):
            remaining.append((s.split('\\')[-1], idx+1, line.strip()))

if remaining:
    print(f"Found {len(remaining)} remaining 600 occurrences:")
    for r in remaining:
        print(f"  {r[0]}:{r[1]}: {r[2]}")
else:
    print("SUCCESS: 0 price references to 600 remaining! All are updated to 750!")
