"""
TODO Tuple - Edit
"""

# 元祖原则上不支持修改，如下可以修改。

t1 = ("aa", "bb", "cc", "bb")
# t1[0] = "11"  # TypeError

t2 = ("aa", "bb", ["cc", "dd"])
print(t2[2])  # ['cc', 'dd']
print(t2[2][0])  # cc
# 此情况下可以修改
t2[2][0] = "Tom"
print(t2)  # ('aa', 'bb', ['Tom', 'dd'])
