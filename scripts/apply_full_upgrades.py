import os
import re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update build_winch_helpers.py
helpers_path = os.path.join(scripts_dir, "build_winch_helpers.py")
with open(helpers_path, "r", encoding="utf-8") as f:
    h_code = f.read()

# Update priceRange in Schema
h_code = h_code.replace('"priceRange": "EGP 600 - EGP 800"', '"priceRange": "EGP 600 - EGP 3500"')

# Update top banner in get_header
old_banner_snippet = '''      <!-- Top announcement bar -->
      <div class="hidden sm:flex items-center justify-between text-xs py-1.5 border-b border-slate-800 text-slate-400">'''

new_banner_snippet = '''      <!-- Top announcement bar with special offer -->
      <div class="hidden sm:flex items-center justify-between text-xs py-1.5 border-b border-slate-800 text-slate-300">
        <div class="flex items-center gap-2">
          <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-black border border-emerald-500/40 text-[10px]">عرض الموسم 2026</span>
          <span class="font-bold text-amber-300">خصم 50% لأول 100 عميل (كود HEGAZY50)</span>
          <span class="text-slate-500">•</span>
          <span class="text-slate-300">بدون أي إكرامية إجبارية للسائق</span>
          <span class="text-slate-500">•</span>
          <span class="text-slate-300">مساهمة في دفع رسوم الكارتة</span>
        </div>
        <div class="flex items-center gap-3 text-[11px]">
          <span>ارتكاز: كارفور العبور وجولف سيتي</span>
          <span class="text-emerald-400 font-bold">● أسطول متأهب الآن</span>
        </div>
      </div>'''

if old_banner_snippet in h_code:
    # replace up to the next </div>
    idx_b1 = h_code.find(old_banner_snippet)
    idx_b2 = h_code.find("</div>", idx_b1 + len(old_banner_snippet)) + 6
    h_code = h_code[:idx_b1] + new_banner_snippet + h_code[idx_b2:]

with open(helpers_path, "w", encoding="utf-8") as f:
    f.write(h_code)
print("SUCCESS: Updated build_winch_helpers.py")


# 2. Update generate_winch_hegazy_site.py
site_gen_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_gen_path, "r", encoding="utf-8") as f:
    s_code = f.read()

# Update Hero section with hero_rescue_bg.jpg
s_code = s_code.replace(
    '<section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden bg-gradient-to-b from-dark-900 via-dark-950 to-dark-950">',
    '<section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden bg-cover bg-center bg-no-repeat" style="background-image: linear-gradient(to bottom, rgba(3, 7, 18, 0.84), rgba(3, 7, 18, 0.96)), url(\'assets/images/hero_rescue_bg.jpg\');">'
)

# Update price occurrences from 250 to 600
s_code = s_code.replace("سحب سيارات يبدأ من 600 جنيه", "سحب سيارات يبدأ من 600 جنيه")
s_code = s_code.replace("من 600 جنيه مصري فقط", "من 600 جنيه مصري فقط")
s_code = s_code.replace(">600 ج.م<", ">600 ج.م<")
s_code = s_code.replace("250 - 350 ج.م", "600 - 750 ج.م")

# Update calculator JS priceMap
old_price_map = """    const priceMap = {
      sedan: { same: '250 - 300 ج.م', center: '350 - 450 ج.م', home: '350 - 500 ج.م', cross: 'يبدأ من 600 ج.م' },
      suv: { same: '300 - 350 ج.م', center: '400 - 550 ج.م', home: '450 - 600 ج.م', cross: 'يبدأ من 750 ج.م' },
      heavy: { same: '500 - 700 ج.م', center: '700 - 1000 ج.م', home: '800 - 1200 ج.م', cross: 'يبدأ من 1400 ج.م' }
    };"""

new_price_map = """    const priceMap = {
      sedan: { same: '600 - 750 ج.م', center: '750 - 950 ج.م', home: '950 - 1300 ج.م', cross: 'يبدأ من 1500 ج.م' },
      suv: { same: '750 - 900 ج.م', center: '900 - 1200 ج.م', home: '1200 - 1600 ج.م', cross: 'يبدأ من 1800 ج.م' },
      heavy: { same: '1200 - 1600 ج.م', center: '1600 - 2200 ج.م', home: '2200 - 3000 ج.م', cross: 'يبدأ من 3000 ج.م' }
    };"""

s_code = s_code.replace(old_price_map, new_price_map)
s_code = s_code.replace("|| '250 - 350 ج.م'", "|| '600 - 750 ج.م'")

with open(site_gen_path, "w", encoding="utf-8") as f:
    f.write(s_code)
print("SUCCESS: Updated generate_winch_hegazy_site.py")


# 3. Update build_articles_engine.py with new Pricing and new Promotional Article
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    e_code = f.read()

# Replace prices in html_pricing
e_code = e_code.replace("تبدأ من 600 ج.م", "تبدأ من 600 ج.م")
e_code = e_code.replace("250 - 300 ج.م", "600 - 750 ج.م")
e_code = e_code.replace("350 - 450 ج.م", "800 - 1100 ج.م")
e_code = e_code.replace("300 - 400 ج.م", "750 - 950 ج.م")
e_code = e_code.replace("يبدأ من 450 ج.م + كم", "يبدأ من 1200 ج.م + كم")
e_code = e_code.replace("يبدأ من 800 ج.م", "يبدأ من 1800 - 3500 ج.م")

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(e_code)
print("SUCCESS: Updated build_articles_engine.py pricing")
