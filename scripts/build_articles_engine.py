import os
import sys
import json

sys.path.append(r"D:\winch-hegazy\scripts")
from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema, generate_faq_schema
)

# -------------------------------------------------------------
# 2. SERVICES.HTML
# -------------------------------------------------------------
services_list = [
    {
        "id": "private-cars",
        "icon": "🚗",
        "title": "إنقاذ وسحب سيارات الملاكي والحديثة",
        "image": "hegazy_luxury_car_flatbed.jpg",
        "desc": "خدمة مخصصة لجميع موديلات السيارات الملاكي (سيدان، هاتشباك، كابريوليه، والسيارات الفاخرة والكهربائية). نستخدم أوناش مسطحة (Flatbed) مزودة بروافع هيدروليكية منخفضة الزوايا تضمن عدم احتكاك أو خدش إكصدامات السيارات المنخفضة وحماية كاملة للعفشة ونظام الدفع.",
        "features": ["تحميل مسطح هيدروليكي بالكامل", "تثبيت بأربطة إطارات مطاطية دون مس الهيكل", "مناسب لسيارات كوبرا وبورش ومرسيدس وBMW", "نقل إلى أي توكيل أو مركز صيانة معتمد"]
    },
    {
        "id": "highways",
        "icon": "⚡",
        "title": "إنقاذ سيارات الدفع الرباعي على الطرق السريعة",
        "image": "hegazy_orange_truck_porsche.jpg",
        "desc": "تمركز دائم على مدار 24 ساعة على أهم المحاور الحيوية: الطريق الدائري بكافة قطاعاته، طريق السويس، طريق الإسماعيلية الصحراوي، والدائري الأوسطي والإقليمي. نصلك في أقل من 10 دقائق لتأمين موقع العطل وتفادي أي حوادث على السرعات العالية.",
        "features": ["سحب سيارات الدفع الرباعي والـ SUV والبورش", "إشارات تحذيرية ضوئية ليلية لتأمين موقع العطل", "معرفة دقيقة بمداخل ومخارج الطرق السريعة", "مرافقة السيارة حتى المكان الآمن"]
    },
    {
        "id": "heavy-machinery",
        "icon": "🏗️",
        "title": "نقل المعدات الثقيلة والكلاركات والروافع الشوكية",
        "image": "hegazy_red_truck_heavy.jpg",
        "desc": "أسطول متخصص في نقل معدات المصانع، خلاطات ومحطات الخرسانة، الروافع الشوكية (Forklifts / كلارك)، والمعدات الهندسية بأعلى حمولات أمان، مع تثبيت بجنازير وسلاسل فولاذية معتمدة لمنع أي انزلاق أثناء النقل بين المناطق الصناعية.",
        "features": ["نقل كلاركات وفورك ليفت مختلف الحمولات", "خدمة المصانع بالعبور وبدر والعاشر من رمضان", "تثبيت ميكانيكي هيدروليكي فائق الأمان", "سائقون وخبراء مؤهلون لنقل المعدات"]
    },
    {
        "id": "caravans",
        "icon": "🏠",
        "title": "نقل الكرفانات والمكاتب المتنقلة والكونتينرات",
        "image": "hegazy_caravan_transport.jpg",
        "desc": "خدمة نقل الكرفانات وغرف الحراسة والمكاتب الإدارية المتنقلة لمواقع الإنشاءات والشركات في المدن الجديدة والعاصمة الإدارية والشروق وبدر. نضمن سلامة الهيكل الخارجي والشبابيك والأسلاك أثناء التحميل والتنزيل.",
        "features": ["أبعاد مسطح ممتدة تناسب أطوال الكرفانات", "تحميل هيدروليكي مرن بدون ميل أو إجهاد", "نقل وتوصيل لمواقع العمل والمشروعات الكبرى", "أسعار تعاقدية لشركات المقاولات والإنشاءات"]
    },
    {
        "id": "semi-trucks",
        "icon": "🚛",
        "title": "سحب ونقل رؤوس التريلات والشاحنات النقل الثقيل",
        "image": "hegazy_semi_truck_head.jpg",
        "desc": "تجهيزات ميكانيكية ضخمة لسحب ونقل كبائن ورؤوس الشاحنات التريلا المعطلة (Mercedes Actros وغيرها) بأمان تام، مع إمكانية التوصيل لورش الحرفيين، كفر بطا، أو الوكلاء المعتمدين للشاحنات في مصر.",
        "features": ["حمولات ونش شاقة مخصصة للشاحنات", "سحب وإنقاذ أعطال الموتور والفتيس للتريلات", "إنقاذ طريق الإسماعيلية وطريق السويس والإقليمي", "فنيون محترفون في فك عمود الكردان والتعليق"]
    },
    {
        "id": "golf-carts",
        "icon": "⛳",
        "title": "نقل عربات الجولف والسيارات الكهربائية للكمبوندات",
        "image": "hegazy_golf_carts_transport.jpg",
        "desc": "نقل سيارات الجولف كارت (Club Cars) والسيارات الترفيهية والكهربائية للمنتجعات والمجمعات السكنية المغلقة في مدينتي، الرحاب، التجمع، والعاصمة الإدارية مع إمكانية نقل أكثر من عربة في النقلة الواحدة بأمان كامل.",
        "features": ["إمكانية نقل سيارتين جولف معاً بنفس المشوار", "حماية العجلات ونظام البطاريات الحساس", "تثبيت محكم بحبال نايلون مخصصة", "توصيل للملاعب والمنتجعات والقرى السياحية"]
    },
    {
        "id": "food-trucks",
        "icon": "🍔",
        "title": "نقل عربات الطعام المتنقلة (Food Trucks) والمقطورات",
        "image": "hegazy_food_truck_transport.jpg",
        "desc": "نقل وتوصيل عربات الطعام المتنقلة والفود كارت والمقطورات التجارية المخصصة للمطاعم والكافيهات والمعارض والفعاليات في مختلف مناطق القاهرة والمحافظات بأعلى درجات العناية بالديكورات والمعدات الداخلية.",
        "features": ["أوناش مسطحة تتيح سهولة صعود العربة", "تثبيت مانع للاهتزاز للحفاظ على أجهزة المطبخ", "نقل إلى المعارض والمولات ومناطق الفعاليات", "مواعيد دقيقة لتجهيز مشروعات الشباب"]
    },
    {
        "id": "roadside",
        "icon": "🛞",
        "title": "خدمات المساعدة السريعة (شحن بطاريات وتغيير إطارات)",
        "image": "hegazy_red_truck_branding.jpg",
        "desc": "ليست كل الأعطال تتطلب سحب السيارة؛ وفرنا لك وحدات التدخل السريع المجهزة بأجهزة فحص وشحن البطاريات (Jump Start)، كومبريسور هواء لتزويد وتغيير الإطارات الاحتياطية (الاستبن)، وتزويد وقود طوارئ لاستئناف رحلتك فوراً.",
        "features": ["شحن بطاريات 12V و 24V بأحدث الأجهزة", "تغيير وفك المسامير المستعصية للإطارات", "تزويد وقود طوارئ (بنزين 92 و 95)", "فحص كمبيوتر سريع للأعطال الطارئة"]
    },
    {
        "id": "underground",
        "icon": "🏢",
        "title": "إنقاذ الجراجات السفلية والبدرومات الضيقة",
        "image": "hegazy_cupra_rear.jpg",
        "desc": "تعطلت سيارتك داخل جراج مول تجاري أو بدروم عمارة سكنية بارتفاع منخفض؟ ونش حجازي يمتلك أوناشاً هيدروليكية خاصة ذات ارتفاعات منخفضة (Low Clearance) مصممة خصيصاً للدخول وسحب السيارات من داخل البدرومات.",
        "features": ["دخول جراجات ارتفاع 2 متر وما دون", "سحب آمن بدون لمس الأسقف المنخفضة", "وايرات مرنة وزوايا دوران ذكية", "خدمة متوفرة في مولات التجمع والعبور وأكتوبر"]
    }
]

