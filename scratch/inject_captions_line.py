# -*- coding: utf-8 -*-
import json

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\scratch\captions_1000.json', encoding='utf-8') as f:
    data = json.load(f)

# Update index.html
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
end_idx = None

for idx, line in enumerate(lines):
    if "const captionsData = {" in line:
        start_idx = idx
    if start_idx is not None and "const poyoiyoiAudios = [" in line:
        end_idx = idx
        break

if start_idx is not None and end_idx is not None:
    json_str = json.dumps(data, ensure_ascii=False, indent=6)
    replacement = [
        f"    const captionsData = {json_str};\n\n",
        "    // Hashtags theo ngôn ngữ\n",
        "    const hashtagsData = {\n",
        '      en: "#CORTIS #코르티스",\n',
        '      kr: "#CORTIS #코르티스"\n',
        "    };\n\n"
    ]
    new_lines = lines[:start_idx] + replacement + lines[end_idx:]
    with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Successfully replaced lines {start_idx} to {end_idx} in index.html!")
else:
    print(f"Error: start_idx={start_idx}, end_idx={end_idx}")
