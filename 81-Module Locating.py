#
# Todo 模块定位顺序
#

# 当导入一个模块，Python解析器对模块位置的搜索顺序是：
# 1. 当前目录
# 2. 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。(PYTHONPATH是安装过程决定的默认目录)
# 3. 如果都找不到，Python会察看默认路径，UNIX下是 /user/local/lib/python/

# 注意事项
# 自己的文件名不要和已有模块名重复。
# 使用 (from 模块名 import 功能) 的时候，如果功能名字重复，调用到的是最后定义或最后导入的功能。

# 拓展
# (import 模块名) 不用担心功能名重复问题
