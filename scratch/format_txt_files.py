# -*- coding: utf-8 -*-
import json

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\scratch\captions_1000.json', encoding='utf-8') as f:
    data = json.load(f)

# Format EN file
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\captions_en_500.txt', 'w', encoding='utf-8') as f:
    f.write("=== 500 CÂU TIẾNG ANH (ENGLISH CAPTIONS FOR CORTIS) ===\n\n")
    for i, s in enumerate(data['en'], 1):
        f.write(f"[{i}]\n{s}\n\n#CORTIS #코르티스\n\n----------------------------------------\n\n")

# Format KR file
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\captions_kr_500.txt', 'w', encoding='utf-8') as f:
    f.write("=== 500 CÂU TIẾNG HÀN (KOREAN CAPTIONS FOR CORTIS) ===\n\n")
    for i, s in enumerate(data['kr'], 1):
        f.write(f"[{i}]\n{s}\n\n#CORTIS #코르티스\n\n----------------------------------------\n\n")

print("Both 500-caption text files formatted and saved cleanly!")
