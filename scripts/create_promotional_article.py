import os
import sys

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")
sys.path.append(scripts_dir)

from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, PHONE_ALT, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema
)
from build_articles_engine import generate_article_file

promo_article = {
    "slug": "winch-offers-discounts-cairo",
    "image": "hegazy_red_truck_branding.webp",
    "title": "عروض وخصومات أوناش إنقاذ أولاد حجازي: خصم 50% لأول 100 عميل، بدون إكرامية للسائق، ومساهمة في رسوم الكارتة",
    "desc": "تعرف على عروض وخصومات أوناش أولاد حجازي لإنقاذ السيارات 2026: خصم يصل إلى 50% لأول 100 عميل، بدون أي إكرامية إجبارية للسائق، ومساهمة في دفع رسوم الكارتة للطرق السريعة مع أسعار حقيقية تبدأ من 750 ج.م.",
    "date": "2026-11-06",
    "category": "عروض وشفافية الأسعار 2026",
    "read_time": "5 دقائق",
    "keywords": ["عروض ونش انقاذ", "خصم ونش سيارات", "ارخص ونش سيارات في مصر", "اسعار ونش الانقاذ بعد البنزين", "ونش بدون اكرامية"],
    "content": f"""
<div class="glass p-6 sm:p-8 rounded-3xl border border-emerald-500/40 mb-10 bg-gradient-to-br from-slate-900 to-emerald-950/40">
  <div class="flex items-center gap-3 mb-4">
    <span class="px-3.5 py-1 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">عرض الموسم الحصري 2026</span>
    <span class="text-xs text-slate-400">ساري حتى اكتمال العدد</span>
  </div>
  <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">كود الخصم الحصري: <span class="text-amber-400 font-mono tracking-wider bg-slate-950 px-3 py-1 rounded-xl border border-amber-500/40">HEGAZY50</span></h2>
  <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6 font-medium">
    احصل فوراً على <strong>خصم يصل إلى 50%</strong> على مشوار سحب وإنقاذ سيارتك من أسطول <strong>أوناش إنقاذ أولاد حجازي</strong>. اذكر كود الخصم <strong>(HEGAZY50)</strong> لمسؤول العمليات أثناء المكالمة وسيتم تطبيق الخصم مباشرة على الفاتورة التقديرية.
  </p>
  <div class="flex flex-wrap items-center gap-3">
    <a href="tel:{PHONE}" class="px-6 py-3.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black rounded-xl text-sm shadow-lg glow-red hover:opacity-95 transition flex items-center gap-2">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
      <span>اتصل واستفد من الخصم: {PHONE_DISPLAY}</span>
    </a>
    <a href="{WHATSAPP_LINK}&text=أريد%20الاستفادة%20من%20كود%20خصم%20HEGAZY50%20لونش%20الإنقاذ" target="_blank" class="px-5 py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-sm transition">
      تفعيل الخصم على واتساب
    </a>
  </div>
</div>

<h2 class="text-xl sm:text-2xl font-black text-amber-300 mt-10 mb-4">1. الشفافية والمصداقية: لماذا تبدأ أسعار أوناش أولاد حجازي من 750 جنيه؟</h2>
<p class="leading-relaxed">
  مع الارتفاعات المتتالية في <strong>أسعار البنزين والسولار وتكاليف تشغيل وصيانة أوناش الإنقاذ الهيدروليكية الحديثة لعام 2026</strong>، يلاحظ الكثير من قائدي السيارات وجود إعلانات مضللة على الإنترنت تدعي أسعاراً وهمية مثل <em>"ونش إنقاذ بـ 200 أو 750 جنيه"</em>.
</p>
<p class="leading-relaxed">
  ولكن ما يحدث على أرض الواقع عند الاتصال بهذه الأرقام، هو أن السائق يفاجئ العميل بعد وصوله بمضاعفة السعر أو طلب 800 إلى 1200 جنيه تحت مسميات "فرق مسافة" أو "سعر السولار الجديد"، مما يضع العميل في موقف حرج وهو متعطل في الشارع.
</p>
<p class="leading-relaxed">
  في <strong>أوناش إنقاذ أولاد حجازي</strong>، نؤمن بأن <strong>المصداقية والأمانة هي رأس مالنا الحقيقي</strong>. لذلك، حددنا تسعيرة واقعية ومحسوبة بدقة تبدأ من <strong>750 جنيه مصري</strong> للسحب الداخلي، ونبلغ العميل بالسعر النهائي الصافي قبل تحرك الونش إليه، وما نتفق عليه في الهاتف هو ما يتم دفعه بالضبط بدون زيادة مليم واحد.
</p>

<h2 class="text-xl sm:text-2xl font-black text-amber-300 mt-10 mb-4">2. سياسة "بدون أي إكرامية إجبارية للسائق" (No Mandatory Tips)</h2>
<p class="leading-relaxed">
  نعلم أن لحظة تعطل السيارة أو وقوع حادث لا قدر الله هي لحظة ضغط عصبي وتوتر. لذلك وضعنا قاعدة صارمة في إدارة أوناش أولاد حجازي:
</p>
<div class="glass p-5 rounded-2xl border border-slate-700 bg-slate-900/60 my-4 space-y-3">
  <div class="flex items-center gap-3 text-emerald-400 font-bold">
    <span class="text-xl">✓</span>
    <span>رواتب وحوافز مجزية: سائقو وفنيو أسطول أوناش أولاد حجازي يتقاضون أجوراً كريمة ومكافآت عن كل عملية إنقاذ ناجحة.</span>
  </div>
  <div class="flex items-center gap-3 text-emerald-400 font-bold">
    <span class="text-xl">✓</span>
    <span>منع طلب أي بقشيش: يُحظر تماماً على أي سائق طلب "إكرامية" أو "شاي" أو إحراج العميل بأي شكل من الأشكال.</span>
  </div>
  <div class="flex items-center gap-3 text-emerald-400 font-bold">
    <span class="text-xl">✓</span>
    <span>السعر المتفق عليه نهائي وشامل: المبلغ المتفق عليه مسبقاً هو المبلغ الوحيد المطلوب سداده.</span>
  </div>
</div>

<h2 class="text-xl sm:text-2xl font-black text-amber-300 mt-10 mb-4">3. مساهمة أوناش أولاد حجازي في دفع رسوم الكارتة للطرق السريعة</h2>
<p class="leading-relaxed">
  إذا تعطلت سيارتك على أحد الطرق السريعة المزودة ببوابات رسوم (مثل <strong>طريق مصر - الإسماعيلية الصحراوي، طريق القاهرة - السويس الصحراوي، طريق العين السخنة، أو الطريق الدائري الإقليمي</strong>)، فإننا في أوناش أولاد حجازي نتحمل أو نساهم في دفع جزء من رسوم الكارتة لتخفيف العبء المالي الإجمالي عنك، وضمان مرور الونش وسيارتك بسلاسة وسرعة فائقة حتى الوصول لبيتك أو مركز الصيانة.
</p>

<h2 class="text-xl sm:text-2xl font-black text-amber-300 mt-10 mb-4">4. جدول مقارنة: أوناش أولاد حجازي مقابل الأوناش الأخرى</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-right text-xs sm:text-sm border border-slate-800 rounded-2xl overflow-hidden">
    <thead class="bg-slate-900 text-amber-300 font-bold">
      <tr>
        <th class="p-3 border-b border-slate-800">وجه المقارنة</th>
        <th class="p-3 border-b border-slate-800 text-emerald-400">أوناش إنقاذ أولاد حجازي</th>
        <th class="p-3 border-b border-slate-800 text-slate-400">الأوناش الفردية الأخرى</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800 text-slate-300">
      <tr>
        <td class="p-3 font-semibold text-white">تسعيرة السحب</td>
        <td class="p-3 text-emerald-400 font-bold">تبدأ من 750 ج.م حقيقية ومعلنة ومحددة مسبقاً</td>
        <td class="p-3 text-red-400">إعلان بسعر وهمي (200 ج) ومطالبة بـ 900 ج عند الوصول</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-white">الإكراميات والبقشيش</td>
        <td class="p-3 text-emerald-400 font-bold">ممنوع تماماً - السعر شامل كل شيء</td>
        <td class="p-3 text-red-400">إصرار على طلب مبالغ إضافية وإحراج العميل</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-white">رسوم بوابات الكارتة</td>
        <td class="p-3 text-emerald-400 font-bold">مساهمة ومشاركة في الدفع عن العميل</td>
        <td class="p-3 text-red-400">تحميل العميل كامل قيمة الكارتة ذهاباً وإياباً</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-white">العروض والخصومات</td>
        <td class="p-3 text-emerald-400 font-bold">خصم 50% لأول 100 عميل شهرياً (HEGAZY50)</td>
        <td class="p-3 text-slate-400">لا توجد أي عروض رسمية أو أكواد خصم</td>
      </tr>
      <tr>
        <td class="p-3 font-semibold text-white">تجهيزات الأسطول</td>
        <td class="p-3 text-emerald-400 font-bold">أوناش مسطحة هيدروليكية كاملة بأربطة إطارات مطاطية</td>
        <td class="p-3 text-slate-400">روافع سلكية قديمة تخدش الإكصدامات وتتلف العفشة</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-xl sm:text-2xl font-black text-amber-300 mt-10 mb-4">5. كيف تضمن الاستفادة من الخصم الآن؟</h2>
<p class="leading-relaxed">
  العرض متاح حالياً لأول 100 متصل فقط. لضمان حصولك على الخصم الفوري:
</p>
<ol class="list-decimal list-inside space-y-2 text-slate-300 font-medium">
  <li>اضغط على زر الاتصال الهاتفي أدناه للتواصل مع غرفة الطوارئ المركزية.</li>
  <li>أبلغ موظف خدمة العملاء بكود الخصم: <strong class="text-amber-400">HEGAZY50</strong>.</li>
  <li>حدد نوع سيارتك وموقعك الحالي عبر الواتساب أو بالوصف.</li>
  <li>سيتم خصم النسبة المقررة فوراً من إجمالي الفاتورة وتحرك أقرب ونش إليك خلال 8 إلى 12 دقيقة.</li>
</ol>
"""
}

