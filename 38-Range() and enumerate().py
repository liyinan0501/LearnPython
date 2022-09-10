# len()

# del and del()
# del 删除目标
# del (删除目标)

str1 = "abcdef"
list1 = [10, 20, 30, 40, 50]
print(max(str1))  # f
print(max(list1))  # 50
print(min(str1))  # a
print(min(list1))  # 10

# range(start, end, step) 生成可循环对象
# end 不包含
# step 可省略，默认为1。
for i in range(1, 10, 1):
    print(i)  # 123456789

for i in range(1, 10, 2):
    print(i)  # 13579

for i in range(10):
    print(i)  # 0123456789

# enumerate(可遍历对象, start=0)
# 返回结果实验组，元组的第一锅数据是原迭代对象数据对应的下标，元祖第二个数据是元迭代对象的数据。
list2 = ["a", "b", "c", "d", "e"]
for i in enumerate(list2):
    print(i)  # (0, 'a')(1, 'b')(2, 'c')(3, 'd')(4, 'e')
for i in enumerate(list2, start=1):
    print(i)  # (1, 'b')(2, 'c')(3, 'd')(4, 'e')
