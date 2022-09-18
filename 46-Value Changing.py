"""
TODO Value Changing
"""
# 方法一：借助第三变量储存数据
# 方法二：
a, b = 1, 2
a, b = b, a
print(a)  # 2
print(b)  # 1
