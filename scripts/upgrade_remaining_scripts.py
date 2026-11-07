import re

scripts = [
    r"D:\winch-hegazy\scripts\generate_cairo_competitor_pages.py",
    r"D:\winch-hegazy\scripts\expand_eastern_cities.py",
    r"D:\winch-hegazy\scripts\create_promotional_article.py"
]

gallery_imgs = [
    "hegazy_lamborghini_night", "hegazy_caterpillar_loader", "hegazy_heavy_equipment_loader",
    "hegazy_red_truck_branding", "hegazy_orange_truck_porsche", "hegazy_luxury_car_flatbed",
    "hegazy_semi_truck_head", "hegazy_caravan_transport", "hegazy_golf_carts_transport",
    "hegazy_food_truck_transport", "hegazy_red_truck_heavy", "hegazy_night_commercial_pickup",
    "hero_rescue_bg", "og_banner"
]

for s in scripts:
    with open(s, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Add <main id="main-content"> if not present
    text = re.sub(
        r'(\{get_header\([^)]*\)\})(?!\s*<main id="main-content">)',
        r'\1\n\n  <main id="main-content">',
        text
    )
    
    # Close </main> before get_footer
    text = re.sub(
        r'(?<!</main>\n\n)(\{get_footer\([^)]*\)\})',
        r'  </main>\n\n\1',
        text
    )
    
    for img in gallery_imgs:
        text = text.replace(f"{img}.jpg", f"{img}.webp")
        
    with open(s, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✓ Upgraded {s.split('\\')[-1]}")
