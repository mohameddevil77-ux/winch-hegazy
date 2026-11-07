with open(r"D:\winch-hegazy\index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("1. Has hero_rescue_mobile.webp preload:", "hero_rescue_mobile.webp" in html)
print("2. Has <picture> with fetchpriority='high':", "fetchpriority=\"high\"" in html and "<picture" in html)
print("3. Has 750 in pricing / hero:", "750" in html)
print("4. Any remaining '600 جنيه' or '600 ج.م':", ("600 جنيه" in html) or ("600 ج.م" in html) or ("600 -" in html))
print("5. calcPrice default in calculator:", "750 - 950 ج.م" in html)
print("6. Schema priceRange:", "750" in html and "3500" in html)
