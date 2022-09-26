# r : read
# w : write
# a : edit

# * r, r+
# open not exist file, will show error.
# 文件指针在开头， r+ 下执行 read() 会读取内容。
# f = open("test.txt", "r")
# f.close

# * w, w+
# open not exits file, will create a new one.
# 文件指针在开头， w+ 下执行 read() 会覆盖原内容。
# f = open("test.txt", "w")
# f.write("testtest")
# f.close

# * a, a+
# open not exits file, will create a new one.
# 文件指针在结尾， a+下执行无法读取数据。
fs = open("test.txt", "a")
fs.write("abc")
fs.close

# 如果访问模式省略，默认为r。
