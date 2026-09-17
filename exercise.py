'''Python va Web Fullstack (django va FastAPI). ===> external packages


Django va FastAPI — Python backend'ining ikki xil kuchi:
Django = To'liq Monolit (Hamma narsa ichida)
Vazifasi: Backend, admin panel, xavfsizlik va baza bilan ishlash (ORM) tayyor holda keladi.
Qachon ishlatiladi: Tayyor web-saytlar va murakkab monolit loyihalar uchun.

FastAPI = Tezkor API (Microservice va AI)
Vazifasi: Faqat backend API (JSON) yaratadi. Asinxron (async/await) bo'lgani uchun o'ta tezkor.
Qachon ishlatiladi: Frontend (React, Vue) ajratilgan loyihalar va Sun'iy Intellekt (AI) xizmatlari uchun.

Qisqa xulosa:
Katta tayyor sayt kerak bo'lsa — Django.
Tezkor API va AI integratsiyasi kerak bo'lsa — FastAPI.
'''
# ============================================================================== #

'''

AI Engineering (Computer Vision & NLP) — bu tayyor Sun'iy Intellekt modellarini amaliy dasturlarga (web, mobil, backend) integratsiya qilish va ularni haqiqiy loyihalarda ishlatish sohasi.

Computer Vision (CV) = AI'ning "Ko'zlari"
Vazifasi: Kompyuterga rasm va videolarni tushunishni, obyektlarni aniqlashni va tahlil qilishni o'rgatadi.
Qayerda ishlatiladi: Yuzni tanish (FaceID), videokuzatuv kameralari, tibbiy skanerlash va haydovchisiz mashinalar.
Python paketlari: OpenCV, YOLO, Pillow, torchvision.

NLP (Natural Language Processing) = AI'ning "Quloqlari va Tili"
Vazifasi: Kompyuterga inson matni va ovozini tushunish, tahlil qilish va javob qaytarishni o'rgatadi.
Qayerda ishlatiladi: ChatGPT/LLM'lar, tarjimonlar (Google Translate), chat-botlar va ovozli yordamchilar.
Python paketlari: transformers (Hugging Face), NLTK, spacy, langchain.

Qisqa xulosa:
Rasmlar va videolar bilan ishlasangiz — Computer Vision.
Matnlar, chat-botlar va LLM'lar bilan ishlasangiz — NLP.
'''

# ============================================================================== #

'''Automation / Testing (Selenium)

Automation / Testing (Selenium) — bu dasturiy ta'minotni (ayniqsa web-saytlarni) inson aralashuvisiz, kod orqali avtomatik ravishda test qilish va brauzer harakatlarini avtomatlashtirish sohasi.
Selenium = Brauzer Avtomatizatsiyasi
Vazifasi: Brauzerni inson kabi boshqaradi — tugmalarni bosadi, shakllarni to'ldiradi, sahifalarni skrolling qiladi va natijani tekshiradi.
Qayerda ishlatiladi: Saytlar to'g'ri ishlayotganini avtomatik test qilish (QA Automation) va web-scraping (ma'lumotlarni yig'ish).
Python paketlari: selenium, pytest (testlarni boshqarish uchun), webdriver-manager.

Qisqa xulosa:
Saytdagi tugmalarni qo'lda bosib o'tirmasdan, kod orqali avtomatik test qilish va brauzerni boshqarish uchun ishlatiladi.
Dasturlash olamida bu yo'nalish asosan QA Automation (Quality Assurance Automation) yoki Web Automation / Scraping deb ataladi.

QA Automation (Avtomatik Testchi): Har bir katta IT-kompaniya o'z mahsulotini (sayt yoki ilovasini) foydalanuvchilarga chiqarishdan oldin yuzlab testlardan o'tkazadi. Buni qo'lda qilish juda ko'p vaqt olgani uchun, Python + Selenium orqali avtomatik test yozadigan mutaxassislarga talab juda yuqori.

Web Scraping / Data Mining: Internetdagi minglab saytlardan ma'lumotlarni (masalan, narxlar, yangiliklar, statistikalar) avtomatik yig'ib oluvchi botlar yaratishda ham ishlatiladi.

Soha hajmi va kelajagi:
Bozor ehtiyoji: Standart Manual (qo'lda) testchilarga qaraganda Automation (kod bilan) testchilarning oylik maoshi va talabi bir necha barobar yuqori.
Qulay kirish nuqtasi: Python'ni o'rganib IT'ga tezroq va nisbatan osonroq kirib kelish uchun eng zo'r yo'nalishlardan biri.
bu faqat birgina kutubxona emas, balki alohida daromadli kasb (QA Automation Engineer) darajasidagi katta soha!
'''

# ============================================================================== #

