#
# Todo 自定义异常
# 将不满足程序逻辑要求的代码，捕获异常，抛出异常类对象。

# 步骤：
# 1. 自定义异常类
# 2. 抛出异常
# 3. 捕获该异常


class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息。
    def __str__(self):
        return (
            f"Your input length is {self.length}, please input at least {self.min_len}"
        )


def main():
    try:
        password = input("Please input password: ")
        if len(password) < 3:
            # 超出异常类创建的对象
            raise ShortInputError(len(password), 3)
    except Exception as result:
        print(result)
    else:
        # 没有异常情况下执行
        print("Password setting succeeds!")


main()
