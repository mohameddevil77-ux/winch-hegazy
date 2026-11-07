with open(r"D:\winch-hegazy\scripts\generate_all_winch_pages.py", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('get_header("contact")')
if idx != -1:
    print(text[idx-50:idx+350])
