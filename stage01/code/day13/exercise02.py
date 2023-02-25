"""
    定义父类
        车（数据：品牌，速度）

    定义子类
        电动车（数据：电池容量，充电功率）

    创建两个对象
    画出内存图
"""


class Vehicle:
    def __init__(self, brand, velocity):
        self.brand = brand
        self.velocity = velocity

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value


class ElectricalVehicle(Vehicle):
    def __init__(self, brand, velocity, battery_capacity, charge_power):
        super(ElectricalVehicle, self).__init__(brand, velocity)
        self.battery_capacity = battery_capacity
        self.charge_power = charge_power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        self.__battery_capacity = value


byd_han = ElectricalVehicle("byd", 180, 55, 100)
toyota_carola = Vehicle("toyota", 240)
