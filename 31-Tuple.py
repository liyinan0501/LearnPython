"""
TODO Tuple
"""

# 一个元祖可以储存多个不同类型的数据，元祖内的数据是不能修改的，只支持查找。

# 定义多个数据元祖：
t1 = (10, 20, 30)
print(t1)  # (10, 20, 30)
print(type(t1))  # <class 'tuple'>

# 定义单个数据元祖：
t2 = (10,)
print(t2)  # (10,)
print(type(t2))  # <class 'tuple'>

# ! 不要按照如下方法定义单个数据元祖。
# t3 = (10)
# print(t3)  # 10
# print(type(t3))  # <class 'int'>

# t4 = ('aaa')
# print(t3)  # aaa
# print(type(t3))  # <class 'str'>


tuple1 = ("aa", "bb", "cc", "bb")
print(tuple1[0])  # aa
print(tuple1.index("bb"))  # 1
print(tuple1.count("bb"))  # 2
print(len(tuple1))  # 4
