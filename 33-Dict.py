"""
TODO Dict
"""
# 定义方法
# 键值对方法
from cmath import log


dict1 = {"name": "Tom", "age": 20, "gender": "male"}
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(type(dict1))  # <class 'dict'>

# 定义空 Dict
dict2 = {}
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(type(dict1))  # <class 'dict'>

dict3 = dict()
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}
print(type(dict1))  # <class 'dict'>

# * 新增
dict1["id"] = 110
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'male', 'id': 110}

# * 修改
dict1["name"] = "Rose"
print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': 'male', 'id': 110}

# * 删除
del dict1["gender"]  # 删除指定的键值对
print(dict1)  # {'name': 'Rose', 'age': 20, 'id': 110}

# del dict1  # 删除整个 dict
# print(dict1)  # NameError: name 'dict1' is not defined

# dict1.clear()  # 清空 dict
# print(dict1)  # {}
