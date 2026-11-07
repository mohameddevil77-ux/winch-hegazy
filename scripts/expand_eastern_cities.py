import os
import sys
import json

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")
sys.path.append(scripts_dir)

from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, PHONE_ALT, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema, MAPS_URL
)
from build_articles_engine import generate_article_file

# Define the 4 new dedicated articles for the user's strategic eastern zones
eastern_articles = [
    {
        "slug": "winch-obour-city",
        "image": "hegazy_red_truck_branding.jpg",
        "title": "ونش إنقاذ مدينة العبور: أسرع ونش سيارات عند كارفور وجولف سيتي وسوق العبور 24 ساعة",
        "desc": "خدمات ونش إنقاذ سيارات في مدينة العبور من أوناش أولاد حجازي. ارتكاز رئيسي أمام كارفور العبور وجولف سيتي وسوق العبور والحي الأول حتى التاسع. وصول خلال 5 إلى 8 دقائق. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ مدينة العبور", "ونش العبور", "ونش كارفور العبور", "ونش سوق العبور", "ونش جولف سيتي"],
        "content": f"""
<div class="glass p-6 rounded-2xl border border-amber-500/30 mb-8 bg-slate-900/80">
  <div class="flex items-center gap-2 mb-3">
    <span class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
    <h2 class="text-xl font-black text-amber-300 m-0">نقطة الارتكاز الميداني المباشر (Home Base):</h2>
  </div>
  <p class="text-white text-base leading-relaxed mb-4 font-medium">
    تعتبر <strong>مدينة العبور</strong> المقر الميداني الرئيسي لأسطول <strong>أوناش إنقاذ أولاد حجازي</strong>. نحن متمركزون مباشرة أمام <strong>كارفور العبور وجولف سيتي مول</strong> ومطلع الطريق الدائري ومحور العبور الرئيسي، مما يتيح لنا الوصول إلى أي نقطة داخل العبور أو سوق العبور في زمن قياسي يتراوح بين <strong>5 إلى 8 دقائق فقط</strong> بأرخص سعر يبدأ من <strong>600 جنيه مصري</strong>.
  </p>
  <div class="flex flex-wrap items-center gap-3 pt-2">
    <a href="tel:{PHONE}" class="px-5 py-2.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black text-sm rounded-xl shadow-lg glow-red">
      اتصل الآن: {PHONE_DISPLAY}
    </a>
    <a href="{MAPS_URL}" target="_blank" class="px-5 py-2.5 bg-slate-900 border border-emerald-500/50 text-emerald-400 font-bold text-sm rounded-xl">
      📍 موقعنا على خرائط Google
    </a>
  </div>
</div>

<h2>تغطية شاملة لكافة أحياء ومناطق مدينة العبور</h2>
<ul class="list-disc list-inside space-y-2">
  <li><strong>كارفور العبور وجولف سيتي مول:</strong> نقطة التمركز الرئيسية الجاهزة للتحرك اللحظي.</li>
  <li><strong>سوق العبور للجملة:</strong> أوناش مجهزة للتعامل مع سيارات النقل والجامبو والملاكي والتريلات على مدار 24 ساعة.</li>
  <li><strong>الأحياء السكنية (من الحي الأول حتى الحي التاسع):</strong> سحب هيدروليكي فائق النعومة للسيارات الملاكي والحديثة داخل الكمبوندات.</li>
  <li><strong>المنطقة الصناعية (أ و ب و ج):</strong> نقل المعدات الثقيلة، الفورك لفت، والشاحنات المعطلة.</li>
  <li><strong>محور العبور الرئيسي وخط 10 ومحور بلبيس:</strong> تأمين المحاور السريعة المؤدية للمدينة.</li>
</ul>
"""
    },
    {
        "slug": "winch-shorouk-badr",
        "image": "hegazy_caravan_transport.jpg",
        "title": "ونش إنقاذ مدينة الشروق ومدينة بدر: أوناش متمركزة على طريق السويس والإسماعيلية والروبيكي",
        "desc": "طلب ونش إنقاذ سيارات في مدينة الشروق ومدينة بدر من أوناش أولاد حجازي 24 ساعة. أوناش حديثة تغطي الروبيكي، هليوبوليس الجديدة، الجامعة البريطانية والروسية. اتصل الآن 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ مدينة الشروق", "ونش الشروق", "ونش مدينة بدر", "ونش الروبيكي", "ونش هليوبوليس الجديدة"],
        "content": f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6 bg-slate-900/80">
  <h2 class="text-xl font-black text-amber-300 mb-2">أسرع ونش إنقاذ في الشروق وبدر</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    لطلب <strong>ونش إنقاذ في الشروق أو بدر</strong>، اتصل مباشرة على <a href="tel:{PHONE}" class="text-amber-400 font-black underline">{PHONE_DISPLAY}</a> أو <a href="tel:{PHONE_ALT}" class="text-white font-bold">{PHONE_ALT}</a>. نصلك خلال <strong>10 دقائق</strong> عند بوابات الشروق (1 و 2 و 3)، مدخل السويس والإسماعيلية، مدينة بدر، والمنطقة الصناعية بالروبيكي.
  </p>
</div>

