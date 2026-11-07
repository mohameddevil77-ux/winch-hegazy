import os

p = r"D:\winch-hegazy\backlinks\PRESS_RELEASE_AR.md"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("مؤسسة", "فريق")
c = c.replace("المؤسسة", "فريق العمل")

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print("SUCCESS: Cleaned PRESS_RELEASE_AR.md")
