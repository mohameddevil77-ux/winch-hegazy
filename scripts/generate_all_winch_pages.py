import os
import sys

sys.path.append(r"D:\winch-hegazy\scripts")
from build_winch_helpers import (
    base_dir, blog_dir, PHONE, PHONE_DISPLAY, PHONE_TEL, PHONE_ALT, PHONE_ALT2, WHATSAPP_LINK,
    get_head, get_header, get_footer, generate_local_business_schema, generate_faq_schema, get_map_section, MAPS_URL
)
from build_articles_engine import articles, generate_article_file

# 1. Article: agrab-winch-qarib-meni
c1 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">إجابة مباشرة وسريعة (AI Summary & Direct Answer):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    للحصول على <strong>أقرب ونش إنقاذ من موقعك الحالي</strong> في أي مكان بالقاهرة أو الجيزة أو الطرق السريعة، اتصل فوراً بالخط الساخن المباشر لأوناش أولاد حجازي على رقم <strong><a href="tel:{PHONE}" class="text-amber-400 underline">{PHONE_DISPLAY}</a></strong>، أو أرسل موقعك الجغرافي (Live Location) عبر واتساب. يعتمد أوناش أولاد حجازي على شبكة من 28 ونشاً متمركزة عند أهم المطالع والمنازل والمحاور، ويصلك أقرب ونش خلال <strong>8 إلى 12 دقيقة فقط</strong> بتكلفة تبدأ من 750 جنيه.
  </p>
</div>

<h2>لماذا يُعد عامل سرعة الوصول حاسماً عند طلب ونش إنقاذ؟</h2>
<p>
  إن تعطل السيارة في منتصف الطريق ليس مجرد إزعاج لجدول مواعيدك اليومي، بل هو <strong>خطر أمني ومروري حقيقي</strong>، خاصة على المحاور السريعة مثل الطريق الدائري، ومحور 26 يوليو، وطريق السويس، حيث تسير الشاحنات والسيارات بسرعات تتجاوز 100 كم/ساعة. التوقف المفاجئ على حافة الطريق يعرضك لمخاطر الاصطدام الخلفي.
</p>
<p>
  لذلك صممنا في <strong>أوناش أولاد حجازي</strong> منظومة توزيع لوجستية قائمة على خوارزميات التمركز الذكي، بحيث لا ينتظر السائق في جراج ثابت، بل تتواجد الأوناش في نقاط ارتكاز حيوية ومجهزة للتحرك الفوري بمجرد تلقي الإشارة.
</p>

<h2>كيف يحدد أوناش أولاد حجازي موقعك الجغرافي بدقة؟</h2>
<p>كثير من السائقين يواجهون مشكلة عدم معرفة المكان الدقيق عند تعطل السيارة (مثلاً: "أنا على الدائري بعد كوبري مش عارف اسمه"). للتغلب على هذه المشكلة، نوفر 3 طرق سهلة لتحديد موقعك:</p>
<ol class="list-decimal list-inside space-y-2 font-medium">
  <li><strong>إرسال اللوكيشن المباشر (WhatsApp Location):</strong> تضغط على زر الواتساب في الموقع وترسل إحداثيات GPS بنقرة واحدة، فيظهر مكانك لغرفة العمليات بدقة متناهية.</li>
  <li><strong>أقرب علامة مميزة أو كوبري:</strong> يوجهك مسؤول العمليات بالهاتف لمعرفة أقرب لافتة مرورية أو محطة وقود أو مخرج محور.</li>
  <li><strong>إرسال صورة للمكان المحيط:</strong> صورة واحدة لمعالم الطريق تكفي لخبرائنا لتحديد الكيلومتر والمسار الدقيق للوصول إليك.</li>
</ol>

