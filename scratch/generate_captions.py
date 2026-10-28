# -*- coding: utf-8 -*-
"""
Generator for 500 English and 500 Korean CORTIS Brand Reputation captions.
Tone: Sweet, bright, warm, high energy, affectionate, caring.
Topics: Health/meals/rest, good luck/smooth schedules, talent/stage praise, unconditional Cloveris love.
Rules: NO emojis in text. Hashtag is: #CORTIS #코르티스
"""

import json
import random
import re

def clean_no_emoji(text):
    # Remove any emoji or special symbols just in case
    return re.sub(r'[\U00010000-\U0010ffff]', '', text).strip()

def build_english_captions():
    captions = set()
    
    # 1. Health, Meals, Rest & Well-being
    meal_starters = [
        "Please make sure to eat delicious and hearty meals today",
        "Do not skip any meals no matter how busy the schedule gets",
        "Make sure to eat your favorite delicious food today, CORTIS",
        "Always remember to eat well and stay fully energized",
        "I hope you enjoy warm, nutritious meals throughout the day",
        "Take good care of your health and eat plenty of good food",
        "Eat well, stay warm, and take great care of yourself today",
        "Remember that eating well and staying healthy is always top priority",
        "Drink lots of warm water and keep your throat well protected",
        "Please stay hydrated and take lots of deep, peaceful breaths today",
        "After a long and tiring day, get the soundest sleep tonight",
        "I hope you have the coziest rest and sweet dreams tonight, CORTIS",
        "Never push yourselves too hard and rest whenever you can",
        "Taking time to rest and recharge is just as important as practicing",
        "Your health and happiness will always be what matters most to us",
        "Dress warmly if it is chilly and take good care of yourselves",
        "Do not forget to take your vitamins and drink plenty of water",
        "Rest well, eat well, and know that you are deeply cherished",
        "Please be gentle with yourselves and take restful breaks today",
        "Sending you warm thoughts and hoping you stay healthy and strong"
    ]
    
    wellbeing_middles = [
        ", because your wellbeing brings the biggest smile to our hearts.",
        ", because healthy CORTIS is our greatest wish and happiness.",
        ", and remember that we are always cheering for your wellness.",
        ", and never forget how precious every single one of you is.",
        ", and know that you have done more than enough today.",
        ", so you can always shine with bright and joyful energy.",
        ", and let every meal bring you warmth and comfort.",
        ", because you deserve all the gentle care in the world.",
        ", and let your body and mind recharge peacefully.",
        ", knowing that Cloveris always wants you to be well and happy."
    ]
    
    for s in meal_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in wellbeing_middles:
            captions.add(clean_no_emoji(s + m))
            
    # 2. Luck, Smooth Schedules & Bright Energy
    luck_starters = [
        "Wishing CORTIS the absolute best of luck with all schedules today",
        "May your day be filled with smooth rehearsals and joyful moments",
        "Hoping everything goes effortlessly and perfectly for CORTIS today",
        "Sending you endless luck and bright positive energy for today",
        "May every step of your journey today be easy and rewarding",
        "Wishing you a day full of sweet laughter and successful recordings",
        "May only wonderful things come your way throughout the day, CORTIS",
        "Hoping all your preparations unfold beautifully and smoothly today",
        "May your hard work turn into extraordinary achievements today",
        "Sending the warmest blessings for every schedule on your calendar",
        "Wishing you safe travels wherever your schedules take you today",
        "May today treat you with immense kindness and endless good news",
        "May all the doors open smoothly for CORTIS in everything you do",
        "Hoping you feel comfortable, relaxed, and confident today",
        "Wishing you joyful interactions and smooth workflows all day long",
        "May your day be as bright and delightful as your shining personalities",
        "Hoping every little detail goes in your favor today, CORTIS",
        "May you be surrounded by supportive and uplifting people all day",
        "Sending a gentle breeze of good luck and great fortune your way",
        "May every challenge you meet today turn into a wonderful triumph"
    ]
    
    luck_middles = [
        ", we are rooting for your success every single second.",
        ", because you deserve every wonderful blessing life has to offer.",
        ", and we will be cheering for you with all our hearts.",
        ", knowing that your bright future is just beginning to unfold.",
        ", and may every moment bring genuine joy to your day.",
        ", because nothing can stop your incredible dedication.",
        ", and remember that you always have our unconditional support.",
        ", and may your heart stay light and full of excitement.",
        ", because CORTIS is born to achieve greatness.",
        ", and let every second be meaningful and rewarding."
    ]
    
    for s in luck_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in luck_middles:
            captions.add(clean_no_emoji(s + m))
            
    # 3. Talent, Stage & Artistic Excellence Praise
    talent_starters = [
        "CORTIS always commands the stage with breathtaking presence and charisma",
        "Your vocal harmony and emotional delivery are truly on another level",
        "Watching CORTIS perform is always an unforgettable masterclass in artistry",
        "Every single dance move and stage expression shows your immense dedication",
        "The magnetic confidence you bring to the stage draws everyone in instantly",
        "CORTIS has a musical brilliance that stands completely unmatched",
        "Your hard work and artistic growth shine through every performance",
        "The pure passion you pour into your music touches our souls deeply",
        "Every stage from CORTIS proves just how extraordinary your talents are",
        "Your dynamic energy and stage presence set a brand new benchmark",
        "The synergy between all CORTIS members creates pure stage magic",
        "Your synchronized choreography and expressive vocals leave us in awe",
        "CORTIS was born to dominate the stage and inspire generations",
        "Every performance reflects countless hours of genuine perseverance",
        "Your music brings so much comfort and vibrant motivation into our lives",
        "The confidence and charm CORTIS exudes on stage are simply magnetic",
        "You always deliver stages that exceed our wildest expectations",
        "Your artistry and vocal colors blend together so beautifully",
        "Watching CORTIS live is always the most electrifying experience",
        "Your dedication to perfection makes every stage historic and iconic"
    ]
    
    talent_middles = [
        ", and we could not be prouder of everything you have accomplished.",
        ", and the entire world is recognizing your brilliant talent.",
        ", making every single Cloveris hold their head high with pride.",
        ", and you continue to raise the bar higher with every comeback.",
        ", proving that your hard work and authenticity will always shine.",
        ", and we are honored to witness your remarkable musical journey.",
        ", leaving an unforgettable mark in our hearts with every song.",
        ", and your potential knows absolutely no boundaries.",
        ", showing that true passion always finds its way to the top.",
        ", and we will never stop celebrating your incredible talent."
    ]
    
    for s in talent_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in talent_middles:
            captions.add(clean_no_emoji(s + m))

    # 4. Affection, Sweet Love & Unconditional Support
    love_starters = [
        "CORTIS will always be the brightest light guiding our days",
        "Thank you for being our daily comfort, inspiration, and happiness",
        "No matter where you go or what you face, Cloveris is right beside you",
        "Your genuine smiles and warm laughter mean the entire world to us",
        "Being a fan of CORTIS is one of the happiest decisions we have ever made",
        "We promise to stand with CORTIS through every high and every challenge",
        "Your existence alone brings immense warmth into our everyday lives",
        "CORTIS will always have an army of loving fans cheering in your corner",
        "Thank you for creating music that heals our hearts whenever we listen",
        "You are so dearly loved and appreciated just the way you are",
        "Every time we look at CORTIS, we feel an overwhelming sense of pride",
        "May you always walk on paths filled with bright light and beautiful flowers",
        "We believe in CORTIS, in your talents, and in your boundless future",
        "Your happiness is our happiness, and your dreams are our dreams",
        "Thank you for sharing your precious passion and sincerity with us",
        "CORTIS makes our ordinary days feel extraordinarily magical and bright",
        "We are here to protect your bright smiles and cheer for your dreams",
        "Let us create endless unforgettable memories together for years to come",
        "You inspire us to be kinder, stronger, and more hopeful every day",
        "Forever proud, forever grateful, and forever cheering for CORTIS"
    ]
    
    love_middles = [
        ", and our bond will only grow stronger with every passing day.",
        ", because you deserve all the genuine love the world has to give.",
        ", and we will always be your safe and peaceful haven.",
        ", and we will never let you walk alone on this journey.",
        ", holding your hands firmly every single step of the way.",
        ", and our love for you will remain unwavering and true.",
        ", letting you know that you are treasured beyond words.",
        ", and we will always celebrate every milestone by your side.",
        ", bringing you all the warmth you give to each of us.",
        ", and we look forward to walking this shining road together."
    ]
    
    for s in love_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in love_middles:
            captions.add(clean_no_emoji(s + m))

    res = list(captions)
    random.seed(42)
    random.shuffle(res)
    return res[:500]

