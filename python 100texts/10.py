"""古典问题：有一对兔子，从出生后到第三个月起，每个月都生一对兔子，小兔子长到第三个月后
每个月又生一对小兔子，假如兔子都不死，问每个月兔子的总数是多少。"""


def rabbit(month):
    if month <= 2:
        return 2
    else:
        return rabbit(month - 1) + rabbit(month - 2)


if __name__ == "__main__":
    month = int(input("请输入："))
    for i in range(1, month):
        print(rabbit(i))