<h2>المناطق المخدومة في الشروق وبدر</h2>
<ul class="list-disc list-inside space-y-2">
  <li><strong>مدينة الشروق:</strong> مدخل طريق السويس، مدخل طريق الإسماعيلية، الجامعة البريطانية (BUE)، الجامعة الفرنسية، ونادي الشروق.</li>
  <li><strong>مدينة بدر:</strong> مدخل طريق السويس، ميدان الحرية، جامعة بدر (BUC)، والجامعة المصرية الروسية (ERU).</li>
  <li><strong>مدينة الروبيكي لصناعة الجلود:</strong> أوناش ثقيلة لنقل البضائع والمقطورات ومعدات المصانع.</li>
  <li><strong>هليوبوليس الجديدة ووصلة أم قمر:</strong> سرعة تدخل على الطرق الرابطة السريعة والدائري الإقليمي.</li>
</ul>
"""
    },
    {
        "slug": "winch-new-capital",
        "image": "hegazy_cupra_rear.jpg",
        "title": "ونش إنقاذ العاصمة الإدارية الجديدة: خدمة VIP على محور بن زايد والحي الحكومي والمال والأعمال",
        "desc": "خدمات ونش إنقاذ سيارات في العاصمة الإدارية الجديدة من أوناش أولاد حجازي. أحدث أسطول هيدروليكي مسطح لنقل السيارات الفاخرة في الحي الحكومي والبرج الأيقوني والدائري الأوسطي 24/7. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ العاصمة الادارية", "ونش العاصمة الادارية", "ونش محور بن زايد", "ونش البرج الايقوني", "ونش الدائري الاوسطي"],
        "content": f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6 bg-slate-900/80">
  <h2 class="text-xl font-black text-amber-300 mb-2">ونش إنقاذ معتمد في العاصمة الإدارية الجديدة</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    يوفر <strong>أوناش أولاد حجازي</strong> أحدث أوناش هيدروليكية مسطحة مصممة لنقل سيارات المسؤولين، السيارات الفاخرة والكهربائية (تسلا، بورش، مرسيدس)، والكرفانات ومعدات الشركات داخل العاصمة الإدارية ومحاورها السريعة (محور محمد بن زايد، الدائري الأوسطي، والدائري الإقليمي). اتصل الآن: <a href="tel:{PHONE}" class="text-amber-400 font-black">{PHONE_DISPLAY}</a>.
  </p>
</div>

<h2>التغطية الميدانية داخل العاصمة الإدارية ومحيطها</h2>
<ul class="list-disc list-inside space-y-2">
  <li><strong>الحي الحكومي وحي الوزارات والبرلمان:</strong> نقل فوري بدون أي تأخير وتأمين كامل للسيارات.</li>
  <li><strong>منطقة الأعمال المركزية (CBD) والبرج الأيقوني:</strong> سحب سيارات الشركات والمستثمرين.</li>
  <li><strong>مدينة الفنون والثقافة والحي الدبلوماسي:</strong> أوناش نظيفة مجهزة بأربطة إطارات مطاطية تحافظ على الهيكل.</li>
  <li><strong>محور الأمل ومحور محمد بن زايد الشمالي والجنوبي:</strong> وصول في أقل من 10 دقائق من خلال الدائري الأوسطي.</li>
</ul>
"""
    },
    {
        "slug": "winch-salam-herfeyein-nahda",
        "image": "hegazy_semi_truck_head.jpg",
        "title": "ونش إنقاذ مدينة السلام والحرفيين والنهضة: أسرع سحب عند موقف العاشر ومحطة عدلي منصور",
        "desc": "طلب ونش إنقاذ سيارات في مدينة السلام، الحرفيين، مساكن النهضة، وموقف العاشر من أوناش أولاد حجازي 24 ساعة. سحب فوري ونقل مباشر لأكبر ورش الصيانة والتوكيلات بأرخص سعر. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش شرق القاهرة والمدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ الحرفيين", "ونش مدينة السلام", "ونش النهضة", "ونش موقف العاشر", "ونش محطة عدلي منصور"],
        "content": f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6 bg-slate-900/80">
  <h2 class="text-xl font-black text-amber-300 mb-2">أسرع ونش إنقاذ في الحرفيين والسلام والنهضة</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    منطقة <strong>الحرفيين ومدينة السلام والنهضة</strong> هي عصب صيانة السيارات في مصر. <strong>أوناش أولاد حجازي</strong> يوفر أوناشاً متمركزة عند كوبري التعمير، محطة عدلي منصور التبادلية، ومطلع الدائري لنقل سيارتك مباشرة إلى ورشة الميكانيكا، السمكرة، أو مركز الصيانة المعتمد داخل الحرفيين في دقائق معدودة. اتصل الآن: <a href="tel:{PHONE}" class="text-amber-400 font-black">{PHONE_DISPLAY}</a>.
  </p>
</div>

<h2>نطاقات التغطية الفورية</h2>
<ul class="list-disc list-inside space-y-2">
  <li><strong>مجمع ورش الحرفيين وجسر السويس:</strong> سحب ونقل سيارات الحوادث والأعطال الميكانيكية للورش المتخصصة.</li>
  <li><strong>مدينة السلام 1 و 2 وميدان الإسكندرية:</strong> وصول سريع في الشوارع الحيوية دون تعطيل السير.</li>
  <li><strong>مساكن النهضة وإسكان الشباب:</strong> تغطية للمناطق السكنية ومحيط ترعة الإسماعيلية.</li>
  <li><strong>محطة عدلي منصور المركزية وموقف العاشر:</strong> نقطة تقاطع كبرى لإنقاذ السيارات المتجهة لمحافظات الدلتا والقناة.</li>
</ul>
"""
    }
]

# Generate the 4 new articles
for art in eastern_articles:
    generate_article_file(art, art["content"])
    print(f"SUCCESS: Generated eastern article {art['slug']}.html")

print("All 4 eastern specialized articles created successfully!")
