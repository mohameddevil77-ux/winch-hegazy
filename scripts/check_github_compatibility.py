import glob
import os
import re

base_dir = r"D:\winch-hegazy"
files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "blog", "*.html"))
pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')

print("Testing exact case sensitivity for Linux / GitHub Pages...")
mismatches = []
total_checked = 0

for f in files:
    rel_html = os.path.relpath(f, base_dir)
    fdir = os.path.dirname(f)
    with open(f, "r", encoding="utf-8") as fl:
        matches = pattern.findall(fl.read())
    
    for m in matches:
        if m.startswith("http") or m.startswith("data:"):
            continue
        total_checked += 1
        target_norm = os.path.normpath(os.path.join(fdir, m))
        parent = os.path.dirname(target_norm)
        fname = os.path.basename(target_norm)
        
        if os.path.exists(parent):
            actual_files = os.listdir(parent)
            if fname not in actual_files:
                matching = [af for af in actual_files if af.lower() == fname.lower()]
                mismatches.append((rel_html, m, fname, matching))

print(f"Total checked: {total_checked}")
print(f"Total case mismatches: {len(mismatches)}")
for item in mismatches:
    print(f"MISMATCH in {item[0]}: requested '{item[1]}' but disk has: {item[3]}")

# 1. Create .nojekyll in D:\winch-hegazy\
nojekyll_path = os.path.join(base_dir, ".nojekyll")
with open(nojekyll_path, "w", encoding="utf-8") as f:
    f.write("")
print("SUCCESS: Created .nojekyll file for GitHub Pages")

# 2. Create .gitignore in D:\winch-hegazy\
gitignore_path = os.path.join(base_dir, ".gitignore")
with open(gitignore_path, "w", encoding="utf-8") as f:
    f.write("""__pycache__/
*.py[cod]
*$py.class
*.log
winch-hegazy-complete.zip
""")
print("SUCCESS: Created .gitignore file")
