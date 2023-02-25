"""
    4．(扩展)自行编写其他消除类游戏:消消乐，消灭星星...
消消乐
需求：游戏界面形成的矩阵中以行或列为一个列表，相同的三个以上的元素进行合并。
"""

# 例如下面就是一个5行5列的游戏地图，
# [
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0]
# ]

import random


def fill_element(ref_map, element_classes):
    """
    填充元素
    :param ref_map: 需要填充元素的地图，二维list类型
    :param element_classes:元素种类，int类型
    :return:
    """
    for r in range(len(ref_map)):
        for c in range(len(ref_map[r])):
            ref_map[r][c] = random.randint(1, element_classes)
    return ref_map


def mark_elements(ref_map, marked_map):
    for r in range(len(ref_map)):
        for c in range(len(ref_map[r]) - 2):
            if ref_map[r][c] == ref_map[r][c + 1] and ref_map[r][c] == ref_map[r][c + 2]:
                marked_map[r][c], marked_map[r][c + 1], marked_map[r][c + 2] = True, True, True
                # 标记大于3个的重复元素
                if c <= len(ref_map[r]) - 3:
                    for compare in range(c + 3, len(ref_map[r])):
                        if ref_map[r][c] == ref_map[r][compare]:
                            marked_map[r][compare] = True
                        else:
                            break


def transpose_map(ref_map):
    temp_map = []
    for c in range(len(ref_map[0])):
        temp_row = []
        for r in range(len(ref_map)):
            temp_row.append(ref_map[r][c])
        temp_map.append(temp_row)
    ref_map[:] = temp_map
    return ref_map


def create_marked_map(ref_map):
    temp_map = []
    for r in range(len(ref_map)):
        temp_line = []
        for c in range(len(ref_map[r])):
            temp_line.append(0)
        temp_map.append(temp_line)
    return temp_map


def erase_marked_element(ref_map, marked_map):
    for r in range(len(marked_map)):
        for c in range(len(marked_map[r])):
            if marked_map[r][c]:
                ref_map[r][c] = -1


def merge_same_elements(ref_map):
    marked_map = create_marked_map(ref_map)
    mark_elements(ref_map, marked_map)
    transpose_map(ref_map)
    transpose_map(marked_map)
    mark_elements(ref_map, marked_map)
    transpose_map(ref_map)
    transpose_map(marked_map)
    erase_marked_element(ref_map, marked_map)
    return ref_map


# game_map = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# 生成游戏地图
# fill_element(game_map, 5)
game_map = [
    [1, 1, 1, 2, 3],
    [1, 2, 2, 5, 3],
    [1, 3, 2, 3, 5],
    [5, 1, 3, 1, 1],
    [2, 3, 5, 5, 3]
]

game_map = merge_same_elements(game_map)
for i in game_map:
    print(i)
