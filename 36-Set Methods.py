"""
TODO Set Methods
"""

# * 增加数据
# add() 增加单一数据，有去重功能。
s1 = {10, 20}
s1.add(100)
s1.add(100)
print(s1)  # {100, 10, 20}

# s1.add([30, 40, 50]) 报错
# print(s1)

# update() 增加序列
s1.update([10, 30, 40, 50])
print(s1)  # {100, 40, 10, 50, 20, 30}

# s1.update(100) 报错
# print(s1)

# * 删除数据
# remove() 删除指定数据，如数据不存在报错。
s1.remove(10)
print(s1)  # {100, 40, 50, 20, 30}
# s1.remove(10) 报错

# discard() 删除指定数据，如数据不存在不会报错。
s1.discard(10)  # 不报错
s1.discard(100)
print(s1)  # {40, 50, 20, 30}

# pop() 随机删除某个数据，并返回删除的数据。
delNum = s1.pop()
print(delNum)  # 40
print(s1)  # {50, 20, 30}

# * 查找数据
s2 = {10, 20, 30, 50}
# in
print(10 in s2)  # True
# not in
print(10 not in s2)  # False
