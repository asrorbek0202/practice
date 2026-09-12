print("====== iterable objects and RANGE ======")
# iterable objects > list, tuple, set, dict, str, range,string, bytes, bytearray, memoryview

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"letter: {letter}")
for ele in range_obj:
    print(f"ele: {ele}")

    print("==== Dictionary iterable object ======")
    # Dictionaries are JSON objects

person = {"name": "Steve", "age": 24, "single": True}
person_obj = dict(name="Steve", age=24, single=True)
print(f"person: {person}")
print(f"person_obj: {person_obj}")

# method: get()
# name = person_obj["name"]  # key
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 1000)  # default value
print(f"name: {name}, hobby: {hobby}, balance: {balance}")


del person_obj["single"]
for key in person_obj:
    print(f"key: {key} > value: {person_obj.get(key)}")
