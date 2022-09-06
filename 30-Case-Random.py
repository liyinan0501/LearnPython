import random

teachers = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[], [], []]

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

i = 1
for office in offices:
    print(f"{i}office: {len(office)}")
    for name in office:
        print(name)
    i += 1
