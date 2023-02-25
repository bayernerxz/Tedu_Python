"""
排序算法训练

重点代码
"""


# 冒泡排序
def bubble(list_):
    n = len(list_)
    # 外层表示比较多少轮
    for i in range(n - 1):
        # 表示每轮两两比较的次数
        for j in range(n - 1 - i):
            # 从小到大排序
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


# 选择排序
def select(list_):
    n = len(list_)
    # 每轮选出一个最小值，需要n轮
    for i in range(n - 1):
        min_index = i  # 假设list_[i]为最小值
        for j in range(i + 1, n + 1):
            if list_[j] < list_[min_index]:
                min_index = j  # 擂主换人
        list_[i], list_[min_index] = list_[min_index], list_[i]


# 插入排序
def sort_by_insert(list_):
    n = len(list_)
    # 控制每次比较的数是谁，从第二个数开始
    for i in range(1, n):
        tmp = list_[i]  # 突出list_[i]的位置
        j = i - 1
        while j >= 0 and list_[j] > tmp:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = tmp


# 快速排序

def quick_sort(list_, low=0, high=-1):
    if high == -1:
        high = len(list_) - 1
    # low表示列表第一个元素索引，high表示最后一个元素索引
    if low < high:
        key = __partition(list_, low, high)
        quick_sort(list_, low, key - 1)
        quick_sort(list_, key + 1, high)


# 快速排序的子函数 完成一轮交换
def __partition(list_, low, high):
    # 选定基准
    x = list_[low]
    # low向后，high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]

    list_[low] = x
    return low


if __name__ == "__main__":
    list01 = [4, 9, 3, 1, 2, 5, 8, 4]
    # bubble(list01)
    # select(list01)
    # sort_by_insert(list01)
    quick_sort(list01)
    print(list01)
