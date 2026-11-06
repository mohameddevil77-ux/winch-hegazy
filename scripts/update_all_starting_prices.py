import glob
import re
import os

base_dir = r"D:\winch-hegazy"
files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "blog", "*.html"))

for f in files:
    filename = os.path.basename(f)
    with open(f, "r", encoding="utf-8") as fl:
        content = fl.read()

    # Skip changing the debunking context in the new promo article
    if filename == "winch-offers-discounts-cairo.html":
        continue

    orig = content
    # Update Schema priceRange
    content = content.replace('"priceRange": "EGP 250 - EGP 800"', '"priceRange": "EGP 600 - EGP 3500"')
    
    # Update text starting prices
    content = content.replace("يبدأ من 250 جنيه", "يبدأ من 600 جنيه")
    content = content.replace("تبدأ من 250 جنيه", "تبدأ من 600 جنيه")
    content = content.replace("يبدأ من 250 ج.م", "يبدأ من 600 ج.م")
    content = content.replace("تبدأ من 250 ج.م", "تبدأ من 600 ج.م")
    content = content.replace("تبدأ من 250 ج", "تبدأ من 600 ج")
    content = content.replace("250 - 300 ج.م", "600 - 750 ج.م")
    content = content.replace("250 إلى 300 جنيه", "600 إلى 750 جنيه")
    content = content.replace("250 - 350 ج.م", "600 - 750 ج.م")
    content = content.replace("بأرخص سعر يبدأ من 250 جنيه", "بأرخص سعر واقعي يبدأ من 600 جنيه")
    content = content.replace("أرخص سعر يبدأ من 250 جنيه", "أرخص سعر واقعي يبدأ من 600 جنيه")
    content = content.replace("من 250 جنيه مصري فقط", "من 600 جنيه مصري فقط")
    
    # In index.html calculator JS
    if filename == "index.html":
        content = content.replace("sedan: { same: '250 - 300 ج.م'", "sedan: { same: '600 - 750 ج.م'")
        content = content.replace("center: '350 - 450 ج.م'", "center: '750 - 950 ج.م'")
        content = content.replace("home: '350 - 500 ج.م'", "home: '950 - 1300 ج.م'")
        content = content.replace("cross: 'يبدأ من 600 ج.م'", "cross: 'يبدأ من 1500 ج.م'")
        content = content.replace("suv: { same: '300 - 350 ج.م'", "suv: { same: '750 - 900 ج.م'")
        content = content.replace("center: '400 - 550 ج.م'", "center: '900 - 1200 ج.م'")
        content = content.replace("home: '450 - 600 ج.م'", "home: '1200 - 1600 ج.م'")
        content = content.replace("cross: 'يبدأ من 750 ج.م'", "cross: 'يبدأ من 1800 ج.م'")
        content = content.replace("heavy: { same: '500 - 700 ج.م'", "heavy: { same: '1200 - 1600 ج.م'")
        content = content.replace("center: '700 - 1000 ج.م'", "center: '1600 - 2200 ج.م'")
        content = content.replace("home: '800 - 1200 ج.م'", "home: '2200 - 3000 ج.م'")
        content = content.replace("cross: 'يبدأ من 1400 ج.م'", "cross: 'يبدأ من 3000 ج.م'")
        content = content.replace("|| '250 - 350 ج.م'", "|| '600 - 750 ج.م'")

    if content != orig:
        with open(f, "w", encoding="utf-8") as fl:
            fl.write(content)
        print(f"Updated {filename}")

print("SUCCESS: Finished updating all starting prices to 600 EGP!")
