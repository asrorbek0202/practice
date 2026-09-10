# Dunder  __builtins__ , __init__
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

print(dir(__builtins__))  # royhatini korsatib beradi funksiyalarni
