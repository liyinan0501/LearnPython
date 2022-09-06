"""
TODO List Traversal
"""

list = ["Tom", "Lily", "Rose"]

i = 0
while i < len(list):
    print(list[i])
    i += 1

# 遍历时候，优选for循环。
for item in list:
    print(item)

list1 = [["小明", "小红", "小绿"], ["Tom", "Lily", "Rose"], ["张三", "李四", "王五"]]

for j in list1:
    x = 0
    while x < len(j):
        print(j[x])
        x += 1
