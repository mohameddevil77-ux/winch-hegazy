# -*- coding: utf-8 -*-
import os

helpers_path = r"D:\winch-hegazy\scripts\build_winch_helpers.py"
with open(helpers_path, "r", encoding="utf-8") as f:
    code = f.read()

old_bar_start = code.find("<!-- Sticky Mobile Emergency Action Bar -->")
old_bar_end = code.find('def generate_local_business_schema', old_bar_start)

if old_bar_start == -1 or old_bar_end == -1:
    print("ERROR: could not locate Sticky Mobile Action Bar in build_winch_helpers.py")
    exit(1)

new_bar_code = '''<!-- Floating Mobile Smart Action Bar (Ultra-Compact, Thumb-Zone Ergonomics & High-Conversion) -->
  <aside aria-label="أزرار الاتصال السريع الميداني" class="fixed bottom-2.5 left-2.5 right-2.5 z-40 max-w-md mx-auto lg:hidden pointer-events-auto">
    <div class="glass bg-slate-950/95 backdrop-blur-xl border border-amber-500/50 rounded-2xl p-1.5 shadow-[0_10px_35px_rgba(0,0,0,0.9)] flex items-center justify-between gap-1.5">
      
      <!-- Button 1: Primary Hotline (01032194206) -->
      <a href="tel:{PHONE}" data-track="call-primary" aria-label="اتصال بالخط الرئيسي 01032194206" class="flex-1 min-w-0 py-2.5 px-2 bg-gradient-to-r from-rescue-600 via-rescue-500 to-amber-600 active:scale-95 hover:brightness-110 text-white font-black rounded-xl shadow-lg glow-red flex items-center justify-center gap-1.5 text-xs transition-transform">
        <svg class="w-4 h-4 shrink-0 animate-pulse text-amber-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
        </svg>
        <span class="truncate font-black">{PHONE_DISPLAY}</span>
      </a>

      <!-- Button 2: Secondary Hotline (01283038303) -->
      <a href="tel:{PHONE_ALT}" data-track="call-secondary" aria-label="اتصال بطوارئ 2 01283038303" class="py-2.5 px-2.5 bg-slate-900 border border-amber-500/30 active:scale-95 hover:border-amber-400 text-amber-300 font-bold rounded-xl shadow flex items-center justify-center gap-1 text-[11px] shrink-0 transition-transform">
        <span class="text-xs">📞</span>
        <span class="font-mono font-bold">{PHONE_ALT}</span>
      </a>

      <!-- Button 3: WhatsApp Location Link -->
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener" data-track="whatsapp-location" aria-label="إرسال اللوكيشن على واتساب" class="py-2.5 px-3 bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white font-black rounded-xl shadow-md flex items-center justify-center gap-1 text-xs shrink-0 transition-transform">
        <svg class="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.173.086.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.072.043.419-.101.824z"/>
        </svg>
        <span class="font-bold">واتساب</span>
      </a>

    </div>
  </aside>
"""

'''

code = code[:old_bar_start] + new_bar_code + code[old_bar_end:]
with open(helpers_path, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: Upgraded get_footer in build_winch_helpers.py with new Floating Action Bar!")
