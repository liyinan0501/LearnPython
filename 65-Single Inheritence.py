#
# Todo 单继承
# 一个子类基层一个父类


class Master(object):
    def __init__(self) -> None:
        self.kongfu = "Special Skill"

    def show_skill(self):
        print(f"{self.kongfu}XXXXXXXXXX")


class Prentice(Master):
    pass


a = Prentice()
print(a.kongfu)  # Special Skill
a.show_skill()  # Special SkillXXXXXXXXXX
