"""
TODO List Methods - Delete
"""

list1 = ["Tom", "Lily", "Rose", "Jack", "Frank"]

# * 1 del(列表或指定数据) - 删除整个列表或指定数据。
# del list1
# print(list1)  # name 'list1' is not defined
del [list1[1]]
print(list1)  # ['Tom', 'Rose', 'Jack', 'Frank']

# * 2 pop() - 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，pop会返回被删除的数据。
delName = list1.pop()
print(delName)  # Frank
print(list1)  # ['Tom', 'Rose', 'Jack']
delName1 = list1.pop(1)
print(delName1)  # Rose
print(list1)  # ['Tom', 'Jack']

# * 3 remove(指定数据内容) - 根据指定数据内容，删除列表中相应的数据。
list1.remove("Jack")
print(list1)  # ["Tom"]

# * 4 clear()
list1.clear()
print(list1)  # []