# Generate the promotional article file
generate_article_file(promo_article, promo_article["content"])
print("SUCCESS: Promotional article generated!")

# Update blog/index.html to include the new promotional article at the top
blog_index_path = os.path.join(blog_dir, "index.html")
with open(blog_index_path, "r", encoding="utf-8") as f:
    b_code = f.read()

promo_card_html = f'''      <!-- Featured Promo Article Card -->
      <div class="glass p-6 sm:p-8 rounded-3xl border border-emerald-500/40 hover:border-emerald-400 transition-all bg-gradient-to-br from-slate-900 to-emerald-950/30 flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between text-xs mb-3">
            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 font-black border border-emerald-500/30">عرض خاص 2026</span>
            <span class="text-slate-400">قراءة في 5 دقائق</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black text-white group-hover:text-amber-400 transition-colors mb-2">
            <a href="winch-offers-discounts-cairo.html">{promo_article["title"]}</a>
          </h2>
          <p class="text-slate-300 text-sm line-clamp-3 mb-4 leading-relaxed">{promo_article["desc"]}</p>
        </div>
        <div class="pt-4 border-t border-slate-800 flex items-center justify-between">
          <span class="text-xs font-bold text-amber-300">كود: HEGAZY50</span>
          <a href="winch-offers-discounts-cairo.html" class="text-xs font-black text-emerald-400 group-hover:text-white flex items-center gap-1">
            <span>تفاصيل العرض والتفعيل</span>
            <span>←</span>
          </a>
        </div>
      </div>
'''

