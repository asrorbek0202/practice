'''
OBJECTS!

1. what is object?
2.iterable objects and RANGE 
3.error handling system
'''


import array   # package/module
import math    # package/module
from math import ceil
print("=== what is object? ===")
# An object has state and method properties.
# In Python, everything is an object.

print(type("Hello World!"))  # str
print(type(100))  # int
print(type(100.0))  # float
print(type(True))  # bool
print(type(array))  # array
print(type(math))  # module

# paradigms > functional programming, object-oriented programming(OOP)
# OOP 4 consepts > encapsulation, abstraction, inheritance, polymorphism

result1 = math.ceil(3.14)  # method
print(f"result1: {result1}")

result2 = ceil(9.89)
print(f"result2: {result2}")
