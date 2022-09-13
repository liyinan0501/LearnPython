"""
TODO Function
"""
# 先定义后使用。


from cgi import test


def add(a, b):
    result = a + b
    return result


total = add(10, 20)
print(total)

# * help() 查看函数的说明文档
# 定义函数说明文档
def sub(a, b):
    """subtraction function"""
    result = a - b
    return result


# 使用
# help(sub)

# * 函数说明文档的高级使用
def sub1(a, b):
    """
    subtraction function

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a - b


# help(sub1)

# * 修改全局变量
a = 100
print(a)  # 100


def testA():
    print(a)  # 100


def testB():
    a = 200  # 如果直接修改 a=200，此时的 a 是局部变量，是局部变量修改。
    print(a)  # 200


def testC():
    global a  # 指明为全局变量
    a = 200  # 此时的 a=200，是全局变量修改。
    print(a)


testA()  # 100
testB()  # 200
print(f"Global a is {a}")  # Global a is 100
testB()  # 200

testC()  # 200
print(f"Global a is {a}")  # Global a is 200

# 一个函数多个返回值
def return_num():
    return 1, 2


final = return_num()
print(final)  # (1, 2) 返回元祖
