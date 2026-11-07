import re

# 1. Upgrade build_articles_engine.py
path_engine = r"D:\winch-hegazy\scripts\build_articles_engine.py"
with open(path_engine, "r", encoding="utf-8") as f:
    text = f.read()

# Add <main id="main-content"> after get_header calls if not already wrapped
for page_type in ['"services"', '"coverage"', '"pricing"', '"blog", is_blog=True']:
    old_call = f"{{get_header({page_type})}}"
    if f"{{get_header({page_type})}}\n\n  <main id=\"main-content\">" not in text:
        text = text.replace(old_call, f"{{get_header({page_type})}}\n\n  <main id=\"main-content\">")

# Close </main> before get_footer
text = re.sub(
    r'(?<!</main>\n\n)(\{get_footer\([^)]*\)\})',
    r'  </main>\n\n\1',
    text
)

# Convert image links to webp and add lazy loading
gallery_imgs = [
    "hegazy_lamborghini_night", "hegazy_caterpillar_loader", "hegazy_heavy_equipment_loader",
    "hegazy_red_truck_branding", "hegazy_orange_truck_porsche", "hegazy_luxury_car_flatbed",
    "hegazy_semi_truck_head", "hegazy_caravan_transport", "hegazy_golf_carts_transport",
    "hegazy_food_truck_transport", "hegazy_red_truck_heavy", "hegazy_night_commercial_pickup",
    "hero_rescue_bg", "og_banner"
]
for img in gallery_imgs:
    text = text.replace(f"{img}.jpg", f"{img}.webp")

with open(path_engine, "w", encoding="utf-8") as f:
    f.write(text)
print("✓ Upgraded build_articles_engine.py")

# 2. Upgrade generate_all_winch_pages.py
path_pages = r"D:\winch-hegazy\scripts\generate_all_winch_pages.py"
with open(path_pages, "r", encoding="utf-8") as f:
    text = f.read()

if '{get_header("contact")}\n\n  <main id="main-content">' not in text:
    text = text.replace('{get_header("contact")}', '{get_header("contact")}\n\n  <main id="main-content">')

text = re.sub(
    r'(?<!</main>\n\n)(\{get_footer\([^)]*\)\})',
    r'  </main>\n\n\1',
    text
)

for img in gallery_imgs:
    text = text.replace(f"{img}.jpg", f"{img}.webp")

with open(path_pages, "w", encoding="utf-8") as f:
    f.write(text)
print("✓ Upgraded generate_all_winch_pages.py")
