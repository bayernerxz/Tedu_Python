"""
一个小球从100m的高度落下
每次弹回原高度的一半
计算：总共弹起来多少次（最小弹起高度0.01m）
    总共走了多少米
"""

count = 1
total_distance = 100
rebound_height = 50

while rebound_height >= 0.01:
    total_distance += rebound_height*2
    rebound_height /= 2
    count += 1
print("总共回弹了%d次，共走了%.3f米。" % (count, total_distance))
