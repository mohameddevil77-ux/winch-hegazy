import glob
import os
import re

base_dir = r"D:\winch-hegazy"

files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)

fixed_count = 0
for f in files:
    if f.endswith(('.html', '.xml', '.txt', '.py', '.json', '.js', '.md')):
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        
        orig = content
        # Fix any multiple winch prefixes like winchawladhegazy.com
        content = re.sub(r'https?://(?:winch)+awladhegazy\.com', 'https://winchawladhegazy.com', content)
        content = re.sub(r'(?:winch)+awladhegazy\.com', 'winchawladhegazy.com', content)
        # Any remaining bare winchawladhegazy.com (not preceded by winch)
        content = re.sub(r'(?<!winch)awladhegazy\.com', 'winchawladhegazy.com', content)
        
        if content != orig:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(content)
            fixed_count += 1
            print(f"✓ Fixed: {os.path.relpath(f, base_dir)}")

print(f"\nTotal files cleaned and fixed: {fixed_count}")
