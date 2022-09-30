# 在类里面书写函数 - 静态方法
# Todo 静态方法
#
# 需要用装饰器@staticmethod来表示其类方法
# 不需要床底类，也不需要传递，也不需要传递实例对象.(形参没有self/cls)
# 静态方法能够通过实例对象和类对象去访问。

# 使用场景：
# 当方法中几不需要使用实例对象（实例对象，实例属性），也不需要使用类对象时（类属性，类方法，创建实例等），定义静态方法。
# 减少不必要内存占用和性能消耗


class Dog(object):
    @staticmethod
    def info_print():
        print("This is a static method.")


w = Dog()
w.info_print()  # This is a static method.
Dog.info_print()  # This is a static method.
