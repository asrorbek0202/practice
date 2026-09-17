print("====== iterable objects and RANGE ======")
# Iterable object — bu elementlarini bittalab, ketma-ket ko'rib chiqish (aylanib o'tish) mumkin bo'lgan obyekt.
# iterable objects > list, tuple, set, dict, str, range,string, bytes, bytearray, memoryview

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"letter: {letter}")
for ele in range_obj:
    print(f"ele: {ele}")

    print("==== Dictionary iterable object ======")
    # Dictionaries are JSON objects
    '''
    Dictionary vazifasi: Ma'lumotlarni tartibli Key: Value (Kalit: Qiymat) ko'rinishida saqlash va ularga tezkor murojaat qilish.
Nega asosiy mavzu? Barcha zamonaviy Web API-lar, Backend serverlar va ma'lumotlar bazalari (JSON) aynan shu tuzilmada ishlaydi. Python'da Dictionaryni mukammal bilish — real loyihalarda va API'lar bilan ishlashda eng poydevor ko'nikmadir.
    
    '''

person = {"name": "Steve", "age": 24, "single": True}
print(f"person: {person}")

person_obj = dict(name="Steve", age=24, single=True)

print(f"person_obj: {person_obj}")
name = person_obj["name"]
print("name", name)


# method: get()
# name = person_obj["name"]  # key
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 1000)  # default value
print(f"name: {name}, hobby: {hobby}, balance: {balance}")


del person_obj["single"]
for key in person_obj:
    print(f"key: {key} > value: {person_obj.get(key)}")