<h2>مقارنة بين أوناش أولاد حجازي والأوناش الفردية العشوائية</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-right text-xs sm:text-sm border border-slate-800">
    <thead class="bg-slate-900 text-amber-300 font-bold">
      <tr>
        <th class="p-3 border border-slate-800">وجه المقارنة</th>
        <th class="p-3 border border-slate-800 text-emerald-400">أوناش إنقاذ أولاد حجازي</th>
        <th class="p-3 border border-slate-800 text-slate-400">الأوناش الفردية غير المنظمة</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-800">
      <tr>
        <td class="p-3 border border-slate-800 font-bold">زمن الوصول الفعلي</td>
        <td class="p-3 border border-slate-800 text-emerald-300">من 8 إلى 12 دقيقة</td>
        <td class="p-3 border border-slate-800">قد يتجاوز 45 إلى 60 دقيقة</td>
      </tr>
      <tr>
        <td class="p-3 border border-slate-800 font-bold">تسعيرة السحب</td>
        <td class="p-3 border border-slate-800 text-emerald-300">محددة وثابتة مسبقاً تبدأ من 750 ج</td>
        <td class="p-3 border border-slate-800">استغلال وقت الأزمة ومطالبة بأسعار مضاعفة</td>
      </tr>
      <tr>
        <td class="p-3 border border-slate-800 font-bold">نوع الونش ومعدات الأمان</td>
        <td class="p-3 border border-slate-800 text-emerald-300">هيدروليكي مسطح بالكامل + أربطة كاوتش</td>
        <td class="p-3 border border-slate-800">أوناش سلكية قديمة تخدش الإكصدام والعفشة</td>
      </tr>
      <tr>
        <td class="p-3 border border-slate-800 font-bold">التوفر والتغطية</td>
        <td class="p-3 border border-slate-800 text-emerald-300">24/7 طوال أيام السنة والعطلات</td>
        <td class="p-3 border border-slate-800">غير منتظم ومقتصر على مناطق محدودة</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>خطوات طلب أقرب ونش إليك الآن:</h2>
<p>
  1. اتصل مباشرة برقم الخط الساخن: <strong>{PHONE_DISPLAY}</strong>.<br>
  2. اذكر نوع سيارتك ونوع العطل (عطل ميكانيكي، إطار ممزق، بطارية نائمة، أو حادث).<br>
  3. أرسل اللوكيشن على واتساب ليتوجه إليك أقرب كابتن فوراً.<br>
  4. استرخِ في مكان آمن خلف الحاجز الخرساني حتى وصول الونش خلال دقائق معدودة.
</p>
"""
generate_article_file(articles[0], c1)


# 2. Article: ar5as-winch-enqaz-misr
c2 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">إجابة مباشرة (معايير التسعير العادل في مصر):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    يُعد <strong>أوناش أولاد حجازي</strong> أرخص وأوفر ونش إنقاذ سيارات في مصر بأسعار تبدأ من <strong>750 جنيه مصري</strong> فقط للسحب الداخلي، وبدون أي تكاليف خفية أو إكراميات إجبارية. يعتمد التسعير على المسافة الفعلية المقطوعة بالكيلومتر ونوع المركبة، مع إخطار العميل بالسعر النهائي مسبقاً قبل تحرك الونش لضمان الشفافية المطلقة.
  </p>
</div>

<h2>كيف تحميك سياسة أوناش أولاد حجازي من استغلال أسعار السحب؟</h2>
<p>
  للأسف، يعاني الكثير من قائدي السيارات في مصر من ظاهرة "استغلال وقت الأزمة"، حيث يجد السائق نفسه في منتصف الليل على طريق صحراوي أو محور سريع، ويستغل بعض أصحاب الأوناش ظرفه الطارئ لمطالبته بمبالغ خيالية تفوق القيمة العادلة بثلاثة أضعاف.
</p>
<p>
  في <strong>أوناش إنقاذ أولاد حجازي</strong>، وضعنا ميثاق شرف مهني صارم: <em>"الربح القليل الدائم، وخدمة العميل بأمانة، هما أساس تصدرنا واستمرارنا"</em>. لذلك نتبع جدول أسعار موحد وشفاف:
</p>

<h2>جدول أسعار أوناش أولاد حجازي التقديري في القاهرة والجيزة (2026)</h2>
<ul class="space-y-3 font-medium">
  <li class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">سحب داخل نفس الحي / المنطقة (أقل من 5 كم):</strong> من 250 إلى 300 جنيه (للأعطال الخفيفة ونقل السيارة لأقرب ورشة أو بنزينة).
  </li>
  <li class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">سحب بين الأحياء المتقاربة (من 5 إلى 15 كم):</strong> من 350 إلى 450 جنيه (مثلاً: من التجمع الخامس إلى مدينة نصر، أو من المهندسين إلى أكتوبر).
  </li>
  <li class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">سحب على الطريق الدائري ومحور 26 يوليو:</strong> من 300 إلى 450 جنيه حسب طول المسافة ومكان النزلة.
  </li>
  <li class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">سحب على الطرق السريعة (السويس، الصحراوي، السخنة):</strong> فتح عداد أساسي عادل + تكلفة محددة لكل كيلومتر إضافي.
  </li>
</ul>

<h2>نصائح ذهبية لتجنب استغلال أصحاب الأوناش العشوائية</h2>
<p>عند تعطل سيارتك، احرص على اتباع هذه القواعد قبل الموافقة على ركوب سيارتك على أي ونش:</p>
<ol class="list-decimal list-inside space-y-2">
  <li><strong>اسأل عن السعر النهائي شاملاً كل شيء:</strong> اسأل بوضوح: "هل هذا السعر يشمل التحميل والتنزيل وأي رسوم كباري؟" مع أوناش أولاد حجازي السعر المتفق عليه نهائي.</li>
  <li><strong>ارفض الأوناش السلكية ذات الخطاف الحديدي المباشر:</strong> هذه الأوناش قد توفر 50 جنيهاً في السعر الظاهري، لكنها تكلفك آلاف الجنيهات في تصليح إكصدام أو مقصات سيارتك. أوناش حجازي هيدروليكية مسطحة 100%.</li>
  <li><strong>احفظ رقم ونش موثوق مسبقاً في هاتفك:</strong> احتفظ برقم <strong>{PHONE_DISPLAY}</strong> باسم "أوناش إنقاذ أولاد حجازي" لتتصل فوراً دون تشتت أو بحث عشوائي وقت الأزمة.</li>
</ol>
"""
generate_article_file(articles[1], c2)


