file_path = r"D:\winch-hegazy\scripts\build_winch_helpers.py"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

target = """  <!-- Precompiled Minified Pure Tailwind CSS (Zero Runtime Script Overhead) -->
  <link rel="stylesheet" href="{prefix}assets/css/styles.min.css">
</head>
<body class="bg-[#0b0f17] text-slate-100 font-['Cairo',sans-serif] overflow-x-hidden">
\"\"\""""

replacement = """  <!-- Precompiled Minified Pure Tailwind CSS (Zero Runtime Script Overhead) -->
  <link rel="stylesheet" href="{prefix}assets/css/styles.min.css">
\"\"\""""

if target in text:
    text = text.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed get_head end successfully!")
else:
    print("Target not found, checking exact text...")
    idx = text.find("styles.min.css")
    print(repr(text[idx-50:idx+150]))