services_cards_list = []
for s in services_list:
    features_html = "".join([f'''
          <div class="flex items-center gap-2 text-xs sm:text-sm text-slate-200">
            <span class="text-emerald-400 font-black">✓</span>
            <span>{feat}</span>
          </div>
    ''' for feat in s["features"]])
    card = f'''
    <div id="{s["id"]}" class="glass p-6 sm:p-8 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-4 rounded-2xl overflow-hidden border border-slate-700/80 shadow-xl aspect-video lg:aspect-square bg-slate-900 group">
        <img src="assets/images/{s["image"]}" alt="{s["title"]} - ونش إنقاذ حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
      </div>
      <div class="lg:col-span-5 space-y-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl p-3 bg-slate-900 rounded-2xl border border-amber-500/30">{s["icon"]}</span>
          <h2 class="text-xl sm:text-2xl font-black text-white">{s["title"]}</h2>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">{s["desc"]}</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2">
          {features_html}
        </div>
      </div>
      <div class="lg:col-span-3 flex flex-col gap-3">
        <a href="tel:{PHONE}" class="w-full py-4 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black text-center rounded-2xl shadow-lg glow-red hover:opacity-95 transition flex items-center justify-center gap-2">
          <span>طلب هذا الونش فوراً</span>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>
        <a href="{WHATSAPP_LINK}" target="_blank" class="w-full py-3 bg-slate-900 border border-emerald-500/40 text-emerald-400 font-bold text-center rounded-2xl hover:bg-slate-800 transition text-sm">
          تواصل مع فني الونش على واتساب
        </a>
      </div>
    </div>
    '''
    services_cards_list.append(card)

services_cards_rendered = "\n".join(services_cards_list)

