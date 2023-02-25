# 练习3：
# 在列表中[54,25,13,23,43,35,17]，选出最大值(不使用max()函数)

list03 = [54, 25, 13, 23, 43, 100, 35, 17]
# 假设第一个是最大的
max_number = list03[0]
# 与后面（从第二个开始）元素进行比较
for i in list03:
    if i > max_number:
        # 如果发现更大的，则替换假设的
        max_number = i
print(f"最大的数字是：{max_number}")


