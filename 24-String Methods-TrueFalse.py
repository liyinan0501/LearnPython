"""
TODO String Methods - True/False
"""
str = "hello world and itcast and itheima and Python"

# .startswith(子串, 开始位置下标, 结束位置下标) - 区分大小写
print(str.startswith("hello"))  # true
print(str.startswith("hello", 15, 20))  # false

# .endswith(子串, 开始位置下标, 结束位置下标) - 区分大小写
print(str.endswith("Python"))  # true
print(str.endswith("python", 15, 20))  # false

str1 = "hello"
str2 = "hello12345"
str3 = "12345"
str4 = "     "
str5 = "123 232"
# .isalpha() - 判断非空字符串所有字符是否是字母
print(str1.isalpha())  # True
print(str2.isalpha())  # False
print(str3.isalpha())  # False
print(str.isalpha())  # False 因为str字符串里有空格

# .isdigit() - 判断非空字符串所有字符是否是数字
print(str1.isdigit())  # False
print(str2.isdigit())  # False
print(str3.isdigit())  # True
print(str5.isdigit())  # False 因为str5字符串里有空格

# .isalnum() - 判断非空字符串所有字符是否是数字或字母
print(str1.isalnum())  # True
print(str2.isalnum())  # True
print(str3.isalnum())  # True
print(str5.isalnum())  # False
print(str.isalnum())  # False 因为str字符串里有空格

# .isspace() - 判断非空字符串所有字符是否是空格
print(str.isspace())  # False
print(str3.isspace())  # False
print(str4.isspace())  # True
print(str5.isspace())  # False
