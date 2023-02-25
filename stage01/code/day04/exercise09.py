# 练习1：在控制台，获取一个字符串，
# 打印每个字符的编码值

word = input("请输入一个字符串：")
for item in word:
    print(ord(item))

# 练习2：在控制台中，重复录入一个编码值，然后打印字符，
#       如果输入空字符串，则退出程序。
while True:
    code_str = input("请输入一个整数：")
    if code_str == "":
        break
    print(chr(int(code_str)))