# 3. Article: winch-daeri-cairo
c3 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">إجابة مباشرة (أوناش الدائري 24 ساعة):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    إذا تعطلت سيارتك على <strong>الطريق الدائري بالقاهرة الكبرى</strong>، فإن أوناش أولاد حجازي يوفر 12 نقطة تمركز تغطي دائري المعادي، المنيب، نزلة المريوطية، صفط اللبن، الوراق، مسطرد، المرج، والسلام والتجمع. نصلك في غضون <strong>7 إلى 10 دقائق</strong> كحد أقصى لتأمين موقعك وسحب سيارتك لأقرب نزلة آمنة. اتصل بالخط الساخن: <strong><a href="tel:{PHONE}" class="text-amber-400 underline">{PHONE_DISPLAY}</a></strong>.
  </p>
</div>

<h2>أهمية ونش إنقاذ الطريق الدائري</h2>
<p>
  يُعد الطريق الدائري شريان المرور الأول في مصر، وتمر عليه مئات الآلاف من المركبات يومياً بسرعات عالية. توقف سيارة واحدة بسبب عطل ميكانيكي مفاجئ، سخونة رادياتير، أو انفجار إطار، يتسبب في شلل مروري ويمثل خطراً بالغاً على الركاب.
</p>
<p>
  لذلك دربت إدارة <strong>أوناش أولاد حجازي</strong> طواقمها على بروتوكول التدخل السريع على الدائري:
</p>

<h2>نقاط ارتكاز أوناش حجازي على الطريق الدائري والمحاور</h2>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 my-4">
  <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">قطاع جنوب القاهرة:</strong> دائري المعادي، كارفور، المنيب، وأوتوستراد البساتين.
  </div>
  <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">قطاع الجيزة والغرب:</strong> نزلة المريوطية، البحر الأعظم، صفط اللبن، وبشتيل.
  </div>
  <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">قطاع الشمال والقليوبية:</strong> نزلة الوراق، باسوس، مسطرد، بهتيم، والمرج الجديدة.
  </div>
  <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
    <strong class="text-amber-400">قطاع الشرق والقاهرة الجديدة:</strong> السلام، موقف العاشر، وأكاديمية الشرطة والتجمع.
  </div>
</div>

