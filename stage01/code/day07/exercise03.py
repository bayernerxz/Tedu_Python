# 练习1：在控制台中循环录入字符串，输入空字符停止。
#       打印所有不重复的文字
# string = ""
# while True:
#     temp_str = input("请输入字符串：")
#     if temp_str == "":
#         break
#     string += temp_str
#
# set_str = set(string)
# for item in set_str:
#     print(item)


# 正面这个参考答案不如我写的
set_result = set()
while True:
    str_input = input("请输入∶")
    if str_input == "":
        break
    set_result.add(str_input)
print(set_result)
