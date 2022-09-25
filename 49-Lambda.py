# lambda 参数 : 表达式
# lambda 表达式的参数可有可无，函数的参数在lambda表达式中完全使用。
# lambda 表达式能接受任何数量的参数，但只能返回一个表达式。


# def fn1():
#     return 100


# result = fn1()
# print(fn1())  # 100

# * 无参数
fn2 = lambda: 100
print(fn2())  # 100

# * 多参数
fn3 = lambda a, b: a + b
print(fn3(3, 4))  # 7

# * 默认参数
fn4 = lambda a, b, c=100: a + b + c
print(fn4(100, 200))  # 400
print(fn4(100, 200, 200))  # 500

# * 可变参数
# 返回元祖
fn5 = lambda *args: args * 2
print(fn5(2, 4, 6, 8))  # (2, 4, 6, 8, 2, 4, 6, 8)

# * 可变参数
# 返回dict
fn6 = lambda **kwargs: kwargs
print(fn6(name="python", age=20))  # {'name': 'python', 'age': 20}

# * 判断
# 三元表达式
fn7 = lambda a, b: a if a > b else b
print(fn7(8000, 9000))  # 9000
