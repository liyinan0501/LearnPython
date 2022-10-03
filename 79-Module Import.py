#
# Todo 模块
#
# 模块是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。
# 模块能定义函数、类和变量，模块里也能包含可执行代码。
# library > package > module

# 三种基本导入模块方式:
# 1. import 模块名
# 2. from 模块名 import 功能名
# 3. from 模块名 import *

# 两种别名导入模块方式：
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# 调用功能：
# 模块名.功能名()

# 1. import 模块名
# import math
# print(int(math.sqrt(9)))  # 3

# 2. from 模块名 import 功能名
# from math import sqrt
# print(int(sqrt(16)))  # 4

# 3. from 模块名 import *
# from math import *
# print(int(sqrt(36)))  # 6

# import 模块名 as 别名
# import time as tt
# tt.sleep(2)
# print("Time module1!")

# from 模块名 import 功能名 as 别名
# from time import sleep as sl
# sl(2)
# print("Time module2!")
