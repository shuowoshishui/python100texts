"""题目四：输入某年，某月，某日，判断这一天是这一年的第几天？"""
"""复习时间函数"""
"""import time
print(time.time())
print(time.localtime())
print(time.asctime(time.localtime()))"""
x = int(input('年：'))
y = int(input('月：'))
z = int(input('日：'))
ping_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
run_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def choose(a, b, c):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        print("闰年")
        z = 0
        for v in run_year[:b - 1]:
            z += v
        day = c + z
    else:  # 平年
        print("平年")
        z = 0
        for v in ping_year[:b - 1]:
            z += v
        print(z)
        day = c + z
    return day


print(choose(x, y, z))
