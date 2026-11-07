import os
import sys
import json

sys.path.append(r"D:\winch-hegazy\scripts")
from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema, generate_faq_schema, generate_video_schema, get_map_section, MAPS_URL
)

# -------------------------------------------------------------
# 1. INDEX.HTML
# -------------------------------------------------------------
faq_home = [
    ("كم تكلفة ونش إنقاذ السيارات في مصر مع أوناش أولاد حجازي؟", 
     "تبدأ أسعار أوناش أولاد حجازي من 600 جنيه مصري فقط للخدمات الأساسية داخل نفس النطاق الجغرافي. نعتمد نظام تسعير عادل وشفاف يعتمد على المسافة الفعلية ونوع السيارة دون أي استغلال لوقت الطوارئ، مع إبلاغك بالسعر النهائي الصافي قبل تحرك الونش إليك."),
    ("كم يستغرق وصول أوناش إنقاذ أولاد حجازي إلى موقعي؟",
     "متوسط وقت الوصول الفعلي يتراوح بين 8 إلى 12 دقيقة داخل مناطق القاهرة الكبرى والجيزة، وبحد أقصى 15 دقيقة على الطرق السريعة والصحراوية (مثل الدائري، طريق السويس، ومصر إسكندرية الصحراوي)، وذلك بفضل شبكة ارتكاز أوناشنا الموزعة على مدار 24 ساعة."),
    ("كيف أحدد موقعي للونش إذا تعطلت سيارتي ولا أعرف مكاني بدقة؟",
     "نوفر لك خدمة إرسال الموقع الجغرافي المباشر بنقرة واحدة عبر تطبيق واتساب (Send Current Location). بمجرد إرسال إحداثياتك، يحدد نظام التوجيه أقرب أوناش أولاد حجازي إليك ويتحرك فوراً مع تتبع مساره حتى الوصول."),
    ("هل أوناش حجازي مجهزة لسحب السيارات الحديثة والمنخفضة (المهبطة) والأوتوماتيك؟",
     "نعم، أسطولنا يضم أحدث أوناش هيدروليكية مغلقة ومزودة بزويا تحميل مسطحة (Full Flatbed) تحمي إكصدامات وعفشة السيارات الرياضية والحديثة بدون أي خدش، مع استخدام أربطة إطارات احترافية (Wheel Straps) مطابقة لأعلى معايير السلامة."),
    ("هل تقدمون خدمات المساعدة على الطريق مثل شحن البطارية وتغيير الإطارات وتوصيل الوقود؟",
     "بالتأكيد، يوفر فريق أوناش أولاد حجازي وحدات دعم سريع مزودة بمعدات فحص وشحن البطاريات (Jump Start)، كومبريسور هواء وتغيير الإطارات، وتوصيل وقود الطوارئ لإنقاذك في مكانك دون الحاجة لسحب السيارة إذا كان العطل بسيطاً.")
]

