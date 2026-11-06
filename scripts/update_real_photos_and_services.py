import os
import sys

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")
sys.path.append(scripts_dir)

# Read build_articles_engine.py
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    code = f.read()

# Expanded services list with real photos
new_services_list_code = '''services_list = [
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
]'''

# Replace services_list definition in code
idx_serv_start = code.find("services_list = [")
idx_serv_end = code.find("html_services = f\"\"\"{get_head(")
if idx_serv_start != -1 and idx_serv_end != -1:
    code = code[:idx_serv_start] + new_services_list_code + "\n\n" + code[idx_serv_end:]

# Replace services cards loop in html_services
old_serv_loop_target = code.find("<!-- Services Detailed Cards -->")
idx_serv_loop_end = code.find("{get_footer()}", old_serv_loop_target)
if old_serv_loop_target != -1 and idx_serv_loop_end != -1:
    new_serv_loop = '''<!-- Services Detailed Cards -->
  <section class="py-16 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
    {\'\'\'.join([f\'\'\'
    <div id="{s[\'id\']}" class="glass p-6 sm:p-8 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-4 rounded-2xl overflow-hidden border border-slate-700/80 shadow-xl aspect-video lg:aspect-square bg-slate-900 group">
        <img src="assets/images/{s[\'image\']}" alt="{s[\'title\']} - ونش إنقاذ حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
      </div>
      <div class="lg:col-span-5 space-y-4">
        <div class="flex items-center gap-3">
          <span class="text-3xl p-3 bg-slate-900 rounded-2xl border border-amber-500/30">{s[\'icon\']}</span>
          <h2 class="text-xl sm:text-2xl font-black text-white">{s[\'title\']}</h2>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">{s[\'desc\']}</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2">
          {\'\'\'.join([f\'\'\'
          <div class="flex items-center gap-2 text-xs sm:text-sm text-slate-200">
            <span class="text-emerald-400 font-black">✓</span>
            <span>{feat}</span>
          </div>
          \'\'\' for feat in s[\'features\']])}
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
    \'\'\' for s in services_list])}
  </section>

'''
    code = code[:old_serv_loop_target] + new_serv_loop + code[idx_serv_loop_end:]

# Update generate_article_file to include real photos and image Schema
old_gen_article_start = code.find("def generate_article_file(art, content_body):")
old_gen_article_end = code.find("print(\"Article generator setup complete.\")")

new_gen_article = '''def generate_article_file(art, content_body):
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

    schema_str = f'<script type="application/ld+json">\\n{json.dumps(schema_article, ensure_ascii=False, indent=2)}\\n</script>'
    
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
'''

if old_gen_article_start != -1 and old_gen_article_end != -1:
    code = code[:old_gen_article_start] + new_gen_article + "\n\n" + code[old_gen_article_end:]

# Write back to build_articles_engine.py
with open(engine_path, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: Updated build_articles_engine.py with real images and expanded services!")
