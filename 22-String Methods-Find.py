"""
TODO String Methods - Find
"""
str = "hello world and itcast and itheima and Python"

# * 三大类：查找、修改和判断。
# * 查找
# .find(子串, 开始位置下标, 结束位置下标) - 查找位置
# .rfind() 从右开始查找
print(str.find("and"))  # 12
print(str.find("and", 15, 30))  # 23
print(str.find("ands"))  # -1 不存在

# .index(子串, 开始位置下标, 结束位置下标) - 查找位置
# .rindex() 从右开始查找
print(str.index("and"))  # 12
print(str.index("and", 15, 30))  # 23
# print(str.index("ands"))  # 不存在的话，会报错。

# .count(子串, 开始位置下标, 结束位置下标) - 统计出现次数
print(str.count("and", 15, 30))  # 1
print(str.count("and"))  # 3
print(str.count("ands"))  # 0
