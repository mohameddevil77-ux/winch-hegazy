import os
from PIL import Image

src_dir = r"D:\winch-hegazy\extracted_user_photos"
out_dir = os.path.join(src_dir, "thumbs")
os.makedirs(out_dir, exist_ok=True)

files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith('.jpeg') or f.lower().endswith('.jpg')])

html = ["<html><body style='background:#111;color:#fff;font-family:sans-serif;'><h2>Extracted User Photos</h2><div style='display:flex;flex-wrap:wrap;gap:15px;'>"]

for i, f in enumerate(files):
    p = os.path.join(src_dir, f)
    try:
        im = Image.open(p)
        # thumbnail
        thumb_name = f"thumb_{i+1}.jpg"
        thumb_p = os.path.join(out_dir, thumb_name)
        im_thumb = im.copy()
        im_thumb.thumbnail((400, 400))
        im_thumb.convert("RGB").save(thumb_p, "JPEG")
        html.append(f"<div style='border:1px solid #444;padding:10px;width:320px;text-align:center;'>")
        html.append(f"<img src='thumbs/{thumb_name}' style='max-width:300px;max-height:220px;'><br>")
        html.append(f"<span style='font-size:12px;'>#{i+1}: {f[:25]}<br>({im.size[0]}x{im.size[1]})</span>")
        html.append(f"</div>")
    except Exception as e:
        html.append(f"<div>Error loading {f}: {e}</div>")

html.append("</div></body></html>")

with open(os.path.join(src_dir, "gallery.html"), "w", encoding="utf-8") as fl:
    fl.write("\n".join(html))

print("Gallery generated at D:\\winch-hegazy\\extracted_user_photos\\gallery.html")
