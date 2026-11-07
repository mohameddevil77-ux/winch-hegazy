import os
from PIL import Image

img_dir = r"D:\winch-hegazy\assets\images"

files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

total_orig_size = 0
total_webp_size = 0

print(f"Converting {len(files)} images to WebP...")

# Also create optimized logo_sm.png and logo_sm.webp (128x128)
logo_path = os.path.join(img_dir, "logo.png")
if os.path.exists(logo_path):
    with Image.open(logo_path) as img:
        img_sm = img.resize((128, 128), Image.Resampling.LANCZOS)
        img_sm.save(os.path.join(img_dir, "logo_sm.png"), "PNG", optimize=True)
        img_sm.save(os.path.join(img_dir, "logo_sm.webp"), "WEBP", quality=90)
        print("Created logo_sm.png and logo_sm.webp (128x128)")

for f in files:
    src_path = os.path.join(img_dir, f)
    base, ext = os.path.splitext(f)
    webp_path = os.path.join(img_dir, f"{base}.webp")
    
    orig_size = os.path.getsize(src_path)
    total_orig_size += orig_size
    
    try:
        with Image.open(src_path) as img:
            # If image is RGBA and format is JPEG, keep RGBA for WebP
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img.save(webp_path, "WEBP", quality=85, method=6)
            else:
                img_rgb = img.convert("RGB")
                # For hero and big images, resize if unnecessarily huge (>1600px width)
                if img_rgb.width > 1600:
                    h = int(img_rgb.height * (1600 / img_rgb.width))
                    img_rgb = img_rgb.resize((1600, h), Image.Resampling.LANCZOS)
                img_rgb.save(webp_path, "WEBP", quality=82, method=6)
                
        webp_size = os.path.getsize(webp_path)
        total_webp_size += webp_size
        savings = (1 - (webp_size / orig_size)) * 100
        print(f"✓ {f} ({orig_size//1024} KB) -> {base}.webp ({webp_size//1024} KB) [{savings:.1f}% saved]")
    except Exception as e:
        print(f"✗ Failed {f}: {e}")

print(f"\nTotal Original: {total_orig_size // 1024} KB")
print(f"Total WebP:     {total_webp_size // 1024} KB")
if total_orig_size > 0:
    print(f"Total Savings:  {((1 - total_webp_size / total_orig_size) * 100):.1f}%")
