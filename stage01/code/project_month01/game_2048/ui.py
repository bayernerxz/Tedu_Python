"""
    2048控制台界面
"""
from bll import GameCoreController
from model import DirectionModel
import os


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        # 产生两个数字
        self.__controller.generate_random_number()
        self.__controller.generate_random_number()
        # 绘制界面
        self.__draw_map()

    def __draw_map(self):
        # 清空控制台
        # os.system("cls")  # windows是cls，linux是clear。在pycharm中的控制台中可以用clear。
        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def __update(self):
        # 循环
        while True:
            # 判定玩家的输入 --> 移动地图
            self.__move_map_for_input()
            # 产生新数字
            self.__controller.generate_random_number()
            # 绘制界面
            self.__draw_map()
            # 游戏结束判定 --> 提示
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    def __move_map_for_input(self):
        dir_ = input("请输入方向（WASD)")
        dict_ = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }
        if dir_ in dict_:
            self.__controller.move(dict_[dir_])


# =============测试代码==================
if __name__ == "__main__":
    view = GameConsoleView()
    view.main()
