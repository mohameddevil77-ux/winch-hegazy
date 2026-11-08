with open(r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('id="videos"')
print(text[idx:idx+900])
