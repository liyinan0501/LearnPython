# 格式化符号
age = 18
name = 'Tom'
weight = 75.5
stuId = 1
stuId2 = 1000
print('My name is %s' % name) # My name is Tom
print('I am %d years old' % age) # I am 18 years old
print('My weight %.2f' % weight) # My weight 75.50
print('My student ID is %d' % stuId) # My student ID is 1
print('My student ID is %03d' % stuId) # My student ID is 001
print('My student ID is %03d' % stuId2) # My student ID is 1000
# %03d, 表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出。
print('My name is %s, and %d years old.' % (name, age)) # My name is Tom, and 18 years old.

# %s 功能强大
print('My name is %s, and %s years old, and my weight is %s.' % (name, age, weight))
# My name is Tom, and 18 years old, and my weight is 75.5.

# f'{表达式}' - Python 3.6 中新增的格式化语法，该方法更简单易读。
print(f'My name is {name}, and {age} years old.') # My name is Tom, and 18 years old.

# 转义符
# \n：换行。
# \t：制表符，一个tab键（4个空格）的距离。
print('Hello \nWorld')
# Hello 
# World
print('\tHello \nWorld')
# 	Hello 
# World

# print 结束符
print('Something')
print('Something2')
print('Something3', end='\n') # print函数默认有换行符。
print('Something4')
print('Something5', end='\t')
print('Something6')
print('Something7', end='...')
print('Something8')
# Something
# Something2
# Something3
# Something4
# Something5	Something6
# Something7...Something8