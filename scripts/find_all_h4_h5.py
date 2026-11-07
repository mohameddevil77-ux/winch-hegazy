with open(r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'<h[45][^>]*>[^<]*</h[45]>', text)
for m in matches:
    print(m)
