"""
从终端输入一个单词
从单词本中找到该单词，打印解释内容
如果找不到则打印“找不到”
"""
word = input("请输入需要查找的单词：")

# 默认r打开
f = open("dict2.txt", encoding="utf-8")

# count = 0
# row = f.readline()
# while count == 0 and row:
#     row = f.readline()
#     list_ = row.split(" ")
#     if word == list_[0]:
#         print(list_[-1])
#         count += 1
#
# if count == 0:
#     print("找不到")

# 每次获取一行
for line in f:
    w = line.split(" ")[0]
    # 如果遍历到的单词已经大于word就结束查找
    if w > word:
        print("找不到")
        break
    elif w == word:
        print(line)
        break
else:
    print("没找到")

f.close()
