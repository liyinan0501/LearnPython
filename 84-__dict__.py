class A(object):
    a = 0

    def __init__(self) -> None:
        self.b = 1


aa = A()
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)

# 返回市里属性和值组成字典
print(aa.__dict__)
