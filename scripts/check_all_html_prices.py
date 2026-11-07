import glob, re

files = glob.glob(r"D:\winch-hegazy\**\*.html", recursive=True)
flagged = []
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    for idx, l in enumerate(lines):
        if re.search(r'(?:سعر|يبدأ|تبدأ|تكلفة|رسوم|جنيه|ج\.م|EGP)\s*.*?\b600\b', l) or re.search(r'\b600\b\s*(?:جنيه|ج\.م|EGP)', l):
            flagged.append((f.replace("D:\\winch-hegazy\\", ""), idx+1, l.strip()))

if flagged:
    print(f"Found {len(flagged)} price references to 600:")
    for fl in flagged:
        print(f"  {fl[0]}:{fl[1]}: {fl[2]}")
else:
    print("SUCCESS: Zero price references to 600 in all HTML files across the entire site!")
