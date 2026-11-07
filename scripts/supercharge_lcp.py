import re

# 1. Update build_winch_helpers.py for responsive LCP preload
helpers_path = r"D:\winch-hegazy\scripts\build_winch_helpers.py"
with open(helpers_path, "r", encoding="utf-8") as f:
    code = f.read()

old_preload = 'preload_lcp_tag = f\'  <link rel="preload" as="image" href="{prefix}{preload_lcp}" fetchpriority="high" type="image/webp">\\n\' if preload_lcp else ""'
new_preload = '''if preload_lcp:
        preload_lcp_tag = f\'\'\'  <!-- Ultra-Fast Responsive LCP Image Preload -->
  <link rel="preload" as="image" href="{prefix}assets/images/hero_rescue_mobile.webp" media="(max-width: 640px)" fetchpriority="high" type="image/webp">
  <link rel="preload" as="image" href="{prefix}assets/images/hero_rescue_bg.webp" media="(min-width: 641px)" fetchpriority="high" type="image/webp">\\n\'\'\'
    else:
        preload_lcp_tag = ""'''

if old_preload in code:
    code = code.replace(old_preload, new_preload)
    with open(helpers_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("✓ Updated build_winch_helpers.py with responsive LCP preload")
else:
    print("Notice: check old_preload in helpers...")

# 2. Update generate_winch_hegazy_site.py Hero section structure
site_path = r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py"
with open(site_path, "r", encoding="utf-8") as f:
    site_code = f.read()

old_hero_start = '''  <!-- Hero Section -->
  <section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden bg-cover bg-center bg-no-repeat" style="background-image: linear-gradient(to bottom, rgba(3, 7, 18, 0.84), rgba(3, 7, 18, 0.96)), url('assets/images/hero_rescue_bg.webp');">'''

new_hero_start = '''  <!-- Hero Section (Optimized for Sub-2.0s Mobile LCP) -->
  <section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden">
    <!-- Eager Responsive LCP Background Picture (Discovered Instantly by Scanner) -->
    <picture class="absolute inset-0 w-full h-full -z-20 pointer-events-none">
      <source media="(max-width: 640px)" srcset="assets/images/hero_rescue_mobile.webp" type="image/webp">
      <img src="assets/images/hero_rescue_bg.webp" alt="ونش إنقاذ سيارات أوناش أولاد حجازي" width="1376" height="768" fetchpriority="high" decoding="sync" loading="eager" class="w-full h-full object-cover">
    </picture>
    <!-- Dark Vignette Overlay for Text Legibility -->
    <div class="absolute inset-0 bg-gradient-to-b from-[#0b0f17]/85 via-[#0b0f17]/90 to-[#0b0f17] -z-10 pointer-events-none"></div>'''

if old_hero_start in site_code:
    site_code = site_code.replace(old_hero_start, new_hero_start)
    with open(site_path, "w", encoding="utf-8") as f:
        f.write(site_code)
    print("✓ Updated generate_winch_hegazy_site.py Hero section structure")
else:
    print("Notice: check old_hero_start in generate_winch_hegazy_site.py...")
    idx = site_code.find("Hero Section")
    print(repr(site_code[idx:idx+250]))
