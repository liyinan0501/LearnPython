import os

# Todo 批量重命名 - 添加和删除字符

os.chdir("58-test")
file_list = os.listdir()
print(file_list)

flag = 2

for i in file_list:
    if flag == 1:
        new_name = "Python_" + i
    elif flag == 2:
        index = len("Python_")
        new_name = i[index:]
    os.rename(i, new_name)

# for i in file_list:
#     new_name = "Python_" + i
#     os.rename(i, new_name)
