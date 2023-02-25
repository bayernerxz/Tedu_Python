class Commodity:
    """
    商品类，用于表示商品
    """

    def __init__(self, cid, name, price):
        """
        :param cid:int，商品编号
        :param name: str，商品名称
        :param price: int，商品单价
        """
        self.id = cid
        self.name = name
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class Order:
    """
    订单类，用于表示单个订单
    """

    def __init__(self, cid=None, count=0):
        """
        :param cid: int，选购的商品编号
        :param count: int，选购的商品数量
        """
        self.cid = cid
        self.count = count

    @property
    def cid(self):
        return self.__cid

    @cid.setter
    def cid(self, value):
        self.__cid = value

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value


class CommodityPurchaseController:
    """
    商品购买控制类，处理商品购买的逻辑
    """

    def __init__(self):
        """
        初始化商品列表和订单列表，因为游戏开始时就有商品列表，所以用init_commodity()处理
        """
        self.__commodity_list = []
        self.init_commodity()
        self.__order_list = []

    @property
    def commodity_list(self):
        return self.__commodity_list

    @property
    def order_list(self):
        return self.__order_list

    def init_commodity(self):
        """
        初始化商品列表
        """
        self.__add_commodity(Commodity(101, "屠龙刀", 10000))
        self.__add_commodity(Commodity(102, "倚天剑", 10000))
        self.__add_commodity(Commodity(103, "九阴白骨爪", 8000))
        self.__add_commodity(Commodity(104, "九阳神功", 9000))
        self.__add_commodity(Commodity(105, "降龙十八掌", 8000))
        self.__add_commodity(Commodity(106, "乾坤大挪移", 10000))

    def __add_commodity(self, commodity):
        """
        在商品列表里增加商品类
        :param commodity: 商品类
        """
        self.__commodity_list.append(commodity)

    def __add_order(self, order):
        """
        在订单列表里增加订单类
        :param order: 订单类
        """
        self.__order_list.append(order)

    def buying(self, cid, count):
        """
        按商品编号购买
        :param cid:int类型，商品id
        """
        order = Order()
        order.cid = cid
        order.count = count
        self.__add_order(order)


class CommodityPurchaseView:
    """
    商品购买视图
    """

    def __init__(self):
        """
        初始化时创建一个控制器
        """
        self.__controller = CommodityPurchaseController()

    def __display_commodity(self):
        """
        打印商品列表里的商品信息
        """
        for item in self.__controller.commodity_list:
            print("编号：%d，名称：%s，单价：%d。" % (item.id, item.name, item.price))

    def __get_commodity_info(self):
        """
        获取并返回商品id
        :return: int类型的商品id
        """
        while True:
            cid = int(input("请输入商品编号："))
            for item in self.__controller.commodity_list:
                if item.id == cid:
                    count = int(input("请输入商品编号："))
                    return cid, count
            else:
                print("该商品不存在")

    def __print_orders_and_calc_total_price(self):
        """
        打印所有订单，计算并返回总价
        :return: float类型，总价
        """
        total_price = 0
        for order in self.__controller.order_list:
            for commodity in self.__controller.commodity_list:
                if commodity.id == order.cid:
                    total_price += commodity.price * order.count
                    print("编号：%d，名称：%s，单价：%d 数量：%d 总计：%d。" % (
                        order.cid, commodity.name, commodity.price, order.count, total_price))
        return total_price

    def __paying(self, total_price):
        """
        支付
        :param total_price: float类型，竞价
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__controller.order_list.clear()
                break
            else:
                print("金额不足。")

    def main(self):
        while True:
            item = input("1键购买，2键结算。")
            if item == "1":
                self.__display_commodity()
                cid, count = self.__get_commodity_info()
                self.__controller.buying(cid, count)
            elif item == "2":
                total_price = self.__print_orders_and_calc_total_price()
                self.__paying(total_price)
            elif item == "":
                break
            else:
                print("输入错误，请重新输入。")


if __name__ == "__main__":
    view = CommodityPurchaseView()
    view.main()
