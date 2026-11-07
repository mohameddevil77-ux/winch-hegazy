import os
from PIL import Image

src_dir = r"D:\winch-hegazy\extracted_user_photos"
files = sorted(os.listdir(src_dir))

manifest = []
for f in files:
    full = os.path.join(src_dir, f)
    try:
        im = Image.open(full)
        manifest.append({
            "name": f,
            "size": im.size,
            "bytes": os.path.getsize(full)
        })
    except Exception as e:
        manifest.append({"name": f, "error": str(e)})

for i, m in enumerate(manifest):
    print(f"[{i+1}] {m.get('bytes', 0):>8} B | {str(m.get('size', 'ERR')):>12} | {m['name']}")
