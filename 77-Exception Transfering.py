#
# Todo 异常传递
#
import time

try:
    f = open("test.txt")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:  # 读取完毕退出
                break
            time.sleep(2)  # 隔2秒钟再打印，有时间按下ctrl+c
            print(content)
    except:
        # 在读取过程中，产生了异常，就会捕获到。
        # 例如 按下了 ctrl+c
        print("Stop accidentally")
    finally:
        f.close()
        print("The file is closed")
except:
    print("The test.txt does not exist.")
