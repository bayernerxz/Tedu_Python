# 练习：使用range()生成1-10之间的数字，将数字的平方存入list01中。

# list01 = []
# for i in range(1, 11):
#     list01.append(i ** 2)

list01 = [i ** 2 for i in range(1, 11)]
print(list01)

# 练习，将list01中所有奇数存入list02
# list02 = []
# for i in list01:
#     if i % 2 != 0:
#         list02.append(i)
list02 = [i for i in list01 if i % 2 != 0]
print(list02)

# 练习，将list01中所有偶数存入list03
list03 = [i for i in list01 if i % 2 == 0]
print(list03)

# 练习，将list01中所有大于5的数字增加1后存入list04
# list04 = []
# for i in list01:
#     if i > 5 and i % 2 == 0:
#         list04.append(i + 1)
list04 = [i + 1 for i in list01 if i > 5 and i % 2 == 0]
print(list04)
