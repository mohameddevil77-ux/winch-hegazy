# -*- coding: utf-8 -*-
import os

engine_path = r"D:\winch-hegazy\scripts\build_articles_engine.py"
with open(engine_path, "r", encoding="utf-8") as f:
    code = f.read()

old_fn_start = code.find("def generate_article_file(art, content_body):")
old_fn_end = code.find('print("Article generator setup complete.")', old_fn_start)

if old_fn_start == -1 or old_fn_end == -1:
    print("ERROR: could not locate generate_article_file boundaries")
    exit(1)

new_fn_code = '''def generate_article_file(art, content_body):
    img_filename = art.get("image", "hegazy_red_truck_branding.jpg")
    
    # 1. Article Schema
    schema_article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art["title"],
        "description": art["desc"],
        "image": {
            "@type": "ImageObject",
            "url": f"https://awladhegazy.com/assets/images/{img_filename}",
            "caption": art["title"]
        },
        "url": f"https://awladhegazy.com/blog/{art['slug']}.html",
        "datePublished": "2026-11-06T10:00:00+02:00",
        "dateModified": "2026-11-06T10:00:00+02:00",
        "author": {
            "@type": "Organization",
            "name": "فريق طوارئ أوناش أولاد حجازي الميداني",
            "url": "https://awladhegazy.com/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "أوناش إنقاذ أولاد حجازي",
            "logo": {
                "@type": "ImageObject",
                "url": "https://awladhegazy.com/assets/images/logo.png"
            }
        },
        "mainEntityOfPage": f"https://awladhegazy.com/blog/{art['slug']}.html"
    }

    # 2. BreadcrumbList Schema
    schema_breadcrumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "الرئيسية",
                "item": "https://awladhegazy.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "دليل مقالات أوناش الإنقاذ",
                "item": "https://awladhegazy.com/blog/index.html"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": art["title"],
                "item": f"https://awladhegazy.com/blog/{art['slug']}.html"
            }
        ]
    }

    # 3. Localized FAQPage Schema
    localized_faqs = [
        (f"ما هي تكلفة طلب ونش إنقاذ سيارات في {art['title'][:35]}؟",
         "تبدأ أسعار أوناش أولاد حجازي من 600 جنيه مصري فقط للخدمات الأساسية. نعتمد نظام تسعير شفاف وعادل يعتمد على الكيلومتر والمسافة الفعلية بدون أي استغلال للظروف الطارئة، مع عدم وجود أي إكرامية إجبارية للسائق ومساهمة المؤسسة في رسوم الكارتة."),
        (f"كم يستغرق وصول ونش أولاد حجازي إلى موقعي؟",
         "متوسط زمن الوصول الفعلي يتراوح بين 8 إلى 12 دقيقة بفضل شبكة التمركز الميداني لأوناشنا على مدار 24 ساعة بمحيط كارفور العبور ومحاور القاهرة الكبرى والجيزة والطرق السريعة."),
        (f"كيف أطلب ونش أولاد حجازي وأرسل موقعي المباشر؟",
         f"يمكنك الاتصال فوراً برقم الطوارئ المعتمد 01032194206 أو 01283038303، أو الضغط على زر واتساب لإرسال إحداثيات موقعك الجغرافي (Send Current Location) ليتحرك أقرب ونش إليك فوراً.")
    ]

    schema_str = f"""<script type="application/ld+json">
{json.dumps(schema_article, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(schema_breadcrumbs, ensure_ascii=False, indent=2)}
</script>
{generate_faq_schema(localized_faqs)}
{generate_local_business_schema(art['title'], art['desc'], f"https://awladhegazy.com/blog/{art['slug']}.html")}"""

    html = f"""{get_head(
        f"{art['title']} | أوناش أولاد حجازي",
        art["desc"],
        f"https://awladhegazy.com/blog/{art['slug']}.html",
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
        <div>بواسطة: <strong class="text-white">فريق العمليات الميدانية - أوناش أولاد حجازي</strong></div>
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
        <p class="text-xs text-slate-300 mt-1">لا تضيع وقتك في البحث.. أسطول أوناش أولاد حجازي متواجد بالقرب منك ويصلك خلال دقائق.</p>
      </div>
      <a href="tel:{PHONE}" class="px-6 py-3 bg-rescue-600 hover:bg-rescue-500 text-white font-black rounded-xl text-sm shrink-0 shadow-lg glow-red flex items-center gap-2">
        <span>اتصل الآن ({PHONE_DISPLAY})</span>
      </a>
    </div>

    <!-- Featured Real Operational Image -->
    <figure class="my-8 rounded-2xl overflow-hidden border border-slate-700/80 shadow-2xl bg-slate-900">
      <img src="../assets/images/{img_filename}" alt="{art['title']} - أوناش إنقاذ أولاد حجازي" class="w-full h-64 sm:h-96 object-cover hover:scale-[1.01] transition-transform duration-500" loading="eager">
      <figcaption class="p-3 text-center text-xs text-slate-400 bg-slate-950/80 border-t border-slate-800 flex items-center justify-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
        <span>صورة حية وموثقة من أسطول أوناش إنقاذ أولاد حجازي الميداني أثناء تنفيذ عمليات السحب والإنقاذ</span>
      </figcaption>
    </figure>

    <!-- Article Body Content -->
    <div class="prose prose-invert max-w-none space-y-6 text-slate-300 text-sm sm:text-base leading-relaxed">
      {content_body}
    </div>

    <!-- Authoritative NAP & Local Business Proof (Council Recommendation) -->
    <div class="mt-12 p-6 glass rounded-2xl border border-amber-500/30 text-xs text-slate-300 space-y-2.5 bg-slate-900/70">
      <div class="flex items-center gap-2 text-amber-400 font-black text-sm">
        <span>📍</span>
        <span>بيانات نقطة الارتكاز الميداني والاعتماد الرسمي:</span>
      </div>
      <p><strong class="text-white">المؤسسة:</strong> أوناش إنقاذ أولاد حجازي (Awlad Hegazy Rescue Winch)</p>
      <p><strong class="text-white">نقطة الارتكاز الرئيسية:</strong> كارفور العبور - جولف سيتي مول (مطلع الطريق الدائري ومحور الإسماعيلية الصحراوي)</p>
      <p><strong class="text-white">إحداثيات الملاحة المباشرة GPS:</strong> <a href="https://maps.app.goo.gl/4JvQjcJFPNFqesXS7?g_st=awb" target="_blank" class="text-amber-400 font-bold hover:underline">30.1741147, 31.4761952 (اضغط لفتح خريطة التمركز)</a></p>
      <p><strong class="text-white">هواتف طوارئ العمليات 24/7:</strong> <a href="tel:01032194206" class="text-emerald-400 font-black hover:underline">01032194206</a> - <a href="tel:01283038303" class="text-slate-300 font-black hover:underline">01283038303</a></p>
      <p><strong class="text-white">سياسة التسعير المعتمدة 2026:</strong> تبدأ من 600 جنيه | كود خصم 50%: <span class="text-amber-300 font-mono font-bold">HEGAZY50</span> | بدون أي إكرامية إجبارية للسائق</p>
    </div>

    <!-- Bottom Action Box -->
    <div class="mt-8 p-8 rounded-3xl glass border border-amber-500/30 text-center space-y-4">
      <h3 class="text-2xl font-black text-white">أوناش إنقاذ أولاد حجازي في خدمتك 24 ساعة</h3>
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

code = code[:old_fn_start] + new_fn_code + "\n\n" + code[old_fn_end:]
with open(engine_path, "w", encoding="utf-8") as f:
    f.write(code)
print("SUCCESS: Upgraded generate_article_file in build_articles_engine.py with Council Recommendations!")
