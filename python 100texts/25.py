"""利用递归的方法求5！"""


def total(i):
    sum = 0
    if i == 1:
        sum = 1
    else:
        sum = i * total(i - 1)
    return sum


print(total(5))
