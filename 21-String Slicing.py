"""
TODO String Slicing
"""
str1 = "012345678"
print(str1)
print(str1[2])  # 2

# * str[开始位置index : 结束位置index : 步长]
#! 不包括结束位置，默认步长为1。
print(str1[0:5])  # 01234
print(str1[:5])  # 01234 -- 开始不写，默认从0开始选取。
print(str1[2:])  # 2345678 -- 结束不写，默认选取到最后。
print(str1[:])  # 012345678 -- 开始结束都不写，默认选取所有。
print(str1[0:8:2])  # 0246

# 负数测试
print(str1[::-1])  # 876543210 -- 如果步长为负数，表示倒序选取。
print(str1[::-2])  # 86420
print(str1[-4:-1])  # 567
print(str1[-4:-1:1])  # 567
print(str1[-4:-1:-1])  # 不能选取数据，从-4开始到-1结束，选取方向为从做到右，但是-1步长：从右向左选取。
#! 如果选取方向（下标开始到结束的方向）和 步长的方向冲突，则无法选取数据。
print(str1[-1:-4:-1])  # 876
print(str1[0:3:-1])  # 选不出
