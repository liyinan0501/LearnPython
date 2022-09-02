"""
TODO Covert DataType
"""
age = input("Your age:")
print(f"{age}")  # 33
print(type(age))  # <class 'str'>

# * 0. int(x [,base]) 将数据转换成整数
age = int(age)
print(f"{age}")  # 33
print(type(age))  # <class 'int'>

num = int("111", base=2)  # 指定字符为2进制的数据，将其转换为十进制
print(f"{num}")  # 7
print(type(num))  # <class 'int'>

# * 1. float() 将数据转换成浮点型
num1 = 1
str1 = "10"
print(type(float(num1)))  # <class 'float'>
print(float(num1))  # 1.0
print(type(float(str1)))  # <class 'float'>
print(float(str1))  # 10.0

# * 2. str() 将数据转换成字符串型
print(type(str(num1)))  # <class 'str'>

# * 3. tuple() 将序列转成元祖
list1 = [10, 20, 30]
print(tuple(list1))  # (10, 20, 30)

# * 4. list() 将元祖转成序列
tuple1 = (40, 50, 60)
print(list(tuple1))  # [40, 50, 60]

# * 5. eval() 计算在字符串中有效的python表达式，并返回一个对象。
# 把字符串中的数据转换成原本的数据类型。
str2 = "1"
str3 = "1.1"
str4 = "(100, 200, 300)"
str5 = "[400, 500, 600]"
print(type(eval(str2)))  # <class 'int'>
print(type(eval(str3)))  # <class 'float'>
print(type(eval(str4)))  # <class 'tuple'>
print(type(eval(str5)))  # <class 'list'>
