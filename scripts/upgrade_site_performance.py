import re

path = r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update get_head call with preload_lcp
old_head_call = '''html_index = f"""{get_head(
    "أوناش إنقاذ أولاد حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"أوناش إنقاذ أولاد حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://winchawladhegazy.com/"
)}'''

new_head_call = '''html_index = f"""{get_head(
    "أوناش إنقاذ أولاد حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"أوناش إنقاذ أولاد حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://winchawladhegazy.com/",
    is_blog=False,
    preload_lcp="assets/images/hero_rescue_bg.webp"
)}'''

if old_head_call in code:
    code = code.replace(old_head_call, new_head_call)
    print("✓ Updated get_head call with LCP preload")
else:
    print("✗ old_head_call not found directly, checking regex...")
    code = re.sub(
        r'html_index = f"""\{get_head\(\s*"أوناش إنقاذ أولاد حجازي.*?"https://awladhegazy\.com/"\s*\)\}',
        new_head_call,
        code,
        flags=re.DOTALL
    )

# 2. Add <main id="main-content"> after get_header and </main> before get_footer
code = code.replace(
    '{get_header("home")}',
    '{get_header("home")}\n\n  <main id="main-content">'
)

code = code.replace(
    '{get_footer()}',
    '  </main>\n\n{get_footer()}'
)
print("✓ Added <main id=\"main-content\"> landmark")

# 3. Hero background image to WebP
code = code.replace(
    "url('assets/images/hero_rescue_bg.jpg')",
    "url('assets/images/hero_rescue_bg.webp')"
)
print("✓ Updated Hero background to hero_rescue_bg.webp")

# 4. Form labels and accessibility in calculator
code = code.replace(
    '<label class="block text-xs font-bold text-slate-300 mb-2">مكان تعطل السيارة الحالي (موقعك):</label>\n            <select id="startLoc"',
    '<label for="startLoc" class="block text-xs font-bold text-slate-300 mb-2">مكان تعطل السيارة الحالي (موقعك):</label>\n            <select id="startLoc" name="startLoc" aria-label="مكان تعطل السيارة الحالي (موقعك)"'
)

code = code.replace(
    '<label class="block text-xs font-bold text-slate-300 mb-2">مكان توصيل السيارة (الوجهة):</label>\n            <select id="endLoc"',
    '<label for="endLoc" class="block text-xs font-bold text-slate-300 mb-2">مكان توصيل السيارة (الوجهة):</label>\n            <select id="endLoc" name="endLoc" aria-label="مكان توصيل السيارة (الوجهة)"'
)
print("✓ Updated calculator labels and aria-labels")

# 5. Heading hierarchy in Why Choose Us
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-2">تسعير محدد مسبقاً قبل تحرك الونش</h4>',
    '<h3 class="text-white font-extrabold text-base mb-2">تسعير محدد مسبقاً قبل تحرك الونش</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-2">أحدث أسطول هيدروليكي 2026</h4>',
    '<h3 class="text-white font-extrabold text-base mb-2">أحدث أسطول هيدروليكي 2026</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-2">سائقون محترفون ومدربون على السلامة المهنية</h4>',
    '<h3 class="text-white font-extrabold text-base mb-2">سائقون محترفون ومدربون على السلامة المهنية</h3>'
)
print("✓ Updated Why Choose Us headings from h4 to h3")

# 6. Real Photos Gallery - WebP images and lazy loading and h3 headings
gallery_images = [
    "hegazy_lamborghini_night",
    "hegazy_caterpillar_loader",
    "hegazy_heavy_equipment_loader",
    "hegazy_red_truck_branding",
    "hegazy_orange_truck_porsche",
    "hegazy_luxury_car_flatbed",
    "hegazy_semi_truck_head",
    "hegazy_caravan_transport",
    "hegazy_golf_carts_transport",
    "hegazy_food_truck_transport",
    "hegazy_red_truck_heavy",
    "hegazy_night_commercial_pickup"
]

for img in gallery_images:
    code = code.replace(f"assets/images/{img}.jpg", f"assets/images/{img}.webp")

# Add loading="lazy" decoding="async" to <img> in gallery if not already present
code = re.sub(
    r'<img src="assets/images/([a-zA-Z0-9_\-]+)\.webp" alt="([^"]+)" class="([^"]+)">',
    r'<img src="assets/images/\1.webp" alt="\2" class="\3" loading="lazy" decoding="async">',
    code
)

# Convert gallery card titles from h4 to h3
code = re.sub(
    r'<h4 class="text-white font-extrabold text-sm mb-1 truncate">',
    r'<h3 class="text-white font-extrabold text-sm mb-1 truncate">',
    code
)
code = re.sub(
    r'</h4>(\s*<p class="text-slate-400 text-xs line-clamp-2)',
    r'</h3>\1',
    code
)
print("✓ Updated gallery images to WebP + lazy loading + h3 headings")

# 7. Videos Section Optimization
# Change section title to h2
code = code.replace(
    '<h3 class="text-3xl sm:text-4xl font-black text-white leading-tight">\n        فيديوهات حصرية لعمليات أسطول',
    '<h2 class="text-3xl sm:text-4xl font-black text-white leading-tight">\n        فيديوهات حصرية لعمليات أسطول'
)
code = code.replace(
    'أوناش أولاد حجازي الميدانية</span>\n      </h3>',
    'أوناش أولاد حجازي الميدانية</span>\n      </h2>'
)

# Change video card titles to h3
code = code.replace(
    '<h4 class="text-white font-extrabold text-base">توثيق سحب سيارة لامبورجيني هوراكان ليلاً</h4>',
    '<h3 class="text-white font-extrabold text-base">توثيق سحب سيارة لامبورجيني هوراكان ليلاً</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base">تحميل ونقل لودر CAT 930 للمشروعات</h4>',
    '<h3 class="text-white font-extrabold text-base">تحميل ونقل لودر CAT 930 للمشروعات</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base">إنقاذ سيارة ربع نقل محملة بالبضائع ليلاً</h4>',
    '<h3 class="text-white font-extrabold text-base">إنقاذ سيارة ربع نقل محملة بالبضائع ليلاً</h3>'
)

# Update video posters to webp
code = code.replace("poster_lamborghini_night.jpg", "poster_lamborghini_night.webp")
code = code.replace("poster_caterpillar_loader.jpg", "poster_caterpillar_loader.webp")
code = code.replace("poster_commercial_pickup.jpg", "poster_commercial_pickup.webp")

# Change preload="metadata" to preload="none"
code = code.replace('preload="metadata"', 'preload="none"')

# Add captions track to videos
caption_track = '<track kind="captions" src="assets/videos/captions.vtt" srclang="ar" label="عربي">\n            متصفحك لا يدعم تشغيل الفيديو.'
code = code.replace('متصفحك لا يدعم تشغيل الفيديو.', caption_track)
print("✓ Updated videos with preload='none', WebP posters, and caption tracks")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("generate_winch_hegazy_site.py fully optimized!")
