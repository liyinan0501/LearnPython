#
# Todo 包
# 将有联系的模块组织在一起并放到同一文件夹下，这个文件夹有个名字为__init__.py文件，那这个文件夹就称之为包。

# 导入自定义包
# 方法1
# import my_package.my_module1

# my_package.my_module1.info_print1()
# 1
# This is my_module1!!

# 方法2
# 设置my_package文件夹中的__init__.py 文件里的 __all__ 列表，添加的是允许导入的模块。
# 虽然 * 代表导入所有，但是也需要设置__init__.py 文件里的 __all__ 列表。
from my_package import *

my_module1.info_print1()
# 1
# This is my_module1!!

# my_module2.info_print2()
# name 'my_module2' is not defined
