import os
import re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

image_map = {
    # Eastern hubs
    "winch-obour-city": "hegazy_red_truck_branding.jpg",
    "winch-shorouk-badr": "hegazy_caravan_transport.jpg",
    "winch-new-capital": "hegazy_cupra_rear.jpg",
    "winch-salam-herfeyein-nahda": "hegazy_semi_truck_head.jpg",
    
    # Cairo competitor districts
    "winch-enqaz-cairo": "hegazy_red_truck_heavy.jpg",
    "winch-nasr-city": "hegazy_orange_truck_porsche.jpg",
    "winch-heliopolis-masr-gedida": "hegazy_porsche_highway_rear.jpg",
    "winch-maadi": "hegazy_luxury_car_flatbed.jpg",
    "winch-downtown-cairo": "hegazy_luxury_car_flatbed.jpg",
    "winch-mokattam": "hegazy_red_truck_branding.jpg",
    "winch-shobra": "hegazy_semi_truck_head.jpg",
    "winch-rehab-madinaty": "hegazy_golf_carts_transport.jpg",
    "winch-giza-haram": "hegazy_food_truck_transport.jpg",
    
    # Core articles
    "agrab-winch-qarib-meni": "hegazy_red_truck_branding.jpg",
    "ar5as-winch-enqaz-misr": "hegazy_luxury_car_flatbed.jpg",
    "winch-daeri-cairo": "hegazy_porsche_highway_rear.jpg",
    "winch-tagamoa-new-cairo": "hegazy_orange_truck_porsche.jpg",
    "winch-zayed-october": "hegazy_cupra_rear.jpg",
    "emergency-breakdown-tips": "hegazy_red_truck_heavy.jpg"
}

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for slug, img in image_map.items():
        pattern = rf'("slug":\s*"{slug}",\s*\n\s*"title":)'
        if f'"slug": "{slug}"' in content and f'"image": "{img}"' not in content:
            replacement = f'"slug": "{slug}",\n        "image": "{img}",\n        "title":'
            content = re.sub(pattern, replacement, content)
            modified = True
            
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated images in {os.path.basename(filepath)}")
    else:
        print(f"No changes needed for {os.path.basename(filepath)}")

update_file(os.path.join(scripts_dir, "build_articles_engine.py"))
update_file(os.path.join(scripts_dir, "generate_cairo_competitor_pages.py"))
update_file(os.path.join(scripts_dir, "expand_eastern_cities.py"))
print("Done updating article image mappings.")
