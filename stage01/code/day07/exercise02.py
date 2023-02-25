# 练习：["无忌","赵敏","周芷若"][101,102,103]合并成一个字典
list01 = ["无忌", "赵敏", "周芷若"]
list02 = [101, 102, 103]
dict01 = {list01[i]: list02[i] for i in range(3)}
print(dict01)

# 需求：字典如何根据value查找key
# dict02 = {}
# for k, v in dict01.items():
#     dict02[v] = k
# print(dict02)
# 解决方案1：键值互换
dict02 = {v: k for k, v in dict01.items()}
# 缺点：如果key重复，交换或则丢失数据
# 如果需要保持所有数据需要使用列表容器，而不能使用字典
# [(k,v),]
list03 = [(v, k) for k, v in dict01.items()]
