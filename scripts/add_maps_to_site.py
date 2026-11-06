import os
import re
import json

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update build_winch_helpers.py
helpers_path = os.path.join(scripts_dir, "build_winch_helpers.py")
with open(helpers_path, "r", encoding="utf-8") as f:
    code = f.read()

# Add constants if not present
if "MAPS_URL" not in code:
    maps_constants = """
# Real Google Maps Location Data
MAPS_URL = "https://maps.app.goo.gl/4JvQjcJFPNFqesXS7?g_st=awb"
MAPS_EMBED_URL = "https://maps.google.com/maps?q=30.1741147,31.4761952&hl=ar&z=16&output=embed"
GEO_LAT = 30.1741147
GEO_LNG = 31.4761952
LOCATION_NAME = "مركز ارتكاز ونش حجازي - كارفور العبور وجولف سيتي مول"
LOCATION_ADDRESS = "كارفور العبور، جولف سيتي مول، مطلع الطريق الدائري وطريق الإسماعيلية الصحراوي، مصر"
"""
    code = code.replace('WHATSAPP_LINK_ALT = "https://wa.me/201283038303?text=%D8%B7%D9%88%D8%A7%D8%B1%D8%A6!%20%D8%A3%D8%AD%D8%AA%D8%A7%D8%AC%20%D9%88%D9%86%D8%B4%20%D8%A5%D9%86%D9%82%D8%A7%D8%B0%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA%20%D9%81%D9%88%D8%B1%D8%A7%D9%8B%D8%8C%20%D9%85%D9%88%D9%82%D8%B9%D9%8A%20%D8%A7%D9%84%D8%AD%D8%A7%D9%84%D9%8A:%20"',
                        'WHATSAPP_LINK_ALT = "https://wa.me/201283038303?text=%D8%B7%D9%88%D8%A7%D8%B1%D8%A6!%20%D8%A3%D8%AD%D8%AA%D8%A7%D8%AC%20%D9%88%D9%86%D8%B4%20%D8%A5%D9%86%D9%82%D8%A7%D8%B0%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA%20%D9%81%D9%88%D8%B1%D8%A7%D9%8B%D8%8C%20%D9%85%D9%88%D9%82%D8%B9%D9%8A%20%D8%A7%D9%84%D8%AD%D8%A7%D9%84%D9%8A:%20"\n' + maps_constants)

# Update Schema with exact Geo and address
old_geo = """"geo": {
            "@type": "GeoCoordinates",
            "latitude": 30.0444,
            "longitude": 31.2357
        },"""
new_geo = """"geo": {
            "@type": "GeoCoordinates",
            "latitude": 30.1741147,
            "longitude": 31.4761952
        },
        "hasMap": "https://maps.app.goo.gl/4JvQjcJFPNFqesXS7?g_st=awb",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "ميدان كارفور العبور - جولف سيتي مول، مطلع الدائري وطريق الإسماعيلية الصحراوي",
            "addressLocality": "مدينة العبور",
            "addressRegion": "محافظة القليوبية / القاهرة الكبرى",
            "postalCode": "6361002",
            "addressCountry": "EG"
        },"""

code = code.replace(old_geo, new_geo)

