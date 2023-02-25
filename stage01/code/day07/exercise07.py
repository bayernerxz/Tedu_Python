# 列表排序（升序）[3,80,45,5,7,1]
# 目标：列表中所有元素两两比较
# 思想：
#   取出第一个元素，与后面元素进行比较
#   取出第二个元素，与后面元素进行比较
#   取出第三个元素，与后面元素进行比较
#   ……
#   取出倒数第二个元素，与后面元素进行比较
#   如果取出的元素大于后面的元素，
#   则交换。

list01 = [3, 80, 45, 5, 7, 1]
list02 = [3, 80, 45, 5, 7, 1]

for i in range(6):
    for j in range(1, len(list01)):
        if list01[j - 1] > list01[j]:
            list01[j - 1], list01[j] = list01[j], list01[j - 1]
print(list01)

for i in range(len(list02) - 1):
    for j in range(i + 1, len(list02)):
        if list02[i] > list02[j]:
            list02[i], list02[j] = list02[j], list02[i]
print(list02)