'''Desktop & Mobile Apps (Kivy & BeeWare)

Desktop & Mobile Apps (Kivy & BeeWare) — bu Python kodi orqali bitta joyda yozib, uni bir vaqtning o'zida ham kompyuterga (Windows, macOS, Linux), ham telefonga (Android, iOS) dastur shaklida chiqarish (Cross-Platform) sohasi.

Kivy = O'yinlar va Custom UI (Grafik Interfeys)
Vazifasi: Shaxsiy va noodatiy interfeyslarni (custom UI) yaratishga mo'ljallangan. U o'zining OpenGL canvas'iga ega bo'lib, barcha platformalarda bir xil ko'rinish beradi.
Qayerda ishlatiladi: Interaktiv ilovalar, multimedia pleyerlari, multi-touch (ko'p barmqli) ekranlar va grafik interfeysli kichik o'yinlar.
Xususiyati: O'zining .kv dizayn tili bor, interfeysi har bir operatsion tizimning standart tugmalariga o'xshamaydi (o'ziga xos uslubda bo'ladi).

BeeWare = Tug'ma (Native) UI va Zamonaviy UI
Vazifasi: Python kodini har bir platformaning o'zining haqiqiy (native) elementlariga aylantirib beradi (Windows'da Windows tugmasi, iOS'da iOS tugmasi kabi ko'rinadi).
Qayerda ishlatiladi: Standart me'yordagi vizual mobil va desktop ilovalarni yaratishda.
Python paketlari: toga (UI freymvorki), briefcase (ilovabop qilib packaging/build qilish quroli).

Qisqa xulosa:

Noodatiy vizual va custom interfeys kerak bo'lsa — Kivy.
Har bir telefon/kompyuterning o'ziga mos native tugma va ko'rinishlari kerak bo'lsa — BeeWare.
'''

# ============================================================================== #

'''HACKING(CSRF va Injection)

CSRF va Injection — bu web-xavfsizlik (Cybersecurity) va Pentesting sohasining eng asosiy va eng ko'p uchraydigan zaifliklaridan (vulnerabilities) biri hisoblanadi.

1. CSRF (Cross-Site Request Forgery)
Foydalanuvchi bilmagan holda uning nomi va brauzer sessiyasi (cookie) orqali yashirin so'rov yuborish hujumi.
Mohiyati: Xaker jabrlanuvchini zararli havola (link) yoki saytga kirishga majbur qiladi. Foydalanuvchi allaqachon biror saytda (masalan, bank yoki ijtimoiy tarmoq) avtorizatsiyadan o'tgan bo'lsa, brauzer avtomatik ravishda uning cookielarini so'rovga qo'shib yuboradi.
Hujum misoli: Bank saytidagi pul o'tkazish So'rovi (POST /transfer). Xaker o'z saytiga yashirin ravishda ushbu so'rovni bajaruvchi kod joylaydi va foydalanuvchi nomidan pul o'tkazib oladi.
Himoyalanish:
CSRF Token: Har bir HTML formaga bir martalik yashirin token qo'shish.
SameSite Cookie: Cookie fayllarga SameSite=Strict yoki Lax atributini o'rnatish.

2. Injection (SQLi, Command Injection)
Foydalanuvchi kiritgan ma'lumot (input) serverda tekshirilmasdan to'g'ridan - to'g'ri buyruq yoki so'rov sifatida bajarilib ketishi.
SQL Injection (SQLi):
Mohiyati: Malumotlar bazasi (Database) so'roviga zararli SQL kodini kiritish.
Misol: Login shakliga admin' OR '1'='1 kiritilganda, baza parolni tekshirmasdan tizimga kirishga ruxsat berib yuboradi.
Himoyalanish: Prepared Statements (Parameterized Queries) va ORM'lardan (masalan, Mongoose, Sequelize) foydalanish.

Command Injection:
Mohiyati: Server operatsion tizimiga (Linux/Windows macOS) terminal buyruqlarini kiritib yuborish.
Misol: Saytdagi fayl nomini kiritish joyiga image.png; rm -rf / yuborib serverdagi fayllarni o'chirib tashlash.
Himoyalanish: Input sanitization (kiritilgan belgilarni tozalash) va exec() kabi xavfli funksiyalarga foydalanuvchi malumotlarini to'g'ridan - to'g'ri uzatmaslik.

Qisqa xulosa:

CSRF — foydalanuvchi brauzerini va uning sessiyasini aldash, Injection esa — server va ma me'lumotlar bazasiga o'z kodingni majburlab bajartirish.
'''


# ============================================================================== #

