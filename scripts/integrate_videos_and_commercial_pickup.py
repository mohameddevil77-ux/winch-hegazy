# -*- coding: utf-8 -*-
import os, re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# =====================================================================
# 1. Update generate_winch_hegazy_site.py
# =====================================================================
gen_site_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(gen_site_path, "r", encoding="utf-8") as f:
    s_code = f.read()

# 1.1 Add 12th Photo Card (Commercial Pickup Night) to Gallery
pickup_card = '''        <!-- Photo 12: Night Commercial Pickup Cargo -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_night_commercial_pickup.jpg" alt="نقل سيارات النقل التجاري والربع نقل بحمولتها ليلاً ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-emerald-600/90 text-white text-[10px] font-black tracking-wider uppercase">نقل تجاري وبضائع</span>
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل سيارات النقل التجاري بحمولتها</h4>
            <p class="text-slate-400 text-xs">سحب وتأمين سيارات الربع نقل المحملة بالبضائع ليلاً على الطرق السريعة دون الحاجة لتفريغ الشحنة.</p>
          </div>
        </div>
'''

target_forklift_end = s_code.find('alt="سحب ونقل الرافعات الشوكية والمعدات الثقيلة في المصانع والصوامع"')
if target_forklift_end != -1:
    target_card_end = s_code.find('</div>\n        </div>\n</div>\n    </div>\n  </section>', target_forklift_end)
    if target_card_end != -1:
        s_code = s_code[:target_card_end + 15] + "\n" + pickup_card + s_code[target_card_end + 15:]
        print("SUCCESS: Added 12th photo card to gallery in generate_winch_hegazy_site.py")
    else:
        target_card_end2 = s_code.find('</div>\n</div>\n    </div>\n  </section>', target_forklift_end)
        if target_card_end2 != -1:
            s_code = s_code[:target_card_end2 + 6] + "\n" + pickup_card + s_code[target_card_end2 + 6:]
            print("SUCCESS: Added 12th photo card (fallback) in generate_winch_hegazy_site.py")
        else:
            print("WARNING: Could not find card end for forklift")
else:
    print("WARNING: Forklift photo card not found in generate_winch_hegazy_site.py")


# 1.2 Add Video Showcase Section below the photo gallery
video_showcase_html = '''
  <!-- Video Showcase Section: Authentic Live Field Operations (E-E-A-T & Video SEO) -->
  <section id="videos" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-slate-800/80 bg-gradient-to-b from-dark-950 via-slate-950 to-dark-950">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-black bg-red-500/15 text-red-400 border border-red-500/30 mb-4 animate-pulse">
        <span class="w-2 h-2 rounded-full bg-red-500"></span>
        توثيق حي بالصوت والصورة من الميدان
      </div>
      <h3 class="text-3xl sm:text-4xl font-black text-white leading-tight">
        فيديوهات حصرية لعمليات أسطول <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500">ونش حجازي الميدانية</span>
      </h3>
      <p class="text-slate-400 text-sm sm:text-base mt-4">
        شاهد بالصوت والصورة احترافية سحب ونقل سيارات السوبر كار ليلاً، تحميل اللوادر والمعدات الهندسية، وإنقاذ سيارات النقل التجاري بحمولتها بأحدث تقنيات السلامة في مصر.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Video 1: Lamborghini Supercar Night -->
      <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all flex flex-col justify-between shadow-2xl bg-slate-900/60 group">
        <div class="relative bg-black rounded-t-3xl overflow-hidden aspect-[9/16] max-h-[520px] flex items-center justify-center">
          <video controls playsinline preload="metadata" poster="assets/images/poster_lamborghini_night.jpg" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_lamborghini_vip_night.mp4" type="video/mp4">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🏎️</span>
            <span>سوبر كار VIP ليلاً</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h4 class="text-white font-extrabold text-base">توثيق سحب سيارة لامبورجيني هوراكان ليلاً</h4>
          <p class="text-slate-400 text-xs leading-relaxed">
            شاهد منظومة الإضاءة التوجيهية وتثبيت السيارة الخارقة بأربطة العجلات المخصصة دون أدنى ملامسة للشاسيه أو الصدام الرياضي المنخفض.
          </p>
          <div class="pt-2 flex items-center justify-between border-t border-slate-800 text-[11px] text-slate-400">
            <span class="text-amber-400 font-bold">✓ أربطة عجلات مطاطية</span>
            <span>تأمين شامل 100%</span>
          </div>
        </div>
      </div>

      <!-- Video 2: Caterpillar Heavy Loader Day -->
      <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all flex flex-col justify-between shadow-2xl bg-slate-900/60 group">
        <div class="relative bg-black rounded-t-3xl overflow-hidden aspect-[9/16] max-h-[520px] flex items-center justify-center">
          <video controls playsinline preload="metadata" poster="assets/images/poster_caterpillar_loader.jpg" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_caterpillar_loader_day.mp4" type="video/mp4">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🏗️</span>
            <span>لودر كاتربيلر CAT 930</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h4 class="text-white font-extrabold text-base">تحميل ونقل لودر CAT 930 للمشروعات</h4>
          <p class="text-slate-400 text-xs leading-relaxed">
            استعراض عملي لقوة الطبلية الهيدروليكية لحجازي وقدرتها على سحب وتحميل اللوادر الضخمة ومعدات الحفر ونقلها لمواقع العمل.
          </p>
          <div class="pt-2 flex items-center justify-between border-t border-slate-800 text-[11px] text-slate-400">
            <span class="text-amber-400 font-bold">✓ حمولات هيدروليكية شاقة</span>
            <span>تثبيت بجنازير صلب</span>
          </div>
        </div>
      </div>

      <!-- Video 3: Commercial Pickup Cargo Night -->
      <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all flex flex-col justify-between shadow-2xl bg-slate-900/60 group">
        <div class="relative bg-black rounded-t-3xl overflow-hidden aspect-[9/16] max-h-[520px] flex items-center justify-center">
          <video controls playsinline preload="metadata" poster="assets/images/poster_commercial_pickup.jpg" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_commercial_pickup_night.mp4" type="video/mp4">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🚚</span>
            <span>نقل بضائع وتجاري</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h4 class="text-white font-extrabold text-base">إنقاذ سيارة ربع نقل محملة بالبضائع ليلاً</h4>
          <p class="text-slate-400 text-xs leading-relaxed">
            توثيق سحب وتأمين شاحنة بضائع تجارية بحمولتها الكاملة على الطريق السريع ليلاً بأضواء ليد محيطية لحماية الشحنة وسلامة الطريق.
          </p>
          <div class="pt-2 flex items-center justify-between border-t border-slate-800 text-[11px] text-slate-400">
            <span class="text-amber-400 font-bold">✓ بدون تفريغ الشحنة</span>
            <span>إضاءات ليلية تحذيرية</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Quick Call Banner Below Videos -->
    <div class="mt-12 glass p-6 rounded-3xl border border-amber-500/30 flex flex-col sm:flex-row items-center justify-between gap-6 max-w-4xl mx-auto bg-slate-900/50">
      <div class="flex items-center gap-4 text-right">
        <span class="text-4xl">📹</span>
        <div>
          <h5 class="text-white font-black text-base">هل تحتاج ونش إنقاذ بمواصفات خاصة الآن؟</h5>
          <p class="text-slate-400 text-xs mt-0.5">سواء سيارة ملاكي، فارهة، لودر، أو نقل تجاري.. أسطولنا الميداني يصلك خلال 15 دقيقة.</p>
        </div>
      </div>
      <div class="flex items-center gap-3 w-full sm:w-auto">
        <a href="tel:01032194206" class="w-full sm:w-auto px-6 py-3 rounded-2xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black text-sm text-center shadow-lg shadow-amber-500/25 transition-all flex items-center justify-center gap-2">
          <span>📞</span>
          <span>اتصل فوراً 01032194206</span>
        </a>
      </div>
    </div>
  </section>
'''

