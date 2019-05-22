"""给一个不多与五位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。"""
'''def p(n):
    print(len(n))
    print(n[::-1])
    "切片逆转"
p(input("输入："))'''


# 递归实现
def p(n):
    if len(n) <= 1:
        return n
    else:
        return n[-1] + p(n[:-1])


print(p(str(1234)))