html_services = f"""{get_head(
    "خدمات ونش إنقاذ حجازي | سحب ملاكي، نقل ثقيل، وحوادث 24 ساعة",
    "تعرف على خدمات ونش إنقاذ حجازي: سحب وإنقاذ السيارات الملاكي والفاخرة، نقل المعدات والكلاركات، نقل الكرفانات، وسحب التريلات والشاحنات، والمساعدة السريعة على الطريق على مدار 24 ساعة.",
    "https://winch-hegazy.com/services.html"
)}
{generate_local_business_schema(
    "خدمات ونش إنقاذ حجازي | سحب ملاكي، نقل ثقيل، وحوادث 24 ساعة",
    "خدمات ونش حجازي لإنقاذ وسحب السيارات في مصر بأحدث أوناش هيدروليكية.",
    "https://winch-hegazy.com/services.html"
)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("services")}

  <!-- Page Header -->
  <section class="py-16 bg-gradient-to-b from-dark-900 to-dark-950 border-b border-slate-800 text-center relative overflow-hidden">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">خدمات الإنقاذ والنقل المتخصص المتكاملة</span>
      <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight">حلول إنقاذ وسحب سيارات ومعدات لكافة الحالات والأعطال</h1>
      <p class="text-slate-400 text-sm sm:text-base mt-4 max-w-2xl mx-auto">أسطول ونش حجازي مجهز لنقل السيارات الفاخرة، المعدات الثقيلة، الكرفانات، التريلات، وعربات الجولف والفود ترك بأعلى معايير الأمان 24 ساعة.</p>
    </div>
  </section>

  <!-- Services Detailed Cards -->
  <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
    {services_cards_rendered}
  </section>

{get_footer()}
</body>
</html>
"""
with open(os.path.join(base_dir, "services.html"), "w", encoding="utf-8") as f:
    f.write(html_services)

print("SUCCESS: services.html generated")


# -------------------------------------------------------------
# 3. COVERAGE.HTML
# -------------------------------------------------------------
zones = [
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
]

