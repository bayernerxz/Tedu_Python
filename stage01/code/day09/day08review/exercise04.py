"""
7．重构shopping.py程序
    不改变原有功能，修改程序代码。
"""


def choose_shopping_or_settle():
    result = input("1键购买，2键结算。")
    if result == "1":
        return True
    elif result == "2":
        return False


def print_info(ref_dict):
    """
    打印商品信息
    :param ref_dict:商品信息组成的dict
    """
    for k, v in ref_dict.items():
        print("编号：%d，名称：%s，单价：%d。" % (k, v["name"], v["price"]))


def get_count():
    """
    获取需要购买的数量
    :return: 返回需要购买的数量，int类型
    """
    return int(input("请输入购买数量："))


def add_item(commodity_id, order):
    count = get_count()
    order.append({"commodity_id": commodity_id, "count": count})
    return order


def calculate_total_price(commodity_dict, list_order):
    """
    计算总价
    :param commodity_dict: 商品信息，dict类型
    :param list_order: 订单信息，list类型
    :return: 总价，int类型
    """
    total_price = 0
    for item in list_order:
        commodity = commodity_dict[item["commodity_id"]]
        print("编号：%d，名称：%s，单价：%d。" % (item["commodity_id"], commodity["name"], commodity["price"]))
        total_price += commodity["price"] * item["count"]
    return total_price


def get_money(total_price):
    """
    获得现有金币
    :param total_price:商品的总价 ，int类型
    :return: 返回现有的金币，int类型
    """
    return int(input("总价%d元，请输入金额：" % total_price))


def buy(money, total_price):
    """
    购买，无返回值
    :param money: 现有金币，int类型
    :param total_price: 总价，int类型
    """
    print("购买成功，找回：%d元。" % (money - total_price))


def settle(commodity_dict, list_order):
    """
    结算
    :param commodity_dict:商品信息
    :param list_order:  订单信息
    """
    total_price = calculate_total_price(commodity_dict, list_order)
    while True:
        money = get_money(total_price)
        if money >= total_price:
            buy(money, total_price)
            list_order.clear()
            break
        else:
            print("金额不足。")


def add_to_cart(commodity_dict, list_order):
    print_info(commodity_dict)
    while True:
        commodity_id = int(input("请输入商品编号："))
        if commodity_id in commodity_dict:
            add_item(commodity_id, list_order)
            break
        else:
            print("该商品不存在")


def shopping(commodity_dict):
    """
    在商品信息组成的字典里，选则商品进行购买。
    :param commodity_dict:商品信息，dict类型
    """
    list_order = []
    while choose_shopping_or_settle():
        add_to_cart(commodity_dict, list_order)
    settle(commodity_dict, list_order)


if __name__ == "__main__":
    dict_commodity_info = {
        101: {"name": "屠龙刀", "price": 10000},
        102: {"name": "倚天剑", "price": 10000},
        103: {"name": "九阴白骨爪", "price": 8000},
        104: {"name": "九阳神功", "price": 9000},
        105: {"name": "降龙十八掌", "price": 8000},
        106: {"name": "乾坤大挪移", "price": 10000}
    }

    shopping(dict_commodity_info)
