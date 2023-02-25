"""
6、一个小球从100m的高度落下，每次弹回原高度的一半。
    计算：总共弹起来多少次（最小弹起高度0.01m）
        总共走了多少米？
"""

height = 100
count = 0
distance = 0

while height >= 0.01:
    # 上面的判断条件也可以改成height/2>=0.01，这样次数可以对了，
    # 但是最后一次的距离没有加上，所以后面的代码也有更改。如21行后面所示。
    count += 1  # 每次触地，计数加1
    height = 0.5 * height
    distance += 3 * height

print(f"总共弹起来{count-1}次")  # 最后一次触地后不弹起，所以弹起数量要加1
print(f"总共弹起的高度{distance-height:0.2f}米")  # 同理，最后一次触地后弹起的高度在上面的循环里已经加上了，必须要再减去

height = 100
count = 0
distance = 0

while height/2 >= 0.01:
    count += 1
    height = 0.5 * height
    distance += 3 * height

print(f"总共弹起来{count}次")
print(f"总共弹起的高度{distance+height:0.2f}米")
