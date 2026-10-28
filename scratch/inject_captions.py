# -*- coding: utf-8 -*-
import json
import re

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\scratch\captions_1000.json', encoding='utf-8') as f:
    data = json.load(f)

# 1. Create captions_en_500.txt
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\captions_en_500.txt', 'w', encoding='utf-8') as f:
    for i, s in enumerate(data['en'], 1):
        f.write(f"{s}\n\n#CORTIS #코르티스\n\n")

# 2. Create captions_kr_500.txt
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\captions_kr_500.txt', 'w', encoding='utf-8') as f:
    for i, s in enumerate(data['kr'], 1):
        f.write(f"{s}\n\n#CORTIS #코르티스\n\n")

print("Exported text files successfully!")

# 3. Update index.html
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', encoding='utf-8') as f:
    html = f.read()

json_str = json.dumps(data, ensure_ascii=False, indent=2)
new_code = f"const captionsData = {json_str};\n\n    const hashtagsData = {{\n      en: \"#CORTIS #코르티스\",\n      kr: \"#CORTIS #코르티스\"\n    }};"

pattern = re.compile(r'const captionsData = \{.*?\};\s*const hashtagsData = \{.*?\};', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(new_code, html)
    with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated with 1000 captions successfully!")
else:
    print("Could not find pattern in index.html, check regex.")
