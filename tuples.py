'''Tuple
1.what is the tuple : typle vs list
2. unpacking arguments
3. zip
'''

print("==== what is the tuple : typle vs list ====")
# java/php/node.js arary ====> python list

# literal
numbers = [3, 7, 9, 20, 17]
# constructor
letters = list("hello world")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)


# tuple ==> ozgarishlar ketma ketligi himoyalanishi kerak yani hech qanaqasiga list tartibi va royhatni ozgartrib bolmaydi

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"


print("==== unpacking arguments ====")
# shunday qilib yozish mumkin lekin iloji boricha qavslar bn yozish kkk
people = "andrew", "john"
animals = "dog"


groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)


# *args > tuple
def calculate(*args):
    print("*args>", args)
    total = 1
    for x in args:
        total *= x
        print(f"the total value: {total}")
        return total


# call
calculate(1, 7, 2, 3)
print("------")
calculate(0, 20, 13)
print("------")
calculate(2, 3)
print("------")


print("------------")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"hi, i am {kwargs["name"]} and i am {kwargs["age"]} years old!")


# call
introduce(name="Steve", age=24)
introduce(name="Shawn", age=30, single=True)


print("------------")


def greeting(*args, **kwargs):
    print("*args", args)
    print("**kwargs >", kwargs)


# call
greeting("hi", True, 100, name="John", age=22)


print("======  ZIP ======")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped", zipped)
result = list(zipped)
print(f"the result: {result}")
