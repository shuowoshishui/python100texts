"""一个数恰好等于他的因子之和，这个数就称之为完数，例如6=1+2+3编程找出1000以内的完数"""
for i in range(0, 1001):
    k = 0
    for j in range(1, i):
        if i % j == 0:
            k = j + k
    # print(k)
    if i == k:
        print(i)
