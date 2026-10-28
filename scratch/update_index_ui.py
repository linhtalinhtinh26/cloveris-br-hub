# -*- coding: utf-8 -*-
import json, re

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for language separation card & divider
old_lang_css = """.lang-section {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 16px;
      position: relative;
      z-index: 10;
    }

    .lang-toolbar-pill {
      background: #eef7f0;
      border: 2px solid #bcdbc2;
      border-radius: 28px;
      padding: 5px 10px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.04), inset 0 2px 3px rgba(255, 255, 255, 0.7);
    }

    .lang-btn {
      font-family: 'Baloo 2', 'Nunito', sans-serif;
      font-size: 15.5px;
      font-weight: 700;
      padding: 7px 18px;
      border-radius: 20px;
      border: 2px solid transparent;
      background: transparent;
      color: #3b5a43;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      user-select: none;
    }

    .lang-btn:hover {
      background: #ffffff;
      color: var(--clover-dark);
      border-color: #aed6b5;
      transform: translateY(-1px);
    }

    .lang-btn:active {
      transform: translateY(1px);
    }

    .lang-btn.active {
      background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
      color: #ffffff;
      border-color: #1b5e20;
      box-shadow: 
        0 4px 10px rgba(46, 125, 50, 0.35),
        inset 0 1px 2px rgba(255, 255, 255, 0.4);
    }"""

new_lang_css = """/* ========================================================
       🌐 1. PHÂN TÁCH KHU VỰC CHỌN NGÔN NGỮ (LANGUAGE SELECTION CARD)
       ======================================================== */
    .lang-card-box {
      width: 100%;
      background: #ffffff;
      border: 2.5px solid #bddac2;
      border-radius: 26px;
      padding: 16px 18px 14px;
      box-shadow: 
        0 6px 18px rgba(45, 122, 70, 0.08),
        inset 0 2px 4px rgba(255, 255, 255, 0.8);
      margin-bottom: 16px;
      position: relative;
      z-index: 10;
    }

    .lang-card-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      border-bottom: 1.5px dashed #d1ebd6;
      padding-bottom: 10px;
    }

    .lang-icon-badge {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--clover-mist);
      border: 1.5px solid #a4d4b0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      flex-shrink: 0;
    }

    .lang-title-group {
      display: flex;
      flex-direction: column;
      text-align: left;
    }

    .lang-card-title {
      font-family: 'Baloo 2', cursive, sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--clover-dark);
      letter-spacing: 0.6px;
      line-height: 1.15;
    }

    .lang-card-subtitle {
      font-family: 'Nunito', sans-serif;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      line-height: 1.25;
    }

    .lang-buttons-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      width: 100%;
    }

    .lang-btn {
      font-family: 'Baloo 2', 'Nunito', sans-serif;
      padding: 10px 12px;
      border-radius: 18px;
      border: 2.5px solid #bddac2;
      background: #f7fbf8;
      color: #2e4d36;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 3px 6px rgba(0, 0, 0, 0.04);
      transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
      user-select: none;
      text-align: left;
    }

    .lang-flag {
      font-size: 24px;
      line-height: 1;
      filter: drop-shadow(0 2px 2px rgba(0, 0, 0, 0.1));
    }

    .lang-btn-text {
      display: flex;
      flex-direction: column;
    }

    .lang-primary {
      font-size: 16px;
      font-weight: 800;
      line-height: 1.15;
    }

    .lang-secondary {
      font-size: 11.5px;
      font-weight: 600;
      color: #63846d;
      margin-top: 2px;
    }

    .lang-btn:hover {
      background: #ffffff;
      border-color: var(--clover-mid);
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(45, 122, 70, 0.15);
    }

    .lang-btn:active {
      transform: translateY(1px);
    }

    .lang-btn.active {
      background: linear-gradient(135deg, #388e3c 0%, #1b5e20 100%);
      color: #ffffff;
      border-color: #144919;
      box-shadow: 
        0 6px 14px rgba(27, 94, 32, 0.35),
        inset 0 1px 2px rgba(255, 255, 255, 0.35);
      transform: scale(1.02);
    }

    .lang-btn.active .lang-secondary {
      color: #dcedc8;
    }

    .lang-status-pill {
      margin-top: 10px;
      background: #eef7f0;
      border-radius: 12px;
      padding: 5px 12px;
      font-family: 'Nunito', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      color: #256637;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }

    /* Ranh giới phân cách giữa khu chọn ngôn ngữ và khu caption */
    .section-divider-stitch {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: 4px 0 14px;
      position: relative;
      z-index: 5;
    }

    .stitch-line {
      flex: 1;
      height: 2px;
      background-image: linear-gradient(to right, transparent, #b5dac0 20%, #b5dac0 80%, transparent);
    }

    .stitch-badge {
      font-family: 'Baloo 2', cursive, sans-serif;
      font-size: 12px;
      font-weight: 800;
      color: #3b744c;
      background: #edf7ef;
      border: 1.5px dashed #9bc8a6;
      padding: 2px 10px;
      border-radius: 14px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }"""

