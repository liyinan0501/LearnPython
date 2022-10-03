#
# Todo __all__
#
# 在被导入的模块中，如果声明__all__，只有__all__ list里的函数才能对外使用。

from my_module2 import *

testA()  # 可以正常打印
# testB()  # name 'testB' is not defined 无法导入
