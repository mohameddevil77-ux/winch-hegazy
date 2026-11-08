import os
import glob

base_dir = r"D:\winch-hegazy"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

DOMAIN = "https://winchawladhegazy.com"

# Standard pages
main_pages = [
    ("", "1.0", "daily"),
    ("services.html", "0.9", "weekly"),
    ("coverage.html", "0.9", "weekly"),
    ("pricing.html", "0.9", "weekly"),
    ("contact.html", "0.9", "weekly"),
    ("blog/index.html", "0.8", "daily")
]

# Blog articles
blog_files = glob.glob(os.path.join(base_dir, "blog", "*.html"))
blog_pages = []
for f in blog_files:
    fname = os.path.basename(f)
    if fname != "index.html":
        blog_pages.append((f"blog/{fname}", "0.8", "monthly"))

# Video watch pages with full Google Video Sitemap metadata
videos = [
    {
        "loc": f"{DOMAIN}/videos/lamborghini-night-rescue.html",
        "title": "توثيق بالفيديو: سحب ونقل سيارة سوبر كار لامبورجيني ليلاً - أوناش أولاد حجازي",
        "desc": "شاهد توثيقاً بالفيديو لعملية سحب ونقل سيارة سوبر كار خارقة (لامبورجيني هوراكان) ليلاً في القاهرة بأحدث أوناش هيدروليكية مغلقة مع حماية الصدام الرياضي وأربطة العجلات المطاطية من أوناش أولاد حجازي.",
        "thumbnail": f"{DOMAIN}/assets/images/poster_lamborghini_night.webp",
        "content_loc": f"{DOMAIN}/assets/videos/hegazy_lamborghini_vip_night.mp4",
        "player_loc": f"{DOMAIN}/videos/lamborghini-night-rescue.html",
        "duration": "45",
        "pub_date": "2026-11-06T20:00:00+02:00"
    },
    {
        "loc": f"{DOMAIN}/videos/caterpillar-loader-transport.html",
        "title": "توثيق بالفيديو: تحميل ونقل لودر كاتربيلر CAT 930 للمشروعات - أوناش أولاد حجازي",
        "desc": "فيديو يوضح قدرة الطبلية الهيدروليكية لأوناش أولاد حجازي على سحب وتحميل اللوادر والمعدات الهندسية الثقيلة مثل لودر كاتربيلر CAT 930 وتأمينها بجنازير صلب متوافقة مع معايير السلامة.",
        "thumbnail": f"{DOMAIN}/assets/images/poster_caterpillar_loader.webp",
        "content_loc": f"{DOMAIN}/assets/videos/hegazy_caterpillar_loader_day.mp4",
        "player_loc": f"{DOMAIN}/videos/caterpillar-loader-transport.html",
        "duration": "35",
        "pub_date": "2026-11-06T20:30:00+02:00"
    },
    {
        "loc": f"{DOMAIN}/videos/commercial-truck-rescue.html",
        "title": "توثيق بالفيديو: إنقاذ ونقل سيارة نقل تجاري بحمولتها ليلاً - أوناش أولاد حجازي",
        "desc": "توثيق ميداني لعملية سحب وتأمين شاحنة نقل تجاري محملة بالبضائع ليلاً على الطريق السريع بأحدث أوناش أولاد حجازي مع إضاءات تحذيرية دون الحاجة لتفريغ الحمولة.",
        "thumbnail": f"{DOMAIN}/assets/images/poster_commercial_pickup.webp",
        "content_loc": f"{DOMAIN}/assets/videos/hegazy_commercial_pickup_night.mp4",
        "player_loc": f"{DOMAIN}/videos/commercial-truck-rescue.html",
        "duration": "40",
        "pub_date": "2026-11-06T21:00:00+02:00"
    }
]

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
xml.append('        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">')

# Main and blog pages
for path, pri, freq in main_pages + blog_pages:
    url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
    xml.append('  <url>')
    xml.append(f'    <loc>{url}</loc>')
    xml.append('    <lastmod>2026-11-08</lastmod>')
    xml.append(f'    <changefreq>{freq}</changefreq>')
    xml.append(f'    <priority>{pri}</priority>')
    xml.append('  </url>')

# Video Watch Pages
for v in videos:
    xml.append('  <url>')
    xml.append(f'    <loc>{v["loc"]}</loc>')
    xml.append('    <lastmod>2026-11-08</lastmod>')
    xml.append('    <changefreq>monthly</changefreq>')
    xml.append('    <priority>0.9</priority>')
    xml.append('    <video:video>')
    xml.append(f'      <video:thumbnail_loc>{v["thumbnail"]}</video:thumbnail_loc>')
    xml.append(f'      <video:title>{v["title"]}</video:title>')
    xml.append(f'      <video:description>{v["desc"]}</video:description>')
    xml.append(f'      <video:content_loc>{v["content_loc"]}</video:content_loc>')
    xml.append(f'      <video:player_loc>{v["player_loc"]}</video:player_loc>')
    xml.append(f'      <video:duration>{v["duration"]}</video:duration>')
    xml.append(f'      <video:publication_date>{v["pub_date"]}</video:publication_date>')
    xml.append('      <video:family_friendly>yes</video:family_friendly>')
    xml.append('    </video:video>')
    xml.append('  </url>')

xml.append('</urlset>')

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write("\n".join(xml) + "\n")

print(f"✓ Generated complete sitemap.xml with {len(main_pages) + len(blog_pages) + len(videos)} URLs (including 3 Google Video Watch Pages)!")