html_coverage = f"""{get_head(
    "مناطق تغطية ونش إنقاذ حجازي | الدائري، التجمع، أكتوبر، والمحافظات",
    "خريطة تغطية ونش إنقاذ حجازي في مصر: أوناش متمركزة في التجمع الخامس، الشيخ زايد، 6 أكتوبر، الطريق الدائري، طريق السويس، وطريق الإسكندرية الصحراوي 24 ساعة.",
    "https://winch-hegazy.com/coverage.html"
)}
{generate_local_business_schema(
    "مناطق تغطية ونش إنقاذ حجازي | الدائري، التجمع، أكتوبر، والمحافظات",
    "تغطية ونش حجازي لإنقاذ السيارات في كافة محاور مصر.",
    "https://winch-hegazy.com/coverage.html"
)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("coverage")}

  <section class="py-16 bg-gradient-to-b from-dark-900 to-dark-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 mb-3 inline-block">خريطة الانتشار الميداني الأوسع في مصر</span>
      <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight">أينما تعطلت.. ونش حجازي متمركز بالقرب منك</h1>
      <p class="text-slate-400 text-sm sm:text-base mt-4 max-w-2xl mx-auto">نوزع أسطولنا استراتيجياً عند مطالع ومنازل الكباري والمحاور السريعة لنضمن الوصول إليك في زمن قياسي لا يتجاوز 10 دقائق.</p>
    </div>



  <!-- Zones Grid -->
  <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {''.join([f'''
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between gap-2 mb-3">
            <span class="text-xs font-black px-2.5 py-1 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30">{z['tag']}</span>
            <span class="text-xs text-emerald-400 font-bold">{z['winches']}</span>
          </div>
          <h2 class="text-xl font-black text-white mb-2">{z['name']}</h2>
          <p class="text-slate-300 text-xs leading-relaxed mb-6"><strong class="text-slate-100">أبرز النطاقات:</strong> {z['places']}</p>
        </div>
        <a href="tel:{PHONE}" class="w-full py-3 bg-slate-900 hover:bg-slate-800 border border-slate-700 hover:border-amber-400 text-white font-bold text-center rounded-xl text-xs flex items-center justify-center gap-1.5 transition">
          <span>طلب ونش في هذا النطاق</span>
          <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
        </a>
      </div>
      ''' for z in zones])}
    </div>



    <!-- Cairo Neighborhoods Direct Navigation (Local SEO Boost) -->
    <div class="mt-16 glass p-8 rounded-3xl border border-amber-500/30">
      <div class="text-center max-w-2xl mx-auto mb-8">
        <span class="text-xs font-black text-amber-300 bg-amber-500/15 border border-amber-500/30 px-3 py-1 rounded-full mb-2 inline-block">تغطية أحياء القاهرة والجيزة التفصيلية</span>
        <h3 class="text-2xl font-black text-white">اختر حيك في القاهرة لطلب أقرب ونش فوراً</h3>
        <p class="text-slate-400 text-xs mt-1">صفحات هبوط مخصصة لكل حي وميدان تحتوي على نقاط التمركز الدقيقة وأرقام الطوارئ المباشرة.</p>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3 text-center text-xs font-bold">
        <a href="blog/winch-obour-city.html" class="p-3 rounded-xl bg-slate-900 border-2 border-emerald-500/60 text-emerald-300 hover:bg-emerald-500 hover:text-black transition shadow font-black">
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
        </a>
        <a href="blog/winch-nasr-city.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 مدينة نصر
        </a>
        <a href="blog/winch-heliopolis-masr-gedida.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 مصر الجديدة
        </a>
        <a href="blog/winch-maadi.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 المعادي
        </a>
        <a href="blog/winch-tagamoa-new-cairo.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 التجمع الخامس
        </a>
        <a href="blog/winch-rehab-madinaty.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 مدينتي والرحاب
        </a>
        <a href="blog/winch-zayed-october.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 الشيخ زايد وأكتوبر
        </a>
        <a href="blog/winch-giza-haram.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 الهرم وفيصل
        </a>
        <a href="blog/winch-downtown-cairo.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 وسط البلد والتحرير
        </a>
        <a href="blog/winch-mokattam.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 المقطم
        </a>
        <a href="blog/winch-shobra.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 شبرا مصر والخيمة
        </a>
        <a href="blog/winch-daeri-cairo.html" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-slate-200 hover:border-amber-400 hover:text-amber-300 transition shadow">
          📍 الطريق الدائري
        </a>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

with open(os.path.join(base_dir, "coverage.html"), "w", encoding="utf-8") as f:
    f.write(html_coverage)

print("SUCCESS: coverage.html generated")


# -------------------------------------------------------------
# 4. PRICING.HTML
# -------------------------------------------------------------
html_pricing = f"""{get_head(
    "أسعار ونش إنقاذ السيارات في مصر | تسعيرة ونش حجازي بدون استغلال",
    "تعرف على أسعار ونش إنقاذ السيارات في مصر مع ونش حجازي. تسعيرة عادلة تبدأ من 600 ج.م، حساب سعر الكيلومتر بشفافية تامة دون أي تكاليف خفية أو إكراميات إجبارية.",
    "https://winch-hegazy.com/pricing.html"
)}
{generate_local_business_schema(
    "أسعار ونش إنقاذ السيارات في مصر | تسعيرة ونش حجازي بدون استغلال",
    "تسعيرة ونش إنقاذ سيارات عادلة ومحددة مسبقاً في مصر.",
    "https://winch-hegazy.com/pricing.html"
)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("pricing")}

  <section class="py-16 bg-gradient-to-b from-dark-900 to-dark-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">ميثاق الشفافية والتسعير العادل</span>
      <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight">أرخص سعر ونش إنقاذ سيارات في مصر بدون استغلال</h1>
      <p class="text-slate-400 text-sm sm:text-base mt-4 max-w-2xl mx-auto">نلتزم بإبلاغك بالتكلفة الإجمالية الصافية قبل تحرك الونش إليك. لا مفاجآت عند الوصول ولا مصاريف خفية وقت الطوارئ.</p>
    </div>



  <!-- Pricing Table -->
  <section class="py-16 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="glass rounded-3xl border border-slate-800 overflow-hidden shadow-2xl">
      <table class="w-full text-right text-sm">
        <thead class="bg-slate-900 text-amber-300 font-black border-b border-slate-800">
          <tr>
            <th class="p-4 sm:p-5">نوع الخدمة / النطاق</th>
            <th class="p-4 sm:p-5">نوع المركبة</th>
            <th class="p-4 sm:p-5">السعر التقديري</th>
            <th class="p-4 sm:p-5">الضمان والميزات</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800 text-slate-300">
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">سحب ونش داخلي (نفس المنطقة / الحي)</td>
            <td class="p-4 sm:p-5">ملاكي / هاتشباك / سيدان</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">600 - 750 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">وصول خلال 10 دقائق + تأمين كامل</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">سحب ونقل إلى التوكيل أو مركز معتمد</td>
            <td class="p-4 sm:p-5">ملاكي أو دفع رباعي SUV</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">800 - 1100 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">توصيل للتوكيل ومساعدة في الاستلام</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">سحب ونش على الطريق الدائري والمحاور</td>
            <td class="p-4 sm:p-5">جميع أنواع الملاكي</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">750 - 950 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">تأمين المكان وتفادي غرامات المرور</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">إنقاذ الطرق السريعة (سويس / صحراوي / سخنة)</td>
            <td class="p-4 sm:p-5">ملاكي / دفع رباعي</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">يبدأ من 1200 ج.م + كم</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">حساب سعر الكيلومتر العادل</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">سحب ونقل سيارات نقل ثقيل وجامبو ورؤوس تريلات</td>
            <td class="p-4 sm:p-5">نقل / تريلا / ميكروباص</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">يبدأ من 600 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">أوناش ثقيلة متخصصة 15 طن</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">نقل عربات الجولف كارت والفود تراك التجارية</td>
            <td class="p-4 sm:p-5">عربات منتجعات / فود تراك</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">يبدأ من 500 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">تثبيت مانع للاهتزاز + حمولة مزدوجة</td>
          </tr>
          <tr class="hover:bg-slate-900/40">
            <td class="p-4 sm:p-5 font-bold text-white">نقل الكرفانات والمكاتب المتنقلة ومعدات المواقع</td>
            <td class="p-4 sm:p-5">كرفانات سكنية / غرف مواقع إنشائية</td>
            <td class="p-4 sm:p-5 font-black text-amber-400 text-base">يبدأ من 700 ج.م</td>
            <td class="p-4 sm:p-5 text-xs text-emerald-400">طبالي مسطحة ممتدة حتى 12 متر</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Assurance Banner -->
    <div class="mt-10 p-6 rounded-3xl bg-slate-900/80 border border-emerald-500/30 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="space-y-1">
        <h3 class="text-lg font-black text-white">ضمان عدم تغيير السعر بعد التحرك</h3>
        <p class="text-slate-400 text-xs">عند الاتصال بنا، سيسألك مسؤول العمليات عن نوع سيارتك والمكان، ويحدد لك السعر الصافي. لن تدفع أي جنيه إضافي فوق ما تم الاتفاق عليه.</p>
      </div>
      <a href="tel:{PHONE}" class="px-6 py-3.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black rounded-xl text-sm shrink-0 shadow-lg glow-red">
        اتصل واستفسر عن سعرك فوراً
      </a>
    </div>



