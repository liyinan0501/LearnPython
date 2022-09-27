#
# Todo 私有权限
# 某些属性和方法不想继承给子类


class Prentice(object):
    def __init__(self) -> None:
        self.kongfu = "Prentice Skill"
        # * 定义私有属性
        self.__money = 2000000

    # * 定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    # * 获取私有属性值
    def get_money(self):
        return self.__money

    # * 修改私有属性值
    def set_money(self):
        self.__money = 500

    def make_cake(self):
        self.__init__()
        print(f"{self.kongfu}-Prentice")


class Tusun(Prentice):
    pass


a = Tusun()
# a.info_print()  # 报错无法访问私有属性或私有方法

print(a.get_money())  # 2000000
a.set_money()
print(a.get_money())  # 500