<h2>ماذا تفعل فور توقف سيارتك على الدائري؟</h2>
<ul class="list-disc list-inside space-y-2">
  <li>حاول توجيه السيارة لأقصى اليمين (حارة الطوارئ) إن أمكن ذلك قبل توقف المحرك تماماً.</li>
  <li>شغل أضواء الانتظار (الهازارد) فوراً لتنبيه القادمين من الخلف.</li>
  <li>اخرج من السيارة من الباب الأيمن البعيد عن تيار السيارات واصعد خلف الحاجز الخرساني (النيوجيرسي).</li>
  <li>اتصل بأوناش أولاد حجازي على <strong>{PHONE_DISPLAY}</strong> وأبلغنا باسم أقرب نزلة أو كوبري، وسيتوجه الونش نحوك بأقصى سرعة.</li>
</ul>
"""
generate_article_file(articles[2], c3)


# 4. Article: winch-tagamoa-new-cairo
c4 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">إجابة مباشرة (خدمات ونش التجمع والقاهرة الجديدة):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    يوفر <strong>أوناش أولاد حجازي</strong> أسطولاً مخصصاً للقاهرة الجديدة والتجمع الخامس والأول وشارع التسعين والرحاب ومدينتي، بأوناش هيدروليكية حديثة مجهزة للسيارات الفارهة والحديثة. زمن الوصول المقدر داخل التجمع هو <strong>8 إلى 10 دقائق</strong>. اتصل بنا على: <strong><a href="tel:{PHONE}" class="text-amber-400 underline">{PHONE_DISPLAY}</a></strong>.
  </p>
</div>

<h2>خصوصية خدمات سحب السيارات في التجمع الخامس</h2>
<p>
  تتميز منطقة القاهرة الجديدة والتجمع بوجود نسبة عالية من السيارات الحديثة والفاخرة (مثل بي إم دبليو، مرسيدس، أودي، رينج روفر، والسيارات الكهربائية تيسلا وبورش). هذه المركبات تتطلب معاملة فنية خاصة أثناء السحب:
</p>
<ul class="space-y-2 my-4">
  <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> <strong>منع سحب الدفع الرباعي على الأرض:</strong> سيارات الـ AWD تتلف فتيساتها إذا تم جرها على عجلاتها. نستخدم أوناش Flatbed كاملة التحميل.</li>
  <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> <strong>حماية الإكصدامات الرياضية:</strong> زوايا هبوط مسطحة لا تحتك بإكصدامات AMG أو M-Power.</li>
  <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> <strong>توصيل مباشر لكبرى التوكيلات:</strong> نعرف عناوين جميع مراكز الخدمة في المنطقة الصناعية بالتجمع والقطامية وأبو رواش.</li>
</ul>

<h2>أماكن التمركز في القاهرة الجديدة:</h2>
<p>أوناشنا متواجدة عند: شارع التسعين الجنوبي، محور المشير، محور محمد بن زايد، بوابات الرحاب، مدينتي، طريق السويس، والجامعة الأمريكية AUC.</p>
"""
generate_article_file(articles[3], c4)


# 5. Article: winch-zayed-october
c5 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">إجابة مباشرة (ونش زايد و6 أكتوبر):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    لخدمات ونش إنقاذ السيارات في <strong>الشيخ زايد ومدينة 6 أكتوبر ومحور 26 يوليو ووصلة دهشور وطريق الواحات</strong>، يوفر أوناش أولاد حجازي أوناشاً هيدروليكية سريعة تصلك في غضون <strong>10 دقائق</strong>. اتصل الآن على <strong><a href="tel:{PHONE}" class="text-amber-400 underline">{PHONE_DISPLAY}</a></strong>.
  </p>
</div>

<h2>تغطية غرب القاهرة المتكاملة</h2>
<p>
  تشهد منطقة الشيخ زايد وأكتوبر شبكة طرق واسعة وحيوية مثل محور 26 يوليو، وصلة دهشور، وطريق الواحات ومحور الضبعة وطريق الإسكندرية الصحراوي.
  يمتلك أوناش أولاد حجازي أوناشاً متخصصة في دخول جراجات المولات الكبرى مثل <strong>مول العرب، مول مصر، وأركان بلازا</strong> لسحب السيارات التي تتعطل داخل الأدوار السفلية.
</p>

