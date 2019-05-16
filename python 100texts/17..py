"""求s=a+aa+aaa+aaaa+aaaaa，其中a是一个数字"""
a = int(input("输入："))
l = [1, 11, 111, 1111, 11111]
s = 0
for i in l:
    s += a * int(i)
print(s)
