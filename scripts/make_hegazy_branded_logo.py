import os
import math
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

def create_hegazy_pro_logo():
    size = 1024
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center = size // 2
    r_outer = 490
    r_inner = 450
    r_core = 420

    # 1. Base dark background circle with subtle gradient simulation
    for r in range(r_outer, 0, -2):
        factor = r / r_outer
        # Dark navy-slate gradient
        cr = int(8 + (15 - 8) * (1 - factor))
        cg = int(14 + (23 - 14) * (1 - factor))
        cb = int(26 + (42 - 26) * (1 - factor))
        draw.ellipse([center - r, center - r, center + r, center + r], fill=(cr, cg, cb, 255))

    # 2. Outer Golden Rim (Double Ring with Metallic Amber/Gold)
    gold_outer = (245, 158, 11, 255)  # #f59e0b
    gold_bright = (251, 191, 36, 255) # #fbbf24
    gold_dark = (180, 83, 9, 255)     # #b45309
    red_rescue = (220, 38, 38, 255)   # #dc2626
    red_bright = (239, 68, 68, 255)

    # Thick golden borders
    draw.ellipse([center - r_outer, center - r_outer, center + r_outer, center + r_outer], outline=gold_dark, width=6)
    draw.ellipse([center - (r_outer - 8), center - (r_outer - 8), center + (r_outer - 8), center + (r_outer - 8)], outline=gold_bright, width=5)
    draw.ellipse([center - r_inner, center - r_inner, center + r_inner, center + r_inner], outline=gold_outer, width=4)

    # 3. Decorative stars on the rim
    font_star = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 36)
    draw.text((center - 440, center - 18), "★", fill=gold_bright, font=font_star)
    draw.text((center + 415, center - 18), "★", fill=gold_bright, font=font_star)

    # 4. Circular Banner ribbon in center: Dark Charcoal with Red & Gold Trim
    banner_top = center - 80
    banner_bot = center + 80
    # Red accent stripes behind banner
    draw.rectangle([60, banner_top - 8, size - 60, banner_bot + 8], fill=red_rescue)
    draw.rectangle([70, banner_top - 4, size - 70, banner_bot + 4], fill=gold_bright)
    draw.rectangle([76, banner_top, size - 76, banner_bot], fill=(15, 23, 42, 255)) # Dark slate-900

    # 5. Bold English Brand Name "AWLAD HEGAZY" in Center Banner
    font_hegazy = ImageFont.truetype(r"C:\Windows\Fonts\ariblk.ttf", 78)
    text_en = "AWLAD HEGAZY"
    bbox_en = draw.textbbox((0, 0), text_en, font=font_hegazy)
    w_en = bbox_en[2] - bbox_en[0]
    h_en = bbox_en[3] - bbox_en[1]
    
    # Shadow for AWLAD HEGAZY
    draw.text((center - w_en // 2 + 4, center - h_en // 2 - 12 + 4), text_en, fill=(0, 0, 0, 200), font=font_hegazy)
    # Bright Gold text
    draw.text((center - w_en // 2, center - h_en // 2 - 12), text_en, fill=gold_bright, font=font_hegazy)

    # Subtitle under AWLAD HEGAZY in banner
    font_sub_en = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 26)
    sub_text = "★ CAR TOWING & HEAVY RESCUE 24/7 ★"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub_en)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text((center - w_sub // 2, banner_bot - 38), sub_text, fill=(226, 232, 240, 255), font=font_sub_en)

    # 6. Upper Arc / Header: Arabic Brand Name "أوناش إنقاذ أولاد حجازي"
    text_ar = "أوناش إنقاذ أولاد حجازي"
    reshaped_ar = arabic_reshaper.reshape(text_ar)
    bidi_ar = get_display(reshaped_ar)
    
    font_ar = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 72)
    bbox_ar = draw.textbbox((0, 0), bidi_ar, font=font_ar)
    w_ar = bbox_ar[2] - bbox_ar[0]
    h_ar = bbox_ar[3] - bbox_ar[1]

    # Draw Arabic brand name on upper section
    draw.text((center - w_ar // 2 + 3, 140 + 3), bidi_ar, fill=(0, 0, 0, 220), font=font_ar)
    draw.text((center - w_ar // 2, 140), bidi_ar, fill=(255, 255, 255, 255), font=font_ar)

    # Stylized tow truck silhouette icon above banner
    truck_y = center - 160
    # Truck cab
    draw.polygon([
        (center - 110, truck_y + 40),
        (center - 110, truck_y - 20),
        (center - 70, truck_y - 45),
        (center - 20, truck_y - 45),
        (center - 20, truck_y + 40)
    ], fill=red_rescue, outline=gold_bright)
    # Cab window
    draw.polygon([
        (center - 65, truck_y - 20),
        (center - 65, truck_y - 38),
        (center - 25, truck_y - 38),
        (center - 25, truck_y - 20)
    ], fill=(226, 232, 240, 240))
    # Emergency red beacon light on cab
    draw.ellipse([center - 55, truck_y - 56, center - 35, truck_y - 44], fill=(255, 255, 255, 255), outline=red_rescue, width=2)
    # Flatbed
    draw.rectangle([center - 20, truck_y + 15, center + 140, truck_y + 35], fill=(203, 213, 225, 255), outline=gold_bright, width=2)
    # Winch crane boom
    draw.line([center + 20, truck_y + 15, center + 90, truck_y - 35], fill=gold_bright, width=8)
    draw.line([center + 90, truck_y - 35, center + 120, truck_y - 10], fill=gold_bright, width=6)
    # Hook
    draw.arc([center + 115, truck_y - 15, center + 135, truck_y + 10], start=0, end=270, fill=gold_bright, width=5)
    # Truck wheels
    draw.ellipse([center - 95, truck_y + 25, center - 60, truck_y + 60], fill=(30, 41, 59, 255), outline=gold_bright, width=4)
    draw.ellipse([center + 60, truck_y + 25, center + 95, truck_y + 60], fill=(30, 41, 59, 255), outline=gold_bright, width=4)
    draw.ellipse([center + 95, truck_y + 25, center + 130, truck_y + 60], fill=(30, 41, 59, 255), outline=gold_bright, width=4)

    # 7. Bottom Arc: Location & Service Info in Arabic
    text_bot1 = "كارفور العبور • القاهرة الكبرى • خدمة 24 ساعة"
    reshaped_bot1 = arabic_reshaper.reshape(text_bot1)
    bidi_bot1 = get_display(reshaped_bot1)
    font_bot = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 36)
    bbox_b1 = draw.textbbox((0, 0), bidi_bot1, font=font_bot)
    w_b1 = bbox_b1[2] - bbox_b1[0]
    draw.text((center - w_b1 // 2, center + 140), bidi_bot1, fill=gold_bright, font=font_bot)

    # Bottom Phone Badge
    phone_badge_y = center + 220
    draw.rounded_rectangle([center - 260, phone_badge_y, center + 260, phone_badge_y + 70], radius=35, fill=red_rescue, outline=gold_bright, width=4)
    phone_text = "طوارئ: 01032194206"
    reshaped_phone = arabic_reshaper.reshape(phone_text)
    bidi_phone = get_display(reshaped_phone)
    font_phone = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 40)
    bbox_p = draw.textbbox((0, 0), bidi_phone, font=font_phone)
    w_p = bbox_p[2] - bbox_p[0]
    h_p = bbox_p[3] - bbox_p[1]
    draw.text((center - w_p // 2, phone_badge_y + (70 - h_p) // 2 - 4), bidi_phone, fill=(255, 255, 255, 255), font=font_phone)

    # Safety & Trust Shield badge at bottom tip
    draw.polygon([
        (center - 35, center + 330),
        (center + 35, center + 330),
        (center + 30, center + 375),
        (center, center + 400),
        (center - 30, center + 375)
    ], fill=gold_bright, outline=(15, 23, 42, 255), width=3)
    font_check = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 34)
    draw.text((center - 13, center + 342), "✓", fill=(15, 23, 42, 255), font=font_check)

    # Save to disk
    dst_dir = r"D:\winch-hegazy\assets\images"
    out_png = os.path.join(dst_dir, "logo.png")
    out_logo_pro = os.path.join(dst_dir, "hegazy_pro_logo.png")
    img.save(out_png, "PNG")
    img.save(out_logo_pro, "PNG")
    print(f"SUCCESS: Generated branded Awlad Hegazy logo at: {out_png}")

    # Generate high quality Favicons
    fav_png = os.path.join(dst_dir, "favicon.png")
    fav_ico = os.path.join(dst_dir, "favicon.ico")
    img_fav = img.resize((128, 128), Image.LANCZOS)
    img_fav.save(fav_png, "PNG")
    img_fav.save(fav_ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print(f"SUCCESS: Generated crisp favicon at: {fav_png} and {fav_ico}")

if __name__ == "__main__":
    create_hegazy_pro_logo()
