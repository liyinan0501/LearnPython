"""
TODO List Methods - Find
"""
# 列表可存储多个，而且不同类型的数据。
# 工作中，尽量一个列表储存相同类型的数据，方便操作。

list = ["Tom", "Lily", "Rose"]
print(list[0])  # Tom

# * 1 .index(数据, 开始位置下标, 结束位置下标)
print(list.index("Tom"))  # 0

# * 2 .count() - 统计某个数据在列表中出现的次数
print(list.count("Lily"))  # 1

# * 3 len() - 统计列表的长度
print(len(list))  # 3

# * 4 in: 判断数据是否在列表中
print("Tom" in list)  # True

# * 5 not in: 判断数据是否不在列表中
print("Tom" not in list)  # False
print("Tos" not in list)  # True

name = input("Your name: ")
if name in list:
    print("Your name exists!")
else:
    list.append(name)
    print("Your name is registered")
print(list)
