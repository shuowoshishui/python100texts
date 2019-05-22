"""将一个数组逆序输出"""
l = [1, 2, 3, 4]
l.reverse()
print(l)
"""另一种list[::-1]"""
for item in reversed(l):
    print(item)
