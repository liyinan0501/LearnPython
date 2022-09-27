#
# Todo 多继承
# 一个子类基层多个父类


class Master(object):
    def __init__(self) -> None:
        self.kongfu = "Special Skill"

    def show_skill(self):
        print(f"{self.kongfu}XXXXXXXXXX")


class School(object):
    def __init__(self) -> None:
        self.kongfu = "School Skill"

    def show_skill(self):
        print(f"{self.kongfu}SSSSSSSSSS")


# 同名属性和方法，默认使用位于第一个位置的父类 : School
class Prentice(School, Master):
    pass


a = Prentice()
print(a.kongfu)
a.show_skill()

# * 查看继承关系
print(Prentice.__mro__)
