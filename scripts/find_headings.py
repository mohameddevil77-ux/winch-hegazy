with open(r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py", "r", encoding="utf-8") as f:
    text = f.read()

for term in ['تسعير محدد مسبقاً قبل تحرك الونش', 'نقل سيارات السوبر كار', 'هل تحتاج ونش إنقاذ بمواصفات خاصة الآن']:
    idx = text.find(term)
    if idx != -1:
        print(f"Term '{term}' found, snippet:")
        print(text[idx-40:idx+80])
        print("="*40)
