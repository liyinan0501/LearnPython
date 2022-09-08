"""
TODO Dict - Find
"""

dict1 = {"name": "Tom", "age": 20, "gender": "male"}

# * 查找
# 指定 key 查找
print(dict1["name"])  # Tom

# .get()
print(dict1.get("name"))  # Tom
print(dict1.get("id", 110))  # 110
print(dict1.get("id"))  # None
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'male'}

# .keys()
# 查找dict里面所有的键，返回个可遍历的对象。
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])

for key in dict1.keys():
    print(key)  # name age gender

# .values()
# 查找dict里面所有的值，返回个可遍历的对象。
print(dict1.values())  # dict_values(['Tom', 20, 'male'])

for value in dict1.values():
    print(value)  # Tom 20 male

# .items()
# 查找dict里面所有的键值对，返回个可遍历的对象，里面的数据是元祖，元祖数据1是字典key，元祖数据2是字典key对应的值
print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', 'male')])

for key, value in dict1.items():
    print(f"{key} -- {value}")  # name -- Tom age -- 20 gender -- male

for item in dict1.items():  # 输出元祖
    print(item)  # ('name', 'Tom') ('age', 20) ('gender', 'male')
