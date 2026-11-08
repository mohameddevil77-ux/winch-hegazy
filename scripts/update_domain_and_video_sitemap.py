import os

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

active_scripts = [
    os.path.join(scripts_dir, "build_winch_helpers.py"),
    os.path.join(scripts_dir, "generate_winch_hegazy_site.py"),
    os.path.join(scripts_dir, "build_articles_engine.py"),
    os.path.join(scripts_dir, "generate_all_winch_pages.py"),
    os.path.join(scripts_dir, "generate_cairo_competitor_pages.py"),
    os.path.join(scripts_dir, "expand_eastern_cities.py"),
    os.path.join(scripts_dir, "create_promotional_article.py")
]

# 1. Replace winchawladhegazy.com with winchawladhegazy.com
for s in active_scripts:
    with open(s, "r", encoding="utf-8") as f:
        text = f.read()
    
    if "winchawladhegazy.com" in text:
        text = text.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        text = text.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")
        text = text.replace("winchawladhegazy.com", "winchawladhegazy.com")
        with open(s, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✓ Updated domain in {os.path.basename(s)}")

# 2. Add watch page links to video cards in generate_winch_hegazy_site.py
site_script = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_script, "r", encoding="utf-8") as f:
    site_code = f.read()

v1_target = '<span>تأمين شامل 100%</span>\n          </div>\n        </div>'
v1_repl = '''<span>تأمين شامل 100%</span>
          </div>
          <a href="videos/lamborghini-night-rescue.html" class="mt-2 block w-full py-2 text-center text-xs font-black text-amber-300 bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 rounded-xl transition">
            🎬 صفحة مشاهدة الفيديو والتقرير الفني الكامل ←
          </a>
        </div>'''
if v1_target in site_code:
    site_code = site_code.replace(v1_target, v1_repl)
    print("✓ Added Watch Page link for Video 1")

v2_target = '<span>تثبيت بجنازير صلب</span>\n          </div>\n        </div>'
v2_repl = '''<span>تثبيت بجنازير صلب</span>
          </div>
          <a href="videos/caterpillar-loader-transport.html" class="mt-2 block w-full py-2 text-center text-xs font-black text-amber-300 bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 rounded-xl transition">
            🎬 صفحة مشاهدة الفيديو والتقرير الفني الكامل ←
          </a>
        </div>'''
if v2_target in site_code:
    site_code = site_code.replace(v2_target, v2_repl)
    print("✓ Added Watch Page link for Video 2")

v3_target = '<span>إضاءات ليلية تحذيرية</span>\n          </div>\n        </div>'
v3_repl = '''<span>إضاءات ليلية تحذيرية</span>
          </div>
          <a href="videos/commercial-truck-rescue.html" class="mt-2 block w-full py-2 text-center text-xs font-black text-amber-300 bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 rounded-xl transition">
            🎬 صفحة مشاهدة الفيديو والتقرير الفني الكامل ←
          </a>
        </div>'''
if v3_target in site_code:
    site_code = site_code.replace(v3_target, v3_repl)
    print("✓ Added Watch Page link for Video 3")

with open(site_script, "w", encoding="utf-8") as f:
    f.write(site_code)

# 3. Update sitemap directly in generate_all_winch_pages.py
pages_script = os.path.join(scripts_dir, "generate_all_winch_pages.py")
with open(pages_script, "r", encoding="utf-8") as f:
    pages_code = f.read()

# Make sure all_urls in generate_all_winch_pages has winchawladhegazy.com
pages_code = pages_code.replace("https://winchawladhegazy.com", "https://winchawladhegazy.com")

with open(pages_script, "w", encoding="utf-8") as f:
    f.write(pages_code)

print("Updated domain in scripts successfully!")
