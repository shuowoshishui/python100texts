"""简单选择排序，先从序列中选择一个最小的数，然后与当前的第一个数换位值，然后子序列重复"""
"""选择排序需要记录位置"""


def select_sort(list):
    for i in range(len(list) - 1):
        index = i
        for j in range(i + 1, len(list)):
            if list[index] < list[j]:
                index = j
            list[i], list[index] = list[index], list[i]
        return list


if __name__ == '__main__':
    print(select_sort([21, 44, 12]))
