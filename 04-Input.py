"""
TODO Input
"""
# 执行input，等待用户输入，输入完成后才继续向下执行。
# input 会把接收到用户输入数据统一当做字符串处理。

name = input("Your name:")
print(f"{name}")
print(type(name))  # <class 'str'>
