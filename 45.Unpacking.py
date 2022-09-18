"""
TODO Unpacking
"""

# unpacking a tuple
def returnNum():
    return 100, 200


num1, num2 = returnNum()
print(num1)  # 100
print(num2)  # 200


# unpacking a dict
dict1 = {"name": "Tom", "age": 12}
a, b = dict1
print(a)  # name
print(b)  # age
print(dict1[a])  # Tom
print(dict1[b])  # 12
