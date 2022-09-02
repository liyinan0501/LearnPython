"""
TODO Logical Operator
"""
# * AND
# 只要一个字为0，结果为0。
print(1 and 0)  # 0
print(0 and 3)  # 0
# 非零数字下，结果为最后一个非零数字。
print(1 and 2)  # 2
print(2 and 1)  # 1

# * OR
# 只有所有值为0，结果为了0
print(0 or 0)  # 0
print(0 or 1)  # 1
print(1 or 0)  # 1
# 非零数字下，结果为第一个非零数字。
print(5 or 3)  # 5
print(3 or 5)  # 3
