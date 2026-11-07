path = r"D:\winch-hegazy\scripts\generate_winch_hegazy_site.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace(
    '<h4 class="text-white font-extrabold text-sm mb-1">',
    '<h3 class="text-white font-extrabold text-sm mb-1">'
)
code = code.replace(
    '<h5 class="text-white font-black text-base">هل تحتاج ونش إنقاذ بمواصفات خاصة الآن؟</h5>',
    '<h3 class="text-white font-black text-base">هل تحتاج ونش إنقاذ بمواصفات خاصة الآن؟</h3>'
)

# And close tags for those cards
for title in [
    'تسعير محدد مسبقاً قبل تحرك الونش',
    'أحدث أسطول هيدروليكي 2026',
    'سائقون محترفون ومدربون على السلامة المهنية',
    'نقل سيارات السوبر كار (لامبورجيني هوراكان)',
    'نقل اللوادر والمعدات (كاتربيلر CAT 930)',
    'خدمة مواقع العمل الصحراوية والمحاجر',
    'أوناش أولاد حجازي الرسمي المعتمد (HEGAZY)',
    'إنقاذ سيارات الدفع الرباعي والبورش',
    'عناية فائقة بالسيارات الحديثة',
    'سحب رؤوس التريلات والشاحنات',
    'نقل الكرفانات والوحدات المتنقلة',
    'نقل عربات الجولف كارت (حمولة مزدوجة)',
    'نقل عربات الطعام (Food Trucks)',
    'نقل المعدات والرافعات الشوكية (TCM)',
    'نقل سيارات النقل التجاري بحمولتها'
]:
    code = code.replace(f'{title}</h4>', f'{title}</h3>')

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed heading hierarchy in generate_winch_hegazy_site.py")