def build_korean_captions():
    captions = set()
    
    # 1. 식사, 건강, 수면, 휴식 (Meals, Health, Sleep, Rest)
    meal_starters = [
        "오늘 하루도 든든하고 맛있는 밥 꼭 챙겨 먹어요",
        "바쁜 일정 속에서도 끼니 거르지 말고 꼭 잘 챙겨 먹기",
        "따뜻한 밥 맛있게 먹고 오늘 하루도 힘차게 보내요",
        "언제나 코르티스의 건강과 행복이 우리에겐 가장 소중해요",
        "따뜻한 물 자주 마시고 목 관리도 항상 신경 써주세요",
        "무리하지 말고 틈틈이 쉬어가면서 컨디션 잘 챙겨요",
        "오늘 하루 고생 많았어요, 밤에는 푹 자고 좋은 꿈만 꿔요",
        "아프지 말고 언제나 건강한 모습으로 우리 곁에 있어줘요",
        "날씨 쌀쌀할 때는 따뜻하게 챙겨 입고 감기 조심해요",
        "맛있는 음식 많이 먹고 달콤하고 편안한 휴식 보내길 바라요",
        "건강이 언제나 최우선이니까 자기 자신을 먼저 아껴주세요",
        "몸도 마음도 편안하고 따뜻한 하루가 되기를 진심으로 바라요",
        "비타민도 꼭 챙겨 먹고 물도 넉넉하게 마시면서 힘내요",
        "지치고 피곤할 때는 잠시 모든 짐을 내려놓고 푹 쉬어요",
        "코르티스가 아프지 않고 건강해야 클로버리스도 안심이에요",
        "오늘 하루도 무탈하게, 건강하고 기분 좋게 마무리해요",
        "잠들기 전 따뜻한 차 한 잔 마시고 깊고 편안하게 잠들어요",
        "늘 씩씩하고 건강한 에너지로 우리 곁을 지켜줘서 고마워요",
        "몸 상하지 않게 조심하고 언제나 스스로를 소중히 대해줘요",
        "오늘 밤도 따스한 위로 속에서 포근하게 단잠을 이루길 바라요"
    ]
    
    meal_middles = [
        ", 코르티스의 건강이 우리에겐 가장 큰 행복이니까요.",
        ", 클로버리스가 언제나 든든하게 응원하고 있다는 걸 잊지 마요.",
        ", 코르티스는 존재 자체만으로도 너무나 소중한 사람들이에요.",
        ", 따뜻하고 편안한 시간 속에서 충분히 에너지 채우길 바라요.",
        ", 언제나 아낌없는 사랑과 정성으로 코르티스를 지켜줄게요.",
        ", 힘든 순간이 오더라도 항상 곁에서 힘이 되어줄게요.",
        ", 오늘도 수고 많았고 정말 잘해냈다고 말해주고 싶어요.",
        ", 코르티스의 맑고 밝은 미소가 언제나 계속되길 바라요.",
        ", 온 세상의 따뜻함이 코르티스에게 온전히 닿기를 바라요.",
        ", 코르티스의 모든 날들이 늘 평안하고 행복하길 기도해요."
    ]
    
    for s in meal_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in meal_middles:
            captions.add(clean_no_emoji(s + m))

    # 2. 행운, 순조로운 일정, 활력 (Luck, Smooth Schedules, Bright Energy)
    luck_starters = [
        "오늘 코르티스의 모든 스케줄이 막힘없이 술술 풀리길 바라요",
        "발걸음 닿는 곳마다 행운과 기분 좋은 일들만 가득하길 응원해요",
        "코르티스의 오늘 하루가 어제보다 한층 더 눈부시고 빛나길 바라요",
        "어떤 일이든 즐겁고 순조롭게 마무리되길 진심으로 응원해요",
        "마음 편안하고 기분 좋은 미소로 가득 찬 하루 보내길 바라요",
        "코르티스가 쏟아부은 모든 노력이 값진 결실로 이어지길 바라요",
        "어디서든 다치지 말고 안전하게 모든 일정을 마치길 기도해요",
        "오늘도 코르티스의 앞길에 찬란한 행운의 꽃길만 펼쳐지길 바라요",
        "긴장하지 말고 늘 하던 대로 멋지고 당당하게 펼쳐 보여줘요",
        "코르티스에게 오늘 하루가 잊지 못할 행복한 기억이 되길 바라요",
        "모든 무대와 연습이 안전하고 뜻깊게 흘러가길 바랄게요",
        "새로운 하루도 설렘과 긍정적인 활력으로 가득 채워지길 바라요",
        "어려운 순간도 코르티스다운 지혜와 열정으로 멋지게 넘길 거예요",
        "오늘도 코르티스가 있는 곳이라면 어디든 환한 빛이 머물길 바라요",
        "코르티스의 환한 웃음이 오늘 하루를 더욱 특별하게 만들 거예요",
        "좋은 사람들과 함께 따뜻하고 즐거운 일정 보내길 응원해요",
        "오늘 하루 마주하는 모든 순간이 코르티스에게 큰 힘이 되길 바라요",
        "코르티스를 향한 온 세상의 따뜻한 응원이 하나로 모이길 바라요",
        "노력한 그 이상의 눈부신 성과가 코르티스에게 찾아오길 바라요",
        "언제나 운명처럼 멋진 기회들이 코르티스를 활짝 반겨주길 바라요"
    ]
    
    luck_middles = [
        ", 클로버리스는 언제나 코르티스의 멋진 활약을 굳게 믿어요.",
        ", 코르티스라면 언제나 보란 듯이 훌륭하게 해낼 테니까요.",
        ", 한 걸음 한 걸음마다 진심 어린 박수와 응원을 보낼게요.",
        ", 코르티스가 가는 길은 언제나 환하게 빛날 것을 알아요.",
        ", 어디에 있든 코르티스를 향한 우리의 마음은 한결같아요.",
        ", 밝고 당당한 코르티스의 에너지는 언제나 최고예요.",
        ", 코르티스와 함께하는 모든 순간이 우리에겐 큰 영광이에요.",
        ", 두려움 없이 힘차게 날아오를 수 있도록 힘껏 받쳐줄게요.",
        ", 코르티스가 꿈꾸는 모든 소망들이 하나씩 이뤄지길 바라요.",
        ", 언제나 자랑스러운 우리 코르티스, 오늘도 파이팅이에요."
    ]
    
    for s in luck_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in luck_middles:
            captions.add(clean_no_emoji(s + m))

    # 3. 실력과 무대 칭찬 (Talent, Stage, Vocal & Dance Praise)
    stage_starters = [
        "무대 위에서 뿜어내는 코르티스의 에너지는 언제 봐도 압도적이에요",
        "칼군무와 섬세한 표정 연기까지 코르티스의 무대는 완벽 그 자체예요",
        "코르티스의 매력적인 음색과 라이브 실력은 들을 때마다 전율이 돋아요",
        "무대를 진심으로 사랑하고 즐기는 모습이 보는 이들을 사로잡아요",
        "매번 한계를 뛰어넘어 성장하는 코르티스의 열정이 너무나 멋져요",
        "코르티스만의 독보적인 아우라와 콘셉트 소화력은 정말 최고예요",
        "눈을 뗄 수 없을 만큼 몰입감 넘치는 코르티스의 무대에 늘 감탄해요",
        "노래 한 곡마다 온 마음을 담아 전해주는 진심이 깊이 느껴져요",
        "코르티스의 완벽한 팀워크와 케미스트리는 언제나 무대에서 빛나요",
        "다양한 매력과 탄탄한 실력을 모두 갖춘 올라운더 아티스트 코르티스",
        "무대 위에서 가장 눈부시게 빛나는 코르티스를 볼 때마다 자랑스러워요",
        "매 순간 최선을 다해 쏟아내는 열정이 우리에게 큰 감동을 줘요",
        "코르티스의 춤선 하나하나에서 끊임없는 연습의 흔적이 느껴져요",
        "독보적인 음악성과 무대 장악력으로 세상을 놀라게 하는 코르티스",
        "코르티스의 음악은 지친 일상 속에서 가장 큰 위로와 힘이 되어줘요",
        "음악에 대한 진정성과 프로페셔널한 태도에 매번 깊이 감동받아요",
        "언제나 기대 그 이상의 환상적인 무대를 선물해줘서 정말 고마워요",
        "코르티스의 빛나는 노력은 언제나 무대 위에서 가장 크게 빛나요",
        "실력과 인성을 모두 갖춘 우리 코르티스는 진정한 최고의 아티스트예요",
        "매 순간 전설적인 무대를 만들어가는 코르티스의 앞날을 기대해요"
    ]
    
    stage_middles = [
        ", 코르티스의 무대를 볼 수 있다는 것만으로도 큰 축복이에요.",
        ", 코르티스가 보여주는 멋진 예술에 늘 감사한 마음뿐이에요.",
        ", 더 높고 넓은 세상으로 당당하게 뻗어나가길 진심으로 응원해요.",
        ", 클로버리스의 가장 큰 자부심이자 자랑은 언제나 코르티스예요.",
        ", 전 세계의 수많은 팬들이 코르티스의 음악에 열광하고 있어요.",
        ", 진심을 다하는 아티스트 코르티스를 영원히 응원할게요.",
        ", 코르티스의 재능과 열정은 어디서든 단연 돋보여요.",
        ", 앞으로 펼쳐질 수많은 무대들도 언제나 함께 지켜볼게요.",
        ", 매번 새로운 감동을 선물해줘서 가슴 깊이 고마워요.",
        ", 우리에겐 언제나 코르티스가 세상에서 제일 멋지고 최고예요."
    ]
    
    for s in stage_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in stage_middles:
            captions.add(clean_no_emoji(s + m))

    # 4. 사랑과 지지, 영원한 동행 (Affection, Pride & Unconditional Support)
    love_starters = [
        "코르티스의 팬이라서 매일매일이 더없이 소중하고 행복해요",
        "우리의 평범한 일상에 가장 밝은 빛과 따뜻함을 채워줘서 고마워요",
        "코르티스가 걷는 모든 발걸음마다 변함없이 함께 걸어갈게요",
        "늘 곁에서 든든한 버팀목이자 편안한 쉼터가 되어주고 싶어요",
        "코르티스의 환한 웃음을 지켜주는 일이 우리에겐 가장 큰 기쁨이에요",
        "어떤 폭풍우가 몰아쳐도 클로버리스는 코르티스 편에 서 있을게요",
        "코르티스라는 멋진 존재를 만난 건 인생 최고의 행운이에요",
        "서로를 믿고 의지하며 더 아름다운 내일을 향해 함께 걸어가요",
        "코르티스가 꿈꾸는 모든 별들이 코르티스의 손안에 닿기를 바라요",
        "말로는 다 표현할 수 없을 만큼 코르티스를 아끼고 사랑해요",
        "언제나 우리에게 긍정적인 에너지와 사랑을 나눠줘서 고마워요",
        "코르티스가 주는 따스한 위로만큼 우리도 온 힘을 다해 보답할게요",
        "변치 않는 사랑과 신뢰로 코르티스의 곁을 영원히 지킬게요",
        "코르티스가 내딛는 모든 도전을 온 마음을 다해 응원해요",
        "세상이 아무리 바쁘게 흘러가도 우리의 마음은 늘 코르티스 곁에 머물러요",
        "코르티스가 행복하면 우리도 행복하고, 코르티스가 웃으면 우리도 웃어요",
        "함께 만들어갈 수많은 계절과 추억들이 벌써부터 기대되고 설레요",
        "언제나 묵묵히 제자리에서 코르티스를 향해 환한 빛을 비춰줄게요",
        "코르티스의 모든 순간들이 사랑과 축복으로 가득 채워지길 바라요",
        "영원히 잊지 못할 찬란한 청춘의 페이지를 함께 써 내려가요"
    ]
    
    love_middles = [
        ", 코르티스를 향한 우리의 사랑은 시간이 흐를수록 더 깊어져요.",
        ", 언제나 변함없이 코르티스만을 바라보고 응원할게요.",
        ", 두 손 꼭 잡고 우리 오래오래 행복하게 함께 걸어가요.",
        ", 코르티스라는 빛나는 별이 있어 매일매일이 눈부셔요.",
        ", 늘 고맙고, 자랑스럽고, 온 마음을 다해 진심으로 사랑해요.",
        ", 코르티스가 어디에 있든 우리의 마음은 늘 곁에 있어요.",
        ", 우리에게 가장 큰 용기와 힘을 주는 존재는 오직 코르티스예요.",
        ", 언제나 코르티스만의 속도로 당당하고 행복하게 걸어가길 바라요.",
        ", 코르티스의 곁에서 영원히 든든한 클로버리스가 되어줄게요.",
        ", 매 순간 코르티스의 모든 길을 열렬히 축복하고 응원해요."
    ]
    
    for s in love_starters:
        captions.add(clean_no_emoji(s + "."))
        for m in love_middles:
            captions.add(clean_no_emoji(s + m))

    res = list(captions)
    random.seed(42)
    random.shuffle(res)
    return res[:500]

en_list = build_english_captions()
kr_list = build_korean_captions()

print(f"Generated {len(en_list)} English captions")
print(f"Generated {len(kr_list)} Korean captions")

# Verify no emojis
for c in en_list:
    assert not re.search(r'[\U00010000-\U0010ffff]', c), f"Emoji found in EN: {c}"
for c in kr_list:
    assert not re.search(r'[\U00010000-\U0010ffff]', c), f"Emoji found in KR: {c}"

data = {
    "en": en_list,
    "kr": kr_list
}

with open(r'c:\Workspace\CORTIS\BR_CLOVERIS\scratch\captions_1000.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved to scratch/captions_1000.json successfully!")