if "winch-offers-discounts-cairo.html" not in b_code:
    # insert promo card right after the article grid starts
    grid_marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">'
    if grid_marker in b_code:
        b_code = b_code.replace(grid_marker, grid_marker + "\n" + promo_card_html)
        with open(blog_index_path, "w", encoding="utf-8") as f:
            f.write(b_code)
        print("SUCCESS: Added promo card to blog/index.html")

# Update sitemap.xml
sitemap_path = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    s_code = f.read()

new_sitemap_entry = f'''  <url>
    <loc>https://awladhegazy.com/blog/winch-offers-discounts-cairo.html</loc>
    <lastmod>2026-11-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
'''

if "winch-offers-discounts-cairo.html" not in s_code:
    s_code = s_code.replace("</urlset>", new_sitemap_entry + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(s_code)
    print("SUCCESS: Added promo article to sitemap.xml")

# Update llms.txt
llms_path = os.path.join(base_dir, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    l_code = f.read()

new_llms_entry = "- [عروض وخصومات أوناش أولاد حجازي (خصم 50% وبدون إكرامية)](https://awladhegazy.com/blog/winch-offers-discounts-cairo.html)\n"
if "winch-offers-discounts-cairo.html" not in l_code:
    l_code = l_code.replace("- [أرقام الطوارئ والتواصل]", new_llms_entry + "- [أرقام الطوارئ والتواصل]")
    with open(llms_path, "w", encoding="utf-8") as f:
        f.write(l_code)
    print("SUCCESS: Added promo article to llms.txt")

print("All promotional updates completed cleanly!")
