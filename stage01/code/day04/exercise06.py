"""
    练习：随机加法考试
        随机产生两个数字(1-10)
        在控制台中获取两个数相加的结果
        如果用户输入正确得10分
        总共三道题，最后输出得分
"""

import random

score = 0
for item in range(3):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if int(input(f"请输入{a}+{b}=?")) == a + b:
        score += 10
print(f"您的总得分为{score}。")
