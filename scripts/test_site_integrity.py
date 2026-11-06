import glob
import os
import re

base_dir = r"D:\winch-hegazy"
files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "blog", "*.html"))
img_regex = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')

missing = []
total = 0
for f in files:
    d = os.path.dirname(f)
    with open(f, "r", encoding="utf-8") as fl:
        srcs = img_regex.findall(fl.read())
        for s in srcs:
            total += 1
            if s.startswith("http"):
                continue
            full = os.path.normpath(os.path.join(d, s))
            if not os.path.exists(full):
                missing.append((f, s, full))

print(f"Total images checked: {total}")
print(f"Missing images: {len(missing)}")
if missing:
    for m in missing[:5]:
        print("MISSING:", m)
else:
    print("ALL IMAGES EXIST AND RESOLVE PERFECTLY ON D: DRIVE!")
