# 练习1
# 在控制台中，录入一个商品单价。
# 再录入一个数量
# 最后获取金额，计算应该找回多少钱。

unit_price = int(float(input("请输入商品总价：")) * 100)
quantity = int(input("请输入商品数量："))
payment = int(float(input("请输入客户付款总额：")) * 100)

total_price = unit_price * quantity
change = (payment - total_price) / 100

print("应找零：" + str(change) + "元")

# 练习2：在控制台中获取分钟
#             再获取小时
#             再获取天
#             计算总秒数
minute = int(input("请输入分钟数"))
hour = int(input("请输入小时数"))
day = int(input("请输入天数"))

second = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60

print("总秒数为:" + str(second))
