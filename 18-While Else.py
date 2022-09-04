"""
TODO While Else
"""
# 只有while语句里正常循环结束后，才执行else语句，否则不会单独执行else语句。
# Break 退出全部循环，属于非正常结束循环，因此不执行else语句。
i = 1
while i <= 5:
    if i == 3:
        print("Silence...")
        break
    print("Are you Ok?")
    i += 1
else:
    print("I'm Ok")

print(".............................")

# continue 退出当次循环，属于正常结束循环，因此执行else语句。
j = 1
while j <= 5:
    if j == 3:
        print("Silence...")
        j += 1
        continue
    print("Are you good?")
    j += 1
else:
    print("I'm Ok")
