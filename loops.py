'''LOOP operators
1. for
2. break/else 
3. while
'''

print("==== for operator ===")
# itereable objects > string, dict, tuple, list , range, map , filter
text = "MIT"
numbers = [10, 29, 7, 23, 1]
car_obj = dict(brand="ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter : {letter}")

print("=========")
for number in numbers:
    print(f"the number : {number}")

print("=========")
for x in range_obj:
    print(f"the element : {x}")


print("=========")
for key in car_obj:
    print(f"the key : {key} ==>value: {car_obj.get(key)}")


print("==== break/else ====")
for x in range(1, 20, 5):
    print(f"the x : {x}")
    if x > 10:
        print("reached break")
        break
    else:
        print("executed successfully")


print("=== while ===")

number = 40
while number > 0:
    number -= 10
    print(f"the number equals {number}")


print("-----------")

count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 41:
        print(f"you found number in {count} steps")
        break
    else:
        print("wrong please try again!")
