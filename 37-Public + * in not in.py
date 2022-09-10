str1 = "aa"
str2 = "bb"

list1 = [1, 2]
list2 = [10, 20]

tuple1 = (1, 2)
tuple2 = (10, 20)

set1 = {1, 2}
set2 = {10, 20}

dict1 = {"name": "Tom"}
dict2 = {"age": 32}

# 合并 + : string, list, tuple
print(str1 + str2)  # aabb
print(list1 + list2)  # [1, 2, 10, 20]
print(tuple1 + tuple2)  # (1, 2, 10, 20)
# print(set1 + set2)  # 报错
# print(dict1 + dict2) # 报错

# 复制 * : string, list, tuple
print(str1 * 5)  # aaaaaaaaaa
print("-" * 5)  # -----
print(list1 * 5)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(tuple1 * 5)  # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# print(set1 * 5) # 报错
# print(dict1 * 5)  # 报错

# 是否存在 in : string, list, tuple, dict, set
# 是否存在 not in : string, list, tuple, dict, set
print("a" in str1)  # True
print("a" not in str1)  # False
print(2 in list1)  # True
print(2 not in list1)  # False
print(1 in tuple1)  # True
print(1 not in tuple1)  # False
print(20 in set2)  # True
print(20 not in set2)  # False
print("name" in dict1)  # True
print("Tom" in dict1)  # False
print("Tom" in dict1.values())  # True
print("name" in dict1.keys())  # True
