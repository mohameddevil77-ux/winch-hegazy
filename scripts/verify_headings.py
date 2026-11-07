import re

with open(r"D:\winch-hegazy\index.html", "r", encoding="utf-8") as f:
    text = f.read()

headings = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', text, re.DOTALL)
prev_level = 0
skipped = 0
for tag, content in headings:
    level = int(tag[1])
    clean = re.sub(r'<[^>]+>', '', content).strip()
    if level > prev_level + 1 and prev_level != 0:
        print(f"WARNING: Skipped level from h{prev_level} to h{level} for: '{clean[:40]}'")
        skipped += 1
    prev_level = level

if skipped == 0:
    print("SUCCESS: Perfect heading hierarchy! Zero skipped heading levels!")
else:
    print(f"Found {skipped} skipped heading levels.")
