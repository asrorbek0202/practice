'''CLASS

1. what is class in python?
2. ordinary and static properties of class
3. special methods of class
'''

print("==== what is class in python? ====")
# class ==> blueprint of object creation
# structure > state constructor method


class Person:
    # state
    messege = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Steve", 24)
person2 = Person("John", 30)
person3 = Person("Alice", 28)

# ordinary state
print("person1.name", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print(" === ordinary and static properties of class ====")
# static state
new_messeage = Person.messege
print("new_messeage", new_messeage)

# static method
Person.explain()


print("=== special methods of class ====")
# special methods are also called magic methods or dunder methods
# __init__(), __str__(), __repr__(), __len__(), __add__(), __sub__(), __mul__(), __truediv__(), __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__()


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def start_engine(self):
        print(f"the {self.name} started engine !")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"the car.name: {self.name} was produced in {self.year} year!"

    def __call__(self):
        print("object called as a function")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("----")
your_car = Car("Tayota", 2026)
print(your_car)
response = your_car()
print("response", response)