{get_footer()}
</body>
</html>
"""

with open(os.path.join(base_dir, "pricing.html"), "w", encoding="utf-8") as f:
    f.write(html_pricing)

print("SUCCESS: pricing.html generated")


# -------------------------------------------------------------
# 5. BLOG/INDEX.HTML & TARGETED ARTICLES
# -------------------------------------------------------------
articles = [
    {
        "slug": "agrab-winch-qarib-meni",
        "title": "أقرب ونش إنقاذ من موقعي: كيف يصلك ونش حجازي في أقل من 10 دقائق؟",
        "desc": "تعرف على كيفية طلب أقرب ونش إنقاذ سيارات من موقعك الجغرافي الحالي في مصر، وكيف تضمن أسرع وصول بدون تأخير أو استغلال على الطرق السريعة والمحاور.",
        "date": "2026-11-06",
        "category": "دليل الإنقاذ السريع",
        "read_time": "4 دقائق",
        "keywords": ["أقرب ونش إنقاذ من موقعي", "ونش قريب مني", "أسرع ونش سيارات", "رقم أقرب ونش"]
    },
    {
        "slug": "ar5as-winch-enqaz-misr",
        "title": "أرخص ونش إنقاذ سيارات في مصر: أسعار حقيقية وكيف تتجنب استغلال الطرق؟",
        "desc": "دليل تسعيرة أوناش إنقاذ السيارات في مصر لعام 2026: كيف يتم حساب التكلفة العادلة؟ ولماذا يعتبر ونش حجازي الخيار الأوفر والأكثر أماناً لسيارتك؟",
        "date": "2026-11-06",
        "category": "شفافية الأسعار",
        "read_time": "5 دقائق",
        "keywords": ["أرخص ونش إنقاذ", "أسعار أوناش السيارات مصر", "تكلفة ونش الإنقاذ", "أرخص ونش سيارات"]
    },
    {
        "slug": "winch-daeri-cairo",
        "title": "ونش إنقاذ الطريق الدائري والمحاور السريعة: أرقام الطوارئ ونقاط التمركز 24 ساعة",
        "desc": "دليل ونش إنقاذ الطريق الدائري ومحور 26 يوليو والأوتوستراد. تعرف على أماكن تمركز أوناش حجازي وكيف تتصرف فور تعطل سيارتك على الدائري.",
        "date": "2026-11-06",
        "category": "تغطية المحاور الحيوية",
        "read_time": "6 دقائق",
        "keywords": ["ونش إنقاذ الطريق الدائري", "ونش الدائري", "ونش محور 26 يوليو", "ونش سيارات الدائري"]
    },
    {
        "slug": "winch-tagamoa-new-cairo",
        "title": "ونش إنقاذ التجمع الخامس والقاهرة الجديدة: خدمة سريعة في كافة الأحياء والتسعين",
        "desc": "خدمات ونش إنقاذ سيارات في التجمع الخامس، شارع التسعين، التجمع الأول، الرحاب، ومدينتي. وصول فوري وأحدث أوناش هيدروليكية لحماية سياراتك الفاخرة.",
        "date": "2026-11-06",
        "category": "تغطية المدن الجديدة",
        "read_time": "4 دقائق",
        "keywords": ["ونش إنقاذ التجمع الخامس", "ونش القاهرة الجديدة", "ونش شارع التسعين", "ونش مدينتي والرحاب"]
    },
    {
        "slug": "winch-zayed-october",
        "title": "ونش إنقاذ الشيخ زايد و6 أكتوبر: وصول فوري على محور 26 يوليو ووصلة دهشور",
        "desc": "طلب ونش إنقاذ سيارات في الشيخ زايد ومدينة 6 أكتوبر وطريق الواحات. أوناش حديثة مجهزة للدخول في جراجات المولات ونقل السيارات لأكبر مراكز الصيانة.",
        "date": "2026-11-06",
        "category": "تغطية غرب القاهرة",
        "read_time": "5 دقائق",
        "keywords": ["ونش إنقاذ الشيخ زايد", "ونش 6 أكتوبر", "ونش وصلة دهشور", "ونش طريق الواحات"]
    },
    {
        "slug": "emergency-breakdown-tips",
        "title": "دليل الطوارئ الشامل: ماذا تفعل فور توقف سيارتك فجأة على طريق سريع؟",
        "desc": "خطوات عملية حاسمة لحماية حياتك وسلامة سيارتك عند حدوث عطل مفاجئ على طريق سريع أو صحراوي في مصر حتى وصول ونش الإنقاذ المعتمد.",
        "date": "2026-11-06",
        "category": "إرشادات الأمان والسلامة",
        "read_time": "5 دقائق",
        "keywords": ["عطل السيارة على الطريق السريع", "إرشادات أمان ونش الإنقاذ", "طوارئ السيارات مصر"]
    },
    {
        "slug": "winch-enqaz-cairo",
        "title": "ونش إنقاذ في القاهرة: أسرع خدمة سحب سيارات 24 ساعة في كافة أحياء العاصمة",
        "desc": "دليل ونش إنقاذ سيارات في القاهرة من ونش حجازي. تغطية شاملة لجميع أحياء القاهرة الكبرى والجيزة خلال 10 دقائق بأحدث أوناش هيدروليكية وأرخص سعر يبدأ من 600 جنيه.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "6 دقائق",
        "keywords": ["ونش انقاذ في القاهرة", "ونش انقاذ القاهرة", "ونش سيارات القاهرة", "رقم ونش انقاذ القاهرة", "ارخص ونش انقاذ في القاهرة"]
    },
    {
        "slug": "winch-nasr-city",
        "title": "ونش إنقاذ في مدينة نصر: أسرع ونش سيارات في مكرم عبيد وعباس العقاد والحي العاشر",
        "desc": "خدمة ونش إنقاذ سيارات في مدينة نصر من ونش حجازي 24 ساعة. متمركزون في مكرم عبيد، عباس العقاد، الحي العاشر، وزهراء مدينة نصر. وصول في 10 دقائق بسعر يبدأ من 600 ج.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في مدينة نصر", "ونش مدينة نصر", "ونش مكرم عبيد", "ونش عباس العقاد", "ونش زهراء مدينة نصر"]
    },
    {
        "slug": "winch-heliopolis-masr-gedida",
        "image": "hegazy_porsche_highway_rear.jpg",
        "title": "ونش إنقاذ في مصر الجديدة: خدمة سريعة في الكوربة وروكسي والنزهة وشيراتون",
        "desc": "طلب ونش إنقاذ سيارات في مصر الجديدة من ونش حجازي. أوناش حديثة متمركزة في روكسي، الكوربة، الميرغني، تريومف، وميدان الحجاز 24 ساعة. اتصل الآن 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في مصر الجديدة", "ونش مصر الجديدة", "ونش روكسي", "ونش الكوربة", "ونش شيراتون"]
    },
    {
        "slug": "winch-maadi",
        "title": "ونش إنقاذ في المعادي: أوناش متمركزة على الأوتوستراد ودجلة وكورنيش المعادي وصقر قريش",
        "desc": "ونش إنقاذ سيارات في المعادي من ونش حجازي. تغطية سريعة على كورنيش المعادي، دجلة، ثكنات المعادي، زهراء المعادي، وصقر قريش 24/7 بسعر يبدأ من 600 ج. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في المعادي", "ونش المعادي", "ونش دجلة المعادي", "ونش صقر قريش", "ونش اوتوستراد المعادي"]
    },
    {
        "slug": "winch-downtown-cairo",
        "title": "ونش إنقاذ في وسط البلد: سحب فوري في التحرير ورمسيس والزمالك وجاردن سيتي",
        "desc": "ونش إنقاذ سيارات في وسط البلد، ميدان التحرير، طلعت حرب، رمسيس، العتبة، وجزيرة الزمالك 24 ساعة. مناورة سريعة وأرخص سعر سحب مع ونش حجازي. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في وسط البلد", "ونش التحرير", "ونش رمسيس", "ونش الزمالك", "ونش وسط البلد"]
    },
    {
        "slug": "winch-mokattam",
        "title": "ونش إنقاذ في المقطم: خدمة سريعة في الهضبة الوسطى وشارع 9 وكورنيش المقطم",
        "desc": "خدمات ونش إنقاذ سيارات في المقطم من ونش حجازي. أوناش قوية مجهزة للمطالع والمنحدرات الجبلية في الهضبة العليا والوسطى وشارع 9 على مدار 24 ساعة. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في المقطم", "ونش المقطم", "ونش الهضبة الوسطى", "ونش شارع 9 المقطم"]
    },
    {
        "slug": "winch-shobra",
        "title": "ونش إنقاذ في شبرا: سحب سيارات في شبرا مصر وشبرا الخيمة وروض الفرج ومظلات",
        "desc": "طلب ونش إنقاذ سيارات في شبرا مصر وشبرا الخيمة وروض الفرج والمظلات 24 ساعة من ونش حجازي. وصول سريع وأرخص تسعيرة سحب سيارات تبدأ من 600 جنيه. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش القاهرة الكبرى",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في شبرا", "ونش شبرا الخيمة", "ونش شبرا مصر", "ونش روض الفرج", "ونش المظلات"]
    },
    {
        "slug": "winch-rehab-madinaty",
        "title": "ونش إنقاذ في الرحاب ومدينتي والشروق والعبور: أوناش حديثة شرق القاهرة 24 ساعة",
        "desc": "خدمات ونش إنقاذ سيارات في مدينتي، الرحاب، الشروق، المستقبل سيتي، وبدر والعبور من ونش حجازي. أحدث أوناش هيدروليكية لحماية السيارات الفاخرة. اتصل الآن 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش المدن الجديدة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ الرحاب", "ونش مدينتي", "ونش الشروق", "ونش المستقبل سيتي", "ونش العبور"]
    },
    {
        "slug": "winch-giza-haram",
        "title": "ونش إنقاذ في الجيزة والهرم وفيصل: أسرع ونش سيارات على الدائري وحدائق الأهرام",
        "desc": "طلب ونش إنقاذ سيارات في الجيزة، شارع الهرم، شارع فيصل، حدائق الأهرام، والرماية 24 ساعة من ونش حجازي. وصول خلال 10 دقائق وأرخص سعر سحب سيارات. اتصل 01032194206.",
        "date": "2026-11-06",
        "category": "أوناش غرب القاهرة والجيزة",
        "read_time": "5 دقائق",
        "keywords": ["ونش انقاذ في الجيزة", "ونش الهرم", "ونش فيصل", "ونش حدائق الاهرام", "ونش الرماية"]
    },
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

]

# Blog Index Page
html_blog_index = f"""{get_head(
    "دليل ومقالات أوناش إنقاذ السيارات في مصر | مدونة ونش حجازي",
    "مقالات وإرشادات شاملة عن خدمات أوناش إنقاذ السيارات في مصر: كيفية العثور على أقرب ونش، أسعار السحب العادلة، تغطية الطريق الدائري والمحاور، وإرشادات السلامة عند الأعطال.",
    "https://winch-hegazy.com/blog/index.html",
    is_blog=True
)}
{generate_local_business_schema(
    "دليل ومقالات أوناش إنقاذ السيارات في مصر | مدونة ونش حجازي",
    "مقالات ونش حجازي لإنقاذ السيارات في مصر.",
    "https://winch-hegazy.com/blog/index.html"
)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("blog", is_blog=True)}

  <section class="py-16 bg-gradient-to-b from-dark-900 to-dark-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">مركز المعرفة والإنقاذ السريع</span>
      <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight">دليل مقالات وأعطال أوناش السيارات في مصر</h1>
      <p class="text-slate-400 text-sm sm:text-base mt-4 max-w-2xl mx-auto">كل ما يهم قائد السيارة في مصر حول أسعار الأوناش، نقاط التمركز على الطرق السريعة، وأسرع طرق طلب النجدة.</p>
    </div>



  <!-- Articles Grid -->
  <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {''.join([f'''
      <article class="glass rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all overflow-hidden flex flex-col justify-between group">
        <div class="p-6 sm:p-7">
          <div class="flex items-center justify-between text-xs text-slate-400 mb-3">
            <span class="px-2.5 py-1 rounded-md bg-slate-900 border border-amber-500/20 text-amber-300 font-bold">{a['category']}</span>
            <span>{a['read_time']}</span>
          </div>
          <h2 class="text-xl font-black text-white group-hover:text-amber-400 transition mb-3 leading-snug">
            <a href="{a['slug']}.html">{a['title']}</a>
          </h2>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed mb-6">{a['desc']}</p>
        </div>
        <div class="px-6 py-4 bg-slate-900/60 border-t border-slate-800/80 flex items-center justify-between">
          <a href="{a['slug']}.html" class="text-xs font-bold text-amber-400 hover:underline flex items-center gap-1">
            <span>قراءة المقال بالكامل</span>
            <span>←</span>
          </a>
          <span class="text-[11px] text-slate-500">{a['date']}</span>
        </div>
      </article>
      ''' for a in articles])}
    </div>



