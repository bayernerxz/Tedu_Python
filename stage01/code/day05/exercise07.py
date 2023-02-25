# 练习：在控制台中循环输入字符串，如果输入空则停止。
# 最后打印所有内容

list_temp = []
while True:
    string = input("请输入需要拼接的字符串：")
    if string == "":
        break
    list_temp.append(string)

result = "".join(list_temp)
print(result)
