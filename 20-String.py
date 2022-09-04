"""
TODO String
"""
# Single quotation marks
# Double quotation marks
a = "Hello World"
print(a)
print(type(a))

# Triple quotation marks
b = """ Hello
        World"""
print(b)
print(type(b))

name = "Tom"
# Output String
print("My name is %s" % name)
print(f"My name is {name}")

# Input String
password = input("Password: ")
print(f"Your password: {password}")
print(type(password))  # <class 'str'>
print(type(int(password)))  # <class 'int'>
