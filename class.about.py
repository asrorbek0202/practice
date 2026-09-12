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
