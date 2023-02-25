# 练习4：在列表中[9,25,12,8]，删除大于10的数字
list01 = [9, 25, 12, 8]
# for i in list01[::-1]:
#     if i > 10:
#         list01.remove(i)

for i in range(len(list01) - 1, -1, -1):
    if list01[i] > 10:
        list01.remove(list01[i])

print(list01)
