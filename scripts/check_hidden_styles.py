# -*- coding: utf-8 -*-
import os, glob, re

base_dir = r"D:\winch-hegazy"
html_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith('.html')]
html_files += [os.path.join(base_dir, 'blog', f) for f in os.listdir(os.path.join(base_dir, 'blog')) if f.endswith('.html')]

print(f"Checking {len(html_files)} files for hidden text or spammy patterns...")

hidden_text_found = []
for fp in html_files:
    rel = os.path.relpath(fp, base_dir)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Check for display:none or visibility:hidden in style attributes
    styles_none = re.findall(r'style=["\'][^"\']*(?:display:\s*none|visibility:\s*hidden|font-size:\s*0|opacity:\s*0)[^"\']*["\']', c, re.I)
    if styles_none:
        hidden_text_found.append((rel, styles_none))
        
print(f"Suspicious hidden style attributes found: {len(hidden_text_found)}")
for r, s in hidden_text_found:
    print(f" - {r}: {s}")
