'''FUNCTIONS
(1) DEFINE & CALL
(2) Parametr & Atguments
(3) Keyword & default arguments
(4) Scope
'''
print("=== DEFINE vs CALL =====")
# build in function > print () type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('Steve')
print(" resultl:", result1)

result2 = greeting("Steve")
print("result:", result2)
