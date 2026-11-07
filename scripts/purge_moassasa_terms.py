# -*- coding: utf-8 -*-
import os, re

base_dir = r"D:\winch-hegazy"
scripts_dir = os.path.join(base_dir, "scripts")

# 1. Update build_winch_helpers.py
helpers_path = os.path.join(scripts_dir, "build_winch_helpers.py")
with open(helpers_path, "r", encoding="utf-8") as f:
    h = f.read()

h = h.replace(
    'المؤسسة الرائدة في خدمات إنقاذ وسحب ونقل السيارات في جمهورية مصر العربية على مدار 24 ساعة بأحدث أوناش هيدروليكية مغلقة وأفضل أسعار بدون استغلال.',
    'الخيار الأول المعتمد لخدمات إنقاذ وسحب ونقل السيارات في جمهورية مصر العربية على مدار 24 ساعة بأحدث أوناش هيدروليكية مغلقة وأفضل أسعار بدون استغلال.'
)
with open(helpers_path, "w", encoding="utf-8") as f:
    f.write(h)
print("SUCCESS: Updated build_winch_helpers.py")

# 2. Update build_articles_engine.py
engine_path = os.path.join(scripts_dir, "build_articles_engine.py")
with open(engine_path, "r", encoding="utf-8") as f:
    e = f.read()

e = e.replace('ومساهمة المؤسسة في رسوم الكارتة', 'مع مساهمتنا في دفع جزء من رسوم الكارتة')
e = e.replace('<strong class="text-white">المؤسسة:</strong>', '<strong class="text-white">اسم الخدمة:</strong>')

with open(engine_path, "w", encoding="utf-8") as f:
    f.write(e)
print("SUCCESS: Updated build_articles_engine.py")

# 3. Update generate_all_winch_pages.py
all_pages_path = os.path.join(scripts_dir, "generate_all_winch_pages.py")
with open(all_pages_path, "r", encoding="utf-8") as f:
    a = f.read()

a = a.replace(
    '> المؤسسة الرائدة في خدمات إنقاذ وسحب ونقل السيارات والمعدات في جمهورية مصر العربية',
    '> أسطول الإنقاذ المتخصص في خدمات إنقاذ وسحب ونقل السيارات والمعدات في جمهورية مصر العربية'
)
with open(all_pages_path, "w", encoding="utf-8") as f:
    f.write(a)
print("SUCCESS: Updated generate_all_winch_pages.py")

# 4. Update llms.txt and llms-full.txt
for fname in ["llms.txt", "llms-full.txt"]:
    p = os.path.join(base_dir, fname)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace(
            '> المؤسسة الرائدة في خدمات إنقاذ وسحب ونقل السيارات والمعدات في جمهورية مصر العربية',
            '> أسطول الإنقاذ المتخصص في خدمات إنقاذ وسحب ونقل السيارات والمعدات في جمهورية مصر العربية'
        )
        c = c.replace('المؤسسة', 'فريق أوناش أولاد حجازي')
        with open(p, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"SUCCESS: Updated {fname}")

# 5. Update backlinks and seo markdown files
for root_target in [os.path.join(base_dir, "backlinks"), os.path.join(base_dir, "seo")]:
    for fname in os.listdir(root_target):
        if fname.endswith((".md", ".json", ".txt")):
            fp = os.path.join(root_target, fname)
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace('المؤسسة الرائدة', 'الخيار الأول المعتمد')
            content = content.replace('مؤسسة أوناش إنقاذ أولاد حجازي', 'فريق أوناش إنقاذ أولاد حجازي')
            content = content.replace('مؤسسة أولاد حجازي', 'فريق أولاد حجازي')
            content = content.replace('هي مؤسسة [أوناش إنقاذ أولاد حجازي]', 'هو فريق [أوناش إنقاذ أولاد حجازي]')
            content = content.replace('أطلقت المؤسسة', 'أطلق فريق أولاد حجازي')
            content = content.replace('للمؤسسة', 'لفريق أولاد حجازي')
            content = content.replace('المؤسسة', 'فريق العمل الميداني')
            
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"SUCCESS: Updated {fname}")

print("All term replacements completed successfully!")
