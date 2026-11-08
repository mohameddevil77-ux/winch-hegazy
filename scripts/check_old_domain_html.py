import glob, re

files = glob.glob(r"D:\winch-hegazy\**\*.html", recursive=True)
count = 0
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    if "winchawladhegazy.com" in content:
        matches = len(re.findall(r'awladhegazy\.com', content))
        print(f"{f.replace('D:\\winch-hegazy\\', '')}: {matches} occurrences of winchawladhegazy.com")
        count += 1

print(f"Total files with old domain winchawladhegazy.com: {count}")
