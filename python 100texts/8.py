"""输出9*9乘法口诀"""
for j in range(1, 10):
    j += 1
    for i in range(1, j):
        k = i * (j - 1)
        print(str(i) + '×' + str(j - 1) + '=' + str(k), end=' ')
    print('\t')
