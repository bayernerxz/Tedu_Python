"""
    2048游戏核心算法
"""


# 练习1. 0元素移至末尾
#    [2,0,2,0] --> [2,2,0,0]
#    [2,0,0,2] --> [2,2,0,0]
#    [2,4,0,2] --> [2,4,2,0]

def move_zero_end(list_ref):
    """
    零元素移动到末尾，改变列表对象的元素
    :param list_ref:
    """
    # 从后向前，如果发现零元素，删除并追加。
    for i in range(len(list_ref) - 1, -1, -1):
        if list_ref[i] == 0:
            del list_ref[i]
            list_ref.append(0)


# 练习2. 将相同数字进行合并，只合一次，从左到右合并
#    [2,2,0,0] --> [4,0,0,0]
#    [2,0,0,2] --> [4,0,0,0]
#    [2,0,4,0] --> [2,4,0,0]
#    [2,2,2,2] --> [4,4,0,0]
def merge_same_element(list_ref):
    """
        合并相同元素，从左向右合并
    :param list_ref: 需要合并的列表
    """
    # 先将中间的零元素移到末尾
    # 再合并相同元素
    move_zero_end(list_ref)
    for i in range(len(list_ref) - 1):
        if list_ref[i] == list_ref[i + 1]:
            # 将后一个累加前一个之上
            list_ref[i] *= 2
            del list_ref[i + 1]
            list_ref.append(0)


# 测试
# list_merge = [4, 2, 0, 2]
# merge_same_element(list_merge)
# print(list_merge)

# 练习3：地图向左移动
def shift_left(ref_map):
    """
    向左移动
    :param ref_map:需要向左移动的地图
    """
    for item in ref_map:
        merge_same_element(item)


# shift_left(game_map)
# print(game_map)

def change_right_to_left(ref_map):
    """
    把向右移动的地图，变更为向左移动地图
    :param ref_map: 需要变更的地图
    :return: 变更后的地图
    """
    temp_map = []
    for item in ref_map:
        temp_map.append(item[::-1])
    return temp_map


def shift_right(ref_map):
    """
    向右移动
    :param ref_map: 需要向右移动的地图
    """
    temp_map = change_right_to_left(ref_map)
    shift_left(temp_map)
    temp_map = change_right_to_left(temp_map)
    ref_map[:] = temp_map


# shift_right(game_map)
# print(game_map)

# 练习4：向上移动，向下移动
def shift_up(ref_map):
    """
    向上移动
    :param ref_map: 需要向右移动的地图
    """
    # 把向上移动的矩阵改为向左移动的矩阵
    temp_map = change_up_to_left(ref_map)
    shift_left(temp_map)
    # 再次改回来
    temp_map = change_up_to_left(temp_map)
    ref_map[:] = temp_map


def change_up_to_left(ref_map):
    """
    把向上移动的地图，变更为向左移动地图
    :param ref_map: 需要变更的地图
    :return: 变更后的地图
    """
    temp_map = []
    for j in range(len(ref_map[0])):
        temp_line = []
        for i in range(len(ref_map)):
            temp_line.append(ref_map[i][j])
        temp_map.append(temp_line)
    return temp_map


def shift_down(ref_map):
    """
    向下移动
    :param ref_map: 需要向右移动的地图
    """
    # 把向上移动的矩阵改为向下移动的矩阵
    temp_map = change_down_to_left(ref_map)
    shift_left(temp_map)
    # 再次改回来
    temp_map = change_down_to_left(temp_map)
    ref_map[:] = temp_map


def change_down_to_left(ref_map):
    """
    把向下移动的地图，变更为向左移动地图
    :param ref_map: 需要变更的地图
    :return: 变更后的地图
    """
    temp_map = []
    for j in range(len(ref_map[0]) - 1, -1, -1):
        temp_line = []
        for i in range(len(ref_map) - 1, -1, -1):
            temp_line.append(ref_map[i][j])
        temp_map.append(temp_line)
    return temp_map


game_map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 0, 2],
    [2, 2, 2, 2],
]
shift_down(game_map)
print(game_map)
