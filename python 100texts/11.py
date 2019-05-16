"""打印楼梯，同时在楼梯上方打印两个笑脸"""
for i in range(1, 11):
    for j in range(1, i):
        print(chr(219), end='')
    print('')
