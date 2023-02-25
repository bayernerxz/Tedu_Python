"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                函数名-->bool
        :return:需要查找的元素，生成器类型
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法，如果有很多个，返回第一个
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                函数名-->bool
        :return:需要查找的元素，生成器类型
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def find_quantity(list_target, func_condition):
        """
            通用的计算符合某个条件的所有元素数量的方法
        :param list_target:需要查找的列表，list类型
        :param func_condition:需要查找的条件，函数类型
                函数名-->bool
        :return:满足条件元素的数量，int类型
        """
        i = 0
        for item in list_target:
            if func_condition(item):
                i += 1
        return i

    @staticmethod
    def is_exist(list_target, func_condition):
        """
            通用的判断符合某个条件的元素是否存在的方法
        :param list_target:需要查找的列表，list类型
        :param func_condition:需要查找的条件，函数类型
                函数名-->bool
        :return: True存在，False不存在，bool类型
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

