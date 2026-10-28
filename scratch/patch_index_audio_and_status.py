# -*- coding: utf-8 -*-
with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', encoding='utf-8') as f:
    html = f.read()

# 1. Add audio element right before closing </main> or in body
if '<audio id="poyoiyoiAudioPlayer"' not in html:
    html = html.replace('</main>', '  <audio id="poyoiyoiAudioPlayer" preload="auto"></audio>\n  </main>')
    print("Added audio element to HTML.")

# 2. Update setLanguage in index.html to update langStatusText
old_set_lang = """    function setLanguage(lang) {
      if (!captionsData[lang]) return;
      currentLang = lang;

      // Update active styling
      document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById(`btn-lang-${lang}`);
      if (activeBtn) activeBtn.classList.add('active');

      // Hide placeholder, show workspace
      welcomePlaceholder.style.display = 'none';
      captionWorkspace.style.display = 'flex';

      // Pick random initial caption
      const list = captionsData[currentLang];
      currentIndex = Math.floor(Math.random() * list.length);
      renderCaption();

      // Korean font tweak
      if (lang === 'kr') {
        captionTextEl.classList.add('lang-kr');
      } else {
        captionTextEl.classList.remove('lang-kr');
      }

      setTimeout(updateScallopFrame, 20);
    }"""

new_set_lang = """    function setLanguage(lang) {
      if (!captionsData[lang]) return;
      currentLang = lang;

      // Update active styling
      document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById(`btn-lang-${lang}`);
      if (activeBtn) activeBtn.classList.add('active');

      // Cập nhật trạng thái lựa chọn rõ ràng
      const langStatusText = document.getElementById('langStatusText');
      if (langStatusText) {
        const langName = lang === 'en' ? 'English (Tiếng Anh)' : '한국어 (Tiếng Hàn)';
        langStatusText.innerHTML = `Đang kích hoạt: <strong>${langName}</strong> · Kho 500 caption sẵn sàng! 🍀`;
      }

      // Hide placeholder, show workspace
      welcomePlaceholder.style.display = 'none';
      captionWorkspace.style.display = 'flex';

      // Pick random initial caption
      const list = captionsData[currentLang];
      currentIndex = Math.floor(Math.random() * list.length);
      renderCaption();

      // Korean font tweak
      if (lang === 'kr') {
        captionTextEl.classList.add('lang-kr');
      } else {
        captionTextEl.classList.remove('lang-kr');
      }

      setTimeout(updateScallopFrame, 20);
    }"""

if old_set_lang in html:
    html = html.replace(old_set_lang, new_set_lang)
    print("Updated setLanguage successfully!")
else:
    print("Warning: old_set_lang not matched exactly.")

# 3. Update playPiyoiyoiSound
old_play_sound = """    function playPiyoiyoiSound() {
      if (poyoiyoiAudios && poyoiyoiAudios.length > 0) {
        const randomAudioUrl = poyoiyoiAudios[Math.floor(Math.random() * poyoiyoiAudios.length)];
        const audio = new Audio(randomAudioUrl);
        audio.play().catch(e => {
          console.warn('Audio play failed, playing fallback synth sound:', e);
          playCuteWebAudioPop();
        });
      } else {
        playCuteWebAudioPop();
      }
    }"""

new_play_sound = """    function playPiyoiyoiSound() {
      if (poyoiyoiAudios && poyoiyoiAudios.length > 0) {
        // Chọn ngẫu nhiên 1 âm thanh từ mảng 35 file trong thư mục assets/audio/
        const randomIndex = Math.floor(Math.random() * poyoiyoiAudios.length);
        const randomAudioUrl = poyoiyoiAudios[randomIndex];

        try {
          const player = document.getElementById('poyoiyoiAudioPlayer');
          if (player) {
            player.pause();
            player.src = randomAudioUrl;
            player.currentTime = 0;
            player.volume = 1.0;
            const playPromise = player.play();
            if (playPromise !== undefined) {
              playPromise.catch(err => {
                console.warn('Audio tag play warning, trying direct Audio:', err);
                const a = new Audio(randomAudioUrl);
                a.volume = 1.0;
                a.play().catch(e => {
                  console.warn('Direct Audio error, using synth:', e);
                  playCuteWebAudioPop();
                });
              });
            }
          } else {
            const a = new Audio(randomAudioUrl);
            a.volume = 1.0;
            a.play().catch(e => playCuteWebAudioPop());
          }
        } catch (e) {
          console.warn('General audio error, using synth:', e);
          playCuteWebAudioPop();
        }
      } else {
        playCuteWebAudioPop();
      }
    }"""

if old_play_sound in html:
    html = html.replace(old_play_sound, new_play_sound)
    print("Updated playPiyoiyoiSound successfully!")
else:
    print("Warning: old_play_sound not matched exactly.")

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
