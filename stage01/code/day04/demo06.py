"""
    通用操作
"""

str01 = "悟空"
str02 = "八戒"
# 字符串拼接
str03 = str01 + str02
# 字符串累加
str01 += str02
print(str01)

# 重复生成
print(str02 * 3)
str02 *= 3
print(str02)
# 一次比较两个容器中元素，一旦不同则返回编码值的比较结果。
print("悟空" > "八戒")  # True
print("a悟空" > "b八戒")  # False

# 成员运算符 in
print("" in "我叫齐天大圣孙悟空")  # True
print("齐大圣" in "我叫齐天大圣孙悟空")  # False

# 索引
msg = "我叫齐天大圣"
# 获取正数第三个字
print(msg[2])  # 齐
# 获取倒数第三个字
print(msg[-3])  # 三

# 切片
print(msg[0:2])  # 我叫
# 开始值默认为开头
print(msg[:2])  # 我叫
# 结束值默认为末尾
print(msg[-2:])  # 大圣
print(msg[:])  # 我叫齐天大圣

print(msg[-2:-5:-1])  # 大天齐
print(msg[::-1])  # 圣大天齐叫我

print(msg[1:1])  # 空字符串""
print(msg[3:1])  # 空字符串""
print(msg[-2:1])  # 想输出"大圣我叫"，但取不到.只能输出空字符串""

# 索引不能越界
# print(msg[7])  # ERROR
# 切片越界不报错
print(msg[1:7])  # 叫齐天大圣