'''

python.org ===> documentation orqali install 
terminal brew orqali install 

warp terminal ==> oddiy terminal bn bir xil ishlaydi va AI integratsiya bolgan , ancha qulay

dasturlash tillarining kodni protsessor tushunadigan ko'rinishga keltirish (bajarish) usuli bo'yicha ikkita asosiy turga bo'linadi: Compiled va Interpreted tillar.
1. COMPILED LANGUAGES (Kompilyatsiya qilinadigan tillar)  
Misollar: C, Java, Go, Rust.   
Qanday ishlaydi: Dasturchi yozgan barcha manba kodi (Source Code) maxsus dastur — Compiler orqali bir vaqtning o'zida to'liq mashina kodiga (01000111...) o'giriladi.Xususiyati: Ishga tushirishdan oldin barcha kod kompyuter tiliga tarjima bo'lib tayyor turadi, shu sababli juda tez ishlaydi.
2. INTERPRETED LANGUAGES (Interpretatsiya qilinadigan tillar)
Misollar: Python, JavaScript (NodeJS), PHP.
Qanday ishlaydi: Kod to'g'ridan - to'g'ri mashina kodiga o'girilmaydi.
CPython (Python interfeysi) dastlab kodni oraliq holatga — ByteCode ga o'tkazadi.ByteCode esa interpretator orqali qatorma-qator (bitta-bitta) o'qilib, mashina kodiga aylantiriladi va bajariladi.
Xususiyati: Kodni alohida kompilyatsiya qilish shart emas (ishlatish oson va moslashuvchan), lekin har safar qatorma-qator tarjima qilingani uchun kompiyatsiyalanuvchi tillarga nisbatan sekinroq ishlaydi.
Asosiy farq (Qisqa xulosa):Compiled: Kod oldindan to'liq tarjima qilib olinadi Protsessor darhol bajaradi (Tez).
Interpreted: Kod oraliq ByteCodega o'tib, keyin real vaqt rejimida qatorma-qator tarjima qilinadi (Moslashuvchan).
'''

# ============================================================================== #


'''

PEP nima? Python’ning rasmiy standartlari, qoidalari va yangiliklar taklif qilinadigan hujjat.
PEP 8 — Kod yozish uslubi va toza format qoidalari (Style Guide).
PEP 20 — Python falsafasi ("The Zen of Python").
PEP 484 — Type Hints (o'zgaruvchilar turini ko'rsatish).

GitHub — Jamoat va Open-Source Makoni
Egalik qiluvchi: Microsoft.
Maqsadi: Ochiq manbali (Open-Source) loyihalar, shaxsiy portfolio va dasturchilar hamjamiyati.
Kod birlashtirish: Pull Request (PR) deb ataladi.
CI/CD (Avtomatlashtirish): GitHub Actions orqali sozlanadi (juda oson va qulay).
Kimlar uchun: Shaxsiy loyihalar, frilanserlar, portfolio yig'uvchilar hamda ochiq kodli loyihalar yaratuvchilar uchun ideal.

GitLab — Kompaniya va DevOps Tizimi
Egalik qiluvchi: GitLab Inc. (Mustaqil).
Maqsadi: Kompaniya loyihalari, bitta joyning o'zida barcha DevOps jarayonlarini boshqarish.
Kod birlashtirish: Merge Request (MR) deb ataladi.
CI/CD (Avtomatlashtirish): Built-in CI/CD (tizimning o'ziga chuqur integratsiya qilingan va juda mukammal).
Self-Hosting: O'zingizning shaxsiy/kompaniya serveringizga tekinga to'liq o'rnatib olish imkoniyati yuqori.
Kimlar uchun: Yirik kompaniyalar, IT-jamoalar va murakkab deployment jarayonlariga ega loyihalar uchun mo'ljallangan.

Qisqa Eslab Qolish Qoidasi:

GitHub — Dasturchilar ijtimoiy tarmoq kabi foydalanadigan, portfolio va ochiq loyihalar joyi.
GitLab — Kompaniyalarda loyihani yaratishdan to serverga joylashgacha (DevOps) ishlatiladigan yopiq platforma.
'''

# ============================================================================== #

'''

Pythonda import ishlatilishining 3 ta asosiy va eng muhim sababi bor:

1. Kompyuter xotirasini (RAM) va tezlikni tejang
Python o'zida yuzlab tayyor imkoniyatlarga ega. Agar Python ishga tushishi bilan matematika, grafikalar, ma'lumotlar bazasi va suniy intellekt uchun kerakli barcha vositalarni birdaniga xotiraga yuklab olganida:
Dastur juda sekin ishga tushgan bo'lardi.
Kompyuter RAM xotirasi befoyda to'lib ketardi.
Shuning uchun Python faqat eng ko'p ishlatiladigan vositalarni (print(), len(), sum()) xotirada tayyor ushlaydi, qolganlarini esa kerak bo'lganda import orqali chaqirib olish uchun alohida modullarda saqlaydi.

2. Nomlar to'qnashuvining (Name Collision) oldini olish
Har xil kutubxonalarda bir xil nomli funksiyalar bo'lishi mumkin.
Masalan, standart Pythonda ham sqrt funksiyasi va math modulida ham math.sqrt() bor. Agar hammasi avtomatik yuklanganida, qaysi biri ishlayotganini ajratish qiyin bo'lar edi. import math qilganingizda, Python uning math moduliga tegishli ekanligini aniq ajratib oladi (math.sqrt(16)).

3. Kodni tartibli va modulli ushlash
Koddagi import math yoki import array degan yozuvni ko'rgan boshqa dasturchi darhol ushbu faylda matematik hisob-kitoblar yoki xotira bilan past darajadagi amallar bajarilishini tushunib oladi.

Daftarga qayd qilish uchun qisqa xulosa:
Import qilish — bu dastur tezroq ishlashi va RAM xotirasini tejash uchun kerakli instrumentlar qutisini (math, array) faqat zarur bo'lganda javondan olib ishlatishdir.
'''

# ============================================================================== #


# ============================================================================== #


# ============================================================================== #


# ============================================================================== #


# ============================================================================== #
