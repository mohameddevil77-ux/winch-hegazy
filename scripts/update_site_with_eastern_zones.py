import os
import sys

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update build_articles_engine.py with the 4 new articles metadata and updated zones
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    code = f.read()

# Add 4 articles to articles list if not present
if "winch-obour-city" not in code:
    new_articles_metadata = """
    {
        "slug": "winch-obour-city",
        "title": "ونش إنقاذ مدينة العبور: أسرع ونش سيارات عند كارفور وجولف سيتي وسوق العبور 24 ساعة",
        "desc": "خدمات ونش إنقاذ سيارات في مدينة العبور من ونش حجازي. ارتكاز رئيسي أمام كارفور العبور وجولف سيتي وسوق العبور والحي الأول حتى التاسع. وصول خلال 5 إلى 8 دقائق. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ مدينة العبور", "ونش العبور", "ونش كارفور العبور", "ونش سوق العبور", "ونش جولف سيتي"]
    },
    {
        "slug": "winch-shorouk-badr",
        "title": "ونش إنقاذ مدينة الشروق ومدينة بدر: أوناش متمركزة على طريق السويس والإسماعيلية والروبيكي",
        "desc": "طلب ونش إنقاذ سيارات في مدينة الشروق ومدينة بدر من ونش حجازي 24 ساعة. أوناش حديثة تغطي الروبيكي، هليوبوليس الجديدة، الجامعة البريطانية والروسية. اتصل الآن 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ مدينة الشروق", "ونش الشروق", "ونش مدينة بدر", "ونش الروبيكي", "ونش هليوبوليس الجديدة"]
    },
    {
        "slug": "winch-new-capital",
        "title": "ونش إنقاذ العاصمة الإدارية الجديدة: خدمة VIP على محور بن زايد والحي الحكومي والمال والأعمال",
        "desc": "خدمات ونش إنقاذ سيارات في العاصمة الإدارية الجديدة من ونش حجازي. أحدث أسطول هيدروليكي مسطح لنقل السيارات الفاخرة في الحي الحكومي والبرج الأيقوني والدائري الأوسطي 24/7. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ العاصمة الادارية", "ونش العاصمة الادارية", "ونش محور بن زايد", "ونش البرج الايقوني", "ونش الدائري الاوسطي"]
    },
    {
        "slug": "winch-salam-herfeyein-nahda",
        "title": "ونش إنقاذ مدينة السلام والحرفيين والنهضة: أسرع سحب عند موقف العاشر ومحطة عدلي منصور",
        "desc": "طلب ونش إنقاذ سيارات في مدينة السلام، الحرفيين، مساكن النهضة، وموقف العاشر من ونش حجازي 24 ساعة. سحب فوري ونقل مباشر لأكبر ورش الصيانة والتوكيلات بأرخص سعر. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ الحرفيين", "ونش مدينة السلام", "ونش النهضة", "ونش موقف العاشر", "ونش محطة عدلي منصور"]
    },
"""
    # Insert right before the last closing bracket of articles = [...]
    last_art = '"keywords": ["ونش انقاذ في الجيزة", "ونش الهرم", "ونش فيصل", "ونش حدائق الاهرام", "ونش الرماية"]\n    }'
    if last_art in code:
        code = code.replace(last_art, last_art + "," + new_articles_metadata)
    else:
        print("Note: last_art pattern needed adjustment")

# Update coverage zones in code to give top priority to user's zones
updated_zones = """zones = [
    {
        "name": "مدينة العبور، الشروق، بدر، والمستقبل",
        "tag": "المقر الرئيسي • وصول خلال 5 إلى 8 دقائق",
        "places": "كارفور العبور، جولف سيتي مول، سوق العبور، الأحياء 1-9، مدينة الشروق بوابات 1-3، مدينة بدر، المستقبل سيتي، والمنطقة الصناعية بالروبيكي.",
        "winches": "10 أوناش متمركزة لحظياً"
    },
    {
        "name": "العاصمة الإدارية الجديدة ومدينتي",
        "tag": "تغطية VIP سريعة 24/7",
        "places": "الحي الحكومي، حي السفارات، البرج الأيقوني، محور محمد بن زايد، الدائري الأوسطي، بوابات مدينتي، ساوث بارك، والكرافت زون.",
        "winches": "8 أوناش هيدروليكية جاهزة"
    },
    {
        "name": "مدينة السلام، الحرفيين، والنهضة",
        "tag": "إنقاذ مباشر لمراكز وورش الصيانة",
        "places": "مجمع ورش الحرفيين، موقف العاشر، محطة عدلي منصور المركزية، مساكن النهضة، مدينة السلام 1 و 2، وكوبري التعمير وجسر السويس.",
        "winches": "7 أوناش متأهبة لنقل الأعطال"
    },
    {
        "name": "طريق مصر الإسماعيلية وطريق السويس",
        "tag": "طوارئ الطرق السريعة ومصايف 24 ساعة",
        "places": "طريق الإسماعيلية الصحراوي، المركز الطبي العالمي، مخرج العاشر من رمضان، طريق السويس، بوابات الشروق ومدينتي وبوابات السخنة.",
        "winches": "8 أوناش سريعة مخصصة"
    },
    {
        "name": "الطريق الدائري ومحور 26 يوليو",
        "tag": "تغطية لحظية خلال 8 دقائق",
        "places": "دائري السلام، المرج، مسطرد، الوراق، المنيب، المريوطية، صفط اللبن، ومحور 26 يوليو من ميدان لبنان حتى بوابات زايد وأكتوبر.",
        "winches": "12 ونش متمركز على مدار الساعة"
    },
    {
        "name": "القاهرة الجديدة والتجمع الخامس",
        "tag": "تغطية شاملة لكافة الأحياء",
        "places": "التجمع الأول، الخامس، الثالث، شارع التسعين الشمالي والجنوبي، الرحاب، الأكاديمية، والبنفسج والياسمين والنرجس.",
        "winches": "8 أوناش متمركزة جاهزة"
    }
]"""

