import os

engine_path = r"D:\winch-hegazy\scripts\build_articles_engine.py"
with open(engine_path, "r", encoding="utf-8") as f:
    code = f.read()

# Let's locate from "services_list = [" to "with open(os.path.join(base_dir, "services.html")"
idx_start = code.find("services_list = [")
idx_end = code.find("with open(os.path.join(base_dir, \"services.html\")")

clean_services_section = '''services_list = [
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
    features_html = "".join([f\'\'\'
          <div class="flex items-center gap-2 text-xs sm:text-sm text-slate-200">
            <span class="text-emerald-400 font-black">✓</span>
            <span>{feat}</span>
          </div>
    \'\'\' for feat in s["features"]])
    card = f\'\'\'
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
    \'\'\'
    services_cards_list.append(card)

services_cards_rendered = "\\n".join(services_cards_list)

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
'''

code = code[:idx_start] + clean_services_section + code[idx_end:]

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: Cleanly resolved services.html rendering in build_articles_engine.py!")