map_target = s_code.find('{get_map_section()}')
if map_target != -1:
    s_code = s_code[:map_target] + video_showcase_html + "\n\n  " + s_code[map_target:]
    print("SUCCESS: Inserted Video Showcase section before get_map_section() in generate_winch_hegazy_site.py")
else:
    print("WARNING: Could not find get_map_section() in generate_winch_hegazy_site.py")

# 1.3 Add VideoObject Schema to head in generate_winch_hegazy_site.py
video_schema_code = '''
  <script type="application/ld+json">
  [
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
  </script>
'''

head_close_idx = s_code.find('</head>')
if head_close_idx != -1:
    s_code = s_code[:head_close_idx] + video_schema_code + "\n" + s_code[head_close_idx:]
    print("SUCCESS: Inserted VideoObject Schema in head of generate_winch_hegazy_site.py")

with open(gen_site_path, "w", encoding="utf-8") as f:
    f.write(s_code)
print("SUCCESS: Saved updated generate_winch_hegazy_site.py")


# =====================================================================
# 2. Update build_articles_engine.py with Commercial Pickups Service
# =====================================================================
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    e_code = f.read()

new_service_dict = '''    {
        "id": "commercial-pickups",
        "icon": "🚚",
        "title": "نقل سيارات النقل التجاري والربع نقل بحمولتها ليلاً ونهاراً",
        "image": "hegazy_night_commercial_pickup.jpg",
        "desc": "خدمة حصرية مخصصة لأصحاب سيارات النقل التجاري والربع نقل والجامبو المحملة بالبضائع، الخضار، والطرود المعطلة على الطرق السريعة ليلاً. نقوم بسحب وتأمين السيارة بحمولتها بالكامل دون الحاجة لتفريغ البضاعة أو تعريضها للتلف أو السرقة.",
        "features": ["تأمين كامل للبضائع والمشمعات أثناء السحب", "أحزمة ربط شديدة المتانة ضد الاهتزاز", "إنقاذ ليلي فوري على طريقي السويس والإسماعيلية والدائري", "إضاءة ليد وتحذيرات سلامة ليلية للمقطورة"]
    },
'''

semi_trucks_target = e_code.find('"id": "semi-trucks",')
if semi_trucks_target != -1:
    card_dict_start = e_code.rfind('{', 0, semi_trucks_target)
    e_code = e_code[:card_dict_start] + new_service_dict + e_code[card_dict_start:]
    print("SUCCESS: Added commercial-pickups service to services_list in build_articles_engine.py")
else:
    print("WARNING: semi-trucks not found in build_articles_engine.py")

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(e_code)
print("SUCCESS: Saved updated build_articles_engine.py")
