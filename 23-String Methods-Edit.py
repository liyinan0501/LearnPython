"""
TODO String Methods - Edit
"""
str = "hello world and itcast and itheima and Python"

# * 修改
# .replace (旧子串, 新子串, 替换次数) -- 替换
#! 返回新的修改后的字符串，不修改原字符串。->间接说明字符串是 不可变类型 数据。
# 替换次数不写，为全部替换。
newStr = str.replace("and", "he")
print(newStr)  # hello world he itcast he itheima he Python
print(str)  # hello world and itcast and itheima and Python
newStr1 = str.replace("and", "he", 1)
print(newStr1)  # hello world he itcast and itheima and Python
# 如果替换次数超出子串出现的次数，表示替换所有这个子串。

# .splice(分割字符,num) -- 分割，返回一个列表。
# num 表示分割字符出现的次数，即将来返回数据个数为num+1个。
list1 = str.split("and")
print(list1)  # ['hello world ', ' itcast ', ' itheima ', ' Python']
# list2 = str.split("and", 1) # ['hello world ', ' itcast and itheima and Python']
list2 = str.split("and", 2)  # ['hello world ', ' itcast ', ' itheima and Python']
print(list2)

# 字符或子串.join(多字符串组成的序列) -- 合并列表里所有的的数据，为一个大字符串。
myList = ["aa", "bb", "cc"]
newList = "...".join(myList)
print(newList)  # aa...bb...cc
newList1 = "".join(myList)
print(newList1)  # aabbcc
