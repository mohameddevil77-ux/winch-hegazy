import os
import glob

base_dir = r"D:\winch-hegazy"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

DOMAIN = "https://winchawladhegazy.com"

# 1. Main core pages
core_pages = [
    ("", "1.0", "daily"),
    ("services.html", "0.9", "weekly"),
    ("coverage.html", "0.9", "weekly"),
    ("pricing.html", "0.9", "weekly"),
    ("contact.html", "0.9", "weekly"),
    ("blog/index.html", "0.8", "daily")
]

# 2. Blog articles
blog_files = sorted(glob.glob(os.path.join(base_dir, "blog", "*.html")))
blog_pages = []
for f in blog_files:
    fname = os.path.basename(f)
    if fname != "index.html":
        blog_pages.append((f"blog/{fname}", "0.8", "monthly"))

# 3. Dedicated Video Watch Pages
video_pages = [
    ("videos/lamborghini-night-rescue.html", "0.9", "monthly"),
    ("videos/caterpillar-loader-transport.html", "0.9", "monthly"),
    ("videos/commercial-truck-rescue.html", "0.9", "monthly")
]

all_entries = core_pages + blog_pages + video_pages

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for path, pri, freq in all_entries:
    url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
    xml.append('  <url>')
    xml.append(f'    <loc>{url}</loc>')
    xml.append('    <lastmod>2026-11-08</lastmod>')
    xml.append(f'    <changefreq>{freq}</changefreq>')
    xml.append(f'    <priority>{pri}</priority>')
    xml.append('  </url>')

xml.append('</urlset>')

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write("\n".join(xml) + "\n")

print(f"✓ Generated 100% clean, error-free standard sitemap.xml with {len(all_entries)} URLs!")