# Replace zones in code
zones_pattern_start = "zones = ["
zones_pattern_end = "html_coverage = f\"\"\""
s = code.find(zones_pattern_start)
e = code.find(zones_pattern_end)
if s != -1 and e != -1:
    code = code[:s] + updated_zones + "\n\n" + code[e:]
    print("Updated coverage zones successfully!")

# Update badges in coverage.html navigation
old_badges = """        <a href="blog/winch-enqaz-cairo.html" class="p-3 rounded-xl bg-slate-900 border border-amber-500/40 text-amber-300 hover:bg-amber-500 hover:text-black transition shadow">
          🚗 ونش إنقاذ القاهرة
        </a>"""

new_badges = """        <a href="blog/winch-obour-city.html" class="p-3 rounded-xl bg-slate-900 border-2 border-emerald-500/60 text-emerald-300 hover:bg-emerald-500 hover:text-black transition shadow font-black">
          ⭐ مدينة العبور (المقر)
        </a>
        <a href="blog/winch-shorouk-badr.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 الشروق وبدر
        </a>
        <a href="blog/winch-new-capital.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 العاصمة الإدارية
        </a>
        <a href="blog/winch-rehab-madinaty.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 مدينتي والمستقبل
        </a>
        <a href="blog/winch-salam-herfeyein-nahda.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 السلام والحرفيين
        </a>
        <a href="blog/winch-salam-herfeyein-nahda.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 النهضة وموقف العاشر
        </a>
        <a href="blog/winch-enqaz-cairo.html" class="p-3 rounded-xl bg-slate-900 border border-amber-500/40 text-amber-300 hover:bg-amber-500 hover:text-black transition shadow">
          🚗 ونش إنقاذ القاهرة
        </a>"""

if old_badges in code:
    code = code.replace(old_badges, new_badges)
    print("Updated coverage badges navigation successfully!")

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_articles_engine.py with all new zones and articles!")


# 2. Update generate_winch_hegazy_site.py to add these cities to calculator dropdown
site_path = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_path, "r", encoding="utf-8") as f:
    site_code = f.read()

calc_options = """              <option value="obour" selected>مدينة العبور (كارفور / سوق العبور / جولف سيتي)</option>
              <option value="shorouk">مدينة الشروق (بوابات طريق السويس والإسماعيلية)</option>
              <option value="badr">مدينة بدر / المنطقة الصناعية بالروبيكي</option>
              <option value="mostaqbal">مدينة المستقبل سيتي / محور الأمل</option>
              <option value="madinaty">مدينتي / الكرافت زون / ساوث بارك</option>
              <option value="capital">العاصمة الإدارية الجديدة / الحي الحكومي والبرج الأيقوني</option>
              <option value="salam">مدينة السلام / مساكن النهضة / ترعة الإسماعيلية</option>
              <option value="herfeyein">الحرفيين / سوق القناة / محطة عدلي منصور</option>
              <option value="ismailia_road">طريق مصر الإسماعيلية الصحراوي / المركز الطبي</option>
              <option value="suez_road">طريق السويس الصحراوي / مدينتي وبدر</option>
              <option value="daeri">الطريق الدائري (دائري السلام والمعادي والمرج)</option>
              <option value="tagamoa">التجمع الخامس / القاهرة الجديدة / شارع التسعين</option>
              <option value="zayed">الشيخ زايد / محور 26 يوليو</option>
              <option value="october">مدينة 6 أكتوبر / المنطقة الصناعية</option>
              <option value="nasrcity">مدينة نصر / مصر الجديدة / صلاح سالم</option>
              <option value="maadi">المعادي / الأوتوستراد / صقر قريش</option>
              <option value="giza">الجيزة / فيصل / الهرم / حدائق الأهرام</option>
              <option value="alex">طريق مصر إسكندرية الصحراوي</option>"""

start_opt_marker = "<select id=\"startLoc\" class=\"w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white font-bold focus:border-amber-400 focus:outline-none\">"
end_opt_marker = "</select>"

s = site_code.find(start_opt_marker)
if s != -1:
    e = site_code.find(end_opt_marker, s)
    site_code = site_code[:s + len(start_opt_marker)] + "\n" + calc_options + "\n            " + site_code[e:]
    print("Updated calculator start location dropdown with all user's cities!")

with open(site_path, "w", encoding="utf-8") as f:
    f.write(site_code)

print("Updated generate_winch_hegazy_site.py successfully!")
