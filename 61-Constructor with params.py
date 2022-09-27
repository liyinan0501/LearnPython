class Washer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 没有配置__str__，打印实例会输出内存地址。
    def __str__(self):
        return "This is Haier"

    def __del__(self):
        print("object is deleted")

    def print_info(self):
        print(f"Washer width: {self.width}")
        print(f"Washer heigth: {self.height}")


haier1 = Washer(10, 20)
haier1.print_info()
# Washer width: 10
# Washer heigth: 20

haier2 = Washer(300, 400)
haier2.print_info()
# Washer width: 300
# Washer heigth: 400

# 没有配置__str__，打印实例会输出内存地址。
print(haier1)  # This is Haier
print(haier2)  # This is Haier

haier3 = Washer(500, 600)
# 即使不调用del 也会调用__del__ 方法，因为内存会自动回收。
del haier3


# haier3 = Washer() 报错
