# -*- coding: utf-8 -*-
import os, json

helpers_path = r"D:\winch-hegazy\scripts\build_winch_helpers.py"
with open(helpers_path, "r", encoding="utf-8") as f:
    h_code = f.read()

video_fn = '''
def generate_video_schema():
    videos = [
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": "توثيق بالفيديو: نقل سيارة سوبر كار لامبورجيني هوراكان ليلاً - ونش إنقاذ حجازي",
            "description": "فيديو ميداني يوثق عملية سحب وتثبيت سيارة سوبر كار لامبورجيني ليلاً على ونش إنقاذ حجازي بأربطة إطارات مطاطية مخصصة وإضاءات ليد توجيهية.",
            "thumbnailUrl": "https://winch-hegazy.com/assets/images/poster_lamborghini_night.jpg",
            "uploadDate": "2026-11-06T20:00:00+02:00",
            "contentUrl": "https://winch-hegazy.com/assets/videos/hegazy_lamborghini_vip_night.mp4",
            "embedUrl": "https://winch-hegazy.com/index.html#videos"
        },
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": "توثيق بالفيديو: تحميل ونقل لودر كاتربيلر CAT 930 نهاراً - ونش إنقاذ حجازي",
            "description": "استعراض لقدرات ونش حجازي الهيدروليكية الثقيلة في سحب ونقل لوادر ومعدات البناء والمشروعات القومية بأمان تام.",
            "thumbnailUrl": "https://winch-hegazy.com/assets/images/poster_caterpillar_loader.jpg",
            "uploadDate": "2026-11-06T20:00:00+02:00",
            "contentUrl": "https://winch-hegazy.com/assets/videos/hegazy_caterpillar_loader_day.mp4",
            "embedUrl": "https://winch-hegazy.com/index.html#videos"
        },
        {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": "توثيق بالفيديو: إنقاذ ونقل سيارة ربع نقل محملة بالبضائع ليلاً - ونش إنقاذ حجازي",
            "description": "توثيق سحب وتأمين شاحنة بضائع تجارية بحمولتها الكاملة على الطريق السريع ليلاً بأضواء ليد محيطية لحماية الشحنة.",
            "thumbnailUrl": "https://winch-hegazy.com/assets/images/poster_commercial_pickup.jpg",
            "uploadDate": "2026-11-06T20:00:00+02:00",
            "contentUrl": "https://winch-hegazy.com/assets/videos/hegazy_commercial_pickup_night.mp4",
            "embedUrl": "https://winch-hegazy.com/index.html#videos"
        }
    ]
    return f'<script type="application/ld+json">\\n{json.dumps(videos, ensure_ascii=False, indent=2)}\\n</script>'
'''

if "def generate_video_schema():" not in h_code:
    h_code += "\n\n" + video_fn
    with open(helpers_path, "w", encoding="utf-8") as f:
        f.write(h_code)
    print("SUCCESS: Added generate_video_schema() to build_winch_helpers.py")
else:
    print("ALREADY EXISTS: generate_video_schema in build_winch_helpers.py")


# Update generate_winch_hegazy_site.py
site_path = r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py"
with open(site_path, "r", encoding="utf-8") as f:
    s_code = f.read()

# Make sure generate_video_schema is imported
if "generate_video_schema" not in s_code:
    s_code = s_code.replace(
        "generate_faq_schema, get_map_section, MAPS_URL",
        "generate_faq_schema, generate_video_schema, get_map_section, MAPS_URL"
    )

# Remove the raw script block in head that caused syntax error
raw_script_start = s_code.find('<script type="application/ld+json">\n  [\n    {')
if raw_script_start != -1:
    raw_script_end = s_code.find('</script>', raw_script_start) + 9
    s_code = s_code[:raw_script_start] + "{generate_video_schema()}\n" + s_code[raw_script_end:]
    print("SUCCESS: Replaced raw script with {generate_video_schema()}")

with open(site_path, "w", encoding="utf-8") as f:
    f.write(s_code)
print("SUCCESS: Saved generate_winch_hegazy_site.py")
