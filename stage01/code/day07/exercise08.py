"""
    练习;
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路∶所有元素俩俩比较，发现相同的则打印结果.(只打印一次）
    所有元素比较结束﹐都没有发现相同项·则打印结果.
"""

list01 = [3, 80, 45, 5, 80, 1]
judgement = False
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if list01[i] == list01[j]:
            # print("列表中的元素%d是重复的" % list01[i])
            print("列表中的元素有重复的")
            judgement = True
            break
    if judgement:
        break
if not judgement:
    print("列表中没有重复的元素。")
