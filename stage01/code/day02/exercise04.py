"""
在控制台中录入距离，时间，初速度，计算加速度。
匀变速直线运动的位移与时间公式：
s=v0t+1/2*at^2
a=2(s-v0t)/t^2
"""

initial_velocity = float(input("初速度："))
distance = float(input("位移："))
time = float(input("时间："))

accelerate = 2 * (distance - initial_velocity * time) / time ** 2

print("加速度：" + str(accelerate))
