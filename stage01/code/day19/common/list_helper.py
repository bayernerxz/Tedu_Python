"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类 LINQ语言集成查询（英语：Language Integrated Query，缩写：LINQ）
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

    @staticmethod
    def sum_property(list_target, func_handle):
        """
            通用的求和元素的某个属性的方法
        :param list_target: 需要求和的列表，list类型
        :param func_handle: 需要求和的处理逻辑，函数类型，函数名-->int,float
        :return: 和，int,float
        """
        result = 0
        for item in list_target:
            result += func_handle(item)
        return result

    @staticmethod
    def screen_to_list(list_target, func_handle):
        """
            通用的筛选所有元素的某个属性的方法，生成一个列表
        :param list_target: 需要筛选的列表，list类型
        :param func_handle: 需要筛选的处理逻辑，函数类型,函数名-->任意类型对象
        :return:list对象
        """
        list_result = []
        for item in list_target:
            list_result.append(func_handle(item))
        return list_result

    @staticmethod
    def screen_to_generator(list_target, func_handle):
        """
            通用的筛选所有元素的某个属性的方法，生成一个生成器
        :param list_target: 需要筛选的列表，list类型
        :param func_handle: 需要筛选的处理逻辑，函数类型,函数名-->任意类型对象
        :return:生成器对象
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用的获取最大元素方法
        :param list_target: 需要搜索的列表，list类型
        :param func_handle: 需要搜索的处理逻辑，函数类型,函数名-->任意类型对象
        :return:最大元素
        """
        max_member = list_target[0]
        for item in list_target:
            if func_handle(max_member) < func_handle(item):
                max_member = item
        return max_member

    @staticmethod
    def get_min(list_target, func_handle):
        """
            通用的获取最小元素方法
        :param list_target: 需要搜索的列表，list类型
        :param func_handle: 需要搜索的处理逻辑，函数类型,函数名-->任意类型对象
        :return:最小元素
        """
        min_member = list_target[0]
        for item in list_target:
            if func_handle(min_member) > func_handle(item):
                min_member = item
        return min_member

    @staticmethod
    def sort_ascending(list_target, func_handle):
        """
            通用的对元素进行升序排序的方法
        :param list_target: 需要搜索的列表，list类型
        :param func_handle: 需要搜索的处理逻辑，函数类型,函数名-->任意类型对象
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_handle(list_target[i]) > func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def sort_descending(list_target, func_handle):
        """
            通用的对元素进行升序排序的方法
        :param list_target: 需要搜索的列表，list类型
        :param func_handle: 需要搜索的处理逻辑，函数类型,函数名-->任意类型对象
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_handle(list_target[i]) < func_handle(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def delete_element(list_target, func_condition):
        """
            通用的删除符合条件的元素的方法
        :param list_target: 需要搜索的列表，list类型
        :param func_condition: 需要搜索的处理逻辑，函数类型,函数名-->任意类型对象
        """
        for i in range(len(list_target) - 1, -1, -1):
            if func_condition(list_target[i]):
                list_target.remove(list_target[i])
