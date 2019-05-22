'''利用递归的方式，将输入的五个字符，以相反的顺序打印出来'''


def p(n):
    next = 0
    if n <= 1:
        next = int(input('输入：'))
        print(next)
    else:
        next = int(input('输入：'))
        p(n - 1)
        print(next)


p(5)
