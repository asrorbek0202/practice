'''COMPREHENSION
what is comprehension & list comp
set and dictionary comp.
'''

print("==== what is comprehension & list comprehension ====")
# comprehension acts like spread operator

'''COMPREHENSION general syntax:
a) *iterable
b) <expression> for item in iterable
c) <expression> for item in iterable <condition>
'''

# list comprehension
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-------------")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 27)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

print("------------")
cars = [
    ("ferrari", 78)
    ("tayota", 87)
    ("audi", 116)
    ("bmw", 109)
    ("pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("====  set and dictionary comprehension  ====")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b versiion
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # c versiion
print("dict_people2:", dict_people2)
