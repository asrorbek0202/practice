# Dunder  __builtins__ , __init__

'''
Dunder nima? Obyektning Pythonda o'zini tutishini va tayyor operatorlar bilan ishlashini belgilaydigan sehrli metodlar.

__init__ — Class'dan yangi obyekt olinganda boshlang'ich qiymat berish uchun avtomatik ishlaydi (Constructor).
__builtins__ — Pythondagi barcha tayyor funksiya (print, len) va tiplarni saqlaydigan ichki modul.
__str__ — Obyektni print() qilganda ekranga qanday matn chiqishini belgilaydi.
__len__ — Obyektga len() qo'llanganda necha qiymat qaytarishini belgilaydi.

'''


message = "PYTHON: Everthing is object"
print(message)

result = type(message)
print("result:", result)

'''
In Python , there are builtin tools:
1. TYPES > iint, float, str, list, dict, tuple, set, bool
2. FUNCTIONS > print(), input(), len(), type(), range(), sum(), min(), max()
3. CONSTANTS > True, False, None
'''

# Python’ni o'rnatilgandayoq, hech qanday qo'shimcha kutubxona yuklamasdan to'g'ridan - to'g'ri ishlatishingiz mumkin bo'lgan poydevor (built-in) vositalar xarita.
print(dir(__builtins__))  # royhatini korsatib beradi funksiyalarni
