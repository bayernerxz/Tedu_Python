# 练习：英文单词反转
# "How are you"-->"you are How"

sentence = "How are you"
list_temp = sentence.split(" ")
# print(list_temp)
str_result = " ".join(list_temp[::-1])
# print(list_temp02)
print(str_result)
