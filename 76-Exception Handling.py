#
# Todo 异常
# 尝试执行可能发生错误的代码语句，如果发生错误，就不执行，而执行错误语句的替代代码。
# 避免让程序报错，向下推进程序，不影响整个程序的运行。

# 尝试以r模式打开，正常情况下如果文件不存在，会报错，如果报错，则以w方式打开。
# try:
#     f = open("test.txt", "r")
# except:
#     f = open("text.txt", "w")

# * 捕获指定异常
# try 下面通常只放一行代码

# 尝试打印不存在变量
try:
    print(num)
except NameError:
    print("Captured!")  # Captured!

# * 捕获多个置顶异常
# 把多个异常类型的名字，放到except后，并使用元组的方式进行书写。
try:
    print(1 / 0)
except (NameError, ZeroDivisionError):
    print("Capture 1/0!")  # Capture 1/0!

# * 捕获异常描述
# 捕获类型 as 后面的变量result储存捕获的异常信息。
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as result:
    print(result)  # division by zero

# * 捕获所有异常
# Exception 是所有程序异常类的父类。
try:
    print(num1)
except Exception as result:
    print(
        f"Captured all type of error! - {result}"
    )  # Captured all type of error! - name 'num1' is not defined

# * 异常的else
# else 表示的是如果没有异常时候，要执行的代码。
try:
    print(1)  # 1
except Exception as result:
    print(result)
else:
    print("No error founded!")  # No error founded!

# * 异常的 finally
# finally 表示的是无论是否有异常，都要执行的代码，例如关闭文件
try:
    f = open("test.txt", "r")
except Exception as result:
    f = open("test.txt", "w")
else:
    print("No error")
finally:
    print("Here is finally")  # Here is finally
    f.close()
