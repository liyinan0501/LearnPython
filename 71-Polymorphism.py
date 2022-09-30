#
# Todo 多态
# 多态最好依赖于继承。
# 调用不同子类创建的实例对象的相同父类方法，也就是调用对象不一样，可以产生不同的结果。
# 实现步骤
# 定义父类，并提供公共方法。
# 定义子类，并重写父类方法。
# 传递子类创建的对象给被调用者，可以看到不同子类执行的不同效果。


class Dog(object):
    def work(self):
        print("woof, woof!")


class ArmyDog(Dog):
    def work(self):
        print("enemy, enemy!")


class DragDog(Dog):
    def work(self):
        print("drag, drag!")


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


dogA = ArmyDog()
dogD = DragDog()
soldier = Person()

soldier.work_with_dog(dogA)  # enemy, enemy!
soldier.work_with_dog(dogD)  # drag, drag!
