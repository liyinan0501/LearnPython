"""
TODO Condition
"""
age = int(input("Your age: "))
if age < 18:
    print("You are under age.")
elif 18 <= age <= 60:
    print("You are adult.")
else:
    print("You are retired.")
print("close....")
