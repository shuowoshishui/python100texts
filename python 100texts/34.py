"""求一个3*3矩阵对角元素之和"""
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('输入：')))
    for k in range(3):
        # print(a[k][k])
        sum += a[k][k]
    print(sum)
