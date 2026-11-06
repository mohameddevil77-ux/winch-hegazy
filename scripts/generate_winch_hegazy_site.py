import os
import sys
import json

sys.path.append(r"D:\winch-hegazy\scripts")
from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema, generate_faq_schema, get_map_section, MAPS_URL
)

# -------------------------------------------------------------
# 1. INDEX.HTML
# -------------------------------------------------------------
faq_home = [
    ("كم تكلفة ونش إنقاذ السيارات في مصر مع ونش حجازي؟", 
     "تبدأ أسعار ونش حجازي من 600 جنيه مصري فقط للخدمات الأساسية داخل نفس النطاق الجغرافي. نعتمد نظام تسعير عادل وشفاف يعتمد على المسافة الفعلية ونوع السيارة دون أي استغلال لوقت الطوارئ، مع إبلاغك بالسعر النهائي الصافي قبل تحرك الونش إليك."),
    ("كم يستغرق وصول ونش إنقاذ حجازي إلى موقعي؟",
     "متوسط وقت الوصول الفعلي يتراوح بين 8 إلى 12 دقيقة داخل مناطق القاهرة الكبرى والجيزة، وبحد أقصى 15 دقيقة على الطرق السريعة والصحراوية (مثل الدائري، طريق السويس، ومصر إسكندرية الصحراوي)، وذلك بفضل شبكة ارتكاز أوناشنا الموزعة على مدار 24 ساعة."),
    ("كيف أحدد موقعي للونش إذا تعطلت سيارتي ولا أعرف مكاني بدقة؟",
     "نوفر لك خدمة إرسال الموقع الجغرافي المباشر بنقرة واحدة عبر تطبيق واتساب (Send Current Location). بمجرد إرسال إحداثياتك، يحدد نظام التوجيه أقرب ونش حجازي إليك ويتحرك فوراً مع تتبع مساره حتى الوصول."),
    ("هل أوناش حجازي مجهزة لسحب السيارات الحديثة والمنخفضة (المهبطة) والأوتوماتيك؟",
     "نعم، أسطولنا يضم أحدث أوناش هيدروليكية مغلقة ومزودة بزويا تحميل مسطحة (Full Flatbed) تحمي إكصدامات وعفشة السيارات الرياضية والحديثة بدون أي خدش، مع استخدام أربطة إطارات احترافية (Wheel Straps) مطابقة لأعلى معايير السلامة."),
    ("هل تقدمون خدمات المساعدة على الطريق مثل شحن البطارية وتغيير الإطارات وتوصيل الوقود؟",
     "بالتأكيد، يوفر فريق ونش حجازي وحدات دعم سريع مزودة بمعدات فحص وشحن البطاريات (Jump Start)، كومبريسور هواء وتغيير الإطارات، وتوصيل وقود الطوارئ لإنقاذك في مكانك دون الحاجة لسحب السيارة إذا كان العطل بسيطاً.")
]

