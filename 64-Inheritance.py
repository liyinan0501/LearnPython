# 所有类默认继承object类，object是顶级类或基类。
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(A):
    pass


result = B()
result.info_print()  # 1