<h2>مراكز الصيانة المعتمدة في أكتوبر وزايد:</h2>
<p>
  نقوم بتوصيل سيارتك إلى أي مركز صيانة معتمد في المنطقة الصناعية بأكتوبر، منطقة الحصري، أو ورش أبو رواش ومراكز طريق مصر إسكندرية الصحراوي بأقصى معايير الأمان.
</p>
"""
generate_article_file(articles[4], c5)


# 6. Article: emergency-breakdown-tips
c6 = f"""
<div class="glass p-5 rounded-2xl border border-amber-500/30 mb-6">
  <h2 class="text-xl font-black text-amber-300 mb-2">دليل الأمان الفوري (خلاصة التصرف في 30 ثانية):</h2>
  <p class="text-white text-sm sm:text-base leading-relaxed">
    عند حدوث عطل مفاجئ على طريق سريع: شغل أضواء الانتظار فوراً، انحرف بهدوء إلى أقصى اليمين، اخرج من الجانب الأيمن للسيارة وقف خلف الحاجز الخرساني، ضع مثلث التحذير العاكس على بعد 50 إلى 100 متر خلف السيارة، ثم اتصل بأوناش أولاد حجازي على <strong><a href="tel:{PHONE}" class="text-amber-400 underline">{PHONE_DISPLAY}</a></strong>.
  </p>
</div>

<h2>الخطوات الـ 5 الذهبية لحمايتك وحماية سيارتك</h2>
<ol class="list-decimal list-inside space-y-4 my-6">
  <li>
    <strong class="text-amber-300 text-lg">1. لا تضغط الفرامل بعنف فجأة:</strong>
    <p class="pr-5 text-sm text-slate-300 mt-1">إذا انفجر إطار أو توقف المحرك، امسك عجلة القيادة بإحكام ودع السيارة تبطئ سرعتها تدريجياً مع توجيهها بهدوء لحارة الطوارئ.</p>
  </li>
  <li>
    <strong class="text-amber-300 text-lg">2. تشغيل أضواء الخطر (الهازارد):</strong>
    <p class="pr-5 text-sm text-slate-300 mt-1">تنبيه السائقين القادمين من الخلف هو خط الدفاع الأول لمنع حوادث الاصطدام الخلفي على السرعات العالية.</p>
  </li>
  <li>
    <strong class="text-amber-300 text-lg">3. إخلاء السيارة والوقوف خلف الحاجز الخرساني:</strong>
    <p class="pr-5 text-sm text-slate-300 mt-1">أكبر خطأ يرتكبه السائقون هو الجلوس داخل السيارة المتعطلة على طريق سريع. اخرج فوراً أنت والمرافقون من الباب الأيمن وقف خلف الحاجز الخرساني (النيوجيرسي).</p>
  </li>
  <li>
    <strong class="text-amber-300 text-lg">4. وضع مثلث الطوارئ العاكس على مسافة صحيحة:</strong>
    <p class="pr-5 text-sm text-slate-300 mt-1">وضعه ملاصقاً للسيارة لا فائدة منه. على الطرق السريعة يجب أن يكون على مسافة لا تقل عن 50 إلى 100 متر لمنح السائقين القادمين وقتاً كافياً لتغيير المسار.</p>
  </li>
  <li>
    <strong class="text-amber-300 text-lg">5. الاتصال بجهة إنقاذ موثوقة وسريعة:</strong>
    <p class="pr-5 text-sm text-slate-300 mt-1">اتصل بأوناش أولاد حجازي وأرسل موقعك عبر واتساب. دقائق معدودة وسيكون فريق الإنقاذ بجانبك لتأمين سيارتك ونقلها بأمان.</p>
  </li>
