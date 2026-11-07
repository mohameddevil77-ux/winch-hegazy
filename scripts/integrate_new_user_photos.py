import os
import shutil
from PIL import Image

src_dir = r"D:\winch-hegazy\extracted_user_photos"
dst_dir = r"D:\winch-hegazy\assets\images"
files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')])

# Map specific gems to clear SEO filenames:
# Index 22 (thumb 23) -> Lamborghini Huracan Night
# Index 23 (thumb 24) -> Caterpillar Loader
# Index 24 (thumb 25) -> Heavy Construction Equipment
# Index 1 (thumb 2) -> Scania Heavy Truck Head
# Index 0 (thumb 1) -> Isuzu Highway Patrol Winch
# Index 25 (thumb 26) -> High-res 3120x4160 Red Hegazy Truck

new_photos = [
    (22, "hegazy_lamborghini_night.jpg"),
    (23, "hegazy_caterpillar_loader.jpg"),
    (24, "hegazy_heavy_equipment_loader.jpg"),
    (1,  "hegazy_scania_truck_head.jpg"),
    (0,  "hegazy_highway_isuzu_patrol.jpg"),
]

for idx, target_name in new_photos:
    src_file = os.path.join(src_dir, files[idx])
    dst_file = os.path.join(dst_dir, target_name)
    im = Image.open(src_file)
    # Save optimized JPEG (max 1600px width/height)
    im_copy = im.copy()
    im_copy.thumbnail((1600, 1600), Image.LANCZOS)
    im_copy.convert("RGB").save(dst_file, "JPEG", quality=88)
    print(f"Copied & optimized: {target_name} ({im_copy.size})")

# Also check index 25 (high-res red truck) and update hegazy_red_truck_heavy.jpg if higher quality
hi_res_red = os.path.join(src_dir, files[25])
im_hi = Image.open(hi_res_red)
im_hi.thumbnail((1600, 1600), Image.LANCZOS)
im_hi.convert("RGB").save(os.path.join(dst_dir, "hegazy_red_truck_heavy.jpg"), "JPEG", quality=90)
print("Updated hegazy_red_truck_heavy.jpg with high-res original!")

print("All new authentic photos added to assets/images successfully!")