html_index = f"""{get_head(
    "أوناش إنقاذ أولاد حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"أوناش إنقاذ أولاد حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://awladhegazy.com/",
    is_blog=False,
    preload_lcp="assets/images/hero_rescue_bg.webp"
)}
{generate_local_business_schema(
    "أوناش إنقاذ أولاد حجازي | أسرع وأرخص ونش إنقاذ سيارات في مصر 24 ساعة",
    f"أوناش إنقاذ أولاد حجازي لإنقاذ السيارات في القاهرة والجيزة والطرق السريعة. وصول خلال 10 دقائق، أحدث أوناش هيدروليكية، وأرخص سعر سحب سيارات يبدأ من 600 جنيه. اتصل الآن {PHONE_DISPLAY}.",
    "https://awladhegazy.com/"
)}
{generate_faq_schema(faq_home)}

  {generate_video_schema()}


</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("home")}

  <main id="main-content">

  <!-- Hero Section -->
  <section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden bg-cover bg-center bg-no-repeat" style="background-image: linear-gradient(to bottom, rgba(3, 7, 18, 0.84), rgba(3, 7, 18, 0.96)), url('assets/images/hero_rescue_bg.webp');">
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
            تعطلت سيارتك في الطريق؟ لا تقلق! أسطول <strong class="text-white font-extrabold">أوناش أولاد حجازي</strong> متمركز على مدار 24 ساعة في جميع أنحاء القاهرة الكبرى والجيزة وكافة المحاور السريعة لنصلك في دقائق معدودة بأحدث أوناش هيدروليكية مغلقة وأرخص سعر بدون أي استغلال.
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
                <img src="assets/images/hegazy_red_truck_branding.webp" alt="أوناش إنقاذ أولاد حجازي الأصلي HEGAZY أحدث أسطول هيدروليكي" class="w-full h-full object-cover" loading="lazy" decoding="async">
                <div class="absolute bottom-2 right-2 left-2 bg-slate-950/85 backdrop-blur-sm p-2 rounded-xl border border-amber-400/40 text-xs flex items-center justify-between">
                  <span class="font-black text-amber-300">أسطول أوناش أولاد حجازي المعتمد (HEGAZY)</span>
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
        <h2 class="text-2xl md:text-4xl font-black text-white">احسب تكلفة ووقت وصول أوناش أولاد حجازي إليك</h2>
        <p class="text-slate-400 text-sm mt-2">اختر موقع تعطل السيارة والوجهة المراد السحب إليها لتقدير التكلفة والوقت مسبقاً بكل شفافية.</p>
      </div>

      <div class="glass p-6 md:p-8 rounded-3xl border border-amber-500/30 max-w-3xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          
          <div>
            <label for="startLoc" class="block text-xs font-bold text-slate-300 mb-2">مكان تعطل السيارة الحالي (موقعك):</label>
            <select id="startLoc" name="startLoc" aria-label="مكان تعطل السيارة الحالي (موقعك)" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white font-bold focus:border-amber-400 focus:outline-none">
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
            <label for="endLoc" class="block text-xs font-bold text-slate-300 mb-2">مكان توصيل السيارة (الوجهة):</label>
            <select id="endLoc" name="endLoc" aria-label="مكان توصيل السيارة (الوجهة)" class="w-full bg-slate-950 border border-slate-700 rounded-xl p-3 text-sm text-white font-bold focus:border-amber-400 focus:outline-none">
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
                <h3 class="text-white font-extrabold text-sm mb-1">تسعير محدد مسبقاً قبل تحرك الونش</h3>
                <p class="text-slate-400 text-xs">لا مفاجآت عند الوصول ولا طلب إكراميات إضافية. السعر المتفق عليه على الهاتف هو السعر النهائي.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-3 rounded-2xl bg-slate-950/60 border border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">✓</div>
              <div>
                <h3 class="text-white font-extrabold text-sm mb-1">أحدث أسطول هيدروليكي 2026</h3>
                <p class="text-slate-400 text-xs">نبتعد عن الأوناش السلكية القديمة التي تضر هياكل السيارات ونستخدم زوايا هبوط كاملة تناسب السيارات الحديثة.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-3 rounded-2xl bg-slate-950/60 border border-slate-800">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">✓</div>
              <div>
                <h3 class="text-white font-extrabold text-sm mb-1">سائقون محترفون ومدربون على السلامة المهنية</h3>
                <p class="text-slate-400 text-xs">فريق عمل مؤهل يضمن تثبيت السيارة بعناية وتأمين مسارها حتى الوصول بأمان تام لوجهتك المطلوبة.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Real Fleet Image Showcase -->
        <div class="grid grid-cols-2 gap-4">
          <img src="assets/images/hegazy_luxury_car_flatbed.webp" alt="سحب وتثبيت السيارات الفاخرة أوناش أولاد حجازي" class="rounded-2xl border border-slate-700 shadow-xl object-cover h-64 w-full" loading="lazy" decoding="async">
          <img src="assets/images/hegazy_orange_truck_porsche.webp" alt="ونش إنقاذ سيارات حديث أوناش أولاد حجازي" class="rounded-2xl border border-slate-700 shadow-xl object-cover h-64 w-full mt-6" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- Real Fleet Photo Gallery (صور حية من أرض الواقع لأسطول أوناش أولاد حجازي) -->
  <section class="py-16 bg-slate-900/60 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="px-3.5 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">أسطولنا المعتمد على أرض الواقع</span>
        <h2 class="text-3xl md:text-5xl font-black text-white">صور حقيقية لعمليات أوناش أولاد حجازي الميدانية</h2>
        <p class="text-slate-400 text-sm md:text-base mt-3">لسنا مجرد أرقام وسيطة.. نحن نمتلك وندير أسطول أوناش إنقاذ حقيقي مسجل باسم "HEGAZY" لإنقاذ السيارات الفارهة والمعدات الثقيلة بأعلى درجات الأمان الاحترافي.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
                <!-- Photo 1: Lamborghini Supercar Night -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_lamborghini_night.webp" alt="نقل سيارات السوبر كار لامبورجيني ليلاً أوناش أولاد حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-rescue-600/90 text-white text-[10px] font-black tracking-wider uppercase">سوبر كار VIP</span>
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل سيارات السوبر كار (لامبورجيني هوراكان)</h3>
            <p class="text-slate-400 text-xs">سحب وتثبيت السيارات الفارهة والخارقة ليلاً بأربطة عجلات مطاطية وإضاءات تأمين كاملة.</p>
          </div>
        </div>

        <!-- Photo 2: Caterpillar Heavy Loader -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_caterpillar_loader.webp" alt="نقل لودر كاتربيلر CAT 930 أوناش أولاد حجازي للمعدات الثقيلة" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-amber-500/90 text-slate-950 text-[10px] font-black tracking-wider">معدات ثقيلة</span>
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل اللوادر والمعدات (كاتربيلر CAT 930)</h3>
            <p class="text-slate-400 text-xs">قدرات شاقة لنقل لوادر ومعدات الإنشاءات والحفر لمواقع المشروعات والعاصمة الإدارية.</p>
          </div>
        </div>

        <!-- Photo 3: Construction Loader Desert Project -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_heavy_equipment_loader.webp" alt="نقل معدات الحفر والصحراء لودر WA100 أوناش أولاد حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-slate-800 text-amber-300 text-[10px] font-black">مواقع ومحاجر</span>
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">خدمة مواقع العمل الصحراوية والمحاجر</h3>
            <p class="text-slate-400 text-xs">نقل معدات البناء والصوامع (لودر WA100) بين المشروعات في بدر والعبور والإسماعيلية.</p>
          </div>
        </div>

        <!-- Photo 4: Red Hegazy Truck Brand -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_branding.webp" alt="أوناش أولاد حجازي المعتمد HEGAZY وأرقام الطوارئ الميدانية الرسمية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">أوناش أولاد حجازي الرسمي المعتمد (HEGAZY)</h3>
            <p class="text-slate-400 text-xs">أسطول إيسوزو حديث مرخص يحمل شعار وأرقام طوارئ أوناش أولاد حجازي الميدانية.</p>
          </div>
        </div>

        <!-- Photo 5: Porsche Highway Flatbed -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_orange_truck_porsche.webp" alt="إنقاذ سيارات الدفع الرباعي بورش على الطرق السريعة" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">إنقاذ سيارات الدفع الرباعي والبورش</h3>
            <p class="text-slate-400 text-xs">تأمين نقل سيارات الـ SUV الفارهة على الطريق الدائري والصحراوي والسويس.</p>
          </div>
        </div>

        <!-- Photo 6: Luxury Cupra Crossover -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_luxury_car_flatbed.webp" alt="سحب وتثبيت السيارات الفاخرة والرياضية بأربطة الإطارات بدون خدوش" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">عناية فائقة بالسيارات الحديثة</h3>
            <p class="text-slate-400 text-xs">تثبيت احترافي بأحزمة الإطارات (Wheel Straps) يمنع أي احتكاك أو ضرر بالهيكل.</p>
          </div>
        </div>

        <!-- Photo 7: Tractor Head Heavy Recovery -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_semi_truck_head.webp" alt="سحب وإنقاذ رؤوس التريلات والشاحنات الضخمة Actros على أوناش أولاد حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">سحب رؤوس التريلات والشاحنات</h3>
            <p class="text-slate-400 text-xs">إنقاذ ميكانيكي للشاحنات التريلا المعطلة وتوصيلها لورش ومراكز الصيانة المعتمدة.</p>
          </div>
        </div>

        <!-- Photo 8: Caravans Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_caravan_transport.webp" alt="نقل الكرفانات والمكاتب الإدارية ومواقع الإنشاءات على أوناش أولاد حجازي مسطح" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل الكرفانات والوحدات المتنقلة</h3>
            <p class="text-slate-400 text-xs">أبعاد طبلية ممتدة حتى 12 متراً لنقل غرف الحراسة ومكاتب المواقع والمشروعات.</p>
          </div>
        </div>

        <!-- Photo 9: Golf Carts Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_golf_carts_transport.webp" alt="نقل عربات الجولف كارت للمنتجعات والملاعب والقرى السياحية" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل عربات الجولف كارت (حمولة مزدوجة)</h3>
            <p class="text-slate-400 text-xs">خدمة مخصصة للمنتجعات والقرى السياحية والمجمعات المغلقة في مدينتي والرحاب.</p>
          </div>
        </div>

        <!-- Photo 10: Food Trucks Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_food_truck_transport.webp" alt="نقل عربات الطعام المتنقلة فود تراك والمقطورات التجارية على أوناش أولاد حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل عربات الطعام (Food Trucks)</h3>
            <p class="text-slate-400 text-xs">توصيل آمن للمقطورات التجارية وأكشاك الطعام للمعارض والمهرجانات والساحات.</p>
          </div>
        </div>

        <!-- Photo 11: Heavy Forklifts Transport -->
        <div class="glass rounded-3xl overflow-hidden border border-slate-800 hover:border-amber-400/50 transition-all group flex flex-col justify-between">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950">
            <img src="assets/images/hegazy_red_truck_heavy.webp" alt="سحب ونقل الرافعات الشوكية والمعدات الثقيلة في المصانع والصوامع" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل المعدات والرافعات الشوكية (TCM)</h3>
            <p class="text-slate-400 text-xs">قدرات جر وسحب فائقة لنقل معدات المصانع، الفورك لفت، والشاحنات في المناطق الصناعية.</p>
          </div>
        
        <!-- Photo 12: Night Commercial Pickup Cargo -->
        <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all group flex flex-col justify-between shadow-xl">
          <div class="aspect-[4/3] overflow-hidden bg-slate-950 relative">
            <img src="assets/images/hegazy_night_commercial_pickup.webp" alt="نقل سيارات النقل التجاري والربع نقل بحمولتها ليلاً أوناش أولاد حجازي" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" decoding="async">
            <span class="absolute top-3 right-3 px-2.5 py-1 rounded-full bg-emerald-600/90 text-white text-[10px] font-black tracking-wider uppercase">نقل تجاري وبضائع</span>
          </div>
          <div class="p-4">
            <h3 class="text-white font-extrabold text-sm mb-1">نقل سيارات النقل التجاري بحمولتها</h3>
            <p class="text-slate-400 text-xs">سحب وتأمين سيارات الربع نقل المحملة بالبضائع ليلاً على الطرق السريعة دون الحاجة لتفريغ الشحنة.</p>
          </div>
        </div>
</div>
</div>
    </div>
  </section>

  
  <!-- Video Showcase Section: Authentic Live Field Operations (E-E-A-T & Video SEO) -->
  <section id="videos" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-slate-800/80 bg-gradient-to-b from-dark-950 via-slate-950 to-dark-950">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-black bg-red-500/15 text-red-400 border border-red-500/30 mb-4 animate-pulse">
        <span class="w-2 h-2 rounded-full bg-red-500"></span>
        توثيق حي بالصوت والصورة من الميدان
      </div>
      <h2 class="text-3xl sm:text-4xl font-black text-white leading-tight">
        فيديوهات حصرية لعمليات أسطول <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-amber-300 to-amber-500">أوناش أولاد حجازي الميدانية</span>
      </h2>
      <p class="text-slate-400 text-sm sm:text-base mt-4">
        شاهد بالصوت والصورة احترافية سحب ونقل سيارات السوبر كار ليلاً، تحميل اللوادر والمعدات الهندسية، وإنقاذ سيارات النقل التجاري بحمولتها بأحدث تقنيات السلامة في مصر.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Video 1: Lamborghini Supercar Night -->
      <div class="glass rounded-3xl overflow-hidden border border-amber-500/40 hover:border-amber-400 transition-all flex flex-col justify-between shadow-2xl bg-slate-900/60 group">
        <div class="relative bg-black rounded-t-3xl overflow-hidden aspect-[9/16] max-h-[520px] flex items-center justify-center">
          <video controls playsinline preload="none" poster="assets/images/poster_lamborghini_night.webp" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_lamborghini_vip_night.mp4" type="video/mp4">
            <track kind="captions" src="assets/videos/captions.vtt" srclang="ar" label="عربي">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🏎️</span>
            <span>سوبر كار VIP ليلاً</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h3 class="text-white font-extrabold text-base">توثيق سحب سيارة لامبورجيني هوراكان ليلاً</h3>
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
          <video controls playsinline preload="none" poster="assets/images/poster_caterpillar_loader.webp" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_caterpillar_loader_day.mp4" type="video/mp4">
            <track kind="captions" src="assets/videos/captions.vtt" srclang="ar" label="عربي">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🏗️</span>
            <span>لودر كاتربيلر CAT 930</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h3 class="text-white font-extrabold text-base">تحميل ونقل لودر CAT 930 للمشروعات</h3>
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
          <video controls playsinline preload="none" poster="assets/images/poster_commercial_pickup.webp" class="w-full h-full object-cover">
            <source src="assets/videos/hegazy_commercial_pickup_night.mp4" type="video/mp4">
            <track kind="captions" src="assets/videos/captions.vtt" srclang="ar" label="عربي">
            متصفحك لا يدعم تشغيل الفيديو.
          </video>
          <div class="absolute top-3 right-3 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-amber-500/40 text-amber-300 text-[11px] font-black flex items-center gap-1.5 pointer-events-none">
            <span>🚚</span>
            <span>نقل بضائع وتجاري</span>
          </div>
        </div>
        <div class="p-5 space-y-3">
          <h3 class="text-white font-extrabold text-base">إنقاذ سيارة ربع نقل محملة بالبضائع ليلاً</h3>
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
          <h3 class="text-white font-black text-base">هل تحتاج ونش إنقاذ بمواصفات خاصة الآن؟</h3>
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


  {get_map_section()}

  <!-- FAQ Section (AEO Structured for Google & AI Overviews) -->
  <section class="py-20 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-2xl mx-auto mb-14">
      <span class="px-3 py-1 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-3 inline-block">الأسئلة الشائعة وإجابات الطوارئ</span>
      <h2 class="text-2xl md:text-4xl font-black text-white">كل ما تحتاج معرفته عن خدمات أوناش أولاد حجازي</h2>
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

  
  <!-- Customer Testimonials & Verified Reviews (100% Google Search Essentials & Spam Policy Compliant) -->
  <section class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-slate-800">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-4">
        <span>⭐</span>
        <span>تقييمات وتجارب العملاء الميدانية المعتمدة</span>
      </div>
      <h3 class="text-3xl sm:text-4xl font-black text-white leading-tight">
        ثقة أكثر من <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500">1420 قائد سيارة</span> في جميع محافظات مصر
      </h3>
      <p class="text-slate-400 text-sm sm:text-base mt-4">
        متوسط تقييم 4.9 من 5 نجوم بناءً على سرعة الاستجابة الميدانية، الأمان التام للشاسيه، والالتزام بالسعر المحدد بدون أي إكراميات.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Review 1 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">عملية إنقاذ موثقة</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "تعطلت سيارتي ليلاً على الطريق الدائري الأوسطي، ونش أولاد حجازي وصل في أقل من 10 دقائق. السائق كان في قمة الاحترام والأمانة، والتزم بالسعر المتفق عليه بدون طلب أي إكرامية."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">م. أحمد ممدوح</strong>
            <span class="text-slate-500 text-[11px]">نقل سيارة ملاكي - التجمع الخامس</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ أسبوع</span>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">سوبر كار VIP</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "عندي سيارة بورش منخفضة جداً وكنت خايف على الصدام الأمامي. الونش هيدروليكي فلات بالكامل واستخدموا أربطة إطارات مطاطية مخصوصة دون أدنى خدش. احترافية تضاهي التوكيلات العالمية."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">كابتن حسام إبراهيم</strong>
            <span class="text-slate-500 text-[11px]">سحب بورش - طريق الإسماعيلية والعبور</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ أسبوعين</span>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">معدات ومصانع</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "تعاملت مع أولاد حجازي لنقل لودر ومعدات هندسية لموقع عمل في العاصمة الإدارية. أوناش شاقة وتثبيت بجنازير معتمدة وسرعة فائقة في التسليم. تعامل راقي وأنصح بهم بشدة."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">الحاج رجب النجار</strong>
            <span class="text-slate-500 text-[11px]">نقل معدات ولوادر - العاصمة وبدر</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ شهر</span>
        </div>
      </div>

    </div>
  </section>


  
  <!-- Customer Testimonials & Verified Reviews (100% Google Search Essentials & Spam Policy Compliant) -->
  <section class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 border-t border-slate-800">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-black bg-amber-500/15 text-amber-300 border border-amber-500/30 mb-4">
        <span>⭐</span>
        <span>تقييمات وتجارب العملاء الميدانية المعتمدة</span>
      </div>
      <h3 class="text-3xl sm:text-4xl font-black text-white leading-tight">
        ثقة أكثر من <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500">1420 قائد سيارة</span> في جميع محافظات مصر
      </h3>
      <p class="text-slate-400 text-sm sm:text-base mt-4">
        متوسط تقييم 4.9 من 5 نجوم بناءً على سرعة الاستجابة الميدانية، الأمان التام للشاسيه، والالتزام بالسعر المحدد بدون أي إكراميات.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Review 1 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">عملية إنقاذ موثقة</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "تعطلت سيارتي ليلاً على الطريق الدائري الأوسطي، ونش أولاد حجازي وصل في أقل من 10 دقائق. السائق كان في قمة الاحترام والأمانة، والتزم بالسعر المتفق عليه بدون طلب أي إكرامية."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">م. أحمد ممدوح</strong>
            <span class="text-slate-500 text-[11px]">نقل سيارة ملاكي - التجمع الخامس</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ أسبوع</span>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">سوبر كار VIP</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "عندي سيارة بورش منخفضة جداً وكنت خايف على الصدام الأمامي. الونش هيدروليكي فلات بالكامل واستخدموا أربطة إطارات مطاطية مخصوصة دون أدنى خدش. احترافية تضاهي التوكيلات العالمية."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">كابتن حسام إبراهيم</strong>
            <span class="text-slate-500 text-[11px]">سحب بورش - طريق الإسماعيلية والعبور</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ أسبوعين</span>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="glass p-6 rounded-3xl border border-slate-800 hover:border-amber-500/40 transition-all flex flex-col justify-between space-y-4">
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <div class="flex text-amber-400 text-sm">★★★★★</div>
            <span class="text-[11px] text-emerald-400 font-bold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">معدات ومصانع</span>
          </div>
          <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            "تعاملت مع أولاد حجازي لنقل لودر ومعدات هندسية لموقع عمل في العاصمة الإدارية. أوناش شاقة وتثبيت بجنازير معتمدة وسرعة فائقة في التسليم. تعامل راقي وأنصح بهم بشدة."
          </p>
        </div>
        <div class="pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
          <div>
            <strong class="text-white block">الحاج رجب النجار</strong>
            <span class="text-slate-500 text-[11px]">نقل معدات ولوادر - العاصمة وبدر</span>
          </div>
          <span class="text-slate-500 text-[11px]">منذ شهر</span>
        </div>
      </div>

    </div>
  </section>


  <!-- Final Urgent CTA Banner -->
  <section class="py-16 bg-gradient-to-r from-rescue-900 via-dark-900 to-amber-950 border-t border-amber-500/30 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl md:text-4xl font-black text-white mb-4">متعطل على الطريق الآن؟ لا تنتظر!</h2>
      <p class="text-slate-300 text-sm md:text-base max-w-2xl mx-auto mb-8">أقرب ونش إنقاذ من أوناش أولاد حجازي على بُعد دقائق منك. اتصل بنا وسنصلك فوراً لموقعك أينما كنت في مصر.</p>
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

  </main>

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
