"""
    集合
"""

# 1、创建集合
# 创建具有默认值的集合
set01 = {1, 2, 3}  # 这种方法不能创建空集合
print(set01)
set02 = set([1, 2, 3])
print(set02)
# set-->str
set03 = set("abc")
list01 = list(set03)
print("".join(list01))

# 2、添加元素
set03.add("qtx")

# 3、删除元素
set03.remove("a")

# 4、获取所有元素
for item in set03:
    print(item)

# 5、数学运算
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集
print(set01 & set02)  # {2 , 3}

# 并集
print(set01 | set02)  # {1 , 2 , 3 , 4}
# 补集
print(set01 ^ set02)  # {1 , 4}
# 差集
print(set01 - set02)  # {1}
print(set02 - set01)  # {4}

set01 = {1, 2}
set02 = {1, 2, 3, 4}
# 子集
print(set01 < set02)
# 超集
print(set02 > set01)
