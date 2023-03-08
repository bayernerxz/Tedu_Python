"""
    列表
"""
# 1、创建列表
# 空
list01 = []
list01 = list()  # 该函数是把一个容器转变为列表

# 默认值
list02 = ["悟空", 100, True]
list02 = list("我是齐天大圣")

# 2、获取元素
# 索引
print(list02[2])  # 齐
# 切片
print(list02[-4:])  # ['齐', '天', '大', '圣']

# 3、添加元素
# append追加（在末尾添加）
list02.append("八戒")
# 插入（在指定
list02.insert(1, True)  # 在索引为1（第二个）的位置添加True
print(list02)

# 4、删除元素
# 根据元素删除
list02.remove("是")
print(list02)
# 根据位置删除
del list02[0]
print(list02)

# 5、定位元素，目的：可以增删改查元素
# 切片
del list02[1:3]
print(list02)  # [True, '齐', '天', '大', '圣', '八戒']
list02[1:3] = ["a", "b"]  # [True, '大', '圣', '八戒']
list02[1:3] = [1, 2, 3, 4, 5, 6]  # [True, 1, 2, 3, 4, 5, 6, '八戒']
list02[1:3] = []  # [True, 3, 4, 5, 6, '八戒']
print(list02)

# 遍历列表
# 获取列表中的所有元素
for item in list02:
    print(item)

# 倒序获取所有元素
# 不建议
# 因为list02[::-1] 通过切片拿元素，会重新创建新列表，浪费内存
for item in list02[::-1]:
    print(item)

# 3 2 1 0
for i in range(len(list02) - 1, -1, -1):
    print(list02[i])
# -1 -2 -3 -4
for i in range(-1, -len(list02)-1, -1):
    print(list02[i])