if old_lang_css in html:
    html = html.replace(old_lang_css, new_lang_css)
    print("Replaced lang CSS successfully!")
else:
    print("Warning: old_lang_css not matched, checking alternate...")

# 2. Update HTML for language section
old_lang_html = """      <!-- ========================================================
           1. LANGUAGE SELECTION (English & Korean Only)
           ======================================================== -->
      <section class="lang-section" aria-label="Chọn ngôn ngữ">
        <div class="lang-toolbar-pill">
          <button type="button" class="lang-btn" id="btn-lang-en" onclick="setLanguage('en')">
            <span>🇬🇧</span>
            <span>English</span>
          </button>
          <button type="button" class="lang-btn" id="btn-lang-kr" onclick="setLanguage('kr')">
            <span>🇰🇷</span>
            <span>한국어</span>
          </button>
        </div>
      </section>"""

new_lang_html = """      <!-- ========================================================
           1. PHÂN TÁCH RÕ RÀNG PHẦN CHỌN NGÔN NGỮ (LANGUAGE CARD)
           ======================================================== -->
      <section class="lang-card-box" aria-label="Chọn ngôn ngữ">
        <div class="lang-card-header">
          <span class="lang-icon-badge">🌐</span>
          <div class="lang-title-group">
            <h2 class="lang-card-title">CHOOSE LANGUAGE</h2>
            <p class="lang-card-subtitle">Chọn ngôn ngữ để hiển thị kho 500 caption</p>
          </div>
        </div>

        <div class="lang-buttons-grid">
          <button type="button" class="lang-btn" id="btn-lang-en" onclick="setLanguage('en')">
            <span class="lang-flag">🇬🇧</span>
            <div class="lang-btn-text">
              <span class="lang-primary">English</span>
              <span class="lang-secondary">Tiếng Anh · 500 câu</span>
            </div>
          </button>
          
          <button type="button" class="lang-btn" id="btn-lang-kr" onclick="setLanguage('kr')">
            <span class="lang-flag">🇰🇷</span>
            <div class="lang-btn-text">
              <span class="lang-primary">한국어</span>
              <span class="lang-secondary">Tiếng Hàn · 500 câu</span>
            </div>
          </button>
        </div>

        <div class="lang-status-pill" id="langStatusPill">
          <span>✨</span>
          <span id="langStatusText">Vui lòng bấm chọn 1 ngôn ngữ bên trên</span>
        </div>
      </section>

      <!-- Ranh giới phân chia rõ ràng phần chọn ngôn ngữ và phần caption -->
      <div class="section-divider-stitch">
        <span class="stitch-line"></span>
        <span class="stitch-badge">🍀 CAPTION STATION 🍀</span>
        <span class="stitch-line"></span>
      </div>"""

if old_lang_html in html:
    html = html.replace(old_lang_html, new_lang_html)
    print("Replaced lang HTML successfully!")
else:
    print("Warning: old_lang_html not matched, checking alternate...")

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved HTML step 1.")
