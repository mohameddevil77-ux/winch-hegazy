with open(r"D:\winch-hegazy\services.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'<link rel="canonical"[^>]*>', text)
print("Canonical in services.html:", matches)
