# 练习1
# 在控制台中，录入一个商品单价。
# 再录入一个数量
# 最后获取金额，计算应该找回多少钱。当钱不够时，提示钱不够，还需要再付多少钱。
# 并进行调试

unit_price = int(float(input("请输入商品总价：")) * 100)
quantity = int(input("请输入商品数量："))
payment = int(float(input("请输入客户付款总额：")) * 100)

total_price = unit_price * quantity
change = (payment - total_price) / 100

if change >= 0:
    print("应找零：" + str(change) + "元")
else:
    print("钱不够。还需要再付" + str(change) + "元")
