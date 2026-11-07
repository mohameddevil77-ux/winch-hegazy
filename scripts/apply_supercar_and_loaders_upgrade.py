import os
import re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update generate_winch_hegazy_site.py Gallery
site_gen_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_gen_path, "r", encoding="utf-8") as f:
    s_code = f.read()

new_gallery_cards = '''        <!-- Photo 1: Lamborghini Supercar Night -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_lamborghini_night.jpg" alt="نقل سيارات السوبر كار لامبورجيني ليلاً ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-rescue-600/90 text-white text-[10px] font-black tracking-wider uppercase">سوبر كار VIP</span>
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل سيارات السوبر كار (لامبورجيني هوراكان)</h4>
            <p class="text-slate-400 text-xs">سحب وتثبيت السيارات الفارهة والخارقة ليلاً بأربطة عجلات مطاطية وإضاءات تأمين كاملة.</p>
          </div>
        </div>

        <!-- Photo 2: Caterpillar Heavy Loader -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_caterpillar_loader.jpg" alt="نقل لودر كاتربيلر CAT 930 ونش حجازي للمعدات الثقيلة" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-amber-500/90 text-slate-950 text-[10px] font-black tracking-wider">معدات ثقيلة</span>
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل اللوادر والمعدات (كاتربيلر CAT 930)</h4>
            <p class="text-slate-400 text-xs">قدرات شاقة لنقل لوادر ومعدات الإنشاءات والحفر لمواقع المشروعات والعاصمة الإدارية.</p>
          </div>
        </div>

        <!-- Photo 3: Construction Loader Desert Project -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_heavy_equipment_loader.jpg" alt="نقل معدات الحفر والصحراء لودر WA100 ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-slate-800 text-amber-300 text-[10px] font-black">مواقع ومحاجر</span>
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">خدمة مواقع العمل الصحراوية والمحاجر</h4>
            <p class="text-slate-400 text-xs">نقل معدات البناء والصوامع (لودر WA100) بين المشروعات في بدر والعبور والإسماعيلية.</p>
          </div>
        </div>

        <!-- Photo 4: Red Hegazy Truck Brand -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_branding.jpg" alt="ونش حجازي المعتمد HEGAZY وأرقام الطوارئ الميدانية الرسمية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">ونش حجازي الرسمي المعتمد (HEGAZY)</h4>
            <p class="text-slate-400 text-xs">أسطول إيسوزو حديث مرخص يحمل شعار وأرقام طوارئ ونش حجازي الميدانية.</p>
          </div>
        </div>

        <!-- Photo 5: Porsche Highway Flatbed -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_orange_truck_porsche.jpg" alt="إنقاذ سيارات الدفع الرباعي بورش على الطرق السريعة" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">إنقاذ سيارات الدفع الرباعي والبورش</h4>
            <p class="text-slate-400 text-xs">تأمين نقل سيارات الـ SUV الفارهة على الطريق الدائري والصحراوي والسويس.</p>
          </div>
        </div>

        <!-- Photo 6: Luxury Cupra Crossover -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_luxury_car_flatbed.jpg" alt="سحب وتثبيت السيارات الفاخرة والرياضية بأربطة الإطارات بدون خدوش" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">عناية فائقة بالسيارات الحديثة</h4>
            <p class="text-slate-400 text-xs">تثبيت احترافي بأحزمة الإطارات (Wheel Straps) يمنع أي احتكاك أو ضرر بالهيكل.</p>
          </div>
        </div>

        <!-- Photo 7: Tractor Head Heavy Recovery -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_semi_truck_head.jpg" alt="سحب وإنقاذ رؤوس التريلات والشاحنات الضخمة Actros على ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">سحب رؤوس التريلات والشاحنات</h4>
            <p class="text-slate-400 text-xs">إنقاذ ميكانيكي للشاحنات التريلا المعطلة وتوصيلها لورش ومراكز الصيانة المعتمدة.</p>
          </div>
        </div>

        <!-- Photo 8: Caravans Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_caravan_transport.jpg" alt="نقل الكرفانات والمكاتب الإدارية ومواقع الإنشاءات على ونش حجازي مسطح" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل الكرفانات والوحدات المتنقلة</h4>
            <p class="text-slate-400 text-xs">أبعاد طبلية ممتدة حتى 12 متراً لنقل غرف الحراسة ومكاتب المواقع والمشروعات.</p>
          </div>
        </div>

        <!-- Photo 9: Golf Carts Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_golf_carts_transport.jpg" alt="نقل عربات الجولف كارت للمنتجعات والملاعب والقرى السياحية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل عربات الجولف كارت (حمولة مزدوجة)</h4>
            <p class="text-slate-400 text-xs">خدمة مخصصة للمنتجعات والقرى السياحية والمجمعات المغلقة في مدينتي والرحاب.</p>
          </div>
        </div>

        <!-- Photo 10: Food Trucks Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_food_truck_transport.jpg" alt="نقل عربات الطعام المتنقلة فود تراك والمقطورات التجارية على ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل عربات الطعام (Food Trucks)</h4>
            <p class="text-slate-400 text-xs">توصيل آمن للمقطورات التجارية وأكشاك الطعام للمعارض والمهرجانات والساحات.</p>
          </div>
        </div>

        <!-- Photo 11: Heavy Forklifts Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_heavy.jpg" alt="سحب ونقل الرافعات الشوكية والمعدات الثقيلة في المصانع والصوامع" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل المعدات والرافعات الشوكية (TCM)</h4>
            <p class="text-slate-400 text-xs">قدرات جر وسحب فائقة لنقل معدات المصانع، الفورك لفت، والشاحنات في المناطق الصناعية.</p>
          </div>
        </div>
'''

old_gallery_target = s_code.find("<!-- Photo 1: Red Hegazy Truck Brand -->")
idx_grid_end = s_code.find("</div>\n    </div>\n  </section>\n\n  {get_m", old_gallery_target)
if old_gallery_target != -1 and idx_grid_end != -1:
    s_code = s_code[:old_gallery_target] + new_gallery_cards + s_code[idx_grid_end:]
    with open(site_gen_path, "w", encoding="utf-8") as f:
        f.write(s_code)
    print("SUCCESS: Updated index.html gallery with Lamborghini and Caterpillar loaders!")
else:
    print("WARNING: Could not match gallery bounds in generate_winch_hegazy_site.py")


# 2. Update build_articles_engine.py services list images
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    e_code = f.read()

# Replace private-cars image with hegazy_lamborghini_night.jpg
e_code = e_code.replace(
    '"id": "private-cars",\n        "icon": "🚗",\n        "title": "إنقاذ وسحب سيارات الملاكي والحديثة",\n        "image": "hegazy_luxury_car_flatbed.jpg"',
    '"id": "private-cars",\n        "icon": "🚗",\n        "title": "إنقاذ وسحب سيارات الملاكي والفاخرة والسوبر كار",\n        "image": "hegazy_lamborghini_night.jpg"'
)

# Replace heavy-machinery image with hegazy_caterpillar_loader.jpg
e_code = e_code.replace(
    '"id": "heavy-machinery",\n        "icon": "🏗️",\n        "title": "نقل المعدات الثقيلة والكلاركات والروافع الشوكية",\n        "image": "hegazy_red_truck_heavy.jpg"',
    '"id": "heavy-machinery",\n        "icon": "🏗️",\n        "title": "نقل المعدات الثقيلة واللوادر والكلاركات",\n        "image": "hegazy_caterpillar_loader.jpg"'
)

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(e_code)
print("SUCCESS: Updated services_list images in build_articles_engine.py!")