# Add get_map_section function
map_section_func = """
def get_map_section():
    return f'''
  <!-- Google Maps Interactive Location Section -->
  <section class="py-16 bg-slate-900/60 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Info Column -->
        <div class="lg:col-span-5 space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-xs font-black">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
            <span>نقطة الارتكاز الميداني المعتمدة (Live GPS)</span>
          </div>

          <h2 class="text-2xl md:text-4xl font-black text-white leading-tight">موقع تمركز ونش إنقاذ حجازي على الخريطة</h2>
          
          <p class="text-slate-300 text-sm leading-relaxed">
            يتمركز أسطول <strong class="text-amber-400">ونش إنقاذ حجازي</strong> عند التقاطع الاستراتيجي الحيوي بين <strong>الطريق الدائري</strong> و<strong>طريق مصر الإسماعيلية الصحراوي</strong> أمام <strong>كارفور العبور وجولف سيتي مول</strong>، مما يتيح لأوناشنا الانطلاق الفوري والوصول خلال <strong>8 إلى 12 دقيقة فقط</strong> لكافة مناطق العبور، الشروق، مدينتي، التجمع، مدينة نصر، مصر الجديدة، والسلام.
          </p>

          <div class="space-y-2.5 text-xs text-slate-300 pt-2">
            <div class="flex items-start gap-2.5 p-3 rounded-xl bg-slate-950/70 border border-slate-800">
              <span class="text-base text-amber-400">📍</span>
              <div>
                <strong class="text-white block mb-0.5">نقطة التمركز الدقيقة:</strong>
                كارفور العبور - جولف سيتي مول، تقاطع الطريق الدائري ومحور الإسماعيلية
              </div>
            </div>
            <div class="flex items-start gap-2.5 p-3 rounded-xl bg-slate-950/70 border border-slate-800">
              <span class="text-base text-emerald-400">⚡</span>
              <div>
                <strong class="text-white block mb-0.5">سرعة الاستجابة الميدانية:</strong>
                تحرك فوري خلال دقيقة واحدة، وصول لموقعك خلال 8 - 12 دقيقة
              </div>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row items-center gap-3 pt-3">
            <a href="{MAPS_URL}" target="_blank" class="w-full sm:w-auto px-6 py-3.5 bg-slate-900 border-2 border-emerald-500/50 hover:border-emerald-400 text-emerald-400 font-extrabold rounded-xl transition flex items-center justify-center gap-2 text-sm shadow-lg">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
              <span>فتح في تطبيق خرائط Google</span>
            </a>
            <a href="tel:{PHONE}" class="w-full sm:w-auto px-6 py-3.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black rounded-xl text-sm shadow-lg glow-red flex items-center justify-center gap-2">
              <span>طلب الونش فوراً ({PHONE_DISPLAY})</span>
            </a>
          </div>
        </div>

        <!-- Map Iframe Column -->
        <div class="lg:col-span-7">
          <div class="relative rounded-3xl overflow-hidden border-2 border-amber-500/30 shadow-2xl bg-slate-950 aspect-[16/10] sm:aspect-[16/9]">
            <iframe 
              src="{MAPS_EMBED_URL}" 
              width="100%" 
              height="100%" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              title="موقع ونش إنقاذ حجازي كارفور العبور خرائط جوجل"
              class="w-full h-full grayscale-[20%] contrast-[110%] hover:grayscale-0 transition-all duration-300">
            </iframe>
            
            <div class="absolute bottom-3 right-3 bg-slate-950/90 backdrop-blur-md px-3 py-1.5 rounded-xl border border-amber-500/30 text-[11px] text-amber-300 font-bold flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>نقطة تمركز ونش حجازي الرسمية (كارفور العبور)</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
'''
"""
if "def get_map_section" not in code:
    code += "\n" + map_section_func

with open(helpers_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_winch_helpers.py with real Google Maps data!")


# 2. Update generate_winch_hegazy_site.py to include map section in index.html
site_script_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_script_path, "r", encoding="utf-8") as f:
    site_code = f.read()

# Add get_map_section to imports
if "get_map_section" not in site_code:
    site_code = site_code.replace("generate_local_business_schema, generate_faq_schema", "generate_local_business_schema, generate_faq_schema, get_map_section, MAPS_URL")

# Insert get_map_section() right after Real Fleet Photo Gallery
gallery_marker = "<!-- FAQ Section (AEO Structured for Google & AI Overviews) -->"
if "{get_map_section()}" not in site_code:
    site_code = site_code.replace(gallery_marker, "{get_map_section()}\n\n  " + gallery_marker)

with open(site_script_path, "w", encoding="utf-8") as f:
    f.write(site_code)

print("Updated generate_winch_hegazy_site.py with map section on index.html!")


# 3. Update generate_all_winch_pages.py to include map section in contact.html & coverage.html
all_pages_path = os.path.join(scripts_dir, "generate_all_winch_pages.py")
with open(all_pages_path, "r", encoding="utf-8") as f:
    pages_code = f.read()

if "get_map_section" not in pages_code:
    pages_code = pages_code.replace("generate_local_business_schema, generate_faq_schema", "generate_local_business_schema, generate_faq_schema, get_map_section, MAPS_URL")

# Insert in contact.html right before get_footer
contact_footer = "{get_footer()}\n</body>\n</html>\n\"\"\"\n\nwith open(os.path.join(base_dir, \"contact.html\")"
if "{get_map_section()}" not in pages_code:
    pages_code = pages_code.replace(contact_footer, "{get_map_section()}\n\n" + contact_footer)

# Update llms.txt with exact map link
if "خرائط Google" not in pages_code:
    pages_code = pages_code.replace(
        "- **رابط واتساب لتحديد الموقع:** {WHATSAPP_LINK}",
        "- **رابط واتساب لتحديد الموقع:** {WHATSAPP_LINK}\n- **موقع الارتكاز الميداني على خرائط Google:** https://maps.app.goo.gl/4JvQjcJFPNFqesXS7\n- **العنوان الدقيق:** كارفور العبور، جولف سيتي مول، تقاطع الطريق الدائري ومحور الإسماعيلية الصحراوي."
    )

with open(all_pages_path, "w", encoding="utf-8") as f:
    f.write(pages_code)

print("Updated generate_all_winch_pages.py with map section in contact.html and llms.txt!")

print("SUCCESS: Google Maps integration script ready!")
