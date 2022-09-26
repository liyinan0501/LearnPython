original_name = input("The name of file want to backup: ")
print(original_name)
print(type(original_name))

index = original_name.rfind(".")

if index > 0:
    postfix = original_name[index:]

copy_name = original_name[:index] + "[copy]" + postfix
print(copy_name)

original_f = open(original_name, "rb")
copy_f = open(copy_name, "wb")

while True:
    content = original_f.read(1024)
    if len(content) == 0:
        break
    copy_f.write(content)

original_f.close()
copy_f.close
