list01 = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"],
    ["D1", "D2", "D3", "D4", "D5"],
    ["E1", "E2", "E3", "E4", "E5"],
]


class Combination:
    def __init__(self, A, B, C, D, E):
        self.composition = [A, B, C, D, E]

    def print_info(self):
        print(self.composition)

    def over_rate(self, combination):
        """
        判定两个Combination是否重复率大于0.4
        :param combination: 对比的Combination的实例
        :return: bool类型，True指重复率过高，False则合格
        """
        temp = 0
        for i in range(len(self.composition)):
            if self.composition[i] == combination.composition[i]:
                temp += 1
        if temp / len(self.composition) > 0.4:
            return True
        else:
            return False


def generate():
    # 生成所有可能的组合
    from itertools import product
    global temp_list
    temp = list(product(list01[0], list01[1], list01[2], list01[3], list01[4]))
    for item in temp:
        temp_list.append(Combination(*item))
    # for pos1 in list01[0]:
    #     for pos2 in list01[1]:
    #         for pos3 in list01[2]:
    #             for pos4 in list01[3]:
    #                 for pos5 in list01[4]:
    #                     temp_list.append(Combination(pos1, pos2, pos3, pos4, pos5))


def zero_not_ok():
    # 把重复率小于0.4的组合置0
    global temp_list
    for index in range(len(temp_list) - 1):
        for j in range(index + 1, len(temp_list)):
            if temp_list[index] != 0 and temp_list[j] != 0:
                # 保留第一个，其余重复率超出要求的置0
                if temp_list[index].over_rate(temp_list[j]):
                    temp_list[j] = 0


def delete_zero():
    for i in range(len(temp_list) - 1, -1, -1):
        if temp_list[i] == 0:
            del temp_list[i]


if __name__ == "__main__":
    temp_list = []
    generate()
    # print(len(temp_list))
    # temp_list[0].print_info()
    # temp_list[100].print_info()
    # temp_list[1000].print_info()

    zero_not_ok()

    delete_zero()

    # 打印结果
    print(len(temp_list))

    for item in temp_list:
        item.print_info()
