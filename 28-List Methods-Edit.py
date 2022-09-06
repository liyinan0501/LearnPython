"""
TODO List Methods - Edit
"""

list = ["Tom", "Lily", "Rose", "Joe"]

# * 1 修改指定下标数据
list[0] = "Jack"
print(list)  # ['Jack', 'Lily', 'Rose', 'Joe']

# * 2 reverse() - 逆序
list.reverse()
print(list)  # ['Joe', 'Rose', 'Lily', 'Jack']

# * 3 sort( key= None, reverse=False) - 排序 升序或降序 False:升序(默认)
list1 = [1, 3, 2, 6, 4, 5]
list1.sort()
print(list1)  # [1, 2, 3, 4, 5, 6]

list1.sort(reverse=True)
print(list1)  # [6, 5, 4, 3, 2, 1]

# * 4 copy() 复制数据 -做修改数据之前，最好复制一份。
list3 = list1.copy()
print(list3)  # [6, 5, 4, 3, 2, 1]