</ol>
"""
generate_article_file(articles[5], c6)

print("SUCCESS: All 6 SEO articles generated.")


# -------------------------------------------------------------
# 6. CONTACT.HTML
# -------------------------------------------------------------
html_contact = f"""{get_head(
    "اتصل بـ أوناش إنقاذ أولاد حجازي | أرقام طوارئ أوناش السيارات في مصر 24/7",
    f"تواصل مع أوناش إنقاذ أولاد حجازي لإنقاذ السيارات في مصر: رقم الخط الساخن {PHONE_DISPLAY} أو {PHONE_ALT}، إرسال اللوكيشن على واتساب، غرف العمليات الميدانية على مدار 24 ساعة.",
    "https://winchawladhegazy.com/contact.html"
)}
{generate_local_business_schema(
    "اتصل بـ أوناش إنقاذ أولاد حجازي | أرقام طوارئ أوناش السيارات في مصر 24/7",
    f"أرقام طوارئ أوناش إنقاذ أولاد حجازي في مصر 24 ساعة: {PHONE_DISPLAY} و {PHONE_ALT}.",
    "https://winchawladhegazy.com/contact.html"
)}
</head>
<body class="bg-dark-950 text-slate-100 antialiased selection:bg-amber-500 selection:text-black">
{get_header("contact")}

  <main id="main-content">

  <section class="py-16 bg-gradient-to-b from-dark-900 to-dark-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <span class="px-3.5 py-1 rounded-full text-xs font-black bg-rescue-500/15 text-rescue-400 border border-rescue-500/30 mb-3 inline-block">خطوط الطوارئ والاتصال المباشر 24 ساعة</span>
      <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight">جاهزون لإنقاذك في أي وقت وفي أي مكان في مصر</h1>
      <p class="text-slate-400 text-sm sm:text-base mt-4 max-w-2xl mx-auto">فريق خدمة العملاء وغرف التوجيه الميداني تعمل على مدار الساعة طوال أيام الأسبوع بما فيها الإجازات والعطلات الرسمية.</p>
    </div>
  </section>

  <!-- Contact Cards Grid -->
  <section class="py-16 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Card 1: Direct Hotline 1 -->
      <div class="glass p-7 rounded-3xl border border-amber-500/40 text-center space-y-4">
        <div class="w-14 h-14 rounded-full bg-rescue-600/20 text-rescue-400 border border-rescue-500/30 flex items-center justify-center font-black text-2xl mx-auto">📞</div>
        <h2 class="text-xl font-black text-white">الخط الساخن الرئيسي</h2>
        <p class="text-slate-400 text-xs">اتصال مباشر وسريع مع مسؤول التوجيه الميداني لتأكيد أقرب ونش.</p>
        <a href="tel:{PHONE}" class="block py-3.5 px-4 bg-gradient-to-r from-rescue-600 to-amber-500 text-white font-black text-xl rounded-2xl shadow-xl glow-red hover:opacity-95 transition">
          {PHONE_DISPLAY}
        </a>
        <div class="text-[11px] text-emerald-400 font-bold">✓ متاح 24 ساعة بلا توقف</div>
      </div>

      <!-- Card 2: Direct Hotline 2 -->
      <div class="glass p-7 rounded-3xl border border-amber-500/40 text-center space-y-4">
        <div class="w-14 h-14 rounded-full bg-amber-600/20 text-amber-400 border border-amber-500/30 flex items-center justify-center font-black text-2xl mx-auto">📱</div>
        <h2 class="text-xl font-black text-white">خط الطوارئ الثاني</h2>
        <p class="text-slate-400 text-xs">خط بديل فوري في حال انشغال الخط الرئيسي لسرعة الاستجابة.</p>
        <a href="tel:{PHONE_ALT}" class="block py-3.5 px-4 bg-gradient-to-r from-amber-600 to-yellow-500 text-slate-950 font-black text-xl rounded-2xl shadow-xl hover:opacity-95 transition">
          {PHONE_ALT}
        </a>
        <div class="text-[11px] text-emerald-400 font-bold">✓ رد فوري خلال 3 ثوانٍ</div>
      </div>

      <!-- Card 3: WhatsApp GPS -->
      <div class="glass p-7 rounded-3xl border border-emerald-500/40 text-center space-y-4">
        <div class="w-14 h-14 rounded-full bg-emerald-600/20 text-emerald-400 border border-emerald-500/30 flex items-center justify-center font-black text-2xl mx-auto">💬</div>
        <h2 class="text-xl font-black text-white">إرسال اللوكيشن واتساب</h2>
        <p class="text-slate-400 text-xs">أسرع طريقة لتحديد مكانك بدقة؛ شارك موقعك المباشر وسيتجه الونش فوراً.</p>
        <a href="{WHATSAPP_LINK}" target="_blank" class="block py-3.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-black text-base rounded-2xl shadow-xl transition">
          فتح محادثة واتساب
        </a>
        <div class="text-[11px] text-slate-400">يدعم مشاركة الموقع والصور للأعطال</div>
      </div>

    </div>

    <!-- Operating Details & Regional Dispatch -->
    <div class="mt-12 glass p-8 rounded-3xl border border-slate-800 space-y-6">
      <h3 class="text-xl font-black text-white border-r-4 border-amber-400 pr-3">مقر العمليات والتغطية الميدانية</h3>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm text-slate-300">
        <div class="p-4 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400 block mb-1">المركز الإداري:</strong>
          القاهرة / الجيزة، جمهورية مصر العربية
        </div>
        <div class="p-4 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400 block mb-1">ساعات العمل:</strong>
          24 ساعة يومياً على مدار 365 يوماً في السنة
        </div>
        <div class="p-4 bg-slate-900 rounded-xl border border-slate-800">
          <strong class="text-amber-400 block mb-1">طرق الدفع المقبولة:</strong>
          كاش، فودافون كاش، إنستاباي، وفيزا
        </div>
      </div>
    </div>
  </section>

