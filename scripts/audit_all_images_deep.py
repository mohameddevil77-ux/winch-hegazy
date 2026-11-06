import glob
import os
import re

base_dir = r"D:\winch-hegazy"
files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "blog", "*.html"))
pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')

print("Auditing all HTML files for image references...")
total = 0
broken = []
details = []

for f in files:
    rel = os.path.relpath(f, base_dir)
    fdir = os.path.dirname(f)
    with open(f, "r", encoding="utf-8") as fl:
        content = fl.read()
    
    matches = pattern.findall(content)
    for m in matches:
        total += 1
        if m.startswith("http") or m.startswith("data:"):
            continue
        # Check actual target
        resolved = os.path.normpath(os.path.join(fdir, m))
        exists = os.path.exists(resolved)
        details.append((rel, m, exists, resolved))
        if not exists:
            broken.append((rel, m, resolved))

print(f"Total images checked: {total}")
print(f"Broken count: {len(broken)}")
for b in broken[:10]:
    print(f"BROKEN: File {b[0]} -> src='{b[1]}' (looking at {b[2]})")

# Also check CSS background-image
bg_pattern = re.compile(r'url\(["\']?([^"\')]+)["\']?\)')
broken_bg = []
for f in files:
    rel = os.path.relpath(f, base_dir)
    fdir = os.path.dirname(f)
    with open(f, "r", encoding="utf-8") as fl:
        content = fl.read()
    for m in bg_pattern.findall(content):
        if m.startswith("http") or m.startswith("data:") or m.startswith("#"):
            continue
        resolved = os.path.normpath(os.path.join(fdir, m))
        if not os.path.exists(resolved):
            broken_bg.append((rel, m, resolved))

print(f"Broken background images: {len(broken_bg)}")
for b in broken_bg[:10]:
    print(f"BROKEN BG: File {b[0]} -> url('{b[1]}') (looking at {b[2]})")
