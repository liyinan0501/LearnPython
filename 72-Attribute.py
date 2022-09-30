#
# 实例属性
class Student(object):
    def __init__(self, name):
        self.name = name


s = Student("Bob")
s.score = 90
print(s.name)  # Bob

# 类属性
# 记录某项数据，始终保持一致时，则需定义类属性。
# 类属性只能通过类对象修改，不能通过实例对象修改。
# 如果通过实例对象修改数学，表所是创建了一个同名的实例属性。
class Person(object):
    age = 10


print(Person.age)
x = Person()
y = Person()  # 10
print(x.age)  # 10
print(y.age)  # 10
