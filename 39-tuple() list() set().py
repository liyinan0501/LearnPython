list1 = [10, 20, 30, 20, 40, 50]
set1 = {100, 300, 200, 500}
tuple1 = ("a", "b", "c", "d", "e")


# tuple() 转换成元元祖
print(tuple(list1))  # (10, 20, 30, 20, 40, 50)
print(tuple(set1))  # (200, 100, 500, 300)

# list() 转换成列表
print(list(set1))  # [200, 100, 500, 300]
print(list(tuple1))  # ['a', 'b', 'c', 'd', 'e']

# set() 转换成集合 有去重功能 没有下标无顺序
print(set(list1))  # {40, 10, 50, 20, 30}
print(set(tuple1))  # {'e', 'd', 'c', 'b', 'a'}
