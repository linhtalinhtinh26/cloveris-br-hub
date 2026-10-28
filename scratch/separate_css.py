# -*- coding: utf-8 -*-
import re

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', encoding='utf-8') as f:
    html = f.read()

# Extract <style>...</style>
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if not style_match:
    print("Error: Could not find <style> block in index.html")
    exit(1)

css_content = style_match.group(1).strip()

# Now, let's adjust the language buttons CSS in css_content
# We want 2 separate, distinct cute pill buttons side by side, clean like Image 1
# Remove old .lang-card-box and replace with clean .lang-section and .lang-pill-btn
new_lang_pill_css = """/* ========================================================
   🌐 1. SEPARATE LANGUAGE PILL BUTTONS (English & 한국어)
   ======================================================== */
.lang-section {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 4px;
  margin-bottom: 18px;
  position: relative;
  z-index: 10;
}

.lang-buttons-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  width: 100%;
  max-width: 340px;
}

.lang-pill-btn {
  flex: 1;
  height: 44px;
  font-family: 'Baloo 2', 'Nunito', sans-serif;
  font-size: 16px;
  font-weight: 700;
  border-radius: 26px;
  border: 2.5px solid #a3d2b0;
  background: #ffffff;
  color: #275e37;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(45, 122, 70, 0.08), inset 0 -2px 0 rgba(0, 0, 0, 0.03);
  transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
  user-select: none;
  letter-spacing: 0.5px;
}

.lang-pill-btn:hover {
  background: #eef8f1;
  border-color: #4caf50;
  color: #1b5e20;
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(45, 122, 70, 0.15);
}

.lang-pill-btn:active {
  transform: translateY(1px);
}

.lang-pill-btn.active {
  background: linear-gradient(135deg, #388e3c 0%, #1b5e20 100%);
  color: #ffffff;
  border-color: #144919;
  box-shadow: 
    0 5px 14px rgba(27, 94, 32, 0.35),
    inset 0 1px 2px rgba(255, 255, 255, 0.35);
  transform: scale(1.03);
}"""

# Replace in css_content
pattern_to_replace = re.compile(r'/\* ========================================================\s*🌐 1\. PHÂN TÁCH KHU VỰC CHỌN NGÔN NGỮ.*?(?=\.welcome-placeholder)', re.DOTALL)
if pattern_to_replace.search(css_content):
    css_content = pattern_to_replace.sub(new_lang_pill_css + "\n\n    ", css_content)
    print("Replaced lang card CSS with separate pill buttons CSS!")
else:
    print("Warning: Pattern for old lang card CSS not matched, prepending new CSS.")
    css_content += "\n\n" + new_lang_pill_css

# Write style.css
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Saved style.css successfully!")

# Now update index.html:
# 1. Replace <style>...</style> with <link rel="stylesheet" href="style.css" />
html = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css" />', html, flags=re.DOTALL)

# 2. Update the language HTML in index.html to 2 separate pill buttons
old_lang_box = re.search(r'<!-- ========================================================\s*1\. PHÂN TÁCH RÕ RÀNG PHẦN CHỌN NGÔN NGỮ.*?<!-- Ranh giới.*?</div>', html, re.DOTALL)

new_lang_html = """      <!-- ========================================================
           1. 2 NÚT CHỌN NGÔN NGỮ TÁCH RỜI (English & 한국어)
           ======================================================== -->
      <section class="lang-section" aria-label="Chọn ngôn ngữ">
        <div class="lang-buttons-row">
          <button type="button" class="lang-pill-btn" id="btn-lang-en" onclick="setLanguage('en')">
            English
          </button>
          <button type="button" class="lang-pill-btn" id="btn-lang-kr" onclick="setLanguage('kr')">
            한국어
          </button>
        </div>
      </section>"""

if old_lang_box:
    html = html.replace(old_lang_box.group(0), new_lang_html)
    print("Replaced language section HTML with 2 separate buttons!")
else:
    print("Warning: old_lang_box regex not matched, trying fallback replace.")

# 3. Update setLanguage in index.html: remove langStatusText reference since it's now 2 clean buttons
html = html.replace("""      // Cập nhật trạng thái lựa chọn rõ ràng
      const langStatusText = document.getElementById('langStatusText');
      if (langStatusText) {
        const langName = lang === 'en' ? 'English (Tiếng Anh)' : '한국어 (Tiếng Hàn)';
        langStatusText.innerHTML = `Đang kích hoạt: <strong>${langName}</strong> · Kho 500 caption sẵn sàng! 🍀`;
      }
""", "")

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")
