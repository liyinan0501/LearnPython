import os

# Todo 文件及文件夹操作

# * os.rename(src, new name): rename a file or a folder
# os.rename("test.txt", "newTest.txt")

# * os.remove(src): remove a file
# os.remove("test[copy].txt")

# * os.mkdir(): create a new folder
# os.mkdir("aa")

# * os.rmdir(): delete a folder
# os.rmdir("aa")

# * os.getcwd(): get the current path
# print(os.getcwd())  # /Users/yinanli/Desktop/Learn/LearnPython

# * os.chdir(): change current path
# 需求: 在aa里面创建bb文件夹
# os.mkdir("aa")
# os.chdir("aa")
# os.mkdir("bb")

# os.chdir("aa/bb")
# os.mkdir("cc")

# os.listdir(): 获取某个文件夹所有文件，返回一个列表。
# print(os.listdir())
# print(os.listdir("aa"))  # ['bb']
