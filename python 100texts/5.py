"""输入三个整数x，y，z，请把这三个数由小到大输出。"""
list = []
for i in range(3):
    x = int(input("第" + str(i + 1) + "个:"))
    list.append(x)
    list.sort()
for j in list:
    print(j)
