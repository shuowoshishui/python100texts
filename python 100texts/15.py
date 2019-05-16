"""学习成绩大于等于90分的同学用A表示，60 - 90分的同学用B表示，60 分以下的用C表示。"""
while 1:
    n = int(input("输入成绩："))
    if n > 90:
        print("A")
    elif n > 60 and n < 90:
        print("B")
    else:
        print("C")
