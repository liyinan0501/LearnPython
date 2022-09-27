#
# Todo 子类调用父类的同名方法和属性
#


class Master(object):
    def __init__(self) -> None:
        self.kongfu = "Master Skill"

    def make_cake(self):
        print(f"{self.kongfu}-Master")


class School(object):
    def __init__(self) -> None:
        self.kongfu = "School Skill"

    def make_cake(self):
        print(f"{self.kongfu}-School")


class Prentice(School, Master):
    def __init__(self) -> None:
        self.kongfu = "Prentice Skill"

    def make_cake(self):
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己的初始化。
        self.__init__()
        print(f"{self.kongfu}-Prentice")

    def master_make_cake(self):
        # 调用父类方法，但是为保证调用到的也是父类属性，必须在调用方法前调用父类的初始化。
        Master.__init__(self)
        Master.make_cake(self)

    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)


a = Prentice()

a.make_cake()  # Prentice Skill-Prentice
a.master_make_cake()  # Master Skill-Master
a.school_make_cake()  # School Skill-School
