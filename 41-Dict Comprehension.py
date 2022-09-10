"""
TODO Dict Comprehension
"""
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}

list1 = ["name", "age", "gender"]
list2 = ["Tom", 20, "man"]
dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)  # {'name': 'Tom', 'age': 20, 'gender': 'man'}
#! 如果两个list 长度不一样 会报错
#! 1. 如果两个列表数据个数相同，len统计任何一个列表长度都可以。
#! 2. 如果两个列表数据个数不同，len统计数据多的列表数据个数报错，len统计数据少的列表数据个数不报错。

counts = {"MBP": 268, "HP": 125, "DELL": 201, "Lenovo": 199, "Acer": 99}
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)  # {'MBP': 268, 'DELL': 201}
