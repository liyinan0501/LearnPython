class Washer:
    # __init__ 的作用是初始化对象。
    # 定义__init__，添加实例属性。
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f"Washer width: {self.width}")
        print(f"Washer height: {self.height}")


haier = Washer()
haier.print_info()
# Washer width: 500
# Washer height: 800