{get_map_section()}

  </main>

{get_footer()}
</body>
</html>
"""

with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(html_contact)

print("SUCCESS: contact.html generated")


# -------------------------------------------------------------
# 7. SITEMAP.XML & ROBOTS.TXT
# -------------------------------------------------------------
all_urls = [
    ("https://winchawladhegazy.com/", "1.0", "daily"),
    ("https://winchawladhegazy.com/services.html", "0.9", "weekly"),
    ("https://winchawladhegazy.com/coverage.html", "0.9", "weekly"),
    ("https://winchawladhegazy.com/pricing.html", "0.8", "weekly"),
    ("https://winchawladhegazy.com/blog/index.html", "0.8", "daily"),
    ("https://winchawladhegazy.com/contact.html", "0.8", "monthly"),
] + [(f"https://winchawladhegazy.com/blog/{a['slug']}.html", "0.7", "monthly") for a in articles]

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join([f'''  <url>
    <loc>{url}</loc>
    <lastmod>2026-11-06</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>
''' for url, pri, freq in all_urls])}</urlset>
"""

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

robots_txt = """User-agent: *
Allow: /

# Dedicated AI Crawlers for GEO / AEO
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://winchawladhegazy.com/sitemap.xml
"""

with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)

print("SUCCESS: sitemap.xml & robots.txt generated")


