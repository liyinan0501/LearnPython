"""
TODO For Else
"""
# 只有for语句里正常循环结束后，才执行else语句，否则不会单独执行else语句。
# Break 退出全部循环，属于非正常结束循环，因此不执行else语句。
str1 = "itheima"
for i in str1:
    if i == "e":
        print("Skip letter e")
        break
    print(i)
else:
    print("ending")

print(".............................")

# continue 退出当次循环，属于正常结束循环，因此执行else语句。
for j in str1:
    if j == "e":
        print("Skip letter e")
        continue
    print(j)
else:
    print("ending")
