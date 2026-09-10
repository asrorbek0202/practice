print("================================")
# in JAVA , variable is a name storage location for data
# in Python , variable is a name that refers to an object in memory

count = 100
count_type = type(count)
print(f" the count: {count}, and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state property
print(f"result1: {result1}, result2: {result2}")


print("============= string ===================")
# METHODS : upper(), lower(), title(), capitalize(), swapcase(), replace(), isupper(), islower(), istitle(), isspace()

course = "AI Python FullStack"
result = type(course)
print(f"the result(1) : {result}")

result = course.title()
print(f"the result(2) : {result}")

result = course.upper()
print(f"the result(3) : {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result(4) : {result}")
