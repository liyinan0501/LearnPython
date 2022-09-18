"""
TODO Reference
"""
# 在python中，值是靠引用来传递的。

# 不可变数据类型：
a = 1
b = a
print(b)  # 1
print(id(a))  # 4416372976
print(id(b))  # 4416372976
a = 2
print(b)  # 1
print(id(a))  # 4358684944 新地址
print(id(b))  # 4416372976

# 可变数据类型
aa = [10, 20]
bb = aa
print(id(aa))  # 4565284032
print(id(bb))  # 4565284032
aa.append(30)
print(aa)  # [10, 20, 30]
print(bb)  # [10, 20, 30]
print(id(aa))  # 4353910464
print(id(bb))  # 4353910464