{get_footer(is_blog=True)}
</body>
</html>
"""

with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_blog_index)

print("SUCCESS: blog/index.html generated")


# Generate Individual Articles
def generate_article_file(art, content_body):
    img_filename = art.get("image", "hegazy_red_truck_branding.jpg")
    schema_article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art["title"],
        "description": art["desc"],
        "image": {
            "@type": "ImageObject",
            "url": f"https://winch-hegazy.com/assets/images/{img_filename}",
            "caption": art["title"]
        },
        "url": f"https://winch-hegazy.com/blog/{art['slug']}.html",
        "datePublished": "2026-11-06T10:00:00+02:00",
        "dateModified": "2026-11-06T10:00:00+02:00",
        "author": {
            "@type": "Organization",
            "name": "فريق طوارئ ونش حجازي الميداني",
            "url": "https://winch-hegazy.com/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "ونش إنقاذ حجازي",
            "logo": {
                "@type": "ImageObject",
                "url": "https://winch-hegazy.com/assets/images/logo.png"
            }
        },
        "mainEntityOfPage": f"https://winch-hegazy.com/blog/{art['slug']}.html"
    }

    schema_str = f'<script type="application/ld+json">\n{json.dumps(schema_article, ensure_ascii=False, indent=2)}\n</script>'
    
    html = f"""{get_head(
        f"{art['title']} | ونش حجازي",
        art["desc"],
        f"https://winch-hegazy.com/blog/{art['slug']}.html",
        is_blog=True
    )}
{schema_str}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("blog", is_blog=True)}

  <!-- Article Container -->
  <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-semibold">
      <a href="../index.html" class="hover:text-amber-400">الرئيسية</a>
      <span>/</span>
      <a href="index.html" class="hover:text-amber-400">المقالات</a>
      <span>/</span>
      <span class="text-amber-400 font-bold truncate">{art['category']}</span>
    </nav>

    <!-- Header -->
    <header class="mb-10 space-y-4">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 text-xs font-black">
        <span>{art['category']}</span>
        <span>•</span>
        <span>قراءة في {art['read_time']}</span>
      </div>

      <h1 class="text-2xl sm:text-4xl lg:text-5xl font-black text-white leading-tight tracking-tight">
        {art['title']}
      </h1>

      <p class="text-slate-300 text-sm sm:text-base leading-relaxed border-r-4 border-amber-400 pr-4 bg-slate-900/60 p-4 rounded-xl">
        {art['desc']}
      </p>

      <div class="flex flex-wrap items-center justify-between text-xs text-slate-400 pt-2 border-t border-slate-800">
        <div>بواسطة: <strong class="text-white">فريق العمليات الميدانية - ونش حجازي</strong></div>
        <div>آخر تحديث: <strong>{art['date']}</strong></div>
      </div>
    </header>

    <!-- Immediate Emergency Callout Card -->
    <div class="my-8 p-5 rounded-2xl bg-gradient-to-r from-rescue-900/80 to-slate-900 border border-rescue-500/50 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        <div class="text-white font-black text-base flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-rescue-500 animate-ping"></span>
          <span>هل أنت متعطل الآن وتحتاج ونش فوري؟</span>
        </div>
        <p class="text-xs text-slate-300 mt-1">لا تضيع وقتك في البحث.. أسطول ونش حجازي متواجد بالقرب منك ويصلك خلال دقائق.</p>
      </div>
      <a href="tel:{PHONE}" class="px-6 py-3 bg-rescue-600 hover:bg-rescue-500 text-white font-black rounded-xl text-sm shrink-0 shadow-lg glow-red flex items-center gap-2">
        <span>اتصل الآن ({PHONE_DISPLAY})</span>
      </a>
    </div>

    <!-- Featured Real Operational Image -->
    <figure class="my-8 rounded-2xl overflow-hidden border border-slate-700/80 shadow-2xl bg-slate-900">
      <img src="../assets/images/{img_filename}" alt="{art['title']} - ونش إنقاذ حجازي" class="w-full h-64 sm:h-96 object-cover hover:scale-[1.01] transition-transform duration-500" loading="eager">
      <figcaption class="p-3 text-center text-xs text-slate-400 bg-slate-950/80 border-t border-slate-800 flex items-center justify-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
        <span>صورة حية وموثقة من أسطول ونش إنقاذ حجازي الميداني أثناء تنفيذ عمليات السحب والإنقاذ</span>
      </figcaption>
    </figure>

    <!-- Article Body Content -->
    <div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-sm sm:text-base leading-relaxed">
      {content_body}
    </div>

    <!-- Bottom Action Box -->
    <div class="mt-12 p-8 rounded-3xl glass border border-amber-500/30 text-center space-y-4">
      <h3 class="text-2xl font-black text-white">ونش إنقاذ حجازي في خدمتك 24 ساعة</h3>
      <p class="text-slate-400 text-sm max-w-xl mx-auto">أرخص سعر، أحدث أوناش هيدروليكية، وأسرع استجابة في جميع محافظات مصر والطرق السريعة.</p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
        <a href="tel:{PHONE}" class="w-full sm:w-auto px-8 py-3.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black rounded-xl shadow-lg glow-red">
          اتصال هاتفي مباشر: {PHONE_DISPLAY}
        </a>
        <a href="{WHATSAPP_LINK}" target="_blank" class="w-full sm:w-auto px-6 py-3.5 bg-emerald-600 hover:bg-emerald-500 text-white font-black rounded-xl shadow-lg">
          إرسال الموقع على واتساب
        </a>
      </div>
    </div>
  </article>

{get_footer(is_blog=True)}
</body>
</html>
"""
    with open(os.path.join(blog_dir, f"{art['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"SUCCESS: Generated {art['slug']}.html")


print("Article generator setup complete.")
