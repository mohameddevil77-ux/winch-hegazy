import os
from PIL import Image

src_dir = r"D:\winch-hegazy\extracted_user_photos"
files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')])

# Let's inspect images 16, 17, 20, 22, 23, 24, 25, 26
targets = [15, 16, 19, 21, 22, 23, 24, 25] # 0-indexed

for idx in targets:
    f = files[idx]
    p = os.path.join(src_dir, f)
    im = Image.open(p)
    # Get image stats
    colors = im.getcolors(maxcolors=10)
    print(f"File #{idx+1}: {f}")
    print(f"  Size: {im.size}, Mode: {im.mode}")
