"""有一个已经排好序的数组，现输入一个数，要求按原来的规律将他插入到数组中。"""
if __name__ == '__main__':
    a = [1, 2, 5, 6]
    num = int(input("输入："))
    if num > a[len(a) - 1]:
        a[len(a)] = num
    else:
        for i in range(len(a) - 1):
            if num < a[i]:
                a.insert(i, num)
                break
    print(a)
