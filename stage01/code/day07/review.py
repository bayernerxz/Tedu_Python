"""
    day06 复习
    容器
        字符串：不可变 存储编码值 序列
        列表：可变 存储变量 序列
            预留内存空间
            扩容：开辟更大的空间
                拷贝原有数据
                替换引用
        元组：不可变 存储变量 序列
            按需分配内存
        字典：可变 存储键值对 散列（无序）
"""

list01 = []
list02 = ["qtx", "xz", "jd"]  # 齐天暄，吕泽，赵旭
list02.append("mm")  # 蒙蒙
list02.insert(1, "wt")  # 魏涛

# item 变量指向列表中的元素
for item in list02:
    print(list02)
# 变量i表示索引
for i in range(len(list02)):
    print(list02[i])

# 修改
list02[0] = "QTX"

# 删除
list02.remove("mm")

dict01 = {}
dict02 = {"qtx": 100, "xz": 80, "jd": 90}
dict02["mm"] = 95

# 获取所有元素
for key in dict02:
    print(key)
    print(dict02[key])

for value in dict02.values():
    print(dict02[key])

for key, value in dict01.items():
    print(key)
    print(value)

# 修改
dict02["qtx"] = 101

# 删除
del dict02["mm"]

list03 = ["看书", "编程", "美食"]
dict03 = {"qtx": list03}
dict03 = {"qtx": list03}
list03.append("听音乐")
print(dict03)
