"""
    字典：
"""

# 1、创建
# 空
dict01 = {}
print(dict01)
dict01 = dict()
print(dict01)
# 默认值
dict01 = {"wj": 100, "zm": 80, "zr": 90}  # {'wj': 100, 'zm': 80, 'zr': 90} 无序
print(dict01)
dict01 = dict([("a", "b"), ("c", "d")])  # {'a': 'b', 'c': 'd'} 无序
print(dict01)

# 2、查找元素（根据key查找value）
print(dict01["a"])
# 如果key不存在，查找时会错误
if "zq" in dict01:  # 如果存在key
    print(dict01["zq"])

# 3、修改元素（之前存在key）
dict01["a"] = "BB"
print(dict01["a"])

# 4、添加（之前不存在key）
dict01["e"] = "f"
print(dict01["a"])

# 5、删除（只能根据键删）
print(dict01)
del dict01["a"]
print(dict01)

# 6、遍历（获取字典中掺的元素）

# 遍历字典，得到的是key
for key in dict01:
    print(key)
    print(dict01[key])

# 遍历字典，得到的是value
for value in dict01.values():
    print(value)

# 遍历字典，得到的是键值对key value（返回元组）
# for item in dict01.items():
#     print(item)
#     print(item[0])
#     print(item[1])
for key, value in dict01.items():  # 利用元组赋值的语法 a,b=(100,200)
    print(key)
    print(value)
