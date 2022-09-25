students = [
    {"name": "Tom", "age": 20},
    {"name": "Rose", "age": 19},
    {"name": "Jack", "age": 22},
]

students.sort(key=lambda x: x["name"])
print(students)
# [{'name': 'Jack', 'age': 22}, {'name': 'Rose', 'age': 19}, {'name': 'Tom', 'age': 20}]
students.sort(key=lambda x: x["name"], reverse=True)
print(students)
# [{'name': 'Tom', 'age': 20}, {'name': 'Rose', 'age': 19}, {'name': 'Jack', 'age': 22}]
students.sort(key=lambda x: x["age"])
print(students)
# [{'name': 'Rose', 'age': 19}, {'name': 'Tom', 'age': 20}, {'name': 'Jack', 'age': 22}]
