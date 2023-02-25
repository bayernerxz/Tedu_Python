# 1．获取列表中所有字符串
# 2.获取列表中所有小数
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.

list01 = [3, "54", True, 4556, 6, "76", 1.6, False, 3.5]


# 1．获取列表中所有字符串

def find01():
    for item in list01:
        if type(item) == str:
            yield item


re01 = find01()
for item in re01:
    print(item)

re02 = (item for item in list01 if type(item) == str)
for item in re02:
    print(item)

re03 = [item for item in list01 if type(item) == str]
for item in re03:
    print(item)


# 2.获取列表中所有小数

def find02():
    for item in list01:
        if type(item) == float:
            yield item


re01 = find02()
for item in re01:
    print(item)

re02 = (item for item in list01 if type(item) == float)
for item in re02:
    print(item)

re03 = [item for item in list01 if type(item) == float]
for item in re03:
    print(item)
