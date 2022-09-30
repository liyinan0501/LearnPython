# 在类里面书写函数 - 类方法
# Todo 类方法
#
# 需要用装饰器@classmethod来表示其类方法
# 对于类方法，第一个参数必须是类，一般以cls作为第一个参数。

# 使用场景：
# 当需要操作私有类属性和类属性的时候就需要使用类方法。


class Dog(object):
    __tooth = 10

    @classmethod
    # cls 指的是 Dog 类
    def get_tooth(cls):
        return cls.__tooth


w = Dog()
result = w.get_tooth()
print(result)  # 10
