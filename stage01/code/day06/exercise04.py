"""
    练习1：在控制台中循环录入商品信息（名称，单价），
    如果名称输入空字符，则停止录入
    将所有信息逐行打印出来
"""
product_dict = {}

while True:
    product_name = input("请输入商品的名称：")
    if product_name == "":
        break

    price = float(input("请输入商品的单价："))
    product_dict[product_name] = price

for k, v in product_dict.items():
    print(f"商品{k}的单价是{v}元")
