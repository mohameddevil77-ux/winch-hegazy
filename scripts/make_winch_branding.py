import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import arabic_reshaper
from bidi.algorithm import get_display

out_dir = r"D:\winch-hegazy\assets\images"
os.makedirs(out_dir, exist_ok=True)

def ar(text):
    return get_display(arabic_reshaper.reshape(text))

# Fonts
font_bold = "C:\\Windows\\Fonts\\segoeuib.ttf"
font_regular = "C:\\Windows\\Fonts\\segoeui.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# 1. Generate Logo Badge (512x512)
logo_img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
d = ImageDraw.Draw(logo_img)

# Outer circle glow
d.ellipse((16, 16, 496, 496), fill=(15, 23, 42, 255), outline=(245, 158, 11, 255), width=8)
d.ellipse((32, 32, 480, 480), outline=(239, 68, 68, 200), width=4)

# Draw central hook / winch icon graphic
# Shield / Hexagon in center
shield_pts = [(256, 70), (410, 150), (410, 310), (256, 420), (102, 310), (102, 150)]
d.polygon(shield_pts, fill=(30, 41, 59, 255), outline=(245, 158, 11, 255))

# Draw Tow Hook shape
d.ellipse((226, 140, 286, 200), outline=(250, 204, 21, 255), width=10) # Hook eye
d.rectangle((246, 195, 266, 260), fill=(250, 204, 21, 255)) # Shank
# Hook curve
d.arc((196, 230, 316, 350), start=0, end=190, fill=(250, 204, 21, 255), width=14)
# Arrow head / barb
d.polygon([(196, 290), (180, 260), (212, 265)], fill=(250, 204, 21, 255))

# Arabic Text
f_title = get_font(font_bold, 48)
f_sub = get_font(font_bold, 24)

# Text banner
t1 = ar("ونش حجازي")
bb1 = d.textbbox((0, 0), t1, font=f_title)
w1 = bb1[2] - bb1[0]
d.text((256 - w1 // 2, 345), t1, fill=(255, 255, 255, 255), font=f_title)

t2 = ar("لإنقاذ السيارات 24 ساعة")
bb2 = d.textbbox((0, 0), t2, font=f_sub)
w2 = bb2[2] - bb2[0]
d.text((256 - w2 // 2, 435), t2, fill=(245, 158, 11, 255), font=f_sub)

logo_path = os.path.join(out_dir, "logo.png")
logo_img.save(logo_path, "PNG")

# Favicon
fav = logo_img.resize((64, 64), Image.Resampling.LANCZOS)
fav.save(os.path.join(out_dir, "favicon.png"), "PNG")
fav.save(os.path.join(out_dir, "favicon.ico"))

# 2. OpenGraph / Social Share Banner (1200x630)
og = Image.new("RGB", (1200, 630), (11, 15, 23))
d_og = ImageDraw.Draw(og)

# Background ambient grid & lighting
for x in range(0, 1200, 40):
    d_og.line([(x, 0), (x, 630)], fill=(20, 30, 45), width=1)
for y in range(0, 630, 40):
    d_og.line([(0, y), (1200, y)], fill=(20, 30, 45), width=1)

# Glowing gradient borders
d_og.rectangle((0, 0, 1200, 8), fill=(245, 158, 11))
d_og.rectangle((0, 622, 1200, 630), fill=(239, 68, 68))

# Header Badge
f_og_badge = get_font(font_bold, 24)
badge_text = ar("خدمة طوارئ وإنقاذ سريع 24/7 • في جميع أنحاء مصر")
d_og.rectangle((350, 45, 850, 95), fill=(30, 41, 59), outline=(245, 158, 11), width=2)
bb_b = d_og.textbbox((0, 0), badge_text, font=f_og_badge)
d_og.text((600 - (bb_b[2] - bb_b[0]) // 2, 55), badge_text, fill=(245, 158, 11), font=f_og_badge)

# Main Title
f_og_title = get_font(font_bold, 64)
main_t = ar("ونش إنقاذ حجازي")
bb_m = d_og.textbbox((0, 0), main_t, font=f_og_title)
d_og.text((600 - (bb_m[2] - bb_m[0]) // 2, 120), main_t, fill=(255, 255, 255), font=f_og_title)

# Subtitle
f_og_sub = get_font(font_bold, 36)
sub_t = ar("أسرع وأرخص ونش إنقاذ سيارات في مصر • نصلك خلال 10 دقائق")
bb_s = d_og.textbbox((0, 0), sub_t, font=f_og_sub)
d_og.text((600 - (bb_s[2] - bb_s[0]) // 2, 205), sub_t, fill=(250, 204, 21), font=f_og_sub)

# 3 Feature Pills
pills = [
    ar("تغطية شاملة للقاهرة والجيزة والطرق السريعة"),
    ar("أحدث أوناش هيدروليكية مغلقة ومؤمنة بالكامل"),
    ar("أسعار عادلة ومحددة مسبقاً بدون استغلال")
]
f_pill = get_font(font_bold, 22)
for i, p in enumerate(pills):
    y_pos = 280 + i * 55
    d_og.rectangle((200, y_pos, 1000, y_pos + 42), fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    bb_p = d_og.textbbox((0, 0), p, font=f_pill)
    d_og.text((600 - (bb_p[2] - bb_p[0]) // 2, y_pos + 8), p, fill=(226, 232, 240), font=f_pill)

# Phone CTA Button
d_og.rectangle((320, 480, 880, 570), fill=(220, 38, 38), outline=(250, 204, 21), width=4)
f_btn = get_font(font_bold, 38)
btn_t = ar("اتصل الآن: 01098174992 (طوارئ 24 ساعة)")
bb_btn = d_og.textbbox((0, 0), btn_t, font=f_btn)
d_og.text((600 - (bb_btn[2] - bb_btn[0]) // 2, 502), btn_t, fill=(255, 255, 255), font=f_btn)

og_path = os.path.join(out_dir, "og_banner.jpg")
og.save(og_path, "JPEG", quality=92)

print("SUCCESS: Brand images generated in:", out_dir)
