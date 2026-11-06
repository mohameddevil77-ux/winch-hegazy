import os
import re

scratch_dir = r"D:\winch-hegazy\scripts"
site_dir = r"D:\winch-hegazy"

NEW_PRIMARY = "01032194206"
NEW_SECONDARY = "01283038303"

# Replacement maps
replacements = [
    ("01032447299", NEW_PRIMARY),
    ("01141729347", NEW_SECONDARY),
    ("01098174992", NEW_SECONDARY),
    ("+201032447299", f"+20{NEW_PRIMARY[1:]}"),
    ("+201141729347", f"+20{NEW_SECONDARY[1:]}"),
    ("+201098174992", f"+20{NEW_SECONDARY[1:]}"),
    ("201032447299", f"20{NEW_PRIMARY[1:]}"),
    ("201141729347", f"20{NEW_SECONDARY[1:]}"),
    ("201098174992", f"20{NEW_SECONDARY[1:]}"),
]

# Update scratch python files
for fname in ["build_winch_helpers.py", "build_articles_engine.py", "generate_cairo_competitor_pages.py", "generate_all_winch_pages.py", "generate_winch_hegazy_site.py"]:
    fpath = os.path.join(scratch_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        for old, new in replacements:
            content = content.replace(old, new)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated python file: {fname}")

print("SUCCESS: Scratch generator files updated with new phone numbers!")
