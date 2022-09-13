"""
TODO Function Params
"""


def userInfo(name, age, gender):
    print(f"Your Info are {name}, {age},{gender}")


# * 位置参数：调用函数时根据函数定义的参数位置来传递参数。
userInfo("Tom", 20, "male")  # Your Info are Tom, 20,male

# * 关键字参数：通过“键=值” 形式加以指定，同时请出来参数顺序要求。
userInfo("Rose", age=20, gender="female")  # Your Info are Rose, 20,female
userInfo("Jack", gender="female", age=20)  # Your Info are Jack, 20,female
# 如果有位置参数像Rose和Jack，位置参数必须在关键字参数前面，否则会报错。

# * 默认参数
# 如果不传，默认使用默认参数。
def userInfo1(name, age, gender="male"):
    print(f"Your Info are {name}, {age},{gender}")


userInfo1("John", 22)  # Your Info are John, 22,male
userInfo1("Lily", 12, "female")  # Your Info are Lily, 12,female

# * 可变参数
# 1. 包裹位置传递
def userInfo2(*args):
    print(args)


userInfo2("Joe")  # ('Joe',) 返回元祖
userInfo2("Joe", 55)  # ('Joe', 55)

# 2. 包裹关键字传递
def userInfo3(**kwargs):
    print(kwargs)


userInfo3(name="Josef")  # {'name': 'Josef'}
userInfo3(
    name="Josef", age=17, id=2013
)  # {'name': 'Josef', 'age': 17, 'id': 2013} 返回字典
