#
# Todo 高阶函数
# 定义：把函数当做参数传入一个函数中。
import functools


def sum_num(a, b, f):
    return f(a) + f(b)


result1 = sum_num(-1, 2, abs)
print(result1)  # 3

result2 = sum_num(2.1, 1.8, round)
print(result2)  # 4

# * map
list1 = [1, 2, 3, 4, 5]
# map(function, list)
result3 = map(lambda x: x**2, list1)
print(result3)  # <map object at 0x10ff2feb0>
print(list(result3))  # [1, 4, 9, 16, 25] list()数据转换成列表

# * reduce
# 作用: 功能函数计算的结果和序列的下一个数据做累计计算
result4 = functools.reduce(lambda a, b: a + b, list1)
print(result4)

# * filter
# 用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。然后需要用list转成序列。
result5 = filter(lambda x: x % 2 == 0, list1)
print(result5)  # <filter object at 0x10e2e75b0>
print(list(result5))  # [2, 4]