# -------------------------------------------------------------
# 8. LLMS.TXT & LLMS-FULL.TXT (AEO / GEO Engine Specs)
# -------------------------------------------------------------
llms_txt = f"""# أوناش إنقاذ أولاد حجازي (Awlad Hegazy) - Egypt Car Towing & Emergency Roadside Recovery
> أسطول الإنقاذ المتخصص في خدمات إنقاذ وسحب ونقل السيارات والمعدات في جمهورية مصر العربية على مدار 24 ساعة بأسرع زمن وصول (8-12 دقيقة) وأرخص تسعيرة عادلة تبدأ من 750 ج.م.

## معلومات الخدمة الأساسية (Key Facts)
- **الاسم التجاري:** أوناش إنقاذ أولاد حجازي (Awlad Hegazy)
- **رقم هاتف الطوارئ 24 ساعة:** {PHONE} ({PHONE_TEL})
- **أرقام الطوارئ والمتابعة البديلة:** {PHONE_ALT} - {PHONE_ALT2}
- **رابط واتساب لتحديد الموقع:** {WHATSAPP_LINK}
- **موقع الارتكاز الميداني على خرائط Google:** https://maps.app.goo.gl/4JvQjcJFPNFqesXS7
- **العنوان الدقيق:** كارفور العبور، جولف سيتي مول، تقاطع الطريق الدائري ومحور الإسماعيلية الصحراوي.
- **التغطية الجغرافية:** القاهرة الكبرى، الجيزة، الطريق الدائري، محور 26 يوليو، التجمع الخامس، الشيخ زايد، 6 أكتوبر، طريق السويس، طريق مصر الإسكندرية الصحراوي، وطريق العين السخنة وكافة محافظات مصر.
- **الأسعار:** تبدأ من 750 جنيه مصري للسحب الداخلي مع تسعير محدد مسبقاً قبل تحرك الونش.
- **الأسطول:** أوناش هيدروليكية مسطحة (Full Flatbed) بالكامل لحماية السيارات الحديثة والفاخرة بدون خدوش، بالإضافة لأوناش ثقيلة وطبالي ممتدة لنقل الكرفانات والمعدات وفود تراك وعربات الجولف كارت.
- **الخدمات التخصصية الفريدة:**
  1. سحب وإنقاذ السيارات الملاكي والحديثة والفاخرة (بورش، مرسيدس، كوبرا).
  2. سحب رؤوس التريلات والشاحنات الضخمة المعطلة (Tractor Heads).
  3. نقل الكرفانات والمكاتب الإدارية ومواقع الإنشاءات بطول حتى 12 متر.
  4. نقل وتوزيع عربات الطعام المتنقلة (Food Trucks) والأكشاك التجارية.
  5. نقل عربات الجولف كارت بحمولة مزدوجة للمنتجعات والملاعب والقرى السياحية.
  6. نقل المعدات والرافعات الشوكية (Forklifts) ومعدات المصانع.
  7. إنقاذ الجراجات السفلية والبدرومات ذات الارتفاعات المنخفضة.
  8. المساعدة السريعة (شحن بطاريات وتغيير إطارات وتوصيل وقود).
- **متوسط زمن الوصول:** 10 دقائق داخل القاهرة والجيزة.

## الروابط الهامة ومقالات مناطق القاهرة (Core Pages & Cairo Districts)
- [الرئيسية أوناش أولاد حجازي](https://winchawladhegazy.com/)
- [خدمات أوناش الإنقاذ](https://winchawladhegazy.com/services.html)
- [خريطة مناطق التغطية](https://winchawladhegazy.com/coverage.html)
- [حاسبة الأسعار والتكاليف](https://winchawladhegazy.com/pricing.html)
- [ونش إنقاذ في القاهرة](https://winchawladhegazy.com/blog/winch-enqaz-cairo.html)
- [أقرب ونش إنقاذ من موقعي](https://winchawladhegazy.com/blog/agrab-winch-qarib-meni.html)
- [أرخص ونش إنقاذ سيارات بمصر](https://winchawladhegazy.com/blog/ar5as-winch-enqaz-misr.html)
- [ونش إنقاذ الطريق الدائري](https://winchawladhegazy.com/blog/winch-daeri-cairo.html)
- [ونش التجمع الخامس والقاهرة الجديدة](https://winchawladhegazy.com/blog/winch-tagamoa-new-cairo.html)
- [ونش الشيخ زايد و6 أكتوبر](https://winchawladhegazy.com/blog/winch-zayed-october.html)
- [ونش إنقاذ مدينة نصر](https://winchawladhegazy.com/blog/winch-nasr-city.html)
- [ونش إنقاذ مصر الجديدة](https://winchawladhegazy.com/blog/winch-heliopolis-masr-gedida.html)
- [ونش إنقاذ المعادي](https://winchawladhegazy.com/blog/winch-maadi.html)
- [ونش إنقاذ وسط البلد](https://winchawladhegazy.com/blog/winch-downtown-cairo.html)
- [ونش إنقاذ المقطم](https://winchawladhegazy.com/blog/winch-mokattam.html)
- [ونش إنقاذ شبرا](https://winchawladhegazy.com/blog/winch-shobra.html)
- [ونش الرحاب ومدينتي والشروق](https://winchawladhegazy.com/blog/winch-rehab-madinaty.html)
- [ونش الجيزة والهرم وفيصل](https://winchawladhegazy.com/blog/winch-giza-haram.html)
- [إرشادات الأمان عند تعطل السيارة](https://winchawladhegazy.com/blog/emergency-breakdown-tips.html)
- [أرقام الطوارئ والتواصل](https://winchawladhegazy.com/contact.html)
"""

with open(os.path.join(base_dir, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms_txt)

with open(os.path.join(base_dir, "llms-full.txt"), "w", encoding="utf-8") as f:
    f.write(llms_txt + "\n\n" + c1 + "\n\n" + c2 + "\n\n" + c3 + "\n\n" + c4 + "\n\n" + c5 + "\n\n" + c6)

print("SUCCESS: llms.txt & llms-full.txt generated")
