import re

file_path = r"D:\winch-hegazy\scripts\build_winch_helpers.py"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace get_head
old_get_head_start = code.find("def get_head(title, description, canonical_url, is_blog=False):")
old_get_head_end = code.find("def get_header(active_page=\"home\", is_blog=False):")

new_get_head = """def get_head(title, description, canonical_url, is_blog=False, preload_lcp=None):
    prefix = "../" if is_blog else ""
    preload_lcp_tag = f'  <link rel="preload" as="image" href="{prefix}{preload_lcp}" fetchpriority="high" type="image/webp">\\n' if preload_lcp else ""
    return f\"\"\"<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{prefix}assets/images/og_banner.webp">
  <meta property="og:locale" content="ar_EG">
  <meta property="og:site_name" content="أوناش إنقاذ أولاد حجازي">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{prefix}assets/images/og_banner.webp">

  <!-- Favicon & Touch Icons -->
  <link rel="icon" type="image/png" href="{prefix}assets/images/favicon.png">
  <link rel="apple-touch-icon" href="{prefix}assets/images/logo_sm.png">
  <meta name="theme-color" content="#0B0F17">

  <!-- LCP Preload if specified -->
{preload_lcp_tag}
  <!-- Fonts Preconnect & Asynchronous Non-Blocking CSS -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@500;700;800;900&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@500;700;800;900&display=swap" media="print" onload="this.media='all'">
  <noscript>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@500;700;800;900&display=swap">
  </noscript>

  <!-- Precompiled Minified Pure Tailwind CSS (Zero Runtime Script Overhead) -->
  <link rel="stylesheet" href="{prefix}assets/css/styles.min.css">
</head>
<body class="bg-[#0b0f17] text-slate-100 font-['Cairo',sans-serif] overflow-x-hidden">
\"\"\"
"""

code = code[:old_get_head_start] + new_get_head + code[old_get_head_end:]

# 2. Update get_header logo size
code = code.replace(
    '<img src="{p}assets/images/logo.png" alt="شعار أوناش إنقاذ أولاد حجازي" class="w-12 h-12 md:w-14 md:h-14 rounded-full border-2 border-amber-400 shadow-md group-hover:scale-105 transition-transform">',
    '<img src="{p}assets/images/logo_sm.png" alt="شعار أوناش إنقاذ أولاد حجازي" width="56" height="56" class="w-12 h-12 md:w-14 md:h-14 rounded-full border-2 border-amber-400 shadow-md group-hover:scale-105 transition-transform">'
)

# 3. Update get_footer logo and accessibility
code = code.replace(
    '<img src="{p}assets/images/logo.png" alt="شعار أوناش أولاد حجازي" class="w-12 h-12 rounded-full border border-amber-400">',
    '<img src="{p}assets/images/logo_sm.png" alt="شعار أوناش أولاد حجازي" width="48" height="48" class="w-12 h-12 rounded-full border border-amber-400">'
)

# Update footer heading levels from h4 to h3
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-4 border-r-4 border-amber-400 pr-2">روابط سريعة</h4>',
    '<h3 class="text-white font-extrabold text-base mb-4 border-r-4 border-amber-400 pr-2">روابط سريعة</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-4 border-r-4 border-rescue-500 pr-2">تغطية المحاور الحيوية</h4>',
    '<h3 class="text-white font-extrabold text-base mb-4 border-r-4 border-rescue-500 pr-2">تغطية المحاور الحيوية</h3>'
)
code = code.replace(
    '<h4 class="text-white font-extrabold text-base mb-4 border-r-4 border-amber-400 pr-2">خطوط الطوارئ 24/7</h4>',
    '<h3 class="text-white font-extrabold text-base mb-4 border-r-4 border-amber-400 pr-2">خطوط الطوارئ 24/7</h3>'
)

# Update footer contrast
code = code.replace(
    'text-slate-400">',
    'text-slate-300">',
    2 # only first two occurrences in footer
)
code = code.replace(
    '<p class="text-sm leading-relaxed text-slate-400">',
    '<p class="text-sm leading-relaxed text-slate-300">'
)
code = code.replace(
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 pt-6 border-t border-slate-900 text-center text-xs text-slate-500 flex flex-col md:flex-row items-center justify-between gap-4">',
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 pt-6 border-t border-slate-800 text-center text-xs text-slate-300 flex flex-col md:flex-row items-center justify-between gap-4">'
)
code = code.replace(
    'جميع الحقوق محفوظة © 2026 - <strong class="text-slate-300">أوناش إنقاذ أولاد حجازي</strong>',
    'جميع الحقوق محفوظة © 2026 - <strong class="text-white">أوناش إنقاذ أولاد حجازي</strong>'
)
code = code.replace(
    '<div class="flex items-center gap-4 text-slate-400">',
    '<div class="flex items-center gap-4 text-slate-300">'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("build_winch_helpers.py upgraded successfully!")
