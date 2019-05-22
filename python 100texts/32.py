"""对十个数进行排序"""


# 冒泡排序
def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(0, len(list) - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


if __name__ == '__main__':
    li = [32, 12, 66, 17, 80, 58]
    print(bubble_sort(li))
