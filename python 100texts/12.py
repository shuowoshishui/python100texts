"""判断101-200之间有多少个素数，并且输出所有的素数"""
import math

l = []
for i in range(101, 201):
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            break
        else:
            l.append(i)
p = list(set(l))
p.sort()
for a in p:
    print("是素数:", a, end='')
