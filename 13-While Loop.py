"""
TODO While Loop
"""
i = 0
while i < 5:
    print("1")
    i += 1

x = 1
result = 0
while x <= 100:
    result += x
    x += 1
print(result)

y = 1
result1 = 0
while y <= 100:
    if y % 2 == 0:
        result1 += y
    y += 1
print(result1)
