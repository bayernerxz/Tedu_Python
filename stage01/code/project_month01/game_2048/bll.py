"""
    2048游戏逻辑控制器，负责处理游戏核心算法
"""
import model
from model import DirectionModel
from model import Location
import random


class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __move_zero_end(self):
        """
        零元素移动到末尾，改变列表对象的元素
        """
        # 从后向前，如果发现零元素，删除并追加。
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge_same_element(self):
        """
            合并相同元素，从左向右合并
        """
        # 先将中间的零元素移到末尾
        # 再合并相同元素
        self.__move_zero_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                # 将后一个累加前一个之上
                self.__list_merge[i] *= 2
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __shift_left(self):
        """
        向左移动
        """
        for item in self.__map:
            self.__list_merge = item
            self.__merge_same_element()

    def __shift_right(self):
        """
        向右移动
        """
        for item in self.__map:
            self.__list_merge = item[::-1]
            self.__merge_same_element()
            item[::-1] = self.__list_merge

    def __shift_up(self):
        """
        向上移动
        """
        self.__square_matrix_transpose()
        self.__shift_left()
        self.__square_matrix_transpose()

    def __shift_down(self):
        """
        向下移动
        """
        self.__square_matrix_transpose()
        self.__shift_right()
        self.__square_matrix_transpose()

    def move(self, direction):
        """
            移动
        :param direction:方向，DirectionModel类型
        """
        if direction == DirectionModel.UP:
            self.__shift_up()
        elif direction == DirectionModel.DOWN:
            self.__shift_down()
        elif direction == DirectionModel.LEFT:
            self.__shift_left()
        elif direction == DirectionModel.RIGHT:
            self.__shift_right()

    def __square_matrix_transpose(self):
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    # def __generate_random_number(self):
    #     # 选出所有的空白位置（行/列），再随机挑选一个。
    #     list_empty_location = []
    #
    #     for r in range(len(self.__map)):
    #         for c in range(len(self.__map[0])):
    #             if self.__map[r][c] == 0:
    #                 # 记录r c --> 元组
    #                 list_empty_location.append((r, c))
    #
    #     # 确定哪个空白位置1 0
    #     loc = random.choice(list_empty_location)
    #
    #     # 产生随机数
    #     if random.randint(1, 10) == 1:
    #         self.__map[loc[0]][loc[1]] = 4
    #     else:
    #         self.__map[loc[0]][loc[1]] = 2

    def generate_random_number(self):
        """
            生成新数字
        """
        # 获取所有空白位置
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        # 产生一个随机数
        loc = random.choice(self.__list_empty_location)
        # if random.randint(1, 10) == 1:
        #     self.__map[loc.r_index][loc.c_index] = 4
        # else:
        #     self.__map[loc.r_index][loc.c_index] = 2
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因为在该位置生成了新数字，所以该位置就不是空位置了。
        self.__list_empty_location.remove(loc)

    @staticmethod
    def __select_random_number():
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据。
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[0])):
                if self.__map[r][c] == 0:
                    # 记录r c --> 元组
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            游戏是否结束
        :return：False表示没有结束 True表示结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False
        # # 判断横向有没有相同的元素
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[r]) - 1):
        #         if self.__map[r][c] == self.__map[r][c + 1]:
        #             return False
        # # 判断坚向有没有相同的元素
        # for c in range(len(self.__map[0])):
        #     for r in range(3):
        #         if self.__map[r][c] == self.__map[r + 1][c]:
        #             return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) - 1):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True


# ================测试代码===========================

if __name__ == "__main__":
    controller = GameCoreController()
    controller.move(DirectionModel.UP)
    print(controller.map)
