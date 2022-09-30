# 类属性
# 记录某项数据，始终保持一致时，则需定义类属性。
# 类属性只能通过类对象修改，不能通过实例对象修改。
# 如果通过实例对象修改数学，表所是创建了一个同名的实例属性。


class Dog(object):
    tooth = 10


x = Dog()
y = Dog()


# Dog.tooth = 22
# print(Dog.tooth)  # 22
# print(x.tooth)  # 22
# print(y.tooth)  # 22

#!修改失败
x.tooth = 888
print(Dog.tooth)  # 10
print(x.tooth)  # 888
print(y.tooth)  # 10
