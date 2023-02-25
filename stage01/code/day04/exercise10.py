word = input("请输入一个字符串（可以是任意长度）：")
# 打印第一个字符
print(word[0])
# 打印最后一个字符
print(word[-1])
# 打印倒数第三个字符
print(word[2])
# 打印前两个字符
print(word[:2])
# 倒序打印字符
print(word[::-1])
# 如果字符串长度是奇数，则打印中间字符.
if len(word) % 2 != 0:
    # print(word[3])
    print(word[len(word)//2])
