"""
TODO List Methods - Add
"""

list = ["Tom", "Lily", "Rose"]

# * 1 .append(新数据) - 修改原列表，在结尾增加数据，可以不拆开增加列表类型的数据。
list.append("Jack")
list.append([11, 22])
print(list)  # ['Tom', 'Lily', 'Rose', 'Jack', [11, 22]]

# * 2 .extend(新数据) -  修改原列表，在结尾增加数据, 可以拆开增加列表类型的数据。
list.extend([33, 44])
list.extend("Li")
print(list)  # ['Tom', 'Lily', 'Rose', 'Jack', [11, 22], 33, 44, 'L', 'i']

# * 3 .insert(位置下标, 新数据) - 在指定位置增加数据
list.insert(1, "Joe")
print(list)  # ['Tom', 'Joe', 'Lily', 'Rose', 'Jack', [11, 22], 33, 44, 'L', 'i']
