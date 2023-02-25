# 练习：一张纸的厚度是0.01毫米
#   请计算对折多少次，超过珠穆朗玛峰8844.43。

thickness = 1e-5
count = 0
while thickness < 8844.43:
    thickness *= 2
    count += 1
else:
    print("对折了%d次" % count)
