import os
import sys

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update build_winch_helpers.py
helpers_file = os.path.join(scripts_dir, "build_winch_helpers.py")
with open(helpers_file, "r", encoding="utf-8") as f:
    h = f.read()

# Replace Top Ticker Bar
old_ticker_start = '  <!-- Top Ticker Bar -->'
old_ticker_end = '  <!-- Main Navigation -->'
new_ticker = '''  <!-- Top Ticker Bar -->
  <div class="bg-gradient-to-r from-rescue-700 via-amber-600 to-rescue-700 text-white text-xs md:text-sm py-2 px-4 text-center font-bold flex flex-wrap items-center justify-center gap-2 md:gap-4 shadow-md">
    <span class="inline-flex items-center gap-1.5">
      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
      <span class="text-amber-200 font-black">🎁 عرض خاص 2026:</span> خصم 50% لأول 100 عميل (كود: <span class="bg-black/40 px-2 py-0.5 rounded font-mono text-amber-300">HEGAZY50</span>)
    </span>
    <span class="hidden sm:inline text-slate-300">|</span>
    <span class="text-emerald-200">✓ بدون أي إكرامية إجبارية للسائق</span>
    <span class="hidden md:inline text-slate-300">|</span>
    <span class="text-amber-100">🛣️ نتحمل جزءاً من رسوم الكارتة</span>
    <span class="hidden md:inline text-slate-300">|</span>
    <a href="tel:{PHONE}" class="underline hover:text-amber-200 font-black">طوارئ 24 ساعة: {PHONE_DISPLAY}</a>
  </div>

  <!-- Main Navigation -->'''

if old_ticker_start in h and old_ticker_end in h:
    idx1 = h.find(old_ticker_start)
    idx2 = h.find(old_ticker_end) + len(old_ticker_end)
    h = h[:idx1] + new_ticker + h[idx2:]

with open(helpers_file, "w", encoding="utf-8") as f:
    f.write(h)
print("SUCCESS: Updated ticker bar in build_winch_helpers.py")

# 2. Update generate_winch_hegazy_site.py to add Trust Box under Calculator
site_file = os.path.join(scripts_dir, "generate_winch_hegazy_site.py")
with open(site_file, "r", encoding="utf-8") as f:
    s = f.read()

trust_box = '''
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
'''

calc_end_tag = '</div>\n    </div>\n  </section>'
if 'ميثاق الشفافية والمصداقية' not in s and 'id="calculator"' in s:
    idx_calc = s.find('id="calculator"')
    idx_insert = s.find('</div>\n    </div>\n  </section>', idx_calc)
    if idx_insert != -1:
        s = s[:idx_insert] + trust_box + s[idx_insert:]

with open(site_file, "w", encoding="utf-8") as f:
    f.write(s)
print("SUCCESS: Updated calculator with trust box in generate_winch_hegazy_site.py")
