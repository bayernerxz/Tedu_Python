# 练习：["无忌","赵敏","周芷若"] 按字符串长度作为值生成字典
# ->{"无忌":2,"赵敏":2,"周芷若":3}
list01 = ["无忌", "赵敏", "周芷若"]
dict01 = {item: len(item) for item in list01}
print(dict01)

