"""
3、按照以下格式，输出变量name="", age=, score=,
    我叫xx，年龄是xx，成绩是xx。
"""
name = "悟空"
age = 800
score = 99.5
msg1 = "我叫%s，年龄是%d，成绩是%.1f。" % (name, age, score)
msg2 = f"我叫{name}，年龄是{age}，成绩是{score:.2f}。"
print(msg1)
print(msg2)
