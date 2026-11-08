import glob
import os

base_dir = r"D:\winch-hegazy"

# 1. Update all HTML files
html_files = glob.glob(os.path.join(base_dir, "**", "*.html"), recursive=True)
updated_html = 0
for f in html_files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    if "winchawladhegazy.com" in content:
        content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        content = content.replace("winchawladhegazy.com", "winchawladhegazy.com")
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(content)
        updated_html += 1

print(f"✓ Updated {updated_html} HTML files with https://winchawladhegazy.com")

# 2. Update all Python scripts
py_files = glob.glob(os.path.join(base_dir, "scripts", "*.py"))
updated_py = 0
for f in py_files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    if "winchawladhegazy.com" in content:
        content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        content = content.replace("winchawladhegazy.com", "winchawladhegazy.com")
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(content)
        updated_py += 1

print(f"✓ Updated {updated_py} Python scripts with https://winchawladhegazy.com")

# 3. Update llms.txt, llms-full.txt, robots.txt, sitemap.xml
for txt_name in ["llms.txt", "llms-full.txt", "robots.txt", "sitemap.xml"]:
    txt_path = os.path.join(base_dir, txt_name)
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as fp:
            content = fp.read()
        if "winchawladhegazy.com" in content:
            content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
            content = content.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
            content = content.replace("winchawladhegazy.com", "winchawladhegazy.com")
            with open(txt_path, "w", encoding="utf-8") as fp:
                fp.write(content)
            print(f"✓ Updated {txt_name} with https://winchawladhegazy.com")
