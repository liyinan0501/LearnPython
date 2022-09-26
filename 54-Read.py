# 如果访问模式省略，默认为r。
f = open("test.txt")

# * read()
# read 不写参数默认一次性读取所有行
# print(f.read())
# print(f.read(10))

# * readlines()
# 把整个文件中的内容包括换行符进行一次性读取
# print(f.readlines())  # ['11111\n', '22222\n', '33333\n', '44444']

# * readline()
# 有一次读取一行内容
# print(f.readline())  # 11111
# print(f.readline())  # 22222
# print(f.readline())  # 33333

f.close()
