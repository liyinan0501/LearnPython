#
# Todo super
#


class Master(object):
    def __init__(self) -> None:
        self.kongfu = "Master Skill"

    def make_cake(self):
        print(f"{self.kongfu}-Master")


class School(Master):
    def __init__(self) -> None:
        self.kongfu = "School Skill"

    def make_cake(self):
        print(f"{self.kongfu}-School")

        # * 对应 Prentice 下 method1 - super() 有参数
        # 如果不写如下代码，Prentice的super只会调用School的方法，并不会调用Master的方法。
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # * 对应 Prentice 下 method1 - super() 无参数
        super().__init__()
        super().make_cake()


class Prentice(School):
    def __init__(self) -> None:
        self.kongfu = "Prentice Skill"

    def make_cake(self):
        self.__init__()
        print(f"{self.kongfu}-Prentice")

    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 一次性调用父类所有方法
    def make_old_cake(self):
        # option 1:
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # * option 2: super()
        # method1 - super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # * method2 - super() 无参数
        # 自动查找父类，遵循__mro__的顺序
        super().__init__()
        super().make_cake()


a = Prentice()
a.make_old_cake()
