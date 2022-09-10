"""
TODO List Comprehension
"""
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = []
for i in range(10):
    list2.append(i)
    i += 1
print(list2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list3 = []
# 读与写都从for开始。
list3 = [i for i in range(10)]
print(list3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# if：
list4 = []
list4 = [i for i in range(0, 10, 2)]
print(list4)  # [0, 2, 4, 6, 8]

list5 = []
list5 = [i for i in range(0, 10, 2) if i % 2 == 0]
print(list5)  # [0, 2, 4, 6, 8]

# 多if： 就是 if 的嵌套
list6 = []
list6 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list6)  # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
