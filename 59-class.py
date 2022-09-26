class Washer:
    def wash(self):
        print("WashWash")
        # self指的是调用该函数的对象。
        print(self)  # 同一内存地址，调用此函数的对象地址。

    def info(self):
        print(f"The attribute from class inside, weight: {self.weight}")


haier = Washer()
haier.wash()
print(haier)  # 同一内存地址，调用此函数的对象地址。

haier1 = Washer()
haier1.wash()
print(haier1)

haier1.weight = 30
print(haier1.weight)  # 30
print(haier1.info())  # The attribute from class inside, weight: 30