html_index = f"""{get_head(
    "ونش إنقاذ حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"ونش إنقاذ حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://winch-hegazy.com/"
)}
{generate_local_business_schema(
    "ونش إنقاذ حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"ونش إنقاذ حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://winch-hegazy.com/"
)}
{generate_faq_schema(faq_home)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("home")}

  <!-- Hero Section -->
  <section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden bg-cover bg-center bg-no-repeat" style="background-image: linear-gradient(to bottom, rgba(3, 7, 18, 0.84), rgba(3, 7, 18, 0.96)), url('assets/images/hero_rescue_bg.jpg');">
    <div class="absolute inset-0 bg-[radial-gradient(#f59e0b_1px,transparent_1px)] [background-size:24px_24px] opacity-10 pointer-events-none"></div>
    <div class="absolute top-1/4 right-1/4 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-1/4 left-1/4 w-96 h-96 bg-rescue-600/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Right Column: Hero Pitch (7 cols) -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-right">
          
          <!-- Urgent Badge -->
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-900 border border-amber-500/40 shadow-lg">
            <span class="w-3 h-3 rounded-full bg-rescue-500 animate-ping"></span>
            <span class="text-xs md:text-sm font-black text-amber-300">خدمة إنقاذ طوارئ سريعة • نصلك خلال 10 دقائق في أي مكان</span>
          </div>

          <!-- Main H1 Headline -->
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white leading-[1.25] tracking-tight">
            أسرع وأرخص <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500">ونش إنقاذ سيارات</span> في مصر
          </h1>

          <!-- Lead Paragraph -->
          <p class="text-slate-300 text-base md:text-lg lg:text-xl leading-relaxed max-w-2xl mx-auto lg:mx-0 font-medium">
            تعطلت سيارتك في الطريق؟ لا تقلق! أسطول <strong class="text-white font-extrabold">ونش حجازي</strong> متمركز على مدار 24 ساعة في جميع أنحاء القاهرة الكبرى والجيزة وكافة المحاور السريعة لنصلك في دقائق معدودة بأحدث أوناش هيدروليكية مغلقة وأرخص سعر بدون أي استغلال.
          </p>

          <!-- Core Call Actions -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-4">
            <a href="tel:{PHONE}" class="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-rescue-600 to-rescue-700 hover:from-rescue-500 hover:to-rescue-600 text-white font-black text-lg rounded-2xl shadow-xl glow-red transition-all transform hover:-translate-y-1 flex items-center justify-center gap-3">
              <svg class="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <span>اتصل فوراً: {PHONE_DISPLAY}</span>
            </a>

            <a href="{WHATSAPP_LINK}" target="_blank" class="w-full sm:w-auto px-6 py-4 bg-slate-900 hover:bg-slate-800 border-2 border-emerald-500/50 hover:border-emerald-400 text-emerald-400 font-extrabold text-base rounded-2xl transition-all flex items-center justify-center gap-2 shadow-lg">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.173.086.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.072.043.419-.101.824z"/>
              </svg>
              <span>أرسل موقعك على واتساب</span>
            </a>
          </div>

          <!-- Proof Metrics Strip -->
          <div class="grid grid-cols-3 gap-3 pt-6 border-t border-slate-800/80 max-w-lg mx-auto lg:mx-0 text-center">
            <div class="glass p-3 rounded-xl border border-amber-500/20">
              <div class="text-xl md:text-2xl font-black text-amber-400">10 دقائق</div>
              <div class="text-[11px] md:text-xs text-slate-400 font-bold">متوسط وقت الوصول</div>
            </div>
            <div class="glass p-3 rounded-xl border border-emerald-500/20">
              <div class="text-xl md:text-2xl font-black text-emerald-400">600 ج.م</div>
              <div class="text-[11px] md:text-xs text-slate-400 font-bold">أرخص سعر بدء خدمة</div>
            </div>
            <div class="glass p-3 rounded-xl border border-cyan-500/20">
              <div class="text-xl md:text-2xl font-black text-cyan-400">24/7</div>
              <div class="text-[11px] md:text-xs text-slate-400 font-bold">طوارئ بلا توقف</div>
            </div>
          </div>
        </div>

        <!-- Left Column: Visual Fleet Card (5 cols) -->
        <div class="lg:col-span-5">
          <div class="relative mx-auto max-w-md">
            <div class="absolute -inset-1.5 rounded-3xl bg-gradient-to-tr from-amber-500 via-rescue-600 to-amber-500 opacity-30 blur-xl"></div>
            
            <div class="relative rounded-3xl bg-slate-900 border-2 border-amber-500/40 overflow-hidden shadow-2xl p-5">
              
              <!-- Card Header -->
              <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                  <span class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
                  <span class="text-xs font-black text-white">شبكة الإنقاذ الميداني المباشر</span>
                </div>
                <span class="text-[10px] bg-amber-500/20 text-amber-300 border border-amber-500/30 px-2 py-0.5 rounded-full font-bold">جاهزية 100%</span>
              </div>

              <!-- Real Truck Image -->
              <div class="my-4 rounded-2xl overflow-hidden border border-slate-700 bg-slate-950 relative aspect-[4/3]">
                <img src="assets/images/hegazy_red_truck_branding.jpg" alt="ونش إنقاذ حجازي الأصلي HEGAZY أحدث أسطول هيدروليكي" class="w-full h-full object-cover">
                <div class="absolute bottom-2 right-2 left-2 bg-slate-950/85 backdrop-blur-sm p-2 rounded-xl border border-amber-400/40 text-xs flex items-center justify-between">
                  <span class="font-black text-amber-300">أسطول ونش حجازي المعتمد (HEGAZY)</span>
                  <span class="text-emerald-400 font-bold">✓ نقل آمن بدون خدوش</span>
                </div>
              </div>

              <!-- Quick Local Coverage Ticker -->
              <div class="space-y-2 text-xs">
                <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950/60 border border-slate-800">
                  <span class="text-slate-300">أقرب ونش متمركز الآن:</span>
                  <span class="text-amber-400 font-bold">الدائري • التجمع • زايد • السويس</span>
                </div>
                <div class="flex items-center justify-between p-2 rounded-lg bg-slate-950/60 border border-slate-800">
                  <span class="text-slate-300">رقم الخط الساخن المباشر:</span>
                  <a href="tel:{PHONE}" class="text-emerald-400 font-black hover:underline">{PHONE_DISPLAY}</a>
                </div>
              </div>

              <!-- Call Now Button inside card -->
              <a href="tel:{PHONE}" class="mt-4 w-full py-3 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black text-sm rounded-xl flex items-center justify-center gap-2 hover:opacity-95 transition shadow-md">
                <span>طلب الونش فوراً إلى موقعي</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Interactive Cost & Distance Estimator Section -->
  <section id="calculator" class="py-16 bg-slate-900/60 border-y border-slate-800 relative">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-10">
        <span class="px-3 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">حاسبة تسعيرة الونش الفورية</span>
        <h2 class="text-2xl md:text-4xl font-black text-white">احسب تكلفة ووقت وصول ونش حجازي إليك</h2>
        <p class="text-slate-400 text-sm mt-2">اختر موقع تعطل السيارة والوجهة المراد السحب إليها لتقدير التكلفة والوقت مسبقاً بكل شفافية.</p>
      </div>

      <div class="glass p-6 md:p-8 rounded-3xl border border-amber-500/30 max-w-3xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          
          <div>
            <label class="block text-xs font-bold text-slate-300 mb-2">مكان تعطل السيارة الحالي (موقعك):</label>
            <select id="startLoc" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white font-bold focus:border-amber-400 focus:outline-none">
              <option value="obour" selected>مدينة العبور (كارفور / سوق العبور / جولف سيتي)</option>
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
              <option value="alex">طريق مصر إسكندرية الصحراوي</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-bold text-slate-300 mb-2">مكان توصيل السيارة (الوجهة):</label>
            <select id="endLoc" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white font-bold focus:border-amber-400 focus:outline-none">
              <option value="same">في نفس المنطقة (ورشة / بنزينة قريبة)</option>
              <option value="center">مركز صيانة / توكيل معتمد</option>
              <option value="home">المنزل / الجراج الخاص</option>
              <option value="cross">محافظة أخرى / نقل بين المدن</option>
            </select>
          </div>

        </div>

        <div class="mb-6">
          <label class="block text-xs font-bold text-slate-300 mb-2">نوع وحجم السيارة:</label>
          <div class="grid grid-cols-3 gap-2">
            <button type="button" onclick="setCarType('sedan')" id="btn-sedan" class="py-2.5 px-3 rounded-xl bg-amber-500 text-slate-950 font-black text-xs border border-amber-400 transition cursor-pointer">ملاكي / سيدان / هاتشباك</button>
            <button type="button" onclick="setCarType('suv')" id="btn-suv" class="py-2.5 px-3 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition cursor-pointer">دفع رباعي / SUV / فان</button>
            <button type="button" onclick="setCarType('heavy')" id="btn-heavy" class="py-2.5 px-3 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition cursor-pointer">نقل / جامبو / بيك آب</button>
          </div>
        </div>

        <!-- Result Box -->
        <div class="bg-slate-950/80 p-5 rounded-2xl border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-4">
          <div>
            <div class="text-xs text-slate-400">التكلفة التقديرية العادلة:</div>
            <div class="text-2xl md:text-3xl font-black text-amber-400" id="calcPrice">600 - 750 ج.م</div>
            <div class="text-[11px] text-emerald-400 font-semibold" id="calcTime">✓ زمن الوصول المقدر: 8 - 12 دقيقة</div>
          </div>
          <a href="tel:{PHONE}" class="w-full md:w-auto px-6 py-3.5 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black text-sm rounded-xl shadow-lg glow-red hover:opacity-95 transition text-center">
            تأكيد الطلب مع أقرب ونش فوراً
          </a>
        </div>
      
        <!-- Trust & Fairness Guarantee Card -->
        <div class="mt-8 p-5 sm:p-6 rounded-3xl bg-gradient-to-r from-amber-500/10 via-emerald-500/10 to-slate-900 border border-amber-500/30 text-right flex flex-col sm:flex-row items-center justify-between gap-4">
          <div class="space-y-1.5">
            <div class="font-black text-amber-300 text-sm sm:text-base flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
              <span>ميثاق الشفافية والمصداقية مع تغيرات أسعار الوقود 2026:</span>
            </div>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-2xl">
              حددنا تسعيرة واقعية تبدأ من <strong>600 ج.م</strong> لضمان الأمانة وعدم المفاجأة عند الاتصال. السعر المتفق عليه نهائي وشامل <strong>بدون أي إكرامية إجبارية للسائق</strong>، مع <strong>مساهمة في دفع رسوم الكارتة</strong> على الطرق السريعة.
            </p>
          </div>
          <a href="blog/winch-offers-discounts-cairo.html" class="px-5 py-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-black rounded-xl text-xs sm:text-sm whitespace-nowrap shadow-lg transition flex items-center gap-1.5">
            <span>تفعيل خصم 50%</span>
            <span>←</span>
          </a>
        </div>
</div>
    </div>
  </section>

  <!-- 8 Core Services Grid -->
  <section class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-rescue-500/15 text-rescue-400 border border-rescue-500/30 mb-3 inline-block">خدماتنا الميدانية المعتمدة</span>
      <h2 class="text-3xl md:text-5xl font-black text-white">خدمات ونش إنقاذ ونقل سيارات ومعدات متكاملة 24 ساعة</h2>
      <p class="text-slate-400 text-sm md:text-base mt-3">نمتلك أسطولاً حديثاً ومجهزاً بأعلى تقنيات السحب والرفع الهيدروليكي للتعامل مع كافة حالات الأعطال والحوادث ونقل المعدات والكرفانات.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      
      <!-- Service 1 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🚗</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">إنقاذ وسحب السيارات الملاكي</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">سحب آمن 100% لجميع فئات السيارات الملاكي والفاخرة بأوناش مسطحة تحافظ على زوايا الصدمات والعفشة.</p>
        </div>
        <a href="services.html#private-cars" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 2 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">⚡</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">إنقاذ سريع على المحاور والدائري</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">نقاط تمركز استراتيجية على محاور الدائري، محور 26 يوليو، وطريق السويس لسرعة التدخل خلال 10 دقائق.</p>
        </div>
        <a href="services.html#highways" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 3 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🛞</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">المساعدة السريعة على الطريق</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">شحن وتدوير بطاريات السيارة في مكانك، تغيير الإطارات الممزقة، وتزويدك بوقود الطوارئ لإنهاء العطل فوراً.</p>
        </div>
        <a href="services.html#roadside" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 4 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🏢</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">إنقاذ الجراجات والبدرومات</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">أوناش ذات ارتفاعات مدروسة قادرة على النزول في جراجات المولات والمباني السكنية وسحب السيارات المتعطلة بالداخل.</p>
        </div>
        <a href="services.html#underground" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 5 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🚛</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">سحب النقل ورؤوس التريلات</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">أوناش عملاقة بقدرات سحب هيدروليكية 15 طناً لنقل الشاحنات ورؤوس التريلات والجامبو وسيارات النقل بأمان.</p>
        </div>
        <a href="services.html#heavy" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 6 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🛡️</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">سحب ونقل سيارات الحوادث</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">فريق متخصص بمعدات رافعة لانتشال السيارات من المنحدرات والرمال وجوانب الطرق بعد الحوادث بدقة متناهية.</p>
        </div>
        <a href="services.html#accidents" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 7 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🏗️</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">نقل الكرفانات والمواقع الإنشائية</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">طبالي مسطحة ممتدة حتى 12 متراً لنقل الكرفانات السكنية والمكاتب المتنقلة وحاويات الشركات بين المدن بأمان.</p>
        </div>
        <a href="services.html#caravans" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

      <!-- Service 8 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/50 transition-all group flex flex-col justify-between">
        <div>
          <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black text-2xl mb-4 group-hover:scale-110 transition-transform">🍔</div>
          <h3 class="text-lg font-black text-white mb-2 group-hover:text-amber-400 transition">نقل الفود تراك وعربات الجولف</h3>
          <p class="text-slate-400 text-xs leading-relaxed mb-4">نقل احترافي لعربات المطاعم المتنقلة (Food Trucks) وأساطيل عربات الجولف كارت للمنتجعات والملاعب والكمبوندات.</p>
        </div>
        <a href="services.html#food-trucks" class="text-xs text-amber-400 font-bold hover:underline flex items-center gap-1">المزيد عن الخدمة ←</a>
      </div>

    </div>
  </section>

  <!-- Why Choose Hegazy (Credibility & Speed) -->
  <section class="py-16 bg-slate-900/40 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div>
          <span class="text-xs font-black text-amber-400 bg-amber-500/10 border border-amber-500/30 px-3 py-1 rounded-full mb-3 inline-block">لماذا يثق بنا آلاف السائقين في مصر؟</span>
          <h2 class="text-3xl md:text-4xl font-black text-white mb-6">سرعة استجابة حقيقية ومصداقية في السعر بدون استغلال وقت الأزمة</h2>
          
          <div class="space-y-4">
            <div class="flex items-start gap-4 p-3 rounded-2xl bg-slate-950/60 border border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">✓</div>
              <div>
                <h4 class="text-white font-extrabold text-sm mb-1">تسعير محدد مسبقاً قبل تحرك الونش</h4>
                <p class="text-slate-400 text-xs">لا مفاجآت عند الوصول ولا طلب إكراميات إضافية. السعر المتفق عليه على الهاتف هو السعر النهائي.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-3 rounded-2xl bg-slate-950/60 border border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">✓</div>
              <div>
                <h4 class="text-white font-extrabold text-sm mb-1">أحدث أسطول هيدروليكي 2026</h4>
                <p class="text-slate-400 text-xs">نبتعد عن الأوناش السلكية القديمة التي تضر هياكل السيارات ونستخدم زوايا هبوط كاملة تناسب السيارات الحديثة.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-3 rounded-2xl bg-slate-950/60 border border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">✓</div>
              <div>
                <h4 class="text-white font-extrabold text-sm mb-1">سائقون محترفون ومدربون على السلامة المهنية</h4>
                <p class="text-slate-400 text-xs">فريق عمل مؤهل يضمن تثبيت السيارة بعناية وتأمين مسارها حتى الوصول بأمان تام لوجهتك المطلوبة.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Real Fleet Image Showcase -->
        <div class="grid grid-cols-2 gap-4">
          <img src="assets/images/hegazy_luxury_car_flatbed.jpg" alt="سحب وتثبيت السيارات الفاخرة ونش حجازي" class="rounded-2xl border border-slate-700 shadow-xl object-cover h-64 w-full">
          <img src="assets/images/hegazy_orange_truck_porsche.jpg" alt="ونش إنقاذ سيارات حديث ونش حجازي" class="rounded-2xl border border-slate-700 shadow-xl object-cover h-64 w-full mt-6">
        </div>
      </div>
    </div>
  </section>

  <!-- Real Fleet Photo Gallery (صور حية من أرض الواقع لأسطول ونش حجازي) -->
  <section class="py-16 bg-slate-900/60 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="px-3.5 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">أسطولنا المعتمد على أرض الواقع</span>
        <h2 class="text-3xl md:text-5xl font-black text-white">صور حقيقية لعمليات ونش حجازي الميدانية</h2>
        <p class="text-slate-400 text-sm md:text-base mt-3">لسنا مجرد أرقام وسيطة.. نحن نمتلك وندير أسطول أوناش إنقاذ حقيقي مسجل باسم "HEGAZY" لإنقاذ السيارات الفارهة والمعدات الثقيلة بأعلى درجات الأمان الاحترافي.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Photo 1: Red Hegazy Truck Brand -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_branding.jpg" alt="ونش حجازي المعتمد HEGAZY وأرقام الطوارئ الميدانية الرسمية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">ونش حجازي الرسمي المعتمد (HEGAZY)</h4>
            <p class="text-slate-400 text-xs">أسطول إيسوزو حديث مرخص يحمل شعار وأرقام طوارئ ونش حجازي الميدانية.</p>
          </div>
        </div>

        <!-- Photo 2: Porsche Highway Flatbed -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_orange_truck_porsche.jpg" alt="إنقاذ سيارات الدفع الرباعي بورش على الطرق السريعة" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">إنقاذ سيارات الدفع الرباعي والبورش</h4>
            <p class="text-slate-400 text-xs">تأمين نقل سيارات الـ SUV الفارهة على الطريق الدائري والصحراوي والسويس.</p>
          </div>
        </div>

        <!-- Photo 3: Luxury Cupra Crossover -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_luxury_car_flatbed.jpg" alt="سحب وتثبيت السيارات الفاخرة والرياضية بأربطة الإطارات بدون خدوش" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">عناية فائقة بالسيارات الحديثة</h4>
            <p class="text-slate-400 text-xs">تثبيت احترافي بأحزمة الإطارات (Wheel Straps) يمنع أي احتكاك أو ضرر بالهيكل.</p>
          </div>
        </div>

        <!-- Photo 4: Tractor Head Heavy Recovery -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_semi_truck_head.jpg" alt="سحب وإنقاذ رؤوس التريلات والشاحنات الضخمة Actros على ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">سحب رؤوس التريلات والشاحنات</h4>
            <p class="text-slate-400 text-xs">قدرات سحب جبارة لنقل رؤوس الشاحنات والتريلات المعطلة بسلامة كاملة.</p>
          </div>
        </div>

        <!-- Photo 5: Caravan Construction Site Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_caravan_transport.jpg" alt="نقل الكرفانات والمكاتب الإدارية ومواقع الإنشاءات على ونش حجازي مسطح" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل الكرفانات وغرف المواقع</h4>
            <p class="text-slate-400 text-xs">طبالي مسطحة ممتدة لنقل الكرفانات السكنية والمكاتب المتنقلة بين المشاريع.</p>
          </div>
        </div>

        <!-- Photo 6: Golf Carts Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_golf_carts_transport.jpg" alt="نقل عربات الجولف كارت للمنتجعات والملاعب والقرى السياحية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل عربات الجولف كارت للمنتجعات</h4>
            <p class="text-slate-400 text-xs">نقل آمن بحمولة مزدوجة لعربات الجولف كارت للكمبوندات والقرى السياحية.</p>
          </div>
        </div>

        <!-- Photo 7: Food Truck Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_food_truck_transport.jpg" alt="نقل عربات الطعام المتنقلة فود تراك والمقطورات التجارية على ونش حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل عربات الطعام (Food Trucks)</h4>
            <p class="text-slate-400 text-xs">نقل وتوصيل مقطورات الفود تراك والأكشاك الحديثة للمعارض والميادين بأمان.</p>
          </div>
        </div>

        <!-- Photo 8: Heavy Forklift Industrial -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_heavy.jpg" alt="سحب ونقل الرافعات الشوكية والمعدات الثقيلة في المصانع والصوامع" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="p-4">
            <h4 class="text-white font-extrabold text-sm mb-1">نقل المعدات والرافعات الشوكية</h4>
            <p class="text-slate-400 text-xs">قدرات جر وسحب فائقة لنقل معدات المصانع، الفورك لفت، والشاحنات.</p>
          </div>
        </div>

      </div>
    </div>
  </section>

  {get_map_section()}

  <!-- FAQ Section (AEO Structured for Google & AI Overviews) -->
  <section class="py-20 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-2xl mx-auto mb-14">
      <span class="px-3 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">الأسئلة الشائعة وإجابات الطوارئ</span>
      <h2 class="text-2xl md:text-4xl font-black text-white">كل ما تحتاج معرفته عن خدمات ونش حجازي</h2>
      <p class="text-slate-400 text-sm mt-2">إجابات واضحة ومباشرة تساعدك على اتخاذ القرار الصحيح عند تعطل سيارتك.</p>
    </div>

    <div class="space-y-4">
      {''.join([f'''
      <div class="glass p-5 rounded-2xl border border-slate-800">
        <h3 class="text-base md:text-lg font-black text-amber-300 mb-2 flex items-center gap-2">
          <span>❓</span>
          <span>{q}</span>
        </h3>
        <p class="text-slate-300 text-xs md:text-sm leading-relaxed pr-6">{a}</p>
      </div>
      ''' for q, a in faq_home])}
    </div>
  </section>

  <!-- Final Urgent CTA Banner -->
  <section class="py-16 bg-gradient-to-r from-rescue-900 via-dark-900 to-amber-950 border-t border-amber-500/30 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl md:text-4xl font-black text-white mb-4">متعطل على الطريق الآن؟ لا تنتظر!</h2>
      <p class="text-slate-300 text-sm md:text-base max-w-2xl mx-auto mb-8">أقرب ونش إنقاذ من ونش حجازي على بُعد دقائق منك. اتصل بنا وسنصلك فوراً لموقعك أينما كنت في مصر.</p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="tel:{PHONE}" class="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-rescue-600 to-amber-500 hover:from-rescue-500 hover:to-amber-400 text-white font-black text-lg rounded-2xl shadow-xl glow-red flex items-center justify-center gap-2">
          <span>اتصال طوارئ فوري: {PHONE_DISPLAY}</span>
        </a>
        <a href="{WHATSAPP_LINK}" target="_blank" class="w-full sm:w-auto px-8 py-4 bg-emerald-600 hover:bg-emerald-500 text-white font-black text-lg rounded-2xl shadow-lg flex items-center justify-center gap-2">
          <span>إرسال اللوكيشن على واتساب</span>
        </a>
      </div>
    </div>
  </section>

{get_footer()}

<script>
  let currentCar = 'sedan';
  const priceMap = {{
    sedan: {{ same: '600 - 750 ج.م', center: '750 - 950 ج.م', home: '950 - 1300 ج.م', cross: 'يبدأ من 1500 ج.م' }},
    suv: {{ same: '750 - 900 ج.م', center: '900 - 1200 ج.م', home: '1200 - 1600 ج.م', cross: 'يبدأ من 1800 ج.م' }},
    heavy: {{ same: '1200 - 1600 ج.م', center: '1600 - 2200 ج.م', home: '2200 - 3000 ج.م', cross: 'يبدأ من 3000 ج.م' }}
  }};
  
  function updateCalc() {{
    const end = document.getElementById('endLoc').value;
    const priceText = priceMap[currentCar][end] || '600 - 750 ج.م';
    document.getElementById('calcPrice').innerText = priceText;
  }}

  function setCarType(type) {{
    currentCar = type;
    ['sedan', 'suv', 'heavy'].forEach(t => {{
      const btn = document.getElementById('btn-' + t);
      if (t === type) {{
        btn.className = 'py-2.5 px-3 rounded-xl bg-amber-500 text-slate-950 font-black text-xs border border-amber-400 transition cursor-pointer';
      }} else {{
        btn.className = 'py-2.5 px-3 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition cursor-pointer';
      }}
    }});
    updateCalc();
  }}

  document.getElementById('startLoc').addEventListener('change', updateCalc);
  document.getElementById('endLoc').addEventListener('change', updateCalc);
</script>
</body>
</html>
"""

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_index)

print("SUCCESS: index.html generated")
