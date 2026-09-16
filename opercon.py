'''OPERATORS & CONDITIONS 
1. Operators
2. Condition
3. Logical Operators
'''

print("======= Operators ======")
#  +, -, >, >=, <, <= , *, /  , //  , % , += , **, is

a = 19
b = 5

print("a > b", a > b)
print("a * b", a * b)
print("a / b", a / b)
print("a + b", a + b)
print("a ** b", a ** b)


result = a // b
left = a % b
print(f"the result: {result} and left : {left}")

print("b**2", b**2)
print("b**3", b**3)


# value jihatdan farq qiladi va reference ham boshqa boshqa
c = dict(name="Steve", age=24)
d = dict(name="Steve", age=24)
e = c

print("c==d", c == d)
print(id(c), id(d))

print("c is d", c is d)
print("c is e", c is e)


print("======= Conditions ======")

x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("=== logical operators ====")

age = 18
persoon = None

if age > 16:
    person = "adult"
else:
    person = "child"

print("person", person)


# Ternary operator

person = "adult" if age > 18 else "minor"
print("person", person)


print("==========================")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("welcome to here , do you want to be a student")
elif is_admin:
    print("please go to this office")
elif is_guest or is_parent:
    print("waiting room is over here")
else:
    print("etc")
