def testA(a, b):
    print(a + b)


# 测试模块：
# testA(1,1)

# 测试模块替代方案：
# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，子不会执行testA函数调用。
# __name__ 是系统变量。
print(__name__)  # __main__
# 如果直接运行此文件，__name__ 的值是 __main__。
# 如果导入此文件，在别的文件下运行，__name__ 的值当前文件名字，也就是 my_module1。

if __name__ == "__main__":
    testA(1, 1)
