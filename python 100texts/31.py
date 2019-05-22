"""求100之内的素数"""
if __name__ == '__main__':
    for i in range(1, 101):
        l = []
        for n in range(1, i + 1):
            if i % n == 0:
                l.append(n)
        # print(l)
        if len(l) <= 2:
            print(i)
